def main():
    total = 0
    count = 0

    while True:
        num = input("Enter a number (-1 to stop): ")

        if num == "-1":
            break

        try:
            num = float(num)
            total += num
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if count == 0:
        print("No numbers entered.")
    else:
        average = total / count
        print(f"The average of the entered numbers is: {average:.2f}")


if __name__ == "__main__":
    main()
