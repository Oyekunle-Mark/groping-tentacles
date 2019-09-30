def binary_search(list, item):
    start = 0
    end = len(list) - 1

    while start < end:
        midpoint = (start + end) // 2

        if list[midpoint] == item:
            return midpoint

        if list[midpoint] > item:
            end = midpoint - 1
        else:
            start = midpoint + 1

    return None
