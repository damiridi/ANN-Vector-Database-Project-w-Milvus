import matplotlib.pyplot as plt

NQ = [200, 400, 600, 800, 1000]
NPROBE = 4

# Std P50
std_p50_10k = [0.07940232792903956, 0.008308423544493427, 0.03534351587448121, 0.02559061684469401, 0.023671897437840074]
std_p50_20k = [0.010087266861260985, 0.03756986766640808, 0.02998068839510234, 0.004785250799927206, 0.02607688154449604]
std_p50_40k = [0.04773924209794021, 0.027009480921512556, 0.047961630665236545, 0.016421416057664416, 0.0361604923605105]

# Std P95
std_p95_10k = [1.4366011804426744, 0.6120421113161096, 0.10507601900911301, 0.09670849974239229, 0.379600736149942]
std_p95_20k = [0.6372237151369203, 0.5606937087172411, 0.08184311369043097, 0.43448368700601764, 0.06022580129160894]
std_p95_40k = [0.08271796614776636, 0.5857980574890466, 0.12136730232898801, 0.06491285811952287, 0.07805711678261963]

# -------- P50 STD --------
plt.figure(figsize=(8, 5))
plt.plot(NQ, std_p50_10k, marker='o', label='NB = 10K')
plt.plot(NQ, std_p50_20k, marker='o', label='NB = 20K')
plt.plot(NQ, std_p50_40k, marker='o', label='NB = 40K')

plt.xlabel('Number of Queries (NQ)')
plt.ylabel('Std Dev of P50 Latency (ms)')
plt.title(f'P50 Latency Std Dev vs NQ — nprobe = {NPROBE}')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -------- P95 STD --------
plt.figure(figsize=(8, 5))
plt.plot(NQ, std_p95_10k, marker='o', label='NB = 10K')
plt.plot(NQ, std_p95_20k, marker='o', label='NB = 20K')
plt.plot(NQ, std_p95_40k, marker='o', label='NB = 40K')

plt.xlabel('Number of Queries (NQ)')
plt.ylabel('Std Dev of P95 Latency (ms)')
plt.title(f'P95 Latency Std Dev vs NQ — nprobe = {NPROBE}')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()