from typing import Optional

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue

from helpers import ListNode, list_to_linked_list


class Solution(BaseSolution):
    title = 'Rotate List'
    leetcode_link = 'https://leetcode.com/problems/rotate-list/'
    automatic_tests = TestCases(
        TestValue(
            inputs=[
                ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
                2
            ],
            expected=ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3))))),
        ),
        TestValue(
            inputs=[
                list_to_linked_list([0, 1, 2]),
                4
            ],
            expected=list_to_linked_list([2, 0, 1])
        )
    )
    __solution_method__ = 'rotateRight'

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        n = 1
        dummy = head
        while dummy.next:
            n += 1
            dummy = dummy.next
        k = k % n
        if k == 0:
            return head
        curr = head
        for _ in range(n - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        dummy.next = head
        return new_head
