def binary_search(list, item):
    start = 0
    end = len(list) - 1

    while start <= end:
        midpoint = (start + end) // 2
        # print(midpoint)

        if list[midpoint] == item:
            return midpoint

        if list[midpoint] > item:
            end = midpoint - 1
        else:
            start = midpoint + 1

    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -2))
print(binary_search(my_list, 9))
print(binary_search([1, 2, 3, 4, 6, 9, 10, 99], 10))
