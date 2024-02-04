# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowPointer,fastPointer = head,head
        while fastPointer != None and fastPointer.next != None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        return slowPointer
        