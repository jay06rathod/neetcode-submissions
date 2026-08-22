# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merging(list1, list2):
            dummy = ListNode(0)
            current = dummy
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
            else:
                current.next = list2
            return dummy.next
        
        if not lists:
            return None
        
        interval = 1

        while interval < len(lists):
            for i in range(0, len(lists)-interval, interval*2):
                lists[i] = merging(lists[i], lists[i+interval])
            
            interval*=2
        
        return lists[0]