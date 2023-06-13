#!/usr/bin/env python

from sys import argv
from glob import glob
from subprocess import run
from tempfile import gettempdir
from os import times, remove, path


def read_block(block_path: str):
    if block_path.endswith('.py'):
        print(f"Running tests for Python block: {block_path}")
        run_tests = run(['python', block_path], capture_output=True)
        run_tests.check_returncode()
    elif block_path.endswith('.pseudo'):
        print(f"Inserting pseudocode block without tests: {block_path}")
    with open(block_path, "r") as block:
        return block.read()


def build_assignment(assignment: str):
    normalized_assignment = assignment.rstrip("/")
    print("Building assignment: {}".format(normalized_assignment))
    for md_file in glob(f"{normalized_assignment}/*.md"):
        print(f"Building file: {md_file}")
        parsed_lines = []
        with open(md_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.strip().startswith("\\read_block{"):
                    block_name = line.split("{")[1].split("}")[0]
                    parsed_lines.append(read_block(f"{normalized_assignment}/{block_name}"))
                else:
                    parsed_lines.append(line)
        temp_file_name = f"{gettempdir()}/mdtopdf{hash(times())}.md"
        with open(temp_file_name, "w+") as temp_file:
            temp_file.writelines(parsed_lines)

        print(f"Running pandoc on {temp_file_name}")
        # For the below code, I chose to use a subprocess instead of using the Python
        # Pandoc library because I don't want the build script to require any external
        # Pip dependencies.  This simplifies the build process as no one needs to create
        # and manage a virtual environment.
        run_build = run(['pandoc', temp_file_name, '-o', f"assignments/{path.basename(md_file).split('.')[0]}.pdf"])
        run_build.check_returncode()
        remove(temp_file_name)


if __name__ == "__main__":
    if len(argv) > 1:
        if argv[1] in ["--help", "-h"]:
            print("Usage: ./build.py <assignment folder>")
            print("Example: ./build.py hw2")
            print("Note: If no assignment folder specified, will build all assignments")
        else:
            build_assignment(argv[1])
    else:
        print("Building all assignments.")
        for assignment in glob("**/"):
            build_assignment(assignment)
