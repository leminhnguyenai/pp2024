def input_helper(firstMsg, retryMsg, dataType):
    try:
        userInput = dataType(input(firstMsg))
        return userInput
    except ValueError:
        return input_helper(retryMsg, retryMsg, dataType)
