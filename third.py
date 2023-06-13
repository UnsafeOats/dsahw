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


def check_mirrored(s: Stack) -> bool:
    stack = Stack()
    found_c = False
    output = True
    for char in s:
        if (not found_c) and (char != 'C'):
            stack.push(char)
        elif char == 'C':
            found_c = True
        else:
            if stack.pop() != char:
                output = False
    return output and stack.is_empty() # using 'and' here to validate stack is empty


def check_each_section(s: str) -> bool:
    section_stack = Stack()
    output = True
    for char in s:
        if char != 'D':
            section_stack.push(char)
        else:
            if not check_mirrored(section_stack):
                output = False
            section_stack = Stack()
    return output and check_mirrored(section_stack) # using 'and' section here to validate final section is truly mirrored


if __name__ == "__main__":
    print("Running test cases...")
    assert check_each_section('xCxDxCx') == True
    assert check_each_section('DxCxDxCx') == True
    assert check_each_section('xCxDxCxD') == True
    assert check_each_section('xyCyxDxyCyx') == True
    assert check_each_section('xyCxyDxyCyx') == False
    assert check_each_section('xyyzaCazyyxDxyCyxDuwqCqwu') == True
    assert check_each_section('xyyzaCazyyxDxyyzaCazyyu') == False
