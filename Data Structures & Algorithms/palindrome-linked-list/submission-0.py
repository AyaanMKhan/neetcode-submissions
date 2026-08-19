# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        prev = None
        cur = slow

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        walker = head
        walker2 = prev

        while walker and walker2:
            if walker.val == walker2.val:
                walker = walker.next
                walker2 = walker2.next
            else:
                return False
        
        return True
        
            
