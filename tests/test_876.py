import pytest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast.next and fast:
            slow = slow.next
            fast = fast.next.next
        return slow
    
def lst_to_linked_lst(lst):
    dummy = ListNode(None)
    tail = dummy

    for val in lst:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

@pytest.mark.parametrize("lst, exp" ,[
    ([1,2,3,4,5], [3,4,5]),
    # Add more test cases as needed
])
def test_middleNode(lst, exp):
    solution = Solution()
    mid_node = solution.middleNode(lst_to_linked_lst(lst))
    assert linked_list_to_list(mid_node) == exp
