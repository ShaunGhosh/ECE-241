
def merge2List(alist, lefthalf, righthalf, i, j, pos):

    comparison = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[pos] = righthalf[j]
            j += 1
        else:
            alist[pos] = lefthalf[i]
            i += 1
        comparison += 1
        pos += 1

    while i < len(lefthalf):
        alist[pos] = lefthalf[i]
        i = i + 1
        pos += 1

    while j < len(righthalf):
        alist[pos]=righthalf[j]
        j=j+1
        pos += 1
    return comparison


def mergeSort_3_way(alist):
    comparison = 0

    if len(alist) == 2:
      if alist[0] < alist[1]:
        y = alist[1]
        alist[1] = alist[0]
        alist[0] = y
      comparison += 1

    if len(alist) > 2:
        x = len(alist) // 3
        firsthalf = alist[:x]
        secondhalf = alist[x:2*x]
        thirdhalf = alist[2*x:]

        mergeSort_3_way(firsthalf)
        mergeSort_3_way(secondhalf)
        mergeSort_3_way(thirdhalf)

        i = 0
        j = 0
        k = 0
        pos = 0

        while i < len(firsthalf) and j < len(secondhalf) and k < len(thirdhalf):
            if firsthalf[i] < secondhalf[j]:
                if thirdhalf[k] < secondhalf[j]:
                    alist[pos] = secondhalf[j]
                    j += 1
                else:
                    alist[pos] = thirdhalf[k]
                    k += 1
            else:
                if thirdhalf[k] < firsthalf[i]:
                    alist[pos] = firsthalf[i]
                    i += 1
                else:
                    alist[pos] = thirdhalf[k]
                    k += 1

            pos += 1
            comparison += 2

        if j == len(secondhalf):
            merge2List(alist, firsthalf, thirdhalf, i, k, pos)
            comparison = comparison + 1
        elif i == len(firsthalf):
            merge2List(alist, secondhalf, thirdhalf, j, k, pos)
            comparison = comparison + 1
        else:
            merge2List(alist, firsthalf, secondhalf, i, j, pos)
            comparison = comparison + 1

        print(comparison)


alist = [5, 10, 9, 6, 8, 3, 1, 4, 2, 7]
mergeSort_3_way(alist)
print(alist)
