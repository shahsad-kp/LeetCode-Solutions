from typing import Optional

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue

from helpers import ListNode


def build_intersecting_lists(a_list, b_list, skip_a, skip_b):
    headA = ListNode(a_list[0])
    currA = headA
    nodesA = [headA]
    for val in a_list[1:]:
        node = ListNode(val)
        currA.next = node
        currA = node
        nodesA.append(node)

    # Build list B
    headB = ListNode(b_list[0])
    currB = headB
    nodesB = [headB]
    for val in b_list[1:]:
        node = ListNode(val)
        currB.next = node
        currB = node
        nodesB.append(node)

    # Connect intersection
    if 0 <= skip_a < len(nodesA) and 0 <= skip_b < len(nodesB):
        nodesB[skip_b].next = nodesA[skip_a]

    return headA, headB


class Solution(BaseSolution):
    __solution_method__ = 'getIntersectionNode'
    title = 'Intersection of Two Linked Lists'
    automatic_tests = TestCases(
        TestValue(
            inputs=[
                *build_intersecting_lists(a_list=[4, 1, 8, 4, 5], b_list=[5, 6, 1, 8, 4, 5], skip_a=2, skip_b=3),
            ],
            expected=8
        )
    )
    leetcode_link = 'https://leetcode.com/problems/intersection-of-two-linked-lists'

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_list = []
        head_a = headA
        while head_a:
            a_list.append(head_a)
            head_a = head_a.next
        head_b = headB
        while head_b:
            if head_b in a_list:
                return head_b.val
            head_b = head_b.next

        return None
