#implement the merge-sort alogrithm
#divide, conquer, combine
#find the middle element and break the list down into havles
#continue this process till you get list of length 1
#compare the values as you combine each list

def merge_sort(arr):
    merge_sort_helper(arr,0,len(arr)-1)
    return

def merge_sort_helper(arr,start,end):
    if start >= end:
        return arr
    mid = (start + end)// 2
    print('start ' + str(start))
    print('mid ' + str(mid))
    print('end ' + str(end))
    merge_sort_helper(arr,start,mid)
    merge_sort_helper(arr,mid+1,end)
    #combine
    i = start
    j = mid+1
    aux = []
    print(arr)
    print(i)
    print(j)
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            aux.append(arr[i])
            i+=1
        else:
            aux.append(arr[j])
            j+=1
    while i <= mid:
        aux.append(arr[i])
        i+=1
    while j <= end:
        aux.append(arr[j])
        j+=1
    arr[start:end+1] = aux
    return

arr1 = [9,2,5,7,3,8]
#arr1 = [2,1,4]
print(merge_sort(arr1))
