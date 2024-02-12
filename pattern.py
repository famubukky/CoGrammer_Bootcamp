def print_pattern(rows):
    for i in range(i, rows * 2):
        if i <= rows:
            print("*" * (2 * rows - i))
            
            
if __name__ == "__main__":
    pattern_size = 10 # This line of code shows number of rows
    print_pattern(pattern_size)