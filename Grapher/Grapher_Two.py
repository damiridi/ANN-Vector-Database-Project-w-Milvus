import matplotlib.pyplot as plt

nprobe_10k = [1, 4, 8, 16, 32]
recall_10k = [0.565, 0.565, 0.565, 0.565, 0.565]

nprobe_20k = [1, 4]
recall_20k = [0.561, 0.561]

plt.figure(figsize=(7,5))
plt.plot(nprobe_10k, recall_10k, marker='o', label='NB = 10,000')
plt.plot(nprobe_20k, recall_20k, marker='o', label='NB = 20,000')
plt.xlabel('nprobe')
plt.ylabel('Recall@10')
plt.title('Effect of nprobe on ANN Recall')
plt.legend()
plt.grid(True)
plt.show()
