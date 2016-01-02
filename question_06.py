__author__ = 'Chaithra'

from listutils import *
#
notes = """
    This is to make you familiar with linked list structures usage in python
    see the listutils.py module for some helper functions
"""
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

#given the head of a list,
# reverse the list and return the head of the reversed list
def reverse_linked_list(head):
        current=Node()
        temp1=None
        while head!=None:
            current=head
            head=head.next
            current.next=temp1
            temp1=current
        return  from_linked_list(temp1)


#write test cases covering all cases for your solution
def test_reverse_linked_list():
    assert [4,3,2,1]==reverse_linked_list(to_linked_list([1,2,3,4]))
    assert []==reverse_linked_list(to_linked_list([]))
    assert [0]==reverse_linked_list(to_linked_list([0]))

