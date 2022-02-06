'''
Problem: Add Two Numbers
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(-1)
        tail = head
        
        carry = 0
        
        while l1 or l2 or carry:
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            num = v1 + v2 + carry
            val = num % 10
            carry = num // 10
            
            tail.next = ListNode(val)
            tail = tail.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            
        return head.next
