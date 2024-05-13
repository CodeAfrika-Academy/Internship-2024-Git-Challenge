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
    pass

# Function to display all courses :Brigit
def display_courses():
    print("All Courses")

# Function to search for courses :Brigit
def search_courses(instructor):
    pass

# Function to enroll a student in a course :Roy
def enroll_student(course_code, student_name):
    pass

# Function to display detailed information about a course :Roy
def display_course_info(course_code):
    pass

# Function to drop a student from a course :Roy
def drop_student(course_code, student_name):
    pass


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
            create_course() #Pass required params
        elif choice == "2":
            display_courses()  #Pass required params
        elif choice == "3":
            instructor = input("Enter keyword to search: ")
            search_courses(instructor)  #Pass required params
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
