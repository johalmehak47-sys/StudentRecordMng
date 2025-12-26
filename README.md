# Student Record Management System

## Project Description
This is a command-line based Student Record Management System built as part of my introduction to Python and AI/ML course. The project manages student records including their roll number, name, age, course, and CGPA. All data is stored in a plain text file to ensure persistence across program sessions.

## Features
The system provides the following functionality:

### Core Features
1. **Add Student** - Register a new student with unique roll number
2. **View All Students** - Display complete list of all registered students
3. **Search Student** - Find a specific student by their roll number
4. **Update Student Details** - Modify existing student information (roll number, name, age, course, or CGPA)
5. **Delete Student** - Remove a student record from the system

### Bonus Features
6. **Sort Students by CGPA** - Display all students ranked from highest to lowest CGPA
7. **Count Total Students** - Show the total number of students in the system

### Additional Capabilities
- **Data Persistence** - All records are saved to `students.txt` and automatically loaded when the program starts
- **Input Validation** - Prevents duplicate roll numbers and handles invalid menu choices
- **Error Handling** - Manages empty records and missing files gracefully

## How to Run the Program

### Prerequisites
- Python 3.x installed on your system

### Steps
1. Save the program file (e.g., `student_management.py`)
2. Open terminal/command prompt in the same directory
3. Run the command:
```bash
   python student_management.py
```
4. The program will:
   - Load existing student records (if `students.txt` exists)
   - Display the main menu
   - Wait for your input

### Using the Program
- Enter a number (1-8) to select an option from the menu
- Follow the on-screen prompts to input data
- The program will continue running until you select option 8 (Exit)

## What I Learned

### Python Concepts Applied

**1. Variables & Data Types**
- Used integers for roll numbers and age
- Strings for names and courses
- Floats for CGPA values
- Learned when to use each data type appropriately

**2. Classes & Objects**
- Created a `Student` class to represent student data
- Used `__init__()` method to initialize attributes
- Understood the difference between a class (blueprint) and objects (instances)
- Learned that class methods operate on single objects, not collections

**3. Functions**
- Created separate functions for each operation (add, view, search, update, delete)
- Understood the importance of single-responsibility principle
- Learned to keep code organized by separating concerns

**4. Loops**
- Used `while True` loop for the continuous menu system
- Applied `for` loops to iterate through student lists
- Learned how to break out of loops when needed

**5. Conditionals**
- Implemented if-elif-else chains for menu navigation
- Used conditionals for validation (duplicate checks, empty records)
- Applied logical operators to make decisions

**6. File Handling**
- Learned to read from files using `open()` with "r" mode
- Wrote data to files using "w" mode
- Understood the pipe-separated format for structured data storage
- Handled `FileNotFoundError` when file doesn't exist

**7. Data Structures**
- Used lists to store multiple student objects in memory
- Applied list methods like `append()` and `remove()`
- Learned about the `sorted()` function with lambda expressions

**8. String Manipulation**
- Used `strip()` to remove whitespace
- Applied `split()` to parse file data
- Formatted output using f-strings

### Key Takeaways

**Problem-Solving Skills:**
- Breaking a large project into smaller, manageable steps
- Thinking about data flow (load → process → save)
- Debugging logical errors (like placing `save_students()` after `return`)

**Program Structure:**
- Importance of separating data (Student class) from operations (functions)
- Why global variables should be used carefully
- How to organize code for readability

**Error Prevention:**
- Validating user input before processing
- Checking for edge cases (empty lists, duplicate entries)
- Providing helpful error messages to users

**Real-World Application:**
- Understanding that programs need persistent storage
- Learning that user experience matters (clear menus, feedback messages)
- Recognizing that simple solutions (text files) can be effective for small projects

### Challenges Faced
1. Initially confused about whether management functions should be inside or outside the Student class
2. Struggled with file format design - learned that pipe-separated values work well
3. Had to debug the `save_students()` placement in update function
4. Learned the importance of the menu loop for continuous program operation

### What's Next
This project gave me a solid foundation in Python basics. Future improvements could include:
- Adding more validation (age ranges, CGPA limits)
- Implementing search by name or course
- Creating backup functionality
- Adding grade calculations based on CGPA

## File Structure
```
project_folder/
│
├── student_management.py    # Main program file
├── students.txt              # Data storage (created automatically)
└── README.md                 # This file
```

## Sample Data Format
The `students.txt` file stores data in this format:
```
101|John Doe|20|Computer Science|8.5
102|Jane Smith|21|Electrical Engineering|9.0
103|Bob Johnson|19|Mechanical Engineering|7.8
```

## Acknowledgments
This project was completed as part of the AI/ML course introduction module, applying concepts from the first two chapters on Python fundamentals.
