class ListNode:
    def __init__(self, x):
        self.val = x
        self.index = 0
        self.next = None

    def __next__(self):
        try:
            self.next = self.val[self.index]
            self.index += 1
        except:
            self.next = 0
        print(self.next)
        return self.next

    def __reversed__(self):
        return reversed(self.val)


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        carry_bit = 0
        while True:
            fn = next(l1, 0)
            sn = next(l2, 0)
            if fn == 0 and sn == 0:
                break
            else:
                if fn + sn + carry_bit >= 10:
                    res.append(fn + sn + carry_bit - 10)
                    carry_bit = 1
                else:
                    res.append(fn + sn + carry_bit)
                    carry_bit = 0
        if carry_bit > 0:
            res.append(carry_bit)
        return res

solution = Solution()
l1 = ListNode([2, 3, 4])
l2 = ListNode([4, 5, 7])
print(solution.addTwoNumbers(reversed(l1), reversed(l2)))
