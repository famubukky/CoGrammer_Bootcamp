#code that register multiple students 
def register_students(num_students):
    with open("reg_form.txt", "w") as file:
        for i in range(1, num_students + 1):
            student_id = input(f"Enter ID number for student {i}: ")#code that ask student to input student number
            file.write(f"{student_id}\n")
            file.write("-" * 20 + "\n")

if __name__ == "__main__":
    num_students = int(input("How many students are registering? "))
    register_students(num_students)
    print("Student registration completed. Check 'reg_form.txt' for the attendance register.")#code that prints student registration complete
