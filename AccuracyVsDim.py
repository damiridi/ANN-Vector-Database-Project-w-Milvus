import matplotlib.pyplot as plt

DIM = [50, 100, 150, 200, 250, 300]

# Baseline Recall@10 values
recall_10k = [
    0.6049999999999999,
    0.5784999999999999,
    0.5560000000000004,
    0.5544999999999998,
    0.5725,
    0.5259999999999996
]

recall_20k = [
    0.6159999999999998,
    0.5515000000000002,
    0.5350000000000001,
    0.547,
    0.5259999999999998,
    0.5149999999999999
]

recall_40k = [
    0.6039999999999994,
    0.5685,
    0.5274999999999999,
    0.5124999999999998,
    0.5109999999999999,
    0.5199999999999998
]

plt.figure(figsize=(8, 5))

plt.plot(DIM, recall_10k, marker='o', label='NB = 10K')
plt.plot(DIM, recall_20k, marker='o', label='NB = 20K')
plt.plot(DIM, recall_40k, marker='o', label='NB = 40K')

plt.xlabel('Vector Dimension (DIM)')
plt.ylabel('Recall@10')
plt.title('Recall@10 vs DIM — Baseline')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()