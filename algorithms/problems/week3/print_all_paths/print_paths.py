'''
'''

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def print_all_paths(node):
    output = []

    def paths_helper(n,path):
        if not n:
            return
        if not n.left and not n.right:
            output.append(''.join(path+str(n.value)))
            return
        if n.left:
            paths_helper(n.left,path+str(n.value))
        if n.right:
            paths_helper(n.right,path+str(n.value))
    paths_helper(node,'')
    return output

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.left = node2
node1.right = node3
node3.right = node4

print(print_all_paths(node1))

