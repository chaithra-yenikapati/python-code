__author__ = 'Chaithra'

notes = '''
This problem deals with circular single linked lists, the tail of the list points back to head.

For this assignment assume that input list is sorted (ie) smallest element is head.
'''

from listutils import *

#insert a new node into the circular linked list so that the circular list loop sorted invariant holds
def insert_node(head, value):
    prev=Node()
    temp=head
    if temp:
        if temp.next==head:
          new_node=Node(value)
          new_node.next=temp
          temp.next=new_node
          if temp.value>value:
              head=new_node
        elif temp.value>value:
            while temp.next!=head:
                temp=temp.next
            p=Node(value)
            p.next=head
            temp.next=p
            head=p
        else:
            while temp.value<value:
                if temp.next!=head:
                    prev=temp
                    temp=temp.next
                else:
                    prev=temp
                    temp=temp.next
                    break
            p=Node(value)
            p.next=temp
            prev.next=p
    else:
        p=Node(value)
        p.next=p
        head=p
    return head


def check_insertion(input, value, output):
    head = to_circular_list(input)
    head = insert_node(head, value)
    assert output == from_circular_list(head)

#if __name__=="__main__":
def test_insert_node():
    check_insertion([3, 5, 7], 4, [3, 4, 5, 7])
    check_insertion([3, 5, 7], 9, [3, 5, 7, 9])
    check_insertion([3, 5, 7], 1, [1, 3, 5, 7])

    check_insertion([], 1, [1])
    check_insertion([1], 3, [1, 3])
    check_insertion([5], 3, [3,5])
