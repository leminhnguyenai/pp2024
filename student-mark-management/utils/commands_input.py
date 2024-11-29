students = []
courses = []


def display_commands():
    print("-- Commands list --\n")
    print("     i students: Add students to the class")
    print("     i courses: Add courses")
    print("     s courses: Select course to modify")
    print("     ls courses: Show all courses")
    print("     ls students: Show all students")
    print("     ls marks: Show students' marks for given course")


def input_helper(firstMsg, retryMsg, dataType):
    try:
        userInput = dataType(input(firstMsg))
        return userInput
    except ValueError:
        return input_helper(retryMsg, retryMsg, dataType)


def insert_students():
    studentAmount = input_helper(
        "Please enter the number of students: ", "Not a number, re enter again: ", int
    )
    studentAmount = int(studentAmount)

    for i in range(studentAmount):
        studentId = input_helper(
            f"Please enter the student number {i+1} id: ",
            "This is not a valid id, re enter again: ",
            int,
        )
        studentId = int(studentId)
        studentName = input_helper(
            f"Please enter the student number {i+1} name: ",
            "This is not a valid name, try again ",
            str,
        )
        studentDoB = input_helper(
            f"Please enter the student number {i+1} date of birth: ",
            "This is not a valid date of birth, try again",
            str,
        )

        students.append({"id": studentId, "name": studentName, "birthday": studentDoB})


# TODO: Add function to input courses
def input_courses():
    coursesAmount = input_helper(
        "Please enter the number of courses ", "That is not a number, try again", int
    )
    coursesAmount = int(coursesAmount)

    for i in range(coursesAmount):
        courseId = input_helper(
            f"Please enter the course number {i+1} id: ",
            "This is not a valid id, re enter again: ",
            int,
        )
        courseId = int(courseId)
        courseName = input_helper(
            f"Please enter the course number {i+1} name: ",
            "This is not a valid name, try again ",
            str,
        )
        courses.append({"id": courseId, "name": courseName})
