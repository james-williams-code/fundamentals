'''
implement the quick select algorithm
this is very simliar to quick sort
the idea is to select a pivot index and find which
side k is on in an array.  We then only look on that side of the array
for the value
'''

def quick_select(arr,left,right,k):
    if left == right:
        return arr[left]

    pi = partition(arr,left,right)

    if pi == k:
        return arr[pi]
    if k < pi:
        return quick_select(arr,left,pi-1,k)
    else:
        return quick_select(arr,pi+1,right,k)

def partition(arr,left,right):
    i = left
    pivot = arr[right]
    for j in range(left,right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

arr1 = [3,6,4,7,8,9,2]
k = 2
print(quick_select(arr1,0,len(arr1)-1,k))
print(arr1)
