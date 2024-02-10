# 707. Design Linked List
# https://leetcode.com/problems/design-linked-list/


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head
        for i in range(index + 1):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        prev = self.head
        for i in range(index):
            prev = prev.next
        
        node = Node(val)
        node.next = prev.next
        prev.next = node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.head
        for i in range(index):
            prev = prev.next

        prev.next = prev.next.next
        
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
import unittest

class TestMyLinkedList(unittest.TestCase):

    def setUp(self):
        # Create a new instance of MyLinkedList before each test
        self.my_linked_list = MyLinkedList()

    def test_addAtHead(self):
        self.my_linked_list.addAtHead(1)
        self.assertEqual(self.my_linked_list.get(0), 1)

        self.my_linked_list.addAtHead(2)
        self.assertEqual(self.my_linked_list.get(0), 2)
        self.assertEqual(self.my_linked_list.get(1), 1)

    def test_addAtTail(self):
        self.my_linked_list.addAtTail(1)
        self.assertEqual(self.my_linked_list.get(0), 1)

        self.my_linked_list.addAtTail(2)
        self.assertEqual(self.my_linked_list.get(0), 1)
        self.assertEqual(self.my_linked_list.get(1), 2)

    def test_addAtIndex(self):
        self.my_linked_list.addAtIndex(0, 1)
        self.assertEqual(self.my_linked_list.get(0), 1)

        self.my_linked_list.addAtIndex(1, 2)
        self.assertEqual(self.my_linked_list.get(0), 1)
        self.assertEqual(self.my_linked_list.get(1), 2)

        self.my_linked_list.addAtIndex(1, 3)
        self.assertEqual(self.my_linked_list.get(0), 1)
        self.assertEqual(self.my_linked_list.get(1), 3)
        self.assertEqual(self.my_linked_list.get(2), 2)

    def test_deleteAtIndex(self):
        self.my_linked_list.addAtTail(1)
        self.my_linked_list.addAtTail(2)
        self.my_linked_list.addAtTail(3)

        self.my_linked_list.deleteAtIndex(1)
        self.assertEqual(self.my_linked_list.get(0), 1)
        self.assertEqual(self.my_linked_list.get(1), 3)
        self.assertEqual(self.my_linked_list.size, 2)

        self.my_linked_list.deleteAtIndex(0)
        self.assertEqual(self.my_linked_list.get(0), 3)
        self.assertEqual(self.my_linked_list.size, 1)

        self.my_linked_list.deleteAtIndex(0)
        self.assertEqual(self.my_linked_list.size, 0)

        # Deleting from an empty list should not cause an error
        self.my_linked_list.deleteAtIndex(0)