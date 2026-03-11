class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def to_string(self):
        return f"{self.student_id},{self.name},{self.marks}"