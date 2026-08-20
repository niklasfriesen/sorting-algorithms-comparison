def bubble_sort(arr: list) -> list:

    result = arr.copy()
    n = len(result)

    for i in range(n):

        is_sorted = True

        for k in range(n - i - 1, ): # i elements are already sorted
            if result[k] > result[ k +1]:
                is_sorted = False
                result[k], result[ k +1] = result[ k +1], result[k]

        # Early exit when already sorted
        if is_sorted:
            break

    return result