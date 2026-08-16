# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        # Set the first node
        merged_list = None
        if list1.val <= list2.val:
            merged_list = list1
            list1 = list1.next
        else:
            merged_list = list2
            list2 = list2.next
        """
        m = 1
        l1 = 2
        l2 = 1
        c = 1
        """

        current = merged_list
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return merged_list