# Контест ID: 88726931


class Stack:
    def __init__(self):
        self.__data = list()

    def push(self, element):
        self.__data.append(element)

    def pop(self):
        if not len(self.__data):
            raise IndexError
        return self.__data.pop()


def calculate(line):
    stack = Stack()
    operator = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y // x,
    }

    for v in line.split(' '):
        try:
            stack.push(int(v))
        except ValueError:
            stack.push(operator[v](stack.pop(), stack.pop()))

    return stack.pop()


if __name__ == '__main__':
    print(calculate(input()))
