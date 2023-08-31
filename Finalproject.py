import uuid
name = input("Enter your name ")
submission = input("Enter your submission")

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()  # Generate a unique course ID
        self.course_name = course_name
        self.course_mark = course_mark

class Student:
    total_students = 0  # Static variable to keep track of total student count

    def __init__(self, student_name, student_age, student_number):
        self.student_id = uuid.uuid4()  # Generate a unique student ID
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []  # List to store enrolled courses

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list) if len(self.courses_list) > 0 else 0


students_list = []

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to Student with Mark\n"
                              "6.Exit\n"))
    except ValueError:
        print("Invalid input. Please enter a valid option.")
        continue

    if selection == 1:
        student_number = input("Enter Student Number: ")
        student_name = input("Enter Student Name: ")
        while True:
            try:
                student_age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Invalid Value")
        new_student = Student(student_name, student_age, student_number)
        students_list.append(new_student)
        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                students_list.remove(student)
                print("Student Deleted Successfully")
                break
        else:
            print("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                print("Student Details:")
                print(student.get_student_details())
                break
        else:
            print("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                average = student.get_student_average()
                print(f"Student Average: {average}")
                break
        else:
            print("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                course_mark = float(input("Enter Course Mark: "))
                new_course = Course(course_name, course_mark)
                student.enroll_course(new_course)
                print("Course Added to Student Successfully")
                break
        else:
            print("Student Not Exist")

    else:
        print("Exiting the program.")
        break
