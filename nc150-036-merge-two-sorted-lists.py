# My solution
# O(n) time complexity, where
# n : length of longer list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ansHead = ListNode()
        ansCurr = ansHead
        curr1 = list1
        curr2 = list2
        while curr1 or curr2:
            if not curr2:
                ansCurr.next = ListNode(curr1.val, None)
                curr1 = curr1.next
            elif not curr1:
                ansCurr.next = ListNode(curr2.val, None)
                curr2 = curr2.next
            elif curr1.val < curr2.val:
                ansCurr.next = ListNode(curr1.val, None)
                curr1 = curr1.next
            else:
                ansCurr.next = ListNode(curr2.val, None)
                curr2 = curr2.next
            ansCurr = ansCurr.next
        return ansHead.next

# Reimplementing official solution
# O(n) time complexity, where
# n : length of shorter list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                # Initializing a new ListNode is better than just 
                # assigning tail.next = list1.
                # The latter copies over the entire list.
                tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            tail = tail.next
        # If list1 has elements, it evaluates as truthy and tail.next
        # gets assigned list1. Ditto for list 2. If both are None,
        # tail.next gets assigned None
        tail.next = list1 or list2
        return dummy.next
