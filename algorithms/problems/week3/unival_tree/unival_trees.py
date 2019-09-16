'''
'''

class Node():

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def unival_trees(root):

    count = 0
    def tree_helper(n,count):
        if not n:
            return False
        if not n.left and not n.right:
            count = count + 1
            print(count)
            return True
        left_is_uni = tree_helper(n.left,count)
        right_is_uni = tree_helper(n.right,count)
        if n.left and n.right and n.left.value == n.value and n.right.value == n.value:
            count = count + 1
            return left_is_uni and right_is_uni
        else:
            return False
    tree_helper(root,count)
    return count

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.left = node2
node1.right = node2
print(unival_trees(node1))

