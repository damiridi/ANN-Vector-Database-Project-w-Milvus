import matplotlib.pyplot as plt

NQ = [200, 400, 600, 800, 1000]

# No probe / baseline
std_p50_no_10k = [0.03625427272758121, 0.020369669120208374, 0.01090101003484549, 0.008192313126461242, 0.04233889730354204]
std_p50_no_20k = [0.009095606297469517, 0.045607173129302146, 0.034504396793588174, 0.04905563331144589, 0.005185463645830783]
std_p50_no_40k = [0.039973962447255935, 0.07072145231347646, 0.018809167189652306, 0.017971348002932985, 0.02046624144369575]

std_p95_no_10k = [0.10635554082162313, 0.4961388098437009, 0.454037420624234, 0.43453102673198024, 0.36548574224927016]
std_p95_no_20k = [0.6436068676231298, 0.5482739682617447, 0.49455249052113553, 0.11981855386559262, 0.028973570405515358]
std_p95_no_40k = [1.3828325719475985, 0.11756541813078764, 0.621598131861313, 0.07157744089452561, 0.056218316136382396]

# With nprobe = 4
std_p50_probe_10k = [0.07940232792903956, 0.008308423544493427, 0.03534351587448121, 0.02559061684469401, 0.023671897437840074]
std_p50_probe_20k = [0.010087266861260985, 0.03756986766640808, 0.02998068839510234, 0.004785250799927206, 0.02607688154449604]
std_p50_probe_40k = [0.04773924209794021, 0.027009480921512556, 0.047961630665236545, 0.016421416057664416, 0.0361604923605105]

std_p95_probe_10k = [1.4366011804426744, 0.6120421113161096, 0.10507601900911301, 0.09670849974239229, 0.379600736149942]
std_p95_probe_20k = [0.6372237151369203, 0.5606937087172411, 0.08184311369043097, 0.43448368700601764, 0.06022580129160894]
std_p95_probe_40k = [0.08271796614776636, 0.5857980574890466, 0.12136730232898801, 0.06491285811952287, 0.07805711678261963]

# P50 std graph
plt.figure(figsize=(9, 5))
plt.plot(NQ, std_p50_no_10k, marker='o', linestyle=':', label='10K no probe')
plt.plot(NQ, std_p50_probe_10k, marker='o', linestyle='-', label='10K nprobe=4')

plt.plot(NQ, std_p50_no_20k, marker='o', linestyle=':', label='20K no probe')
plt.plot(NQ, std_p50_probe_20k, marker='o', linestyle='-', label='20K nprobe=4')

plt.plot(NQ, std_p50_no_40k, marker='o', linestyle=':', label='40K no probe')
plt.plot(NQ, std_p50_probe_40k, marker='o', linestyle='-', label='40K nprobe=4')

plt.xlabel('Number of Queries (NQ)')
plt.ylabel('Std Dev of P50 Latency (ms)')
plt.title('P50 Latency Std Dev vs NQ: No Probe vs nprobe=4')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# P95 std graph
plt.figure(figsize=(9, 5))
plt.plot(NQ, std_p95_no_10k, marker='o', linestyle=':', label='10K no probe')
plt.plot(NQ, std_p95_probe_10k, marker='o', linestyle='-', label='10K nprobe=4')

plt.plot(NQ, std_p95_no_20k, marker='o', linestyle=':', label='20K no probe')
plt.plot(NQ, std_p95_probe_20k, marker='o', linestyle='-', label='20K nprobe=4')

plt.plot(NQ, std_p95_no_40k, marker='o', linestyle=':', label='40K no probe')
plt.plot(NQ, std_p95_probe_40k, marker='o', linestyle='-', label='40K nprobe=4')

plt.xlabel('Number of Queries (NQ)')
plt.ylabel('Std Dev of P95 Latency (ms)')
plt.title('P95 Latency Std Dev vs NQ: No Probe vs nprobe=4')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
