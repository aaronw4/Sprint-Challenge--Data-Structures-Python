class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []
        self.total = 0
        self.count = 0

    def append(self, item):
        if self.total >= self.capacity:
            if self.count == self.capacity:
                self.count -= self.capacity
            self.arr[self.count] = item
        else:
            self.arr.append(item)
        self.count += 1
        self.total += 1

    def get(self):
        return self.arr