import random
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # render to file without needing a display
import matplotlib.pyplot as plt

from src.algorithms.bubble_sort import bubble_sort
from src.algorithms.heap_sort import heap_sort
from src.algorithms.insertion_sort import insertion_sort
from src.algorithms.merge_sort import merge_sort
from src.algorithms.quick_sort import quick_sort
from src.algorithms.selection_sort import selection_sort

ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Heap Sort": heap_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Selection Sort": selection_sort,
}

# Input size -> number of runs to average over (fewer repeats for larger,
# slower inputs so the O(n^2) algorithms don't dominate total runtime).
SIZES_AND_REPEATS = {
    100: 5,
    1_000: 3,
    5_000: 2,
    10_000: 1,
}

OUTPUT_PATH = Path(__file__).resolve().parent.parent / "benchmark_results.png"


def measure(sort_fn, data: list, repeats: int) -> float:
    total = 0.0
    for _ in range(repeats):
        start = time.perf_counter()
        sort_fn(data)
        total += time.perf_counter() - start
    return total / repeats


def run_benchmark() -> dict:
    random.seed(42)
    results = {name: [] for name in ALGORITHMS}

    for size, repeats in SIZES_AND_REPEATS.items():
        data = [random.randint(-1_000_000, 1_000_000) for _ in range(size)]
        print(f"n = {size}")

        for name, sort_fn in ALGORITHMS.items():
            avg_time = measure(sort_fn, data, repeats)
            results[name].append(avg_time)
            run_label = "run" if repeats == 1 else "runs"
            print(f"  {name:<15} {avg_time:.6f} s (avg of {repeats} {run_label})")

    return results


def plot_results(results: dict) -> None:
    sizes = list(SIZES_AND_REPEATS.keys())

    plt.figure(figsize=(9, 6))
    for name, times in results.items():
        plt.plot(sizes, times, marker="o", label=name)

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input size (n)")
    plt.ylabel("Average runtime (s)")
    plt.title("Sorting algorithm runtime comparison")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    print(f"\nChart saved to {OUTPUT_PATH}")


def main() -> None:
    results = run_benchmark()
    plot_results(results)


if __name__ == "__main__":
    main()
