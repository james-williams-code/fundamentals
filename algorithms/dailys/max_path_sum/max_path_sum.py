'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

class Node:

    def __init__():
        value = None
        left_child = None
        right_child = None


def find_path(arr,i=0,path_sum=0):
    path = None

    if arr[0] is not None:
        path_sum += arr[0]
    else:
        return 0

    l = 2 * i + 1
    r = 2 * i + 2
    if l < len(arr) and arr[l] is not None:
        path_sum += arr[l]

    if r < len(arr) and arr[r] is not None:
        path_sum += arr[r]

    if len(arr) > 3:
        path_sum += find_path(arr[3:],i+1)
    return path_sum



test1 = [1,2,3]
p_sum = find_path(test1,0,0)
print(p_sum)

test2 = [1,2,3,4]
p_sum2 = find_path(test2,0,0)
print(p_sum2)

test3 = [1,5,2,None,None,1,1]
'''
        1
     /    \
    5       2
   / \     / \
None None 1   1
'''
p_sum3 = find_path(test3,0,0)
print(p_sum3)



