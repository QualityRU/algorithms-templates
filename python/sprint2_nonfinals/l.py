# 88758136

class Solution:
    def __init__(self):
        self.ab = [1, 1]

    def fibonacci(self, n, k):
        d = 10**k
        if n < 2:
            fib = 1
        else:
            n -= 1
            for i in range(n):
                s = (self.ab[0] + self.ab[1]) % d
                self.ab[0] = self.ab[1]
                self.ab[1] = s
                fib = self.ab[1]
        return fib


if __name__ == '__main__':
    n, k = (int(i) for i in input().split())
    solution = Solution()
    fib = solution.fibonacci(n, k)
    print(fib)
