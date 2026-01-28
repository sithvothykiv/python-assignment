# Python Assignment: Student Management Program (OOP Practice)
## Objective
Practice functions, classes, objects, attributes, methods, and basic OOP concepts by building a simple Student Management Program.


### Assignment Description
You are asked to create a program that can:

* Store student information
* Calculate student average score
* Display student details
* Use functions, class, object, and OOP principles



## Part 1: Create a Student Class
Create a class named Student with the following:

Attributes:
* name (string)
* student_id (string or integer)
* marks (dictionary: subject → score)

Methods:
* __init__(self, name, student_id, marks)
* calculate_average(self)
    * Returns the average score
* display_info(self)
* Prints student name, ID, marks, and average


## Part 2: Use Functions (Outside the Class)
Write these functions:
1. add_student()
    * Return a Student object with fixed values.
    * Return a Student object
2. show_all_students(students_list)
    * Loop through list and display all students


## Part 3: Main Program (Object Usage)
* Create at least 3 students using add_student()
* Store them in a list
* Call functions and class methods

## Expected Output:
```python
Name: Lina
ID: 101
Marks: {'Math': 85, 'Science': 90, 'English': 88}
Average: 87.67
--------------------
Name: Sok
ID: 102
Marks: {'Math': 78, 'Science': 95, 'English': 80}
Average: 84.33
```