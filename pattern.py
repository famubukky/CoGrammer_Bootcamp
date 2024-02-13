def print_pattern(rows):
    for i in range(1, rows * 2):
        if i <= rows:
            print("*" * i)
        else:
            print("*" * (2 * rows - i))


if __name__ == "__main__":
    pattern_size = 5
    print_pattern(pattern_size)
