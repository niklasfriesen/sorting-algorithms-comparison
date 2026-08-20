
def heap_sort(arr: list) -> list:

    result = arr.copy()
    n = len(result)

    for i in range(n // 2 - 1, -1, -1):
        _heapify(result, n, i)

    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        _heapify(result, i, 0)

    return result


def _heapify(arr: list, heap_size: int, root: int) -> None:

    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        _heapify(arr, heap_size, largest)
