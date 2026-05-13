import matplotlib.pyplot as plt

DIM = [50, 100, 150, 200, 250, 300]

# =========================
# BASELINE
# =========================

baseline_p95_10k = [0.577936, 1.003871, 0.737924, 1.369962, 1.248363, 1.395645]
baseline_p95_20k = [1.205857, 1.162140, 1.295159, 1.560850, 1.765148, 1.908542]
baseline_p95_40k = [1.193495, 1.729075, 1.881042, 2.045810, 2.366799, 2.876032]

# =========================
# NPROBE = 4
# =========================

probe4_p95_10k = [0.718130, 0.766281, 0.903561, 1.269165, 1.263102, 1.383370]
probe4_p95_20k = [0.903599, 1.059215, 1.703287, 1.504014, 1.653253, 1.935192]
probe4_p95_40k = [1.322160, 1.635643, 1.961522, 2.320511, 2.772310, 2.961422]

# =========================
# NPROBE = 16
# =========================

probe16_p95_10k = [0.787106, 1.054503, 1.060630, 1.292943, 1.263630, 1.349770]
probe16_p95_20k = [0.934153, 1.024706, 1.373708, 1.604388, 1.744477, 1.929545]
probe16_p95_40k = [1.210840, 1.649106, 2.068186, 2.341548, 2.732380, 2.947263]

# ============================================
# GRAPH 1: BASELINE vs NPROBE = 4
# ============================================

plt.figure(figsize=(9, 5))

plt.plot(DIM, baseline_p95_10k, linestyle=':', marker='o', label='10K Baseline')
plt.plot(DIM, probe4_p95_10k, linestyle='-', marker='o', label='10K nprobe=4')

plt.plot(DIM, baseline_p95_20k, linestyle=':', marker='o', label='20K Baseline')
plt.plot(DIM, probe4_p95_20k, linestyle='-', marker='o', label='20K nprobe=4')

plt.plot(DIM, baseline_p95_40k, linestyle=':', marker='o', label='40K Baseline')
plt.plot(DIM, probe4_p95_40k, linestyle='-', marker='o', label='40K nprobe=4')

plt.xlabel('Vector Dimension (DIM)')
plt.ylabel('Average P95 Latency (ms)')
plt.title('P95 Latency vs DIM: Baseline vs nprobe=4')

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# ============================================
# GRAPH 2: BASELINE vs NPROBE = 16
# ============================================

plt.figure(figsize=(9, 5))

plt.plot(DIM, baseline_p95_10k, linestyle=':', marker='o', label='10K Baseline')
plt.plot(DIM, probe16_p95_10k, linestyle='-', marker='o', label='10K nprobe=16')

plt.plot(DIM, baseline_p95_20k, linestyle=':', marker='o', label='20K Baseline')
plt.plot(DIM, probe16_p95_20k, linestyle='-', marker='o', label='20K nprobe=16')

plt.plot(DIM, baseline_p95_40k, linestyle=':', marker='o', label='40K Baseline')
plt.plot(DIM, probe16_p95_40k, linestyle='-', marker='o', label='40K nprobe=16')

plt.xlabel('Vector Dimension (DIM)')
plt.ylabel('Average P95 Latency (ms)')
plt.title('P95 Latency vs DIM: Baseline vs nprobe=16')

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
