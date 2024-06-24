arr = [1, 1, 2, 3, 4, 5, 5]


def rem(arr):
    return list(set(arr))


# print(rem(arr))

def rem2(arr):
    seen = set()
    fin = []

    for i in arr:
        if i not in fin:
            # seen.add(i)
            fin.append(i)
    return fin


print(rem2(arr))
