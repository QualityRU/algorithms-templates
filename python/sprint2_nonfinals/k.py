# 88757965


class Solution:
    def __init__(self):
        self.__memo = {}

    def fibonacci(self, n):
        if n in self.__memo:
            return self.__memo[n]

        if n == 0 or n == 1:
            result = 1
        else:
            result = self.fibonacci(n - 1) + self.fibonacci(n - 2)

        self.__memo[n] = result
        return result


if __name__ == '__main__':
    n = int(input())
    solution = Solution()
    print(solution.fibonacci(n))
