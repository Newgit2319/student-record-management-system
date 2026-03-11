import sqlite3

def create_connection():
    conn = sqlite3.connect("students.db")
    return conn
def create_table():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id TEXT PRIMARY KEY,
        name TEXT,
        marks INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP           
    )
    """)

    conn.commit()

    conn.close()

def insert_student(student_id, name, marks):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (id, name, marks) VALUES (?, ?, ?)",
        (student_id, name, marks)
    )

    conn.commit()

    conn.close()
def get_students():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return students
def search_student(student_id):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    conn.close()

    return student
def delete_student(student_id):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()
def update_student(student_id, new_marks):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET marks = ? WHERE id = ?",
        (new_marks, student_id)
    )

    conn.commit()
    conn.close()