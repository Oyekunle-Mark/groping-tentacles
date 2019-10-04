def quick_sort(arr):
    """Implementation of the quick sort algorithm

    Arguments:
        arr {list} -- array to be sorted

    Returns:
        list -- the sorted list
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [num for num in arr[1:] if num < pivot]
        greater_than_pivot = [num for num in arr[1:] if num > pivot]

        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


print(quick_sort([5, 3, 6, 2, 10]))
print(quick_sort([12, 3, 232, 32, -3, 0, 23, -2, 2]))
