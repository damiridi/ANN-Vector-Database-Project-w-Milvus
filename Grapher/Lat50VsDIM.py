import matplotlib.pyplot as plt

DIM = [50, 100, 150, 200, 250, 300]

# =========================
# BASELINE
# =========================

baseline_p50_10k = [0.454849, 0.523025, 0.643915, 0.895751, 0.921386, 1.081610]
baseline_p50_20k = [0.602287, 0.952089, 1.077396, 1.393360, 1.458061, 1.609927]
baseline_p50_40k = [0.876302, 1.360995, 1.616609, 1.898158, 2.183682, 2.479935]

# =========================
# NPROBE = 4
# =========================

probe4_p50_10k = [0.481093, 0.558311, 0.650638, 0.840056, 0.895917, 1.177478]
probe4_p50_20k = [0.597674, 0.793415, 1.138455, 1.291800, 1.504362, 1.620263]
probe4_p50_40k = [0.935680, 1.331979, 1.626301, 1.915908, 2.216768, 2.456915]

# =========================
# NPROBE = 16
# =========================

probe16_p50_10k = [0.488907, 0.539738, 0.690919, 0.829560, 0.903779, 1.061380]
probe16_p50_20k = [0.603509, 0.779563, 1.109701, 1.290220, 1.472658, 1.641768]
probe16_p50_40k = [0.888395, 1.303118, 1.633143, 1.895905, 2.198589, 2.484500]

# ============================================
# GRAPH 1: BASELINE vs NPROBE = 4
# ============================================

plt.figure(figsize=(9, 5))

plt.plot(DIM, baseline_p50_10k, linestyle=':', marker='o', label='10K Baseline')
plt.plot(DIM, probe4_p50_10k, linestyle='-', marker='o', label='10K nprobe=4')

plt.plot(DIM, baseline_p50_20k, linestyle=':', marker='o', label='20K Baseline')
plt.plot(DIM, probe4_p50_20k, linestyle='-', marker='o', label='20K nprobe=4')

plt.plot(DIM, baseline_p50_40k, linestyle=':', marker='o', label='40K Baseline')
plt.plot(DIM, probe4_p50_40k, linestyle='-', marker='o', label='40K nprobe=4')

plt.xlabel('Vector Dimension (DIM)')
plt.ylabel('Average P50 Latency (ms)')
plt.title('P50 Latency vs DIM: Baseline vs nprobe=4')

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# ============================================
# GRAPH 2: BASELINE vs NPROBE = 16
# ============================================

plt.figure(figsize=(9, 5))

plt.plot(DIM, baseline_p50_10k, linestyle=':', marker='o', label='10K Baseline')
plt.plot(DIM, probe16_p50_10k, linestyle='-', marker='o', label='10K nprobe=16')

plt.plot(DIM, baseline_p50_20k, linestyle=':', marker='o', label='20K Baseline')
plt.plot(DIM, probe16_p50_20k, linestyle='-', marker='o', label='20K nprobe=16')

plt.plot(DIM, baseline_p50_40k, linestyle=':', marker='o', label='40K Baseline')
plt.plot(DIM, probe16_p50_40k, linestyle='-', marker='o', label='40K nprobe=16')

plt.xlabel('Vector Dimension (DIM)')
plt.ylabel('Average P50 Latency (ms)')
plt.title('P50 Latency vs DIM: Baseline vs nprobe=16')

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
