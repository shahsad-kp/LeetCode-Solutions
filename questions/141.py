from typing import Optional

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def generate_input_one() -> list[ListNode]:
    first_node = ListNode(3)
    second_node = ListNode(2)
    third_node = ListNode(0)
    fourth_node = ListNode(-4)
    first_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = second_node
    return [first_node]


def generate_input_two() -> list[ListNode]:
    first_node = ListNode(1)
    second_node = ListNode(2)
    first_node.next = second_node
    second_node.next = first_node
    return [first_node]


class Solution(BaseSolution):
    title = 'Linked List Cycle'
    leetcode_link = 'https://leetcode.com/problems/linked-list-cycle'
    automatic_tests = TestCases(
        TestValue(
            inputs=generate_input_one,
            expected=True,
        ),
        TestValue(
            inputs=generate_input_two,
            expected=True,
        ),
        TestValue(
            inputs=[ListNode(1)],
            expected=False,
        )
    )
    __solution_method__ = 'hasCycle'

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
