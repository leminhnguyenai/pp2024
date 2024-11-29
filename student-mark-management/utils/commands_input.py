def display_commands():
    print("-- Commands list --\n")
    print("     i students: Add students to the class")
    print("     i courses: Add courses")
    print("     s courses: Select course to modify")
    print("     ls courses: Show all courses")
    print("     ls students: Show all students")
    print("     ls marks: Show students' marks for given course")


commandList = {"h": display_commands}


def isValidCommand(userInput):
    return commandList.get(userInput)


def listen_to_input():
    userInput = ""
    while True:
        userInput = input("")

        if userInput == "quit":
            print("Bye")
            break

        if not isValidCommand(userInput):
            print("Invalid command")
            continue

        # WARNING: This is for the convinence of testing only, change this later
        commandList[userInput]()
