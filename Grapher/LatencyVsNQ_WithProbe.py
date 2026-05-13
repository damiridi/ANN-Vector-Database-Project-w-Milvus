import matplotlib.pyplot as plt

NQ = [200, 400, 600, 800, 1000]
NPROBE = 4

# With nprobe = 4
p50_10k = [0.6242632865905762, 0.5708396434783936, 0.6547331809997559, 0.5830764770507812, 0.5721569061279297]
p50_20k = [0.9522855281829834, 0.966864824295044, 0.9451150894165039, 0.9341180324554443, 0.9346365928649902]
p50_40k = [1.5148580074310303, 1.537090539932251, 1.4879822731018066, 1.450967788696289, 1.472228765487671]

p95_10k = [1.1172747611999512, 0.8405667543411253, 0.848094820976257, 0.7309794425964355, 0.806037187576294]
p95_20k = [1.212860345840454, 1.2471723556518555, 1.084572672843933, 1.1304789781570432, 1.0421890020370483]
p95_40k = [1.6498816013336182, 1.817474365234375, 1.6376054286956783, 1.5527212619781494, 1.5831589698791504]

# -------------------------
# P50 plot
# -------------------------
plt.figure(figsize=(8, 5))
plt.plot(NQ, p50_10k, marker='o', label='NB = 10K')
plt.plot(NQ, p50_20k, marker='o', label='NB = 20K')
plt.plot(NQ, p50_40k, marker='o', label='NB = 40K')

plt.xlabel('Number of Queries (NQ)')
plt.ylabel('Average P50 Latency (ms)')
plt.title(f'P50 Latency vs NQ — nprobe = {NPROBE}')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------
# P95 plot
# -------------------------
plt.figure(figsize=(8, 5))
plt.plot(NQ, p95_10k, marker='o', label='NB = 10K')
plt.plot(NQ, p95_20k, marker='o', label='NB = 20K')
plt.plot(NQ, p95_40k, marker='o', label='NB = 40K')

plt.xlabel('Number of Queries (NQ)')
plt.ylabel('Average P95 Latency (ms)')
plt.title(f'P95 Latency vs NQ — nprobe = {NPROBE}')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
