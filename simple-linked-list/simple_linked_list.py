class Node(object):
    def __init__(self, value, next=None):
        self.__value = value
        self.__next = next

    def value(self):
        return self.__value

    def next(self):
        return self.__next


class LinkedList(object):
    def __init__(self, values=[]):
        self.__head = None

        for value in values:
            self.__head = Node(value, self.__head)

    def __len__(self):
        return sum(1 for _ in self)

    def __iter__(self):
        node = self.__head

        while node is not None:
            yield node.value()
            node = node.next()

    def head(self):
        if self.__head is None:
            raise EmptyListException("List contains no items")

        return self.__head

    def push(self, value):
        self.__head = Node(value, self.__head)

    def pop(self):
        if self.__head is None:
            raise EmptyListException("List contains no items")

        last = self.__head
        self.__head = last.next()
        return last.value()

    def reversed(self):
        return LinkedList(f for f in self)


class EmptyListException(Exception):
    pass
