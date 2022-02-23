# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse(pointer):
            previous_pointer = None
            current = pointer
            while current:
                next_pointer = current.next
                current.next = previous_pointer
                previous_pointer = current
                current = next_pointer
            return previous_pointer

        # find the middle of the linked list
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the linked list
        reversed_second_half_head = reverse(slow)

        # compare first half and reversed second half
        # if list length is odd number,middle number is common for both halfs
        # so if any half of the list reached to end,which means a palindrome list
        reversed_head = reversed_second_half_head
        original_head = head
        while original_head and reversed_head:
            if original_head.val != reversed_head.val:
                break
            original_head = original_head.next
            reversed_head = reversed_head.next

        if not original_head or not reversed_head:
            return True
        return False
