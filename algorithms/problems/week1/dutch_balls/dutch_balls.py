'''
solve dutch balls
'''

def dutch_balls(arr):
    end = len(arr)
    r = 0
    g = 0
    b = len(arr) - 1
    while g <= b:
        if arr[g] == 'R':
            arr[g],arr[r] = arr[r],arr[g]
            g = g + 1
            r = r + 1
        elif arr[g] == 'G':
            g = g + 1
        else:
            arr[g], arr[b] = arr[b], arr[g]
            b = b - 1
    return arr

arr1 = ['B','R','G']
r1 = dutch_balls(arr1)
print(r1)
