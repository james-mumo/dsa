def linSearch(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


arr = [1, 2, 3, 4, 5]


# print(linSearch(arr, 2))


def binSearch(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = l+(r - l) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

arr = [1, 2, 3, 4, 5]
print(binSearch(arr, 4))

print(3//2)
