class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)
    def merge(self, left, right):
        dummy = ListNode(0)
        current = dummy
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        if left:
            current.next = left
        if right:
            current.next = right
        return dummy.next