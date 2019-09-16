'''

'''

class Node():

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def is_bst(node):

    def bst_helper(n):
        if not n:
            return False
        if not n.left and not n.right:
            return True
        left_is_bst = bst_helper(n.left)
        right_is_bst = bst_helper(n.right)
        this_is_bst = False
        if n.right and n.left:
            this_is_bst = n.left.value <= n.value and n.right.value >= n.value
        elif n.right:
            this_is_bst = n.right.value >= n.value
        elif n.left:
            this_is_bst = n.left.value <= n.value
        return left_is_bst and right_is_bst and this_is_bst
    return bst_helper(node)


node1 = Node(5)
node2 = Node(4)
node3 = Node(6)
node4 = Node(7)
node1.left = node2
node1.right = node3
node3.right = node4
print(is_bst(node1))
