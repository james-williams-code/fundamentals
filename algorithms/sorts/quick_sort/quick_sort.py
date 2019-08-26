'''
implement the quick sort algorithm using the lumoto's pationing
use the first value in the list as the pivot
'''






def quick_sort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)

        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low,high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

arr1 = [9,4,7,2,1,8,6]
quick_sort(arr1,0,len(arr1)-1)
print(arr1)
