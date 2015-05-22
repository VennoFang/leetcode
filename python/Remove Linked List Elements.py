__author__ = 'Venno'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while head:
            if head.val == val:
                pre.next = head.next
                head = pre
            pre = head
            head = head.next
        return dummy.next

