# My solution; creates a new list
# O(n) time complexity and O(n) space complexity, where
# n : length of list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ansListCurr = ansList = ListNode()
        head = head.next
        currSum = 0
        while head:
            if head.val == 0:
                ansListCurr.next = ListNode(currSum)
                ansListCurr = ansListCurr.next
                currSum = 0 
            currSum += head.val
            head = head.next
        return ansList.next

# Reimplementing the logic in the editorial, this modifies the list in place
# O(n) time complexity and O(1) extra space required, where
# n : length of list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Store the first nonzero value in modify, update modify when you reach a zero
        # node. Use nextSum to iterate through the list.
        modify = nextSum = head.next
        currSum = 0
        while nextSum:
            if nextSum.val == 0:
                modify.val = currSum
                currSum = 0
                # move modify to the next nonzero value
                modify.next = nextSum.next
                modify = modify.next
            currSum += nextSum.val
            nextSum = nextSum.next
        return head.next
