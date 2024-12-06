import pickle

class CourseGrades:
    def __init__(self):
        self.course_name = ""
        self.stu_ID = []
        self.stu_grade = []

    def get_details(self):
        self.course_name = input("Enter course name: ")
        print("Enter details for at least 5 students:")
        for _ in range(5):
            stu_id = input("Enter student ID: ")
            stu_grade = float(input("Enter student grade (0-100): "))
            while stu_grade < 0 or stu_grade > 100:
                print("Invalid grade. Please enter a grade between 0 and 100.")
                stu_grade = float(input("Enter student grade (0-100): "))
            self.stu_ID.append(stu_id)
            self.stu_grade.append(stu_grade)

    def display(self):
        print("\nCourse Name:", self.course_name)
        print("Student IDs and Grades:")
        for id_, grade in zip(self.stu_ID, self.stu_grade):
            print(f"  ID: {id_}, Grade: {grade:.2f}")


def main():
    courses = []
    for i in range(4):
        print(f"\nEntering details for Course {i + 1}")
        course = CourseGrades()
        course.get_details()
        courses.append(course)

    with open('grades_info.dat', 'ab') as file:
        for course in courses:
            pickle.dump(course, file)
    print("\nAll courses have been saved to 'grades_info.dat'.")

    print("\nReading objects from the file...")
    try:
        with open('grades_info.dat', 'rb') as file:
            for i in range(4):
                course = pickle.load(file)
                course.display()
    except EOFError:
        print("Unexpected end of file.")
    except Exception as e:
        print("Error reading the file:", e)


if __name__ == "__main__":
    main()
