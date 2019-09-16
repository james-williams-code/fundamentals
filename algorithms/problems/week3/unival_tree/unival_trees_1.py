'''
'''
class Node():

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def unival_trees(node):
    count = 0

    def tree_helper(n,c):
        if not node:
            return False, c
        #if not n.left and not n.right:
        #    return True, c + 1
        is_left_correct, c = tree_helper(n.left,c)
        is_right_correct, c = tree_helper(n.right,c)
        if is_left_correct:
            c += 1
        if is_right_correct:
            c += 1
        if n.left.value == n.value and n.right.value == n.value:
            c += 1
        #print(c)
        return is_left_correct and is_right_correct,c
    is_correct, count = tree_helper(node,count)
    print(count)
    return is_correct

node1 = Node(1)
node2 = Node(1)
node3 = Node(1)
node1.left = node2
node1.right = node3
#print(unival_trees(node1))
node4 = Node(2)
node5 = Node(2)
node6 = Node(2)
node3.right = node4
node4.left = node5
node4.right = node6
print(unival_trees(node2))
