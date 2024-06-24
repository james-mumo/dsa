arr = [1, 1, 2, 3, 4, 5, 5]

def Max1(arr):
    return max(arr)

print(Max1(arr))

def max2(arr):
    if not arr:
        raise ValueError("Empty")

    mini = arr[0]

    for i in arr[1:]:
        if i < mini:
            mini = i
    return mini


print(max2(arr))


