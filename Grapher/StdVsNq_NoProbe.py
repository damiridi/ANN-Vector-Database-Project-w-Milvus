import matplotlib.pyplot as plt

NQ = [200, 400, 600, 800, 1000]

# Std P50
std_p50_10k = [0.03625427272758121, 0.020369669120208374, 0.01090101003484549, 0.008192313126461242, 0.04233889730354204]
std_p50_20k = [0.009095606297469517, 0.045607173129302146, 0.034504396793588174, 0.04905563331144589, 0.005185463645830783]
std_p50_40k = [0.039973962447255935, 0.07072145231347646, 0.018809167189652306, 0.017971348002932985, 0.02046624144369575]

# Std P95
std_p95_10k = [0.10635554082162313, 0.4961388098437009, 0.454037420624234, 0.43453102673198024, 0.36548574224927016]
std_p95_20k = [0.6436068676231298, 0.5482739682617447, 0.49455249052113553, 0.11981855386559262, 0.028973570405515358]
std_p95_40k = [1.3828325719475985, 0.11756541813078764, 0.621598131861313, 0.07157744089452561, 0.056218316136382396]

# -------- P50 STD --------
plt.figure(figsize=(8, 5))
plt.plot(NQ, std_p50_10k, marker='o', label='NB = 10K')
plt.plot(NQ, std_p50_20k, marker='o', label='NB = 20K')
plt.plot(NQ, std_p50_40k, marker='o', label='NB = 40K')

plt.xlabel('Number of Queries (NQ)')
plt.ylabel('Std Dev of P50 Latency (ms)')
plt.title('P50 Latency Std Dev vs NQ — No nprobe')
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
plt.title('P95 Latency Std Dev vs NQ — No nprobe')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
