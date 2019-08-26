'''
Implement the merge_k_sorted using heap sort
'''

def merge_k_sorted(arrs):
    arr = []
    for a in arrs:
        print(a)
        arr.extend(a)
    for i in range(len(arr),0,-1):
        arr = heapify_down(arr,0)
    return arr

def heap_sort_up(arr):
    if len(arr) > 1:
        end = len(arr) - 1
        for j in range(end,0,-1):
            print(arr)
            if arr[j] < arr[j//2]:
                arr[j], arr[j//2] = arr[j//2], arr[j]
    return arr

def heapify_down(arr,i):
    if len(arr) > 1:
        end = len(arr)
        #for i in range(len(arr)-1,0,-1):
        smallest = i
        left = 2*i+1
        right = 2*i+2
        if left < end and arr[left] < arr[smallest]:
            smallest = left
        if right < end and arr[right] < arr[smallest]:
            smallest = right
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            heapify_down(arr,smallest)
    return arr


arr1 = [[1,3,5,7],[2,4,6,8]]
r1 = merge_k_sorted(arr1)
print(r1)
