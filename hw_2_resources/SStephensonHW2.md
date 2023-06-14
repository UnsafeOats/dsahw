# Homework 2
Shane Stephenson - 06/12/2023

All code used in this assignment, the markdown files used to build this PDF, and the PDF building script can be found in GitHub [here](https://github.com/UnsafeOats/dsahw).

# Problems
## Problem 1a
Pseudo-code implementation.  In this, `i` is the element to insert at base of stack and `s` is the input stack:
\small
```lua
\read_block{problem1a.pseudo}
```
\normalsize
\newpage

## Problem 1b
Pseudo-code implementation.  In this, `i` is the element to insert in the third position of the stack and `s` is the input stack:
```lua
\read_block{problem1b.pseudo}
```
\newpage

## Problem 2a
The below table represents each character as it's being iterated over, what the stack looks like, and any stack operation that is being applied:

\small
|Character|Stack|Stack Operation|
|---------+-----+---------------|
|{        |{    |Push '{'       |
|[        |[{   |Push '['       |
|A        |[{   |None           |
|+        |[{   |None           |
|B        |[{   |None           |
|]        |{    |Pop '['        |
|-        |{    |None           |
|[        |[{   |Push '['       |
|(        |([{  |Push '('       |
|C        |([{  |None           |
|-        |([{  |None           |
|D        |([{  |None           |
|)        |[{   |Pop '('        |
|]        |{    |Pop '['        |
|END      |{    |Check empty    |
\normalsize
After iterating through all characters, stack is non-empty so delimiters are not properly matching.
\newpage

## Problem 2b
The below table represents each character as it's being iterated over, what the stack looks like, and any stack operation that is being applied:

\small
|Character|Stack|Stack Operation|
|---------+-----+---------------|
|(        |(    |Push '('       |
|(        |((   |Push '('       |
|H        |((   |None           |
|)        |(    |Pop '('        |
|\*        |(    |None           |
|{        |{(   |Push '{'       |
|(        |({(  |None           |
|[        |[({( |Push '['       |
|J        |[({( |None           |
|+        |[({( |None           |
|K        |[({( |None           |
|]        |({(  |Pop '['        |
|)        |{(   |Pop '('        |
|}        |(    |Pop '{'        |
|)        |     |Pop '('        |
|END      |     |Check empty    |
\normalsize

After iterating through all characters, stack is empty so delimiters are properly matching.
\newpage

## Problem 3
Pseudo-code implementation checking mirrored strings.  In this function, `w` is the input string in form xCy that will be tested for being mirrored:
\small
```lua
\read_block{problem3.pseudo}
```
\normalsize
A Python implementation of the above algorithm with some test cases is as follows.  As these problems become more complex, I feel it more necessary to convert the pseudo-code into real code that I can use to test various test cases.
\small
```python
\read_block{problem3.py}
```
\normalsize
\newpage

## Problem 4
Within the below pseudo-code, the function named `check_each_section` takes an input string and returns `true` if it matches the pattern and `false` if there is a non-symmetric xCy substring.
\small
```lua
\read_block{problem4.pseudo}
```
The below code is a slight modification and extension of the above Python code.  For this implementation, we use two stacks.  One stack collects everything inbetween the 'D's (the 'D-segments') and the second stack is used within the function to test if the extracted D-segment sequence stack represents a valid xCy mirrored string.  Again, test strings are asserted at the end.
\small
```python
\read_block{problem4.py}
```
\normalsize
\newpage

## Problem 5
Within the pseudo-code implementation below, the function `insert` shows how a second stack can be used to insert a new element into the primary stack and the function `read` will read the element from the stack.

For both these functions, the input parameters `i` are the index to insert/read at, `s` is the stack to do the reading/insertion in, and `e` is the element to insert (for the insertion function).

In this implementation, the bottom of the stack will be indexed at 0 and will increase by increments of +1 for each additional element added to the stack.  Once the stack has been popped a number of times equivalent to the index, the element to insert is pushed onto the stack before moving everything from the secondary stack back onto the primary stack.
The `read` function works similarly to the `insert` function, but it simply peeks once it gets to the appropriate index instead of pushing a new element onto the stack.
\small
```lua
\read_block{problem5.pseudo}
```
Python implementation with test cases are shown below:
\small
```python
\read_block{problem5.py}
```
\normalsize
\newpage

## Problem 6
Need to come back to complete.
\small
```lua
\read_block{problem6.pseudo}
```
\normalsize
\newpage

## Problem 7a
We can parse the expression `(A+B)*(C$(D-E)+F)-G` for postfix in the following steps.  The stack starts with '(' inside.
\small

|Character|Stack|Current expression|
|---------+-----+------------------|
|(|((|NONE|
|A|((|A|
|+|((+|A|
|B|((+|AB
|)|(|AB+|
|\*|(\*|AB+|
|(|(\*(|AB+|
|C|(\*(|AB+C|
|\\$|(\*(|AB+C\$|
|(|(\*((|AB+C\$|
|D|(\*((|AB+C\$D|
|-|(\*((-|AB+C\$D|
|E|(\*((-|AB+C\$DE|
|)|(\*(|AB+C\$DE-|
|+|(\*(+|AB+C\$DE-|
|F|(\*(+|AB+C\$DE-F|
|)|(\*|AB+C\$DE-F+|
|-|(-|AB+C\$DE-F+\*|
|G|(-|AB+C\$DE-F+\*G|
|)|NONE|AB+C\$DE-F+\*G-|

\normalsize
So postfix notation for the expression is `AB+C$DE-F+*G-`
\newpage
For prefix notation, we can parse as follows:
\small

|Character|Stack|Current expression|
|---------+-----+------------------|
|G|(|G|
|-|(-|G|
|(|(-(|G|
|F|(-(|GF|
|+|(-(+|GF|
|(|(-(+(|GF|
|E|(-(+(|GFE|
|-|(-(+(-|GFE|
|D|(-(+(-|GFED|
|)|(-(+|GFED-|
|\$.g|(-(+|GFED-$|
|C|(-(+|GFED-\$.gC|
|)|(-|GFED-\$.gC+|
|\*|(-\*|GFED-\$.gC+|
|(|(-\*(|GFED-\$.gC+|
|B|(-\*(|GFED-\$.gC+B|
|+|(-\*(+|GFED-\$.gC+B|
|A|(-\*(+|GFED-\$.gC+BA|
|)|(-\*|GFED-\$.gC+BA+|
|)|NONE|GFED-\$.gC+BA+\*-|

\normalsize
So the prefix notation for that expression is `GFED-$C+BA+*-`.
\newpage

## Problem 7b
We can parse the expression `A+(((B-C)*(D-E)+F)/G)$(H-J)` in postfix notation using the following steps:
\small

|Character|Stack|Current expression|
|---------+-----+------------------|
|A|(|A|
|+|(+|A|
|(|(+(|A|
|(|(+((|A|
|(|(+(((|A|
|B|(+(((|AB|
|-|(+(((-|AB|
|C|(+(((-|ABC|
|)|(+((|ABC-|
|\*|(+((\*|ABC-|
|(|(+((\*(|ABC-|
|D|(+((\*(|ABC-D|
|-|(+((\*(-|ABC-D|
|E|(+((\*(-|ABC-DE|
|)|(+((\*|ABC-DE-|
|+|(+((+|ABC-DE-\*|
|F|(+((+|ABC-DE-\*F|
|)|(+(|ABC-DE-\*F+|
|/|(+(/|ABC-DE-\*F+|
|G|(+(/|ABC-DE-\*F+G|
|)|(+|ABC-DE-\*F+G/|
|\$|(+|ABC-DE-\*F+G/\$|
|(|(+(|ABC-DE-\*F+G/\$|
|H|(+(|ABC-DE-\*F+G/\$H|
|-|(+(-|ABC-DE-\*F+G/\$H|
|J|(+(-|ABC-DE-\*F+G/\$HJ|
|)|(+|ABC-DE-\*F+G/\$HJ-|
|)|NONE|ABC-DE-\*F+G/\$HJ-+|

\normalsize
So the postfix notation for the expression is `ABC-DE-*F+G/$HJ-+`.
\newpage
To parse the expression into prefix notation, we complete the following steps:
\small

|Character|Stack|Current expression|
|---------+-----+------------------|
|(|((|NONE|
|J|((|J|
|-|((-|J|
|H|((-|JH|
|)|(|JH-|
|\$|(|JH-\$|
|(|((|JH-\$|
|G|((|JH-\$G|
|/|((/|JH-\$G|
|(|((/(|JH-\$G|
|F|((/(|JH-\$GF|
|+|((/(+|JH-\$GF|
|(|((/(+(|JH-\$GF|
|E|((/(+(|JH-\$GFE|
|-|((/(+(-|JH-\$GFE|
|D|((/(+(-|JH-\$GFED|
|)|((/(+|JH-\$GFED-|
|\*|((/(+\*|JH-\$GFED-|
|(|((/(+\*(|JH-\$GFED-|
|C|((/(+\*(|JH-\$GFED-C|
|-|((/(+\*(-|JH-\$GFED-C|
|B|((/(+\*(-|JH-\$GFED-CB|
|)|((/(+\*|JH-\$GFED-CB-|
|)|((/|JH-\$GFED-CB-\*+|
|)|(|JH-\$GFED-CB-\*+/|
|+|(+|JH-\$GFED-CB-\*+/|
|A|(+|JH-\$GFED-CB-\*+/A|
|)|NONE|JH-\$GFED-CB-\*+/A+|

\normalsize
So the prefix notation for the expression is `JH-$GFED-CB-*+/A+`

## Problem 8a
Out of time.
