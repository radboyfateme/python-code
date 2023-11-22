class Counter:
    def __init__(self, start, end, step=3):
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            current_value = self.current
            self.current += self.step
            return current_value


counter_instance = Counter(10, 100)


for number in counter_instance:
    print(number)


