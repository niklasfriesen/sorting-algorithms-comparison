def insertion_sort(arr: list) -> list:

    result = arr.copy()
    n = len(result)

    for i in range(n):

        current = result[i]
        k = i - 1

        while k >= 0 and result[k] > current:
            result[k + 1] = result[k]
            k -= 1

        result[k + 1] = current

    return result
