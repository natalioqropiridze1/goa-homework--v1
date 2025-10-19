class Student:
    _student_count = 0

    def __init__(self, grade, student_id):
        self._grade = grade
        self.__id = student_id
        Student._student_count += 1

    @classmethod
    def get_student_count(cls):
        return cls._student_count