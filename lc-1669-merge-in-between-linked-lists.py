# My solution
# O(b) time complexity and O(1) extra space required, where
# b : argument b

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Get pointer to tail of list2
        l2Tail = list2
        while l2Tail.next:
            l2Tail = l2Tail.next
        
        # Get pointer to (a - 1)th node of list1
        aMin1Node = list1
        for i in range(a - 1):
            aMin1Node = aMin1Node.next
        
        # Get pointer to (b + 1)th node of list1
        bPlus1Node = aMin1Node
        for i in range(b - a + 2):
            bPlus1Node = bPlus1Node.next
        
        # Connect (a - 1)th node of list1 to head of list2.
        # Connect tail of list2 to (b + 1)th node of list1
        aMin1Node.next = list2
        l2Tail.next = bPlus1Node

        return list1
