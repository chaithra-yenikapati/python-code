__author__ = 'Chaithra'

notes = '''
This problem deals with circular single linked lists, the tail of the list points back to head.
'''

from listutils import *


# delete a node in the list so that the resulting list is still circular.
def delete_node(head, value):
    if head:
        if(head.value==value):
            if(head.next!=head):
                temp=head
                while(temp.next!=head):
                    temp=temp.next
                temp.next=head.next
                head=head.next
            else:
                head=None
        else:
            temp=head
            while(temp.next.value!=value):
                temp=temp.next
                if(temp.next==head):
                    return head
            temp.next=temp.next.next
        return head
    else:
        return None


def check_deletion(input, value, output):
    head = to_circular_list(input)
    head = delete_node(head, value)
    assert output == from_circular_list(head)

def test_delete_node():
    check_deletion(range(1,6), 1, range(2,6))
    check_deletion(range(1,6), 5, range(1,5))
    check_deletion(range(1,6), 3, [1,2,4,5])
    check_deletion(range(1,6), 10, range(1,6))
    check_deletion([1], 10, [1])
    check_deletion([1], 1, [])
    check_deletion([], 1, [])



