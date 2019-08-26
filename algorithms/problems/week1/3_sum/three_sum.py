'''
implement 3 sum
'''

def three_sum(arr):
    if not arr or len(arr)<3:
        return arr
    print(arr)
    end = len(arr)
    result = []
    arr.sort()
    for i in range(0,end -1):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left = i + 1
        right = end - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s > 0:
                right = right - 1
            elif s < 0:
                left = left + 1
            else:
                result.append([arr[i], arr[left], arr[right]])
                while left + 1 < right and arr[left] == arr[left + 1]:
                    left = left + 1
                while right -1 > left and arr[right] == arr[right - 1]:
                    right = right -1
                right = right - 1
                left = left + 1
    res = []
    print(result)
    for r in result:
        res.append(str(r).strip('[]'))
    return res
#arr1 = [-4,4,0,3,-2,-1]
#r1 = three_sum(arr1)
#print(r1)

arr2 = [-1,0,1,2,-1,-4]
r2 = three_sum(arr2)
print(r2)

