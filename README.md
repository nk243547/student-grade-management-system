# Student Grade Management System
# Overview
A Python-based grade management system that allows educators to efficiently manage student grades, perform statistical analysis, and generate insightful reports. The system features file-based data persistence, interactive menu navigation, and robust error handling.

# Features
# Core Functionality
File-based Data Storage: Read and manage student grades from text files

Interactive Menu System: User-friendly command-line interface

Real-time Data Analysis: Calculate averages and identify top performers

Data Validation: Comprehensive input validation and error handling

# Technical Capabilities
Add new student records with grade validation

Calculate class average grade

Identify students performing above average

View all student records in organized format

Persistent data storage with automatic loading

# Quick Start
# 1. If you are using Visual Studio Code run the program directly:
`python3 main.py`

# 2. If you are using Jupyter notebook
Open the .ipynb file in  jupyter and execute the cells one by one

# Data File Format
```
StudentName1 Grade1
StudentName2 Grade2
StudentName3 Grade3
```

# Example:
```
Alice 85
Bob 92
Charlie 78
David 88
Emma 95
```

# Usage Guide

# Menu Options
1. Add New Student Data
Input: Student name and grade (0-100)

Validation: Checks for valid grade range and numeric input

Features: Prevents duplicate entries with warning

2. Calculate Average Grade
Output: Class average with precision to 2 decimal places

Handles: Empty database scenarios gracefully

3. Print Above Average Students
Analysis: Identifies students scoring above class average

Presentation: Sorted by grade (descending) with formatted output

4. View All Students
Display: Alphabetically sorted list of all students

Format: Clean, tabular presentation

5. Exit
Clean program termination with farewell message

# Example Session with Output
```
Options:
1. Add new student data
2. Calculate average grade
3. Print students who scored above average
4. View all students
5. Exit
Enter your choice (1-5):  1
Enter student name:  John
Enter student grade (0-100):  78
Success: Added John with grade 78.0

Options:
1. Add new student data
2. Calculate average grade
3. Print students who scored above average
4. View all students
5. Exit
Enter your choice (1-5):  4

All Students:
-------------------------
Alice           :  85.00
Bob             :  92.00
Charlie         :  78.00
David           :  88.00
Emma            :  95.00
Frank           :  72.00
John            :  78.00

Options:
1. Add new student data
2. Calculate average grade
3. Print students who scored above average
4. View all students
5. Exit
Enter your choice (1-5):  3

Students above average (84.00):
----------------------------------------
Emma            :  95.00
Bob             :  92.00
David           :  88.00
Alice           :  85.00

Options:
1. Add new student data
2. Calculate average grade
3. Print students who scored above average
4. View all students
5. Exit
Enter your choice (1-5):  5
Thank you for using Student Grade Management System!
```

# Technical Implementation
# Key Functions
`read_file_to_dict(filename)`
Purpose: File I/O and data parsing

Features: Error handling, data validation, graceful degradation

Returns: Dictionary of student-grade pairs

`add_student(student_dict, name, grade)`
Purpose: Data entry with validation

Validation: Grade range (0-100), numeric input, duplicate handling

Returns: Success/error messages

`calculate_average(student_dict)`
Purpose: Statistical analysis

Handles: Empty dictionaries

Returns: Float representing average grade

`print_above_average_students(student_dict, average)`
Purpose: Data filtering and reporting

Features: Conditional filtering, sorted output, formatted display

# Error Handling
The system includes comprehensive error handling for:

File Operations: Missing files, permission issues

Data Validation: Invalid grades, malformed input

User Input: Invalid menu choices, non-numeric grades

Edge Cases: Empty databases, no above-average students
