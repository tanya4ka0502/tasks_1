class MinStack:
    def __init__(self):
        self._data = []
        self._min = []

    def push(self, x: int) -> None:
        self._data.append(x)
        if not self._min:
            self._min.append(x)
        else:
            self._min.append(min(x, self._min[-1]))

    def pop(self) -> None:
        if not self._data:
            raise IndexError("pop from empty stack")
        self._data.pop()
        self._min.pop()

    def top(self) -> int:
        if not self._data:
            raise IndexError("top from empty stack")
        return self._data[-1]

    def get_min(self) -> int:
        if not self._min:
            raise IndexError("get_min from empty stack")
        return self._min[-1]
