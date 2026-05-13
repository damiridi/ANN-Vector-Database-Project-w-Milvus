import matplotlib.pyplot as plt

NQ = [200, 400, 600, 800, 1000]

# No nprobe / baseline
p50_10k = [0.672680139541626, 0.5727529525756836, 0.5630016326904297, 0.557166337966919, 0.5736589431762695]
p50_20k = [0.9199023246765137, 0.9627461433410645, 0.98610520362854, 0.9489834308624268, 0.9248793125152588]
p50_40k = [1.482391357421875, 1.5330910682678223, 1.4641404151916504, 1.467519998550415, 1.4529883861541748]

p95_10k = [0.8095407485961912, 0.8163362741470335, 0.7846653461456297, 0.769728422164917, 0.8006840944290161]
p95_20k = [1.1814570426940916, 1.2290328741073608, 1.2585121393203735, 1.0941064357757568, 1.0204410552978516]
p95_40k = [1.9048839807510372, 1.7317712306976318, 1.718975901603698, 1.5772122144699097, 1.5583759546279907]

# -------------------------
# P50 plot
# -------------------------
plt.figure(figsize=(8, 5))
plt.plot(NQ, p50_10k, marker='o', label='NB = 10K')
plt.plot(NQ, p50_20k, marker='o', label='NB = 20K')
plt.plot(NQ, p50_40k, marker='o', label='NB = 40K')

plt.xlabel('Number of Queries (NQ)')
plt.ylabel('Average P50 Latency (ms)')
plt.title('P50 Latency vs NQ — No nprobe')
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
plt.title('P95 Latency vs NQ — No nprobe')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()