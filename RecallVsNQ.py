import matplotlib.pyplot as plt

NQ = [200, 400, 600, 800, 1000]

# Recall@10 values from your 20-run averages
recall_10k = [
    0.5649999999999997,
    0.5669999999999987,
    0.5604999999999991,
    0.561,
    0.5656000000000013
]

recall_20k = [
    0.5609999999999997,
    0.5614999999999994,
    0.5583333333333339,
    0.5588750000000017,
    0.5575000000000014
]

recall_40k = [
    0.5314999999999998,
    0.5364999999999996,
    0.5294999999999999,
    0.5278750000000001,
    0.528600000000001
]

plt.figure(figsize=(8, 5))

plt.plot(NQ, recall_10k, marker='o', label='NB = 10K')
plt.plot(NQ, recall_20k, marker='o', label='NB = 20K')
plt.plot(NQ, recall_40k, marker='o', label='NB = 40K')

plt.xlabel('Number of Queries (NQ)')
plt.ylabel('Recall@10')
plt.title('Recall@10 vs NQ')
plt.legend()
plt.grid(True)

plt.ylim(0.52, 0.58)
plt.tight_layout()
plt.show()