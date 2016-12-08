from node import Node

def merge(node1, node2):
    if node1 != None and node1.data != None:
        tmp = returnBack(node1)
        tmp.next = node2
        return node1
    elif node2 != None and node2.data != None:
        tmp = returnBack(node2)
        tmp.next = node1
        return node2
    return None


def returnBack(node):
    while(node.next):
        node = node.next
    return node

def printList(node):
    while node:
        print node
        node = node.next
    print "-----------"

# Zastosowanie.
head1 = None
head1 = Node(1, head1)
head1 = Node(2, head1)
head2 = None
head2 = Node(5, head2)
head2 = Node(7, head2)
printList(head1)
printList(head2)
head3 = merge(head1, head2)
printList(head3)
head1 = None
head4 = merge(head3, head1)
printList(head4)
head5 = merge(head1, head3)
printList(head5)
head2 = None
head6 = merge(head1, head2)
printList(head6)
