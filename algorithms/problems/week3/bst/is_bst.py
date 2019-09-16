'''
'''
class Node():

    def __init__(self,value=0):
        self.value = value
        self.left = None
        self.right = None

def is_bst(node):

    def bst_helper(n):
        if not n:
            return True
        if not n.left and not n.right:
            return True
        left = bst_helper(n.left)
        right = bst_helper(n.right)
        if n.left and n.left.value > n.value:
            return False
        if n.right and n.right.value < n.value:
            return False
        return left and right
    return(bst_helper(node))


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.left = node2
node1.right = node3
node3.right = node4
print(is_bst(node1))
