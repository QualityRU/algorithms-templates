# 88757555


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]


def is_correct_bracket_seq(s):
    stack = Stack()
    brackets = {'(': ')', '{': '}', '[': ']'}

    for x in s:
        if x in brackets:
            stack.push(x)
        elif not stack.isEmpty() and brackets[stack.peek()] == x:
            stack.pop()
        else:
            stack.push(x)
            break

    return stack.isEmpty()


if __name__ == '__main__':
    seq = input()
    result = is_correct_bracket_seq(seq)
    print(result)
