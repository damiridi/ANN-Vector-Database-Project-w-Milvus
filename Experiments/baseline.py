import time
import numpy as np
from pymilvus import MilvusClient

# -------------------------
# Config
# -------------------------
client = MilvusClient("milvus_demo.db")
COLLECTION = "ann_baseline"
DIM = 128
NB = 40000   # number of database vectors
NQ = 200     # number of queries
TOP_K = 10

# -------------------------
# Generate data
# -------------------------
np.random.seed(0)
base_vectors = np.random.random((NB, DIM)).astype("float32")
query_vectors = np.random.random((NQ, DIM)).astype("float32")

# -------------------------
# Ground truth (exact search)
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
# Insert data
# -------------------------
data = [{"id": i, "vector": base_vectors[i].tolist()} for i in range(NB)]
client.insert(collection_name=COLLECTION, data=data)

# ADD THIS BLOCK HERE
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
# Search baseline
# -------------------------
latencies = []
results = []

for q in query_vectors:
    t0 = time.time()
    res = client.search(
        collection_name=COLLECTION,
        data=[q.tolist()],
        limit=TOP_K,
        search_params={"params": {"nprobe": 1}}
    )
    t1 = time.time()

    latencies.append((t1 - t0) * 1000)

    ids = [hit["id"] for hit in res[0]]
    results.append(ids)

# -------------------------
# Recall@10
# -------------------------
def recall_at_k(results, gt, k):
    total = 0
    for pred, truth in zip(results, gt):
        total += len(set(pred[:k]) & set(truth[:k])) / k
    return total / len(results)

recall = recall_at_k(results, ground_truth, TOP_K)

# -------------------------
# Output
# -------------------------
print("P50 latency (ms):", np.percentile(latencies, 50))
print("P95 latency (ms):", np.percentile(latencies, 95))
print("Recall@10:", recall)
