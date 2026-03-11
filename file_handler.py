def save_student(student):
    with open("data.txt", "a") as file:
        file.write(student.to_string() + "\n")


def read_students():
    students = []

    with open("data.txt", "r") as file:
        for line in file:
            students.append(line.strip())

    return students