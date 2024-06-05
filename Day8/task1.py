class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.enrolled_courses = []

    def enroll_in_course(self, course):
        self.enrolled_courses.append(course)

    def __str__(self):
        enrolled_courses_names = [course.name for course in self.enrolled_courses]
        return f"""
___________________________________
Name --> ({self.name})
Student ID --> ({self.student_id})
Grade --> ({self.grade})
Enrolled Courses --> ({', '.join(enrolled_courses_names)})
___________________________________
"""

class Teacher:
    def __init__(self, name, teacher_id, subject):
        self.name = name
        self.teacher_id = teacher_id
        self.subject = subject
        self.assigned_courses = []

    def assign_course(self, course):
        self.assigned_courses.append(course)

    def __str__(self):
        assigned_courses_names = [course.name for course in self.assigned_courses]
        return f"""
___________________________________
Name --> ({self.name})
Teacher ID --> ({self.teacher_id})
Subject --> ({self.subject})
Assigned Courses --> ({', '.join(assigned_courses_names)})
___________________________________
"""

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.enrolled_students = []
        self.teacher = None

    def add_student(self, student):
        self.enrolled_students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def enrol_std(self):
        return [student.name for student in self.enrolled_students]

    def __str__(self):
        students_names = ', '.join(self.enrol_std())
        teacher_name = self.teacher.name if self.teacher else "None"
        return f"""
___________________________________
Course ID --> ({self.course_id})
Name --> ({self.name})
Teacher --> ({teacher_name})
Students --> ({students_names})
___________________________________
"""

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def assign_teacher_to_course(self, teacher, course):
        teacher.assign_course(course)
        course.assign_teacher(teacher)

    def enroll_student_in_course(self, student, course):
        student.enroll_in_course(course)
        course.add_student(student)

    def __str__(self):
        return f"""
School Name: {self.name}
Students: {len(self.students)}
Teachers: {len(self.teachers)} 
Courses: {len(self.courses)})
"""


school = School("Scholl Number 9")

def menu():
    print("\n--- Menu ---")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Add Course")
    print("4. Assign Teacher to Course")
    print("5. Enroll Student in Course")
    print("6. Display Details")
    print("7. Exit")
    return input("Choose an option: ")

while True:
    choice = menu()
    
    if choice == '1':
        name = input("Student Name: ")
        student_id = input("Student ID: ")
        grade = input("Student Grade: ")
        student = Student(name, student_id, grade)
        school.add_student(student)
        print("Student added.")
    
    elif choice == '2':
        name = input("Teacher Name: ")
        teacher_id = input("Teacher ID: ")
        subject = input("Teacher Subject: ")
        teacher = Teacher(name, teacher_id, subject)
        school.add_teacher(teacher)
        print("Teacher added.")
    
    elif choice == '3':
        course_id = input("Course ID: ")
        name = input("Course Name: ")
        course = Course(course_id, name)
        school.add_course(course)
        print("Course added.")
    
    elif choice == '4':
        teacher_id = input("Teacher ID: ")
        course_id = input("Course ID: ")
        teacher = next((t for t in school.teachers if t.teacher_id == teacher_id), None)
        course = next((c for c in school.courses if c.course_id == course_id), None)
        if teacher and course:
            school.assign_teacher_to_course(teacher, course)
            print("Teacher assigned to course.")
        else:
            print("Teacher or course not found.")
    
    elif choice == '5':
        student_id = input("Student ID: ")
        course_id = input("Course ID: ")
        student = next((s for s in school.students if s.student_id == student_id), None)
        course = next((c for c in school.courses if c.course_id == course_id), None)
        if student and course:
            school.enroll_student_in_course(student, course)
            print("Student enrolled in course.")
        else:
            print("Student or course not found.")
    
    elif choice == '6':
        print(school)
        for student in school.students:
            print(student)
        for teacher in school.teachers:
            print(teacher)
        for course in school.courses:
            print(course)
    
    elif choice == '7':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please try again.")
