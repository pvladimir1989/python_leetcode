import pytest

from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(None)
#         tail = dummy

#         while list1 and list2:
#             if list1.val > list2.val:
#                 tail.next = list2
#                 list2 = list2.next
#             else:
#                 tail.next = list1
#                 list1 = list1.next

#             tail = tail.next

#         if list1:
#             tail.next = list1
#         elif list2:
#             tail.next = list2
#         return dummy.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(None)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        tail.next = list1 or list2
        return dummy.next


def list_to_linked_list(lst):
    dummy = ListNode(None)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
    # Add more test cases as needed
])
def test_mergeTwoLists(list1, list2, expected):
    solution = Solution()
    merged = solution.mergeTwoLists(list_to_linked_list(list1), list_to_linked_list(list2))
    assert linked_list_to_list(merged) == expected
