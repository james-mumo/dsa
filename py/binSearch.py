def binSearch(arr, target):
    l, r = 0, len(arr)-1

    while l<=r:
        mid = l + (r-l)//2

        if arr[mid]==target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

arr = [1,2,4,6]

print(binSearch(arr, 6))