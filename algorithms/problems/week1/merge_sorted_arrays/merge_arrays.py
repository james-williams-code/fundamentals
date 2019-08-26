
'''
merge sorted arrays
'''

def merge_arrays(arr):
    arr_1 = arr[0]
    arr_2 = arr[1]
    mid = len(arr_1)-1
    end = len(arr_1)-1
    i = len(arr_2)-1
    while i >= 0 or mid >= 0 and end >= 0:
        #print(arr_1[end])
        #print(arr_2[mid])
        #print(mid)
        #print(end)
        print(arr_2)
        if mid < 0:
            arr_2[i] = arr_1[end]
            end = end - 1
        elif end < 0:
            arr_2[i] = arr_2[mid]
            mid = mid - 1
        elif arr_2[mid] >= arr_1[end]:
            arr_2[i] = arr_2[mid]
            mid = mid - 1
        else:
            arr_2[i] = arr_1[end]
            end = end - 1
        i = i - 1
    return arr_2
print('r1')
arr1 = [[1,2,3],[4,5,6,0,0,0]]
r1 = merge_arrays(arr1)
print(r1)
print('r2')
arr2 = [[4,5,6],[1,2,3,0,0,0]]
r2 = merge_arrays(arr2)
print(r2)
print('r3')
arr3 = [[1,3,5],[2,4,6,0,0,0]]
r3 = merge_arrays(arr3)
print(r3)
print('r4')
arr4 = [[2,3,4,7,9],[1,3,5,6,8,0,0,0,0,0]]
r4 = merge_arrays(arr4)
print(r4)
