def insertion_sort(arr,n):
    # walk the list from from to back
    # with each element compare it to the next element
    # if the element is less than then move the elements down and continue to compare
    #else put the element in the current open position
    if n <= 0:
        return
    insertion_sort(arr, n-1)
    j = n - 1
    while j >= 0 and arr[j] > arr[j + 1]:
        arr[j + 1],arr[j] = arr[j],arr[j + 1]
        j = j-1
    return arr

def insertion_sort_opt(arr,n):
    #in this version we will shift the elements instead of
    #swapping every element
    if n <= 0:
        return
    insertion_sort_opt(arr,n-1)
    j = n - 1
    nth = arr[n]
    while j >= 0 and arr[j] > nth:
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = nth
    return arr

def insertion_sort_itr(arr,n):
    #in this version we remove the recursive step
    #and add an iterative for loop
    if n <= 0:
        return
    for i in range(1,n):
        j = i - 1
        ith = arr[n]
        while j >= 0 and arr[j] > ith:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = ith
    return arr

arr1 = [7,3,8,4,2,5]
print(insertion_sort(arr1,len(arr1)-1))
print(insertion_sort_opt(arr1,len(arr1)-1))
print(insertion_sort_itr(arr1,len(arr1)-1))



