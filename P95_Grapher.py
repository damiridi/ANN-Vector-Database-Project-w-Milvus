import matplotlib.pyplot as plt

# NB = 10k
nprobe_10k = [1, 4, 8, 16, 32]
p95_10k = [4.817, 5.520, 4.091, 4.597, 4.919]

# NB = 20k
nprobe_20k = [1, 4]
p95_20k = [3.771, 3.840]

plt.figure(figsize=(7,5))
plt.plot(nprobe_10k, p95_10k, marker='o', label='NB = 10,000')
plt.plot(nprobe_20k, p95_20k, marker='o', label='NB = 20,000')

plt.xlabel('nprobe')
plt.ylabel('P95 Latency (ms)')
plt.title('Effect of nprobe on P95 Latency')
plt.legend()
plt.grid(True)

plt.show()