'''
'''

class Node():

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def print_paths(node):

    output = []
    def print_path(n,path):
        if not n:
            return
        if not n.left and not n.right:
            output.append(path+str(n.value))
            return
        print_path(n.left,path + str(n.value))
        print_path(n.right,path + str(n.value))
    print_path(node,'')
    return output

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.left = node2
node1.right = node3
node3.right = node4
r1 = print_paths(node1)
print(r1)
