import utils


class Student:
    def __init__(
        self,
    ) -> None:
        self.__id = -1
        self.__name = ""
        self.__dob = ""
        self.__marks = {}

    def get_id(self):
        return self.__id

    def set_id(self, number):
        studentId = utils.input_helper(
            f"Please enter the student number {number+1} id: ",
            "This is not a valid id, re enter again: ",
            int,
        )

        self.__id = studentId

    def get_name(self):
        return self.__name

    def set_name(self, number):
        studentName = utils.input_helper(
            f"Please enter the student number {number+1} name: ",
            "This is not a valid name, re enter again: ",
            str,
        )

        self.__name = studentName

    def get_dob(self):
        return self.__dob

    def set_dob(self, number):
        studentDob = utils.input_helper(
            f"Please enter the student number {number+1} dob: ",
            "This is not a valid dob, re enter again: ",
            str,
        )

        self.__dob = studentDob

    def get_marks(self):
        return self.__marks

    def set_mark(self, courseName, mark):
        mark = utils.input_helper(
            f"Please enter student's mark for {courseName}",
            "That is not a valid mark, please enter again",
            int,
        )

        self.__marks[courseName] = mark
