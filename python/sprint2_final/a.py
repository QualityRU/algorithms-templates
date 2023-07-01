# Контест ID: 88726817


class IsFullException(Exception):
    """Кастомное исключение для is_full() метода."""


class IsEmptyException(Exception):
    """Кастомное исключение для is_empty() метода."""


class Deque:
    """Дек."""

    def __init__(self, size):
        self.__max_size = size
        self.__buffer = [None] * size
        self.__front = 0
        self.__rear = 0
        self.__count = 0

    def is_empty(self):
        return self.__count == 0

    def is_full(self):
        return self.__count == self.__max_size

    def push_back(self, value):
        if self.is_full():
            raise IsFullException
        self.__buffer[self.__rear] = value
        self.__rear = (self.__rear + 1) % self.__max_size
        self.__count += 1

    def push_front(self, value):
        if self.is_full():
            raise IsFullException
        self.__front = (self.__front - 1) % self.__max_size
        self.__buffer[self.__front] = value
        self.__count += 1

    def pop_back(self):
        if self.is_empty():
            raise IsEmptyException
        self.__rear = (self.__rear - 1) % self.__max_size
        print(self.__buffer[self.__rear])
        self.__buffer[self.__rear] = None
        self.__count -= 1

    def pop_front(self):
        if self.is_empty():
            raise IsEmptyException
        print(self.__buffer[self.__front])
        self.__buffer[self.__front] = None
        self.__front = (self.__front + 1) % self.__max_size
        self.__count -= 1


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    deque = Deque(m)
    cmds = {
        'push_back': deque.push_back,
        'push_front': deque.push_front,
        'pop_front': deque.pop_front,
        'pop_back': deque.pop_back,
    }

    for _ in range(n):
        cmd, *values = input().strip().split()
        values = tuple(map(int, values))
        try:
            cmds.get(cmd, lambda: print('Нет такой команды!'))(*values)
        except (IsFullException, IsEmptyException):
            print('error')
        except Exception as e:
            print(f'error:\n{e}')
