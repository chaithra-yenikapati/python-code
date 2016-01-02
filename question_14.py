__author__ = 'Chaithra'

from listutils import *


def merge_lists(head1, head2):
  temp1=head1
  temp2=head2
  prev=Node()
  if head1 and head2:
    while temp1 and temp2:
        if temp1.value <= temp2.value:
            prev=temp1
            temp1 = temp1.next
        else:
          if temp2:
            p=Node()
            p=temp2
            temp2=temp2.next
            prev.next=p
            p.next=temp1
    if temp1==None:
        while temp2:
            prev.next=temp2
            prev=prev.next
            temp2=temp2.next
    return head1
  elif head2:
      return head2
  else:
      return head1
def test_merge_lists():
    head1 = to_linked_list([1, 2, 3])
    head2 = to_linked_list([1, 2, 3, 4, 5])

    result = merge_lists(head1, head2)
    assert [1, 1, 2, 2, 3, 3, 4, 5] == from_linked_list(result)

    head1 = to_linked_list([1, 2, 5])
    head2 = to_linked_list([4, 6, 7])

    result = merge_lists(head1, head2)
    assert [1, 2, 4, 5, 6, 7] == from_linked_list(result)

    head1 = to_linked_list([])
    head2 = to_linked_list([1, 2, 3, 4])

    result = merge_lists(head1, head2)
    assert [1, 2, 3, 4] == from_linked_list(result)

    result = merge_lists(None, None)
    assert [] == from_linked_list(result)






