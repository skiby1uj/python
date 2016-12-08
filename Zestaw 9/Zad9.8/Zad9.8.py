from tree import Tree

def bst_insert(top, data):
    if top is None:
        return Tree(data)
    if data < top.data:
        top.left = bst_insert(top.left, data)
    elif data > top.data:
        top.right = bst_insert(top.right, data)
    return top

def bst_max(top):
    if not isinstance(top, Tree):
        raise ValueError('Korzen nie jest typu Tree')
    if top.data == None:
        raise ValueError('Drzewo jest puste')
    if top.right == None:
        return top.data
    while(top.right):
        top = top.right
    return top.data

def bst_min(top):
    if not isinstance(top, Tree):
        raise ValueError('Korzen nie jest typu Tree')
    if top.data == None:
        raise ValueError('Drzewo jest puste')
    if top.left == None:
        return top.data
    while(top.left):
        top = top.left
    return top.data

root = Tree(4)
root = bst_insert(root, 4)
root = bst_insert(root, 3)
root = bst_insert(root, 6)
root = bst_insert(root, 1)
root = bst_insert(root, 10)
print bst_min(root)
print bst_max(root)
