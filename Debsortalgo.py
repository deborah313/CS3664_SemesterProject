def Insertionsort(arr):

    for i in range(1, len(arr)): #Starts comparisons from the second element in the array
        value = arr[i]              #assigning the value we are comparing

        while arr[i-1] > value and i > 0: #comparing the value variable to the elements before it, without the -1 index bc python will wrap around
            temp = arr[i]       # using the 3 lines below to just swap out their positions, if left number in array is larger then value
            arr[i] = arr[i-1]
            arr[i-1] = temp

            i = i - 1   #decrements the i value to make sure we check all values to the left of value in array
    
    return arr          #returns our sorted array



def Quicksort(arr):

    if len(arr) <= 1:           #if we have 0 or 1 items in our array, then we return it and exit
        return arr
    else:
        pivot = arr.pop(0)       #this will remove the first element of the array and make it our pivot

    lower =[]                   #initializing 2 empty lists/arr for numbers higher/lower than our pivot
    higher = []

    for i in range(0,len(arr)): #we go through the array
        if pivot > arr[i]:      #if pivot is higher than index then we append it to the higher list
            higher.append(arr[i])
        else:
            lower.append(arr[i])    #if pivot is lower than index then we append it to the lower list




    return Quicksort(higher) + [pivot] + Quicksort(lower)   #we call the quicksort on the higher and lower arrays and concatenate the fixed pivot values




print(Insertionsort([1,6,8,4,7,3,4,8,4,4,6]))
print(Quicksort([1,6,8,4,7,3,4,8,4,4,6]))

