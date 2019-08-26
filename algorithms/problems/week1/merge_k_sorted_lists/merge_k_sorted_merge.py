'''
Implement k sorted using merge sort

'''

def merge_k_sorted(arrs):
    res = []
    is_descending = False
    ar = arrs[0]
    if ar[0] > ar[1]:
        is_descending = True
    for a in arrs:
        res.extend(a)
    ret = merge_sort(res,is_descending)
    return res

def merge_sort(arr,is_descending):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left,is_descending)
        merge_sort(right,is_descending)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if is_descending == False:
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i = i + 1
                else:
                    arr[k] = right[j]
                    j = j + 1
            else:
                if left[i] > right[j]:
                    arr[k] = left[i]
                    i = i + 1
                else:
                    arr[k] = right[j]
                    j = j + 1
            k = k + 1
        while i < len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            arr[k] = right[j]
            j = j + 1
            k = k + 1
    return arr


arr1 = [[1,3,5,7],[2,4,6,8]]
r1 = merge_k_sorted(arr1)
print(r1)

arr2 = [[7,5,3,1],[8,6,4,2]]
r2 = merge_k_sorted(arr2)
print(r2)
