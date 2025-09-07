from typing import Optional

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue

from helpers import ListNode


class Solution(BaseSolution):
    title = 'Add Two Numbers'
    leetcode_link = 'https://leetcode.com/problems/add-two-numbers'
    automatic_tests = TestCases(
        TestValue(
            inputs=[
                ListNode(2, ListNode(4, ListNode(3))),
                ListNode(5, ListNode(6, ListNode(4)))
            ],
            expected=ListNode(7, ListNode(0, ListNode(8)))
        ),
        TestValue(
            inputs=[
                ListNode(0),
                ListNode(0)
            ],
            expected=ListNode(0)
        ),
        TestValue(
            inputs=[
                ListNode(9, ListNode(9, ListNode(9))),
                ListNode(1)
            ],
            expected=ListNode(0, ListNode(0, ListNode(0, ListNode(1))))
        )
    )

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
