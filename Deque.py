from Queue import Queue


class Deque:
    def __init__(self, initial_capacity):
        self._queue = Queue(initial_capacity)
        self._max_capacity = initial_capacity

    def is_empty(self):
        return self._queue.is_empty()

    def first(self):
        return self._queue.first()

    def last(self):
        aux_queue = Queue(self._max_capacity)
        element = self._queue.first()
        while self._queue.first():
            element = self._queue.first()
            aux_queue.enqueue(self._queue.dequeue())
        self._queue = aux_queue
        return element

    def __len__(self):
        return len(self._queue)

    def size(self):
        return self._queue.size()

    def add_first(self, element):
        if self.size() == self._max_capacity:
            self._recapacity(2 * self._max_capacity)
        aux_queue = Queue(self._max_capacity)
        aux_queue.enqueue(element)
        while self._queue.first():
            aux_queue.enqueue(self._queue.dequeue())
        self._queue = aux_queue

    def add_last(self, element):
        if self.size() == self._max_capacity:
            self._recapacity(2 * self._max_capacity)
        self._queue.enqueue(element)

    def delete_first(self):
        if self.is_empty():
            return None
        element = self._queue.dequeue()
        if self.size() < self._max_capacity * 0.3:
            self._recapacity(int(self._max_capacity // 1.2))
        return element

    def delete_last(self):
        if self.is_empty():
            return None
        last = self.last()
        aux_queue = Queue(self._max_capacity)
        while self._queue.first() != last:
            aux_queue.enqueue(self._queue.dequeue())
        self._queue = aux_queue
        if self.size() < self._max_capacity * 0.3:
            self._recapacity(int(self._max_capacity // 1.2))
        return last

    def _recapacity(self, new_capacity):
        self._queue.recapacity(new_capacity)
        self._max_capacity = new_capacity

    def rotate(self, k):
        if self.size() > 0:
            k = k % self.size()
            for x in range(k):
                element = self._queue.dequeue()
                self._queue.enqueue(element)

    def __str__(self):
        return "Deque: " + str(list(self._queue))
