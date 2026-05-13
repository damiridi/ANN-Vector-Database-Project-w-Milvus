import matplotlib.pyplot as plt

# -------------------------------------------------
# Cases:
# B = baseline
# ANN = IVF_FLAT with nprobe = 16
# -------------------------------------------------

cases = [
    "B\nLow Size\nLow NQ",
    "ANN\nLow Size\nLow NQ",
    "B\nLarge Size\nLow NQ",
    "ANN\nLarge Size\nLow NQ",
    "B\nLow Size\nHigh NQ",
    "ANN\nLow Size\nHigh NQ",
    "B\nLarge Size\nHigh NQ",
    "ANN\nLarge Size\nHigh NQ",
]

# -------------------------------------------------
# Color baseline bars red
# ANN bars blue
# -------------------------------------------------

colors = [
    "red", "blue",
    "red", "blue",
    "red", "blue",
    "red", "blue",
]

# -------------------------------------------------
# Total runtimes from cProfile
# -------------------------------------------------

total_runtime = [
    5.703,
    6.377,

    42.938,
    43.013,

    7.308,
    8.027,

    46.574,
    47.071,
]

# -------------------------------------------------
# Raw category times from cProfile output
# -------------------------------------------------

category_times = {
    "Insert / Data Loading": [
        3.353,
        3.419,

        39.612,
        39.018,

        3.376,
        3.407,

        38.541,
        38.644,
    ],

    "Search": [
        0.0,
        0.0,

        0.668,
        0.663,

        0.916,
        0.923,

        1.967,
        1.951,
    ],

    "Milvus / gRPC Overhead": [
        3.508,
        3.570,

        39.883,
        39.229,

        3.875,
        4.030,

        39.964,
        40.005,
    ],

    "PyMilvus Validation Overhead": [
        0.0, 0.0,
        0.0, 0.0,
        0.0, 0.0,
        0.0, 0.0,
    ],

    "Sleep / Waiting": [
        1.007,
        1.510,

        1.008,
        1.516,

        1.006,
        1.516,

        1.010,
        1.511,
    ],
}

# -------------------------------------------------
# Convert category times to percentages
# -------------------------------------------------

category_percentages = {}

for category, times in category_times.items():
    percentages = []

    for time_val, total in zip(times, total_runtime):
        percentages.append((time_val / total) * 100)

    category_percentages[category] = percentages

# -------------------------------------------------
# Plot one chart per category
# -------------------------------------------------

for category, percentages in category_percentages.items():

    plt.figure(figsize=(11, 5))

    plt.bar(cases, percentages, color=colors)

    plt.ylabel("Percent of Total Runtime (%)")
    plt.title(f"{category} as Percentage of Total Runtime")

    plt.xticks(rotation=0)

    plt.grid(axis="y", linestyle="--", alpha=0.6)

    plt.tight_layout()

    plt.show()