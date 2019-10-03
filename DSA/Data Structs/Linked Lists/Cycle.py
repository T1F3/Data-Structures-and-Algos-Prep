class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        travel_p =  self.has_cycle(head)
        if not travel_p:
            return None
        start_p = head
        while start_p != travel_p:
            start_p = start_p.next
            travel_p = travel_p.next
        return start_p
    def has_cycle(self, head):
        p1 = p2 = head
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return p1
        return 0

