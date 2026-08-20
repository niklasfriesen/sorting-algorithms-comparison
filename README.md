# sorting-algorithms-comparison
Runtime and complexity comparison of different sorting algorithms with benchmarks across different input sizes.


## Algorithms
Implemented in [src/algorithms/](src/algorithms/):
- Bubble Sort
- Heap Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Selection Sort


## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Running the benchmark
```bash
python3 -m src.benchmark
```
This prints timing results per algorithm and input size, then writes a runtime
comparison chart to `benchmark_results.png`.

## Running the tests
```bash
hash -r
pytest
```