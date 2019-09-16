'''

'''

class Node():

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def unival_trees(node):

    count = 0
    def tree_helper(n,count):
        print(count)
        if not n:
            return
        if not n.left and not n.right:
            return
        left_same = tree_helper(n.left,count)
        right_same = tree_helper(n.right,count)
        if not left_same or :
            return False
        elif n.left and n.left.value == n.value and n.right and n.right.value == n.value:
            count += count
            return True
        else:
            return False
    tree_helper(node,0)
    return count

node1 = Node(1)
node2 = Node(1)
node3 = Node(1)
node1.left = node2
node1.right = node3
print(unival_trees(node1))
