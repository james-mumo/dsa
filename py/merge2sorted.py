# def mergeTwoArrays(arr1, arr2):
#     result = []
#     i, j, = 0, 0
#
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] <= arr2[j]:
#             result.append(arr1[i])
#             i += 1
#         else:
#             result.append(arr2[j])
#             j += 1
#
#     while i < len(arr1):
#         result.append(arr1[i])
#         i += 1
#
#     while j < len(arr2):
#         result.append(arr2[j])
#         j += 1
#
#     return result
#
#
# arr1 = [1, 3, 5, 7]
# arr2 = [2, 4, 6, 8, 9]
#
# print(mergeTwoArrays(arr1, arr2))


def merge(arr1, arr2):
    l, r = 0, 0
    res = []

    while l <= len(arr1) and r <= len(arr2):
        if arr1[l] <= arr2[r]:
            res.append(arr1[l])
        else:
            # arr2[r]<=arr1[l]:
            res.append(arr2[r])
    return res


arr1 = [1, 2, 3]
arr2 = [2, 33, 44]

print(merge(arr1, arr2))
