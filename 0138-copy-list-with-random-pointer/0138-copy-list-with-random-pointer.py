class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
        old_to_new = {}
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            copy_node = old_to_new[current]
            copy_node.next = old_to_new.get(current.next)
            copy_node.random = old_to_new.get(current.random)
            current = current.next
        return old_to_new[head]