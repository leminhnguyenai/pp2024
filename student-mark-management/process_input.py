from utils.commands_input import display_commands

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
