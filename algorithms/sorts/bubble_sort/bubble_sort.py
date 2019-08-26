def bubble_sort(arr):
    #start at the back of the list
    #for each element if selected is les than ith move the elements forward one
    #once find elementn that it is greater than, add it to the empty spot we just moved the element from

    for i in range(0,len(arr)):
        print('next i ' + str(arr[i]))
        for j in range(len(arr)-1,i,-1):
            print('next j ' + str(arr[j]))
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return(arr)

arr1 = [3,7,2,4]
print(bubble_sort(arr1))
