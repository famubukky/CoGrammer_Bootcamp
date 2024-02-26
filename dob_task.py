#Display of codes that write a program and read data form text file and print it in two different sections 
def print_dob_data(file_path):
    names = []
    birthdates = []

    # Read data from file
    with open(DOB.txt) as file:
     for line in file:
            # Split each line into name and birthdate
            name, birthdate = line.strip().split(',')

            # Append name and birthdate to their respective lists
            names.append(name)
            birthdates.append(birthdate)

    # Print names section
    print("Name")
    for name in names:
        print(name)

    print()  # Print an empty line for spacing

    # Print birthdates section
    print("Birthdate")
    for birthdate in birthdates:
        print(birthdate)


if __name__ == "__main__":
    file_path = "DOB.txt"
    print_dob_data(file_path)

