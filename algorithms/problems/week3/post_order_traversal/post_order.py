'''
'''
class Node():

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class Stack():
    def __init__(self):
        self.stack = []

    def top(self):
        value = self.stack[-1]
        return value

    def pop(self):
        value = self.stack[-1]
        self.stack = self.stack[:-1]
        return value

    def push(self,n):
        self.stack.append(n)

def post_order_traversal(node):

    stack = Stack()
    stack.push(node)
    output = '' 

    while len(stack.stack):
        n = stack.top()
        if not n.left and not n.right:
            output = output + str(n.value)
            print(output)
            stack.pop()
        else:
            if n.right:
                stack.push(n.right)
                n.right = None
            if n.left:
                stack.push(n.left)
                n.left = None
    return output
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.left = node2
node1.right = node3
r1 = post_order_traversal(node1)
print(r1)


