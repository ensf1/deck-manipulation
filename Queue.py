class Queue:
    def __init__(self, initial_capacity):
        self._data = [None] * initial_capacity
        self._size = 0
        self._first = 0

    def __len__(self):
        return self._size

    def size(self):
        return len(self)

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            return None
        return self._data[self._first]

    def enqueue(self, e):
        available = (self._first + self._size) % len(self._data)
        self._data[available] = e
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        result = self._data[self._first]
        self._data[self._first] = None
        self._first = (self._first + 1) % len(self._data)
        self._size -= 1
        return result

    def recapacity(self, new_capacity):
        aux_data = self._data
        self._data = [None] * new_capacity
        index = self._first
        for k in range(self._size):
            self._data[k] = aux_data[index]
            index = (1 + index) % len(aux_data)
        self._first = 0
