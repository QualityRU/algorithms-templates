# 88757334


class StackMaxEffective:
    def __init__(self):
        self.__items = []
        self.__max = []

    def is_empty(self):
        return not self.__items

    def push(self, item):
        if not self.__max or item > self.__max[-1]:
            self.__max.append(item)
        else:
            self.__max.append(self.__max[-1])
        self.__items.append(item)

    def get_max(self):
        if self.is_empty():
            return None
        return self.__max[-1]

    def pop(self):
        if self.is_empty():
            return 'error'
        self.__max.pop()
        return self.__items.pop()


if __name__ == '__main__':
    s = StackMaxEffective()
    n = int(input())
    results = []

    for _ in range(n):
        command = input().split()
        if command[0] == 'push':
            s.push(int(command[1]))
        elif command[0] == 'pop':
            if s.pop() == 'error':
                results.append('error')
        elif command[0] == 'get_max':
            results.append(s.get_max())

    for result in results:
        print(result)
