from typing import List


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    data: List[str]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.clear()

    def read(self) -> str:
        if self.data:
            return self.data.pop(0)
        else:
            raise BufferEmptyException("Nothing has been written to the buffer")

    def write(self, data: str) -> None:
        if self.full:
            raise BufferFullException(
                "The buffer is at capacity and cannot be written to"
            )

        self.data.append(data)

    def overwrite(self, data: str) -> None:
        if self.full:
            self.read()

        self.write(data)

    def clear(self) -> None:
        self.data = []

    @property
    def full(self) -> bool:
        return len(self.data) is self.capacity
