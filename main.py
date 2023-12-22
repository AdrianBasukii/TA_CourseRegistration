from Courses import Course
from Students import Student

def write_courses_to_file(courses, filename):
    with open(filename, 'w') as file:
        for course in courses:
            file.write(course.to_string())

def read_courses_from_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line)

def write_students_to_file(students, filename):
    with open(filename, 'w') as file:
        for student in students:
            file.write(student.to_string())

def read_students_from_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line)


def main():
    MATH101 = Course("MATH101", "Scientific Computing", 20)
    MATH201 = Course("MATH201", "Discrete Mathematics", 20)
    COMP301 = Course("COMP301", "Program Design Methods", 20)
    COMP101 = Course("COMP101", "Human Computer Interaction", 20)
    COMP202 = Course("COMP202", "Algorithm and Programming", 20)
    CB101 = Course("CB101", "Character Building: Pancasila", 20)

    # Display list of available courses
    print("List of Available Courses:")
    for i, course in enumerate([MATH101, MATH201, COMP301, COMP101, COMP202, CB101], start=1):
        print(f"{i}. {course.title} | {course.courseCode}")

    print("------------------------------------------------------------------------------")
    
    courses = [MATH101, MATH201, COMP301, COMP101, COMP202, CB101]
    coursesStr = ["MATH101", "MATH201", "COMP301", "COMP101", "COMP202", "CB101"]

    studentsList = []

    with open('students.txt', 'r') as file:
        for line in file:
            storedData = line.split(" | ")
            storedData[-1] = storedData[-1].strip()
            storedStudent = Student(storedData[0], storedData[1])
            studentsList.append(storedStudent)

            for x in storedData[-1].split(','):
                courseIndex = coursesStr.index(x)
                storedStudent.enrollInCourseNOPRINT(courses[courseIndex])
            

    while True:
        print("Actions:")
        print("1. Register New Student")
        print("2. View Students")
        print("3. View Course Info")
        print("4. Quit")

        userInput = input("Option Number: ")

        if userInput == "1":
            print("------------------------------------------------------------------------------")
            print("")
            newStudent = input("Enter Name: ").title()
            newStudentID = input("Enter ID: ").upper()

            if len(studentsList) != 0:
                for eachStudent in studentsList:
                    if eachStudent.name == newStudent and eachStudent.studentID == newStudentID:
                        studentCourse = int(input("Enter Course Number (1-6): "))
                        eachStudent.enrollInCourse(courses[studentCourse-1])
                        break

                    else: 
                        studentData = Student(newStudentID, newStudent)
                        studentCourse = int(input("Enter Course Number (1-6): "))
                        studentData.enrollInCourse(courses[studentCourse-1])
                        studentsList.append(studentData)
                        break

            else: 
                studentData = Student(newStudentID, newStudent)
                studentCourse = int(input("Enter Course Number (1-6): "))
                studentData.enrollInCourse(courses[studentCourse-1])
                studentsList.append(studentData)

            write_courses_to_file(courses, 'courses.txt')
            print("")
            print("------------------------------------------------------------------------------")

        elif userInput == "2":
            print("------------------------------------------------------------------------------")
            print("")
            print("ID | Name | Course")
            read_students_from_file('students.txt')
            print("")
            print("------------------------------------------------------------------------------")    

        elif userInput == "3":
            print("------------------------------------------------------------------------------")
            print("")
            read_courses_from_file('courses.txt')
            print("")
            print("------------------------------------------------------------------------------")    

        elif userInput == "4":
            print("")
            print("See You Next Time")
            break
  
        write_students_to_file(studentsList, 'students.txt')
main()
