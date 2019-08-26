'''
implement top k
'''

from heapq import heappop, heappush

def top_k(arr,k):
    print(arr)
    print(k)
    heap = []
    heap_set = set()
    for i in range(0,len(arr)):
        if arr[i] in heap_set:
            continue
        if len(heap) < k:
            heappush(heap,arr[i])
            heap_set.add(arr[i])
        elif arr[i] > heap[0]:
            if arr[i] not in heap_set:
                current = heappop(heap)
                heap_set.remove(current)
                heappush(heap,arr[i])
                heap_set.add(arr[i])
    return heap


arr1 = [4,3,6,5,9,2]
k = 2
r1 = top_k(arr1,k)
print(r1)
