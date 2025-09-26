import sys

index = int(sys.stdin.readline())
node = {}

for i in range(index):
    input_node = list(map(str, sys.stdin.readline().split()))
    node[input_node[0]] = input_node[1], input_node[2]

parents = set(node.keys())
children = set()

for p in node:
    l, r = node[p]
    if l != '.': 
        children.add(l)
    if r != '.': 
        children.add(r)

root = (parents - children).pop()

def preorder(root):
    if root == '.':
        return ''
    left, right = node[root]
    return root + preorder(left) + preorder(right)

def inorder(root):
    if root == '.':
        return ''
    l, r = node[root]
    return inorder(l) + root + inorder(r)

def postorder(root):
    if root == '.':
        return ''
    l, r = node[root]
    return postorder(l) + postorder(r) + root

print(preorder(root))
print(inorder(root))
print(postorder(root))
