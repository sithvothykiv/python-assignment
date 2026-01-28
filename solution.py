class Student:
    def __init__(self, name, student_id, marks):
        self.name = name
        self.student_id = student_id
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks.values()) / len(self.marks)

    def display_info(self):
        print("Name:", self.name)
        print("ID:", self.student_id)
        print("Marks:", self.marks)
        print("Average:", round(self.calculate_average(), 2))
        print("-" * 20)


# Function with static values
def add_student(name, student_id, marks):
    return Student(name, student_id, marks)


def show_all_students(students):
    for student in students:
        student.display_info()


# Main Program
students = []

# Static students
s1 = add_student("Lina", 101, {"Math": 85, "Science": 90, "English": 88})
s2 = add_student("Sok", 102, {"Math": 78, "Science": 95, "English": 80})
s3 = add_student("Dara", 103, {"Math": 92, "Science": 89, "English": 94})

students.append(s1)
students.append(s2)
students.append(s3)

show_all_students(students)
