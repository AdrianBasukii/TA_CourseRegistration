class Student:
    def __init__(self, studentID, name):
        self.studentID = studentID
        self.name = name
        self.coursesEnrolled = []

    def enrollInCourse(self, course):
        if course.isCourseFull():
            print(f"Sorry, {course.title} is already full. Cannot enroll {self.name}.")
        elif course.courseCode in self.coursesEnrolled:
            print(f"{self.name} is already enrolled in {course.title}.")
        else:
            self.coursesEnrolled.append(course.courseCode)
            course.enrollStudent(self.name)
            print(f"{self.name} has been enrolled in {course.title}.")

    def enrollInCourseNOPRINT(self, course):
        if course.isCourseFull():
            pass
        elif course.courseCode in self.coursesEnrolled:
            pass
        else:
            self.coursesEnrolled.append(course.courseCode)
            course.enrollStudent(self.name)

    def get_enrolled_courses(self):
        return self.coursesEnrolled
    
    def to_string(self):
        return f"{self.studentID} | {self.name} | {','.join(self.coursesEnrolled)}\n"
    
    def from_string(student_string):
        studentData = student_string.strip().split(',')
        studentID, name, *coursesEnrolled = studentData
        student = Student(studentID, name)
        student.coursesEnrolled = coursesEnrolled if coursesEnrolled[0] != '' else []
        return student
