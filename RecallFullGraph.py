import matplotlib.pyplot as plt

NB = [
    2500, 5000, 7500, 10000,
    12500, 15000, 17500, 20000,
    22500, 25000, 27500, 30000,
    32500, 35000, 37500, 40000
]

recall = [
    0.6025,
    0.5980,
    0.5740,
    0.5650,
    0.5715,
    0.5590,
    0.5540,
    0.5610,
    0.5420,
    0.5270,
    0.5360,
    0.5365,
    0.5265,
    0.5180,
    0.5300,
    0.5315
]

plt.figure(figsize=(8, 5))
plt.plot(NB, recall, marker='o')

plt.xlabel('Number of Database Vectors (NB)')
plt.ylabel('Recall@10')
plt.title('Recall@10 vs Database Size')
plt.grid(True)

plt.show()