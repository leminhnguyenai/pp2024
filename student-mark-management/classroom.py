import student


class Classroom:
    def __init__(self) -> None:
        self.__students = []

    def get_students(self):
        return self.__students

    def add_student(self, students_no):
        new_student = student.Student()

        new_student.set_id(students_no)
        new_student.set_name(students_no)
        new_student.set_dob(students_no)

        self.__students.append(new_student)
