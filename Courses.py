class Course:
    def __init__(self, courseCode, title, maxCapacity):
        self.courseCode = courseCode
        self.title = title
        self.maxCapacity = maxCapacity
        self.currentEnrollment = 0
        self.students = []

    def enrollStudent(self, student_name):
        if self.currentEnrollment < self.maxCapacity:
            self.students.append(student_name)
            self.currentEnrollment += 1

    def getCurrentEnrollment(self):
        return self.currentEnrollment

    def isCourseFull(self):
        return self.currentEnrollment == self.maxCapacity
    
    def to_string(self):
        return f"({self.courseCode}) {self.title}: \n Available Slots: {self.maxCapacity - self.currentEnrollment} \n Students: {','.join(self.students)}\n"
    
    def from_string(course_string):
        courseData = course_string.strip().split(',')
        courseCode, title, maxCapacity, currentEnrollment, *students = courseData
        course = Course(courseCode, title, int(maxCapacity))
        course.currentEnrollment = int(currentEnrollment)
        course.students = students if students[0] != '' else []
        return course