class Stack(list):
    def __init__(self):
        super().__init__()

    def push(self, item):
        self.append(item)

    def is_empty(self):
        return len(self) == 0


def check_mirrored(s: Stack) -> bool:
    stack = Stack()
    found_c = False
    for char in s:
        if (not found_c) and (char != "C"):
            stack.push(char)
        elif char == "C":
            found_c = True
        else:
            if stack.pop() != char:
                return False
    return (
        stack.is_empty()
    )  # Need to ensure stack is empty after popping all matching elements


def check_each_section(s: str) -> bool:
    section_stack = Stack()
    for char in s:
        if char != "D":
            section_stack.push(char)
        else:
            if not check_mirrored(section_stack):
                return False
            section_stack = Stack()
    return check_mirrored(section_stack)  # Need to check last D-segment


if __name__ == "__main__":
    print("Running test cases...")
    assert check_each_section("xCxDxCx") == True
    assert check_each_section("DxCxDxCx") == True
    assert check_each_section("xCxDxCxD") == True
    assert check_each_section("xyCyxDxyCyx") == True
    assert check_each_section("xyCxyDxyCyx") == False
    assert check_each_section("xyyzaCazyyxDxyCyxDuwqCqwu") == True
    assert check_each_section("xyyzaCazyyxDxyyzaCazyyu") == False
