import matplotlib.pyplot as plt

nprobe_10k = [1, 4, 8, 16, 32]
p50_10k = [0.634, 0.658, 0.611, 0.606, 0.591]

nprobe_20k = [1, 4]
p50_20k = [1.003, 0.966]

plt.figure(figsize=(7,5))
plt.plot(nprobe_10k, p50_10k, marker='o', label='NB = 10,000')
plt.plot(nprobe_20k, p50_20k, marker='o', label='NB = 20,000')
plt.xlabel('nprobe')
plt.ylabel('Average P50 Latency (ms)')
plt.title('Effect of nprobe on ANN Query Latency')
plt.legend()
plt.grid(True)
plt.show()