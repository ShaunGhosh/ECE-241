def findLeftMost(arr, i, n):
    if (2*i+1) < n:
        return findLeftMost(arr, 2*i+1, n)
    else:
        return i


def findRightMost(arr, i , n):
    if (2*i + 2) < n:
        return findRightMost(arr, 2*i + 2, n)
    else:
        return i


arr = [5, 10, 9, 6, 8, 3, 1, 4, 2, 7]
n = len(arr)
i = findLeftMost(arr, 0, n)
r = findRightMost(arr, 0, n)
print("Leftmost node - index: ", i, " value: ", arr[i])
print("Rightmost node - index: ", r, " value: ", arr[r])