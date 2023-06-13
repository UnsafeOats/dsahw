class Stack(list):
    def __init__(self):
        super().__init__()

    def push(self, item):
        self.append(item)

    def is_empty(self):
        return len(self) == 0

    def peek(self):
        return self[-1]

    def insert(self, item, index: int) -> 'Stack':
        secondary_stack = Stack()
        for _ in range(index):
            secondary_stack.push(self.pop())
        self.push(item)
        for _ in range(index):
            self.push(secondary_stack.pop())
        return self

    def read(self, index: int):
        secondary_stack = Stack()
        for _ in range(index):
            secondary_stack.push(self.pop())
        output = self.peek()
        for _ in range(index):
            self.push(secondary_stack.pop())
        return output


if __name__ == "__main__":
    print("Running test cases...")
    # create the test stack Stack(a, b, c, d)
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    stack.push('d')

    # check if each item in the stack returns proper index
    assert stack.read(0) == 'd'
    assert stack.read(1) == 'c'
    assert stack.read(2) == 'b'
    assert stack.read(3) == 'a'

    # insert 'e' into index 2 of the stack
    stack.insert('e', 2)
    assert stack.read(0) == 'd'
    assert stack.read(1) == 'c'
    assert stack.read(2) == 'e'
    assert stack.read(3) == 'b'
    assert stack.read(4) == 'a'

    # insert 'z' into index 5 of the stack
    stack.insert('z', 5)
    assert stack.read(0) == 'd'
    assert stack.read(1) == 'c'
    assert stack.read(2) == 'e'
    assert stack.read(3) == 'b'
    assert stack.read(4) == 'a'
    assert stack.read(5) == 'z'
