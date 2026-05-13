import time
import numpy as np
from pymilvus import MilvusClient

# -------------------------
# Config
# -------------------------
client = MilvusClient("milvus_demo.db")
COLLECTION = "ann_baseline"
DIM = 300 #128
NB = 40000
NQ = 200
TOP_K = 10
NPROBE = 16
NUM_RUNS = 20

# -------------------------
# Generate data
# -------------------------
np.random.seed(0)
base_vectors = np.random.random((NB, DIM)).astype("float32")
query_vectors = np.random.random((NQ, DIM)).astype("float32")

# -------------------------
# Ground truth
# -------------------------
def exact_topk(base, queries, k):
    gt = []
    for q in queries:
        dists = np.sum((base - q) ** 2, axis=1)
        topk = np.argsort(dists)[:k]
        gt.append(topk)
    return np.array(gt)

ground_truth = exact_topk(base_vectors, query_vectors, TOP_K)

# -------------------------
# Reset collection
# -------------------------
if client.has_collection(COLLECTION):
    client.drop_collection(COLLECTION)

client.create_collection(
    collection_name=COLLECTION,
    dimension=DIM,
)

# -------------------------
# Insert data once
# -------------------------
data = [{"id": i, "vector": base_vectors[i].tolist()} for i in range(NB)]
client.insert(collection_name=COLLECTION, data=data)

# -------------------------
# Create index once
# -------------------------
index_params = client.prepare_index_params()
index_params.add_index(
    field_name="vector",
    index_type="IVF_FLAT",
    metric_type="L2",
    params={"nlist": 128},
)

client.create_index(
    collection_name=COLLECTION,
    index_params=index_params
)

client.load_collection(COLLECTION)

# -------------------------
# Recall@10
# -------------------------
def recall_at_k(results, gt, k):
    total = 0
    for pred, truth in zip(results, gt):
        total += len(set(pred[:k]) & set(truth[:k])) / k
    return total / len(results)

# -------------------------
# Run search 5 times
# -------------------------
p50_list = []
p95_list = []
recall_list = []

for run in range(NUM_RUNS):
    latencies = []
    results = []

    for q in query_vectors:
        t0 = time.time()
        res = client.search(
            collection_name=COLLECTION,
            data=[q.tolist()],
            limit=TOP_K,
            search_params={"params": {"nprobe": NPROBE}}
        )
        t1 = time.time()

        latencies.append((t1 - t0) * 1000)

        ids = [hit["id"] for hit in res[0]]
        results.append(ids)

    p50 = np.percentile(latencies, 50)
    p95 = np.percentile(latencies, 95)
    recall = recall_at_k(results, ground_truth, TOP_K)

    p50_list.append(p50)
    p95_list.append(p95)
    recall_list.append(recall)

    print(f"Run {run + 1}: P50={p50:.3f} ms, P95={p95:.3f} ms, Recall@10={recall:.4f}")

# -------------------------
# Output averages
# -------------------------
print("\n===== AVERAGES OVER 20 RUNS =====")
print("NB:", NB)
print("nprobe:", NPROBE)
print("Avg P50 latency (ms):", np.mean(p50_list))
print("Avg P95 latency (ms):", np.mean(p95_list))
print("Avg Recall@10:", np.mean(recall_list))

print("\n===== STANDARD DEVIATIONS =====")
print("Std P50 latency (ms):", np.std(p50_list))
print("Std P95 latency (ms):", np.std(p95_list))
print("Std Recall@10:", np.std(recall_list))
