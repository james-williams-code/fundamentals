def selection_sort(arr):
    #select the first element in the list
    #set it to min
    #search through the rest of the list checking if the value you have is the min
    #if find less tahn min, becomes new min
    #insert the element into the list, swapping with the orginal first
    for i in range (0,len(arr)):
        min = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

arr1 = [9,4,3,7,2,5]
print(selection_sort(arr1))
