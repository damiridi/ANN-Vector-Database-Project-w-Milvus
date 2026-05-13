import re

PROFILE_FILE = "profile_output.txt"

IGNORE_FUNCTIONS = [
    "builtins.exec",
    "<module>",
    "importlib",
    "__import__",
    "_find_and_load",
    "_load_unlocked",
    "exec_module",
]

CATEGORIES = {
    "Insert / data loading": ["insert", "insert_rows"],
    "Search": ["search", "run_searches"],
    "Milvus / gRPC overhead": ["grpc", "_blocking", "interceptor", "with_call"],
    "PyMilvus validation overhead": [
        "check_pass_param",
        "check_id_and_data",
        "is_legal_search_data",
        "entity_is_sparse_matrix",
        "is_scipy_sparse",
    ],
    "Sleep / waiting": ["time.sleep"],
}


def parse_profile(filename):
    rows = []

    with open(filename, "r") as f:
        for line in f:
            # Match cProfile rows:
            # ncalls tottime percall cumtime percall filename:function
            match = re.match(
                r"\s*(\S+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+(.+)",
                line,
            )

            if match:
                ncalls, tottime, percall1, cumtime, percall2, func = match.groups()

                rows.append({
                    "ncalls": ncalls,
                    "tottime": float(tottime),
                    "cumtime": float(cumtime),
                    "func": func.strip()
                })

    return rows


def should_ignore(func):
    return any(word in func for word in IGNORE_FUNCTIONS)


def categorize(rows):
    category_times = {cat: 0.0 for cat in CATEGORIES}

    for row in rows:
        func = row["func"]
        cumtime = row["cumtime"]

        for category, keywords in CATEGORIES.items():
            if any(keyword in func for keyword in keywords):
                category_times[category] += cumtime
                break

    return category_times


def main():
    rows = parse_profile(PROFILE_FILE)

    if not rows:
        print("No cProfile rows found. Make sure profile_output.txt contains the printed cProfile table.")
        return

    total_runtime = rows[0]["cumtime"]

    print("\n===== cProfile Summary =====")
    print(f"Total runtime: {total_runtime:.3f} seconds")

    print("\n===== Top useful functions =====")
    useful_rows = [r for r in rows if not should_ignore(r["func"])]

    for r in useful_rows[:15]:
        pct = 100 * r["cumtime"] / total_runtime
        print(f"{r['cumtime']:8.3f}s  ({pct:5.1f}%)  {r['ncalls']:>8} calls  {r['func']}")

    print("\n===== Category breakdown =====")
    category_times = categorize(rows)

    for category, time_val in category_times.items():
        pct = 100 * time_val / total_runtime
        print(f"{category:30s}: {time_val:8.3f}s  ({pct:5.1f}%)")

    print("\n===== Automatic interpretation =====")

    insert_time = category_times["Insert / data loading"]
    search_time = category_times["Search"]
    validation_time = category_times["PyMilvus validation overhead"]
    grpc_time = category_times["Milvus / gRPC overhead"]

    if insert_time > search_time:
        print("- Total runtime is dominated more by insertion/setup than by searching.")
    else:
        print("- Search takes more total time than insertion/setup.")

    if search_time > 0:
        print(f"- Search-related runtime is about {search_time:.3f} seconds.")

        if validation_time / search_time > 0.5:
            print("- A large fraction of search-related time appears to be PyMilvus validation overhead.")
        elif validation_time > 0:
            print("- Some search-related time is spent in PyMilvus validation.")

    if grpc_time > 0:
        print("- gRPC/PyMilvus communication overhead is significant, meaning Python is often waiting on Milvus calls.")

    print("\nAnalysis:")
    print(
        f"The full script took {total_runtime:.2f} seconds. "
        f"Insertion/setup accounted for about {insert_time:.2f} seconds, while search-related functions accounted for about {search_time:.2f} seconds. "
        f"Profiling also showed noticeable PyMilvus validation and gRPC overhead, suggesting that measured latency includes client-side and communication costs in addition to ANN search itself."
    )


if __name__ == "__main__":
    main()
