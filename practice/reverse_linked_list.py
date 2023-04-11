class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Time Complexity O(n)
    Memory Complexity O(1)
    """
    def reverse_linked_list(self, head: ListNode) -> ListNode:
        prev, curr = None, head 

        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt

        return prev 
    

class Solution_two:
    def reverse_linked_list(self, head: ListNode) -> ListNode:
        # recursive: Time O(n), M O(n)

        if not head:
            return None
        
        new_head = head 
        if head.next:
            new_head = self.reverse_linked_list(head.next)
            head.next.next = head 

        head.next = None 

        return new_head