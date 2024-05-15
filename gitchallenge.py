# Initialize the courses List with 5 courses
courses = [
    ['P101', 'Introduction to Programming with Python', 'Ngeno Victor', []],
    ['W201', 'Web Design Fundamentals', 'Helu Bore', []],
    ['DS110', 'Data Structures & Algorithms Basics', 'Ngeno Victor', []],
    ['G201', 'Git & GitHub Basics', 'Ngeno Victor', []],
    ['D101', 'Database Fundamentals', 'Brigit Chelangat', []]
]


# Function to create a new course :Brigit
def create_course(course_code, course_name, instructor):
    courses.append([course_code, course_name, instructor])

# Function to display all courses :Brigit
def display_courses(coursesList):
    print("Available Courses: ")
    for course in coursesList:
        course_code, course_name, instructor = course[0], course[1], course[2]
        print(f"Course Code: {course_code}, Course Name:  {course_name}, Instructor: {instructor}")

# Function to search for courses :Brigit
def search_courses(instructor):
    matching_courses = []
    for course in courses:
        if course[2] == instructor:
            matching_courses.append(course)
    return matching_courses

# Function to enroll a student in a course :Roy
def enroll_student(course_code, student_name):
    found = False
    for course in courses:
        if course[0] == course_code:
            found = True
            course[3].append(student_name)
            print(f"You have successfully enrolled {student_name} in the course {course[1]}.")
    if not found:
        print(f"There is no course with the code {course_code}")
        
    




# Function to display detailed information about a course :Roy
def display_course_info(course_code):
    requested_course = False
    for course in courses:
        if course[0] == course_code:
            requested_course = True
            print("Course code:", course[0])
            print("Course title:", course[1])
            print("Instructor:", course[2])
            print("Students enrolled:", course[3])
            
    if not requested_course:
        print(f"There is no course with the code {course_code}")

# Function to drop a student from a course :Roy
def drop_student(course_code, student_name):
    course_code_found = False
    for course in courses:
        if course[0] == course_code:
            course_code_found = True
            if student_name in course[3]:
                course[3].remove(student_name)
                print(f"{student_name} has been dropped from the course {course[1]}.")
            else:
                print(f"{student_name} is not enrolled in the course {course[1]}.")
    if not course_code_found:
        print(f"There is no course with the code {course_code}")



def main():
    while True:
        print("\nMenu:")
        print("1: Create Course")
        print("2: Display Courses")
        print("3: Search Courses")
        print("4: Enroll Student")
        print("5: Display Course Information")
        print("6: Drop Student")
        print("0: Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            course_code = input("Enter the course code: ")
            course_name = input("Enter the course name: ")
            instructor = input("Enter the name of the instructor: ")
            create_course(course_code, course_name, instructor) #Pass required params
        elif choice == "2":
            display_courses(courses)  #Pass required params
        elif choice == "3":
            instructor_name = input("Enter the name of the instructor to search for: ")
            matching_courses = search_courses(instructor_name)
            if matching_courses:
               print(f"Courses offered by {instructor_name}:")
               for course in matching_courses:
                   print(f"Course Code: {course[0]}, Course Name: {course[1]}")
            else:
                print(f"No courses found for instructor {instructor_name}.")
        elif choice == "4":
            course_code = input("Enter course code: ")
            student_name = input("Enter student name: ")
            enroll_student(course_code, student_name)  #Pass required params
        elif choice == "5":
            course_code = input("Enter course code: ")
            display_course_info(course_code) #Pass required params
        elif choice == "6":
            course_code = input("Enter course code: ")
            student_name = input("Enter student name: ")
            drop_student(course_code, student_name) #Pass required params
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
