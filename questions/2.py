from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other: 'ListNode') -> bool:
        if not isinstance(other, ListNode):
            return False
        current_self = self
        current_other = other
        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return current_self is None and current_other is None


class Solution:
    __question__ = 'Add Two Numbers'
    __leetcode__ = 'https://leetcode.com/problems/add-two-numbers'
    __test_cases__ = [
        {
            'input': [
                ListNode(2, ListNode(4, ListNode(3))),
                ListNode(5, ListNode(6, ListNode(4)))
            ],
            'output': ListNode(7, ListNode(0, ListNode(8)))
        },
        {
            'input': [
                ListNode(0),
                ListNode(0)
            ],
            'output': ListNode(0)
        },
        {
            'input': [
                ListNode(9, ListNode(9, ListNode(9))),
                ListNode(1)
            ],
            'output': ListNode(0, ListNode(0, ListNode(0, ListNode(1))))
        }
    ]
    __solution_method__ = 'addTwoNumbers'

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = result = None
        carier = 0

        while l1 or l2:
            sum_result = 0
            if l1:
                sum_result += l1.val
                l1 = l1.next
            if l2:
                sum_result += l2.val
                l2 = l2.next

            sum_result += carier
            last_digit = sum_result % 10
            carier = sum_result // 10
            node = ListNode(val=last_digit)

            if result is None:
                result = head = node
            else:
                result.next = node
                result = result.next
        if carier:
            result.next = ListNode(val=carier)
        return head