from node import Node

def remove_head(node):
    if node.data == None:
        raise ValueError("Lista jest pusta")
    return node.next, node.next.data

def remove_tail(node):
    if node.data == None:
        raise ValueError("Lista jest pusta")
    almostLast = None
    head = node
    while node.next:
        almostLast = node
        node = node.next
    if almostLast == None:#zostal jeden element listy wiec go usuwamy
        return Node(None), None
    almostLast.next = None
    return head, head.data

def printList(node):
    while node:
        print node
        node = node.next
    print "-----------"

head = None
head = Node(1, head)
head = Node(2, head)
printList(head)
head, data = remove_tail(head)
printList(head)
head, data = remove_tail(head)
printList(head)
head, data = remove_tail(head)
