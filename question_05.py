__author__ = 'Chaithra'

notes = """
    This is to introduce you to create data structures of your own without help of built-in structures.
"""


#Convert a number into linked list such that each digit is in a node and pointing to node having next digit.
#The function should return head of the linked list.
#Do not use built-in functions.

from listutils import *
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def number_to_LinkedList(numbers):
    if numbers < 0:
        numbers=abs(numbers)
    else:
        if numbers==0:
           head=Node()
           head.value=0
           head.next=None
           return head

    head=Node()
    head.next=None
    head.value=numbers%10
    numbers=numbers/10
    while numbers>0:
              current=Node()
              current.value=numbers%10
              numbers=numbers/10
              current.next=head
              head=current
    return head


#write down tests covering all possible cases to your solution
#Hint: Here tests can use built-in functions
def test_number_to_LinkedList():
    l=from_linked_list(number_to_LinkedList(123))
    assert [1,2,3]==l
    l=from_linked_list(number_to_LinkedList(456))
    assert [4,5,6]==l
    l=from_linked_list(number_to_LinkedList(-123))
    assert [1,2,3]==l
    l=from_linked_list(number_to_LinkedList(0))
    assert [0]==l


