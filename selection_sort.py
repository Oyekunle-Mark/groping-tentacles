def find_index_of_minimum(arr):
    minimum = arr[0]
    index_of_minimum = 0

    for index, item in enumerate(arr):
        if item < minimum:
            minimum = item
            index_of_minimum = index

    return index_of_minimum


def selection_sort(arr):
    sorted_arr = []

    for _ in range(len(arr)):
        index_of_minimum = find_index_of_minimum(arr)
        sorted_arr.append(arr.pop(index_of_minimum))

    return sorted_arr


print(selection_sort([5, 3, 6, 2, 10]))
