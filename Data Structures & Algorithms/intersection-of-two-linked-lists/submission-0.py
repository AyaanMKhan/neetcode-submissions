# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        while headA:
            cur = headB
            while cur:
                if headA == cur:
                    return headA
                
                cur = cur.next
            
            headA = headA.next
        
        return None