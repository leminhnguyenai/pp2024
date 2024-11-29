from utils import commands_input

commandList = {"i students": commands_input.insert_students}


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
            commands_input.display_commands()
            continue

        if not isValidCommand(userInput):
            print("Invalid command")
            continue

        commandList[userInput]()
