__author__ = 'Chaithra'

from listutils import *
notes = """
    This is to make you familiar with linked list structures usage in python
    see the listutils.py module for some helper functions
"""


#given you a list 1->2->3->4->5 swap alternate elements and return the new head
#the new list head should result out 2->1->4->3->5
def swap_alternate_nodes_of_list(head):
    if head==None or head.next==None:
        return head
    temp=head
    head=head.next
    while temp!=None and temp.next!=None:
        current=prev=temp
        later=prev.next
        prev.next=later.next
        later.next=prev
        temp=temp.next
        if temp!=None and temp.next!=None:
            current.next=temp.next
    return from_linked_list(head)



#write test cases covering all cases for your solution
def test_swap_alternate_nodes_of_list():
    assert [2,1,4,3,5]== swap_alternate_nodes_of_list(to_linked_list([1,2,3,4,5]))
    assert [2,4,6,8]== swap_alternate_nodes_of_list(to_linked_list([4,2,8,6]))
    assert None== swap_alternate_nodes_of_list(to_linked_list([]))
