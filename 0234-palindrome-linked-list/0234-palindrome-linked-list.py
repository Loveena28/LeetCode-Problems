# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = deque()
        temp = head
        while temp:
            nodes.append(temp.val)
            temp = temp.next
        temp = head
        while temp:
            if temp.val != nodes.pop():
                return False
            temp = temp.next
        return True
        
            
        