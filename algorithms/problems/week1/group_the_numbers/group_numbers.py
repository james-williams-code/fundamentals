'''
implement group numbers, evens on left, odds on  right
'''

def group_numbers(arr):
    print(arr)
    left = 0
    right = len(arr) - 1
    while left < right:
        while arr[left] % 2 == 0:
            left = left + 1
        while arr[right] % 2 != 0:
            right = right - 1
        arr[left], arr[right] = arr[right], arr[left]
    arr[left], arr[right] = arr[right], arr[left]
    return arr

arr1 = [1,3,5,7,2,4,6,8]
r1 = group_numbers(arr1)
print(r1)
