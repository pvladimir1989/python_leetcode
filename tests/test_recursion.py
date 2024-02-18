# https://www.youtube.com/watch?v=IJDJ0kBx2LM
import unittest

def reversal_string(s: str) -> str:
    if s == "":
        return s
    return reversal_string(s[1:]) + s[0]

def test_reversal_string():
    assert reversal_string("") == ""
    assert reversal_string("hello") == "olleh"
    assert reversal_string("racecar") == "racecar"
    assert reversal_string("12345") == "54321"
    assert reversal_string("a") == "a"
    assert reversal_string("abcdef") == "fedcba"

def ispalindrome(s: str) -> str:
    if len(s) == 0 or len(s) == 1:
        return True

    if s[0] == s[-1]:
        return ispalindrome(s[1:-1])

    return False 

def test_ispalindrome():
    assert ispalindrome("") == True
    assert ispalindrome("a") == True
    assert ispalindrome("abba") == True
    assert ispalindrome("racecar") == True
    assert ispalindrome("hello") == False
    assert ispalindrome("12321") == True
    assert ispalindrome("12345") == False

def decimal_to_binary(decimal: int, result: str) -> str:
    if decimal == 0:
        return result
    
    result = str(decimal % 2) + result
    return decimal_to_binary(decimal // 2, result)

def test_decimal_to_binary():
    assert decimal_to_binary(233, "") == "11101001"

def sum_of_natural_numbers(num: int) -> int:
    if num <= 1:
        return num
    
    return num + sum_of_natural_numbers(num-1)

def test_sum_of_natural_numbers():
    assert sum_of_natural_numbers(10) == 55

def binary_search(lst: list, num: int) -> int:
    l, r = 0, len(lst)-1
    if l > r:
        return -1
    
    mid = (l + r) // 2
    if lst[mid] == num:
        return num

    if  num < lst[mid]:
        return binary_search(lst[:mid], num)
    
    return binary_search(lst[mid+1:], num)


def test_binary_search():
    assert binary_search([1,6,9,17,20], 17) == 17

# merge_sort missed
    

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

def reverse_linked_list(head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    new_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return new_head


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list(self):
        # Создаем связанный список: 1 -> 2 -> 3 -> 4 -> 5
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        # Переворачиваем связанный список
        reversed_head = reverse_linked_list(head)
        
        # Проверяем, что перевернутый список верен
        self.assertEqual(reversed_head.val, 5)
        self.assertEqual(reversed_head.next.val, 4)
        self.assertEqual(reversed_head.next.next.val, 3)
        self.assertEqual(reversed_head.next.next.next.val, 2)
        self.assertEqual(reversed_head.next.next.next.next.val, 1)   



# Merge Two Sorted Linked Lists missed