import os


def _extract_lines(file):
    with open(file, encoding="utf-8") as input_file:
        lines = input_file.readlines()
    return lines


def file_coverage_parser():
    file = "./htmlcov/coverage.txt"
    lines = _extract_lines(file)

    for index in range(2, len(lines) - 2):
        blocks = lines[index].split(" ")
        if blocks[-1][:-1] != "100%":
            message = blocks[0] + ": " + blocks[-1][:-1]
            print(message)
            return False
    print("true")
    return True


def whole_coverage_parser(file):
    lines = _extract_lines(file)

    blocks = lines[-1].split(" ")
    if blocks[-1][:-1] != "100%":
        message = "whole coverage: " + blocks[-1][:-1]
        print(message)
        return False
    print("true")
    return True


def print_file_name():
    print("Directory contents:")
    for f in os.listdir():
        print(f)
