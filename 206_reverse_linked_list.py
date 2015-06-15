# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        def rev_help(head):
            if not head or not head.next:
                return (head, head)
            (n_head, tail) = rev_help(head.next)
            if tail:
                tail.next = head
                head.next = None
                return (n_head, head)
            (n_head, _) = rev_help(head)
            return n_head

