import matplotlib.pyplot as plt

NQ = [200, 400, 600, 800, 1000]

# No probe / baseline
p50_no_10k = [0.672680139541626, 0.5727529525756836, 0.5630016326904297, 0.557166337966919, 0.5736589431762695]
p50_no_20k = [0.9199023246765137, 0.9627461433410645, 0.98610520362854, 0.9489834308624268, 0.9248793125152588]
p50_no_40k = [1.482391357421875, 1.5330910682678223, 1.4641404151916504, 1.467519998550415, 1.4529883861541748]

p95_no_10k = [0.8095407485961912, 0.8163362741470335, 0.7846653461456297, 0.769728422164917, 0.8006840944290161]
p95_no_20k = [1.1814570426940916, 1.2290328741073608, 1.2585121393203735, 1.0941064357757568, 1.0204410552978516]
p95_no_40k = [1.9048839807510372, 1.7317712306976318, 1.718975901603698, 1.5772122144699097, 1.5583759546279907]

# With nprobe = 4
p50_probe_10k = [0.6242632865905762, 0.5708396434783936, 0.6547331809997559, 0.5830764770507812, 0.5721569061279297]
p50_probe_20k = [0.9522855281829834, 0.966864824295044, 0.9451150894165039, 0.9341180324554443, 0.9346365928649902]
p50_probe_40k = [1.5148580074310303, 1.537090539932251, 1.4879822731018066, 1.450967788696289, 1.472228765487671]

p95_probe_10k = [1.1172747611999512, 0.8405667543411253, 0.848094820976257, 0.7309794425964355, 0.806037187576294]
p95_probe_20k = [1.212860345840454, 1.2471723556518555, 1.084572672843933, 1.1304789781570432, 1.0421890020370483]
p95_probe_40k = [1.6498816013336182, 1.817474365234375, 1.6376054286956783, 1.5527212619781494, 1.5831589698791504]

# P50 graph
plt.figure(figsize=(9, 5))
plt.plot(NQ, p50_no_10k, marker='o', linestyle=':', label='10K no probe')
plt.plot(NQ, p50_probe_10k, marker='o', linestyle='-', label='10K nprobe=4')

plt.plot(NQ, p50_no_20k, marker='o', linestyle=':', label='20K no probe')
plt.plot(NQ, p50_probe_20k, marker='o', linestyle='-', label='20K nprobe=4')

plt.plot(NQ, p50_no_40k, marker='o', linestyle=':', label='40K no probe')
plt.plot(NQ, p50_probe_40k, marker='o', linestyle='-', label='40K nprobe=4')

plt.xlabel('Number of Queries (NQ)')
plt.ylabel('Average P50 Latency (ms)')
plt.title('P50 Latency vs NQ: No Probe vs nprobe=4')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# P95 graph
plt.figure(figsize=(9, 5))
plt.plot(NQ, p95_no_10k, marker='o', linestyle=':', label='10K no probe')
plt.plot(NQ, p95_probe_10k, marker='o', linestyle='-', label='10K nprobe=4')

plt.plot(NQ, p95_no_20k, marker='o', linestyle=':', label='20K no probe')
plt.plot(NQ, p95_probe_20k, marker='o', linestyle='-', label='20K nprobe=4')

plt.plot(NQ, p95_no_40k, marker='o', linestyle=':', label='40K no probe')
plt.plot(NQ, p95_probe_40k, marker='o', linestyle='-', label='40K nprobe=4')

plt.xlabel('Number of Queries (NQ)')
plt.ylabel('Average P95 Latency (ms)')
plt.title('P95 Latency vs NQ: No Probe vs nprobe=4')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()