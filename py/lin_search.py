arr = [2, 3, 4, 5, 6]


def search(a, k):
    for x in range(len(a)):
        if a[x] == k:
            return x
    return -1
    # if k in a:
    #     return True
    # else:
    #     return False


print(search(arr, 3))
