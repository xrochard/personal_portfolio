def file_coverage_parser(file, debug=False):
    if debug:
        lines = file.splitlines(True)
    else:
        with open(file) as f:
            lines = f.readlines()
    for index in range(2, len(lines) - 2):
        blocks = lines[index].split(" ")
        if blocks[-1][:-1] != "100%":
            message = blocks[0] + ": " + blocks[-1][:-1]
            raise ValueError(message)
