__author__ = 'Chaithra'


notes = """
    This is to make you familiar with linked list structures usage in python
    see the listutils.py module for some helper functions
"""

from listutils import *
#Given sorted list with one sublist reversed,
#find the reversed sublist and correct it
#Ex: 1->2->5->4->6->7
# sort the list as: 1->2->4->5->6->7
def sort_reversed_sublist(head):
    if(head==None):
        return []
    count=0
    temp=head
    temp1=temp
    while temp.next!=None:
        if  temp.value<temp.next.value:
            count=1
            temp1=temp
            temp=temp.next
        else:
            temp2=temp
            temp=temp.next
            temp3=temp.next
            temp.next=temp2
            temp1.next=temp
            temp2.next=temp3
            break
    if(count==1):
        return from_linked_list(head)
    else:
        return from_linked_list(temp)


#write test cases covering all cases for your solution
def test_sort_reversed_sublist():
    assert [1,2,4,5,6,7]==sort_reversed_sublist(to_linked_list([1,2,5,4,6,7]))
    assert [1,2,3]==sort_reversed_sublist(to_linked_list([2,1,3]))
    assert [2,3]==sort_reversed_sublist(to_linked_list([3,2]))
    assert [2]==sort_reversed_sublist(to_linked_list([2]))
    assert []==sort_reversed_sublist(to_linked_list([]))