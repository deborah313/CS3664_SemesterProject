def Insertionsort(arr):

    Replace = []

    for i in range(1, len(arr)):
        value = arr[i]

        while arr[i-1] > value and i > 0:
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp

            i = i - 1
    
    return arr



def Quicksort(arr):

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    lower =[]
    higher = []

    for i in range(0,len(arr)):
        if pivot > arr[i]:
            higher.append(arr[i])
        else:
            lower.append(arr[i])




    return Quicksort(higher) + [pivot] + Quicksort(lower)


print(Insertionsort([1,6,8,4,7,3,4,8,4,4,6]))
print(Quicksort([1,6,8,4,7,3,4,8,4,4,6]))

