"""
--- Add lists ---
Write a function, add_lists, that takes in the head of two linked lists, each representing a number. The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.

Say we wanted to compute 621 + 354 normally. The sum is 975:

   621
 + 354
 -----
   975

Then, the reversed linked list format of this problem would appear as:

    1 -> 2 -> 6
 +  4 -> 5 -> 3
 --------------
    5 -> 7 -> 9
"""
import unittest
from node import Node
from _019_linked_list_values import str_list


def add_lists(head_1, head_2):
    dummy = Node(None)
    tail = dummy
    current1 = head_1
    current2 = head_2
    carry = 0

    while current1 or current2 or carry:
        val1 = current1.val if current1 else 0
        val2 = current2.val if current2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        tail.next = Node(digit)
        tail = tail.next

        current1 = current1.next if current1 else None
        current2 = current2.next if current2 else None

    return dummy.next


def add_lists_rec(head_1, head_2):
    return _add_lists(head_1, head_2, 0)


def _add_lists(head_1, head_2, carry):
    if not head_1 and not head_2 and not carry:
        return None

    val1 = head_1.val if head_1 else 0
    val2 = head_2.val if head_2 else 0
    total = val1 + val2 + carry
    val = total % 10
    new_carry = total // 10

    result = Node(val)

    head_1 = head_1.next if head_1 else None
    head_2 = head_2.next if head_2 else None
    result.next = _add_lists(head_1, head_2, new_carry)

    return result


class Test(unittest.TestCase):

    def test_00(self):
        #   621
        # + 354
        # -----
        #   975

        a1 = Node(1)
        a2 = Node(2)
        a3 = Node(6)
        a1.next = a2
        a2.next = a3
        # 1 -> 2 -> 6

        b1 = Node(4)
        b2 = Node(5)
        b3 = Node(3)
        b1.next = b2
        b2.next = b3
        # 4 -> 5 -> 3

        result = add_lists(a1, b1)
        assert str_list(result) == "5 -> 7 -> 9"

    def test_01(self):
        #  7541
        # +  32
        # -----
        #  7573

        a1 = Node(1)
        a2 = Node(4)
        a3 = Node(5)
        a4 = Node(7)
        a1.next = a2
        a2.next = a3
        a3.next = a4
        # 1 -> 4 -> 5 -> 7

        b1 = Node(2)
        b2 = Node(3)
        b1.next = b2
        # 2 -> 3

        result = add_lists(a1, b1)
        assert str_list(result) == "3 -> 7 -> 5 -> 7"

    def test_02(self):
        #   39
        # + 47
        # ----
        #   86

        a1 = Node(9)
        a2 = Node(3)
        a1.next = a2
        # 9 -> 3

        b1 = Node(7)
        b2 = Node(4)
        b1.next = b2
        # 7 -> 4

        result = add_lists(a1, b1)
        assert str_list(result) == "6 -> 8"

    def test_03(self):
        #   89
        # + 47
        # ----
        #  136

        a1 = Node(9)
        a2 = Node(8)
        a1.next = a2
        # 9 -> 8

        b1 = Node(7)
        b2 = Node(4)
        b1.next = b2
        # 7 -> 4

        result = add_lists(a1, b1)
        assert str_list(result) == "6 -> 3 -> 1"

    def test_04(self):
        #   999
        #  +  6
        #  ----
        #  1005

        a1 = Node(9)
        a2 = Node(9)
        a3 = Node(9)
        a1.next = a2
        a2.next = a3
        # 9 -> 9 -> 9

        b1 = Node(6)
        # 6

        result = add_lists(a1, b1)
        assert str_list(result) == "5 -> 0 -> 0 -> 1"

    def test_05(self):
        #   621
        # + 354
        # -----
        #   975

        a1 = Node(1)
        a2 = Node(2)
        a3 = Node(6)
        a1.next = a2
        a2.next = a3
        # 1 -> 2 -> 6

        b1 = Node(4)
        b2 = Node(5)
        b3 = Node(3)
        b1.next = b2
        b2.next = b3
        # 4 -> 5 -> 3

        result = add_lists_rec(a1, b1)
        assert str_list(result) == "5 -> 7 -> 9"

    def test_06(self):
        #  7541
        # +  32
        # -----
        #  7573

        a1 = Node(1)
        a2 = Node(4)
        a3 = Node(5)
        a4 = Node(7)
        a1.next = a2
        a2.next = a3
        a3.next = a4
        # 1 -> 4 -> 5 -> 7

        b1 = Node(2)
        b2 = Node(3)
        b1.next = b2
        # 2 -> 3

        result = add_lists_rec(a1, b1)
        assert str_list(result) == "3 -> 7 -> 5 -> 7"

    def test_07(self):
        #   39
        # + 47
        # ----
        #   86

        a1 = Node(9)
        a2 = Node(3)
        a1.next = a2
        # 9 -> 3

        b1 = Node(7)
        b2 = Node(4)
        b1.next = b2
        # 7 -> 4

        result = add_lists_rec(a1, b1)
        assert str_list(result) == "6 -> 8"

    def test_08(self):
        #   89
        # + 47
        # ----
        #  136

        a1 = Node(9)
        a2 = Node(8)
        a1.next = a2
        # 9 -> 8

        b1 = Node(7)
        b2 = Node(4)
        b1.next = b2
        # 7 -> 4

        result = add_lists_rec(a1, b1)
        assert str_list(result) == "6 -> 3 -> 1"

    def test_09(self):
        #   999
        #  +  6
        #  ----
        #  1005

        a1 = Node(9)
        a2 = Node(9)
        a3 = Node(9)
        a1.next = a2
        a2.next = a3
        # 9 -> 9 -> 9

        b1 = Node(6)
        # 6

        result = add_lists_rec(a1, b1)
        assert str_list(result) == "5 -> 0 -> 0 -> 1"


if __name__ == "__main__":
    unittest.main()
