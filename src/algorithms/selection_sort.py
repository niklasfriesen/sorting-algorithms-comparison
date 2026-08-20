def selection_sort(arr):

    result = arr.copy()
    n = len(result)

    for i in range(n):

        lowest_index = i

        for k in range(i + 1, len(result)):

            if result[k] < result[lowest_index]:
                lowest_index = k

        result[i], result[lowest_index] = result[lowest_index], result[i]

    return result