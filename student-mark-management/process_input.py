commandList = {
    # "i students": commands_input.insert_students,
    # "i courses": commands_input.input_courses,
}


def display_commands():
    print("-- Commands list --\n")
    print("     i students: Add students to the class")
    print("     i courses: Add courses")
    print("     s courses: Select course to modify")
    print("     ls courses: Show all courses")
    print("     ls students: Show all students")
    print("     ls marks: Show students' marks for given course")


def isValidCommand(userInput):
    return commandList.get(userInput)


def listen_to_input():
    userInput = ""
    while True:
        userInput = input("")

        if userInput == "quit":
            print("Bye")
            break

        if userInput == "h":
            display_commands()
            continue

        if not isValidCommand(userInput):
            print("Invalid command")
            continue
