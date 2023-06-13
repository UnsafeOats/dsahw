# Homework Problems
Shane Stephenson
JHU EN.605.202.81.SU23

## Overview
This repository contains the writeup and any generated code for each homework assignment in my data structures course.

The outlines for the final PDFs to be submitted are done in a modified version of markdown extended by Pandoc and a custom build process.  You need to create a markdown .md file and generally outline the homework problems and answers.  There's a build script that will impute any specified code files you write using the `\read_block{}` command.  For example, if I have an answer to problem one written in a Python script named `problem1.py`, I can include it within the final PDF with:
```
# Problem 1
The below code implements the requirements in the first problem:
```python
\read_block{problem1.py}
```
```

Once you've got your extended markdown file created, you can build the PDF by simply calling `build.py` and pointing it towards the folder with your markdown file and code snippets in it.  For example, if all our assignment resources are in a folder named `/assignment_1`, we can build the PDF like so:
```console
foo@bar: ~$ python3 build.py assignment_1
```

The output name of the generated PDF will match the name of your markdown file.

## Requirements

In order to use the build tool to create your PDF, you need to have the Pandoc CLI installed and an appropriate TeX renderer.  Additionally, you need a Python installation at least greater than 3.9.
