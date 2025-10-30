def read_file_to_dict(filename):
    """
    Reads student data from a file and returns a dictionary.
    Handles file errors and data validation gracefully.
    """
    student_dict = {}
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split()
                    if len(parts) >= 2:
                        name = parts[0]
                        try:
                            grade = float(parts[1])
                            if 0 <= grade <= 100:  # Validate grade range
                                student_dict[name] = grade
                            else:
                                print(f"Warning: Grade out of range for {name} on line {line_number}")
                        except ValueError:
                            print(f"Warning: Invalid grade format for {name} on line {line_number}")
                    else:
                        print(f"Warning: Insufficient data on line {line_number}")
    except FileNotFoundError:
        print(f"Info: File '{filename}' not found. Starting with empty database.")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    return student_dict


def add_student(student_dict, name, grade):
    """
    Adds a new student to the dictionary with validation.
    """
    try:
        grade = float(grade)
        if grade < 0 or grade > 100:
            return "Error: Grade must be between 0 and 100"
        
        if name in student_dict:
            return f"Warning: {name} already exists. Overwriting grade."
        
        student_dict[name] = grade
        return f"Success: Added {name} with grade {grade}"
    except ValueError:
        return "Error: Grade must be a valid number"


def calculate_average(student_dict):
    """
    Calculates the average grade from the dictionary.
    Returns 0 if dictionary is empty.
    """
    if not student_dict:
        return 0
    return sum(student_dict.values()) / len(student_dict)


def print_above_average_students(student_dict, average):
    """
    Prints students who scored above the given average.
    Handles empty dictionaries and edge cases.
    """
    if not student_dict:
        print("No student data available.")
        return
    
    above_average_students = {
        name: grade for name, grade in student_dict.items() 
        if grade > average
    }
    
    if not above_average_students:
        print("No students scored above the average.")
        return
    
    print(f"\nStudents above average ({average:.2f}):")
    print("-" * 40)
    for name, grade in sorted(above_average_students.items(), 
                             key=lambda x: x[1], reverse=True):
        print(f"{name:<15} : {grade:>6.2f}")


# Main program
if __name__ == "__main__":
    # Initialize data from file
    filename = "students.txt"
    students = read_file_to_dict(filename)
    
    print("Student Grade Management System")
    print("=" * 40)
    
    if students:
        print(f"Loaded {len(students)} student records from file.")
    else:
        print("No existing student records found.")
    
    # Interactive menu system
    while True:
        print("\nOptions:")
        print("1. Add new student data")
        print("2. Calculate average grade")
        print("3. Print students who scored above average")
        print("4. View all students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            grade = input("Enter student grade (0-100): ").strip()
            result = add_student(students, name, grade)
            print(result)

        elif choice == "2":
            average = calculate_average(students)
            if students:
                print(f"\nAverage grade: {average:.2f}")
                print(f"Total students: {len(students)}")
            else:
                print("No students in database.")

        elif choice == "3":
            average = calculate_average(students)
            print_above_average_students(students, average)

        elif choice == "4":
            if students:
                print("\nAll Students:")
                print("-" * 25)
                for name, grade in sorted(students.items()):
                    print(f"{name:<15} : {grade:>6.2f}")
            else:
                print("No students in database.")

        elif choice == "5":
            print("Thank you for using Student Grade Management System!")
            break

        else:
            print("Invalid choice. Please enter a number between 1-5.")