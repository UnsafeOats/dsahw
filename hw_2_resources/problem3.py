class Stack(list):
    # This is just a wrapper class around Python lists to so that we can interact
    # with the lists in a way that idiomatic of a stack with methods to push and check
    # if the stack is empty.
    def __init__(self):
        super().__init__()

    def push(self, item):
        self.append(item)

    def is_empty(self):
        return len(self) == 0


def check_mirrored(s: str) -> bool:
    stack = Stack()
    found_c = False
    output = True
    for char in s:
        if (not found_c) and (char != "C"):
            stack.push(char)
        elif char == "C":
            found_c = True
        else:
            if stack.pop() != char:
                output = False
    return output and stack.is_empty()  # using 'and' here to validate stack is empty


if __name__ == "__main__":
    print("Running test cases...")
    assert check_mirrored("xCx") == True
    assert check_mirrored("xyCyx") == True
    assert check_mirrored("xyCy") == False
    assert check_mirrored("xyCxy") == False
    assert check_mirrored("xyyzaCazyyx") == True
    assert check_mirrored("xyyzaCazyyu") == False
