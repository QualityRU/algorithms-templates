# 88757832


class ListQueue:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get(self):
        if self.is_empty():
            return 'error'
        x = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1
        return x.value

    def put(self, x):
        new_node = self.Node(value=x)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1


if __name__ == '__main__':
    n = int(input())
    s = ListQueue()
    res = []

    for _ in range(n):
        command = input().split()
        if len(command) == 2:
            a = s.put(command[1])
            if a == 'error':
                res.append(a)
        elif command[0] == 'get':
            res.append(s.get())
        elif command[0] == 'size':
            res.append(s.size)

    for x in res:
        print(x)
