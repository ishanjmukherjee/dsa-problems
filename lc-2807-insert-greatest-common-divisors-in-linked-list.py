# My solution
# O(n) time complexity, where
# n : length of list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            temp = curr.next
            curr.next = ListNode(gcd(curr.val, curr.next.val), curr.next)
            curr = temp
        return head
