# 暴力求解
class Solution1(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)


# 动态规划
class Solution2(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        else:
            prev, curr, f = 0, 1, 0
            for i in range(2, n + 1):
                f = prev + curr
                prev = curr
                curr = f
            return f
