from flask import Flask, render_template, request, redirect
from database.db import (
    create_table,
    insert_student,
    get_students,
    search_student,
    delete_student,
    update_student
)

app = Flask(__name__)

create_table()


@app.route("/")
def home():
    students = get_students()
    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def add_student():

    student_id = request.form["id"]
    name = request.form["name"]
    marks = request.form["marks"]

    insert_student(student_id, name, marks)

    return redirect("/")


@app.route("/delete/<student_id>")
def delete(student_id):

    delete_student(student_id)

    return redirect("/")


@app.route("/update", methods=["POST"])
def update():

    student_id = request.form["id"]
    marks = request.form["marks"]

    update_student(student_id, marks)

    return redirect("/")


@app.route("/search", methods=["POST"])
def search():

    student_id = request.form["id"]

    student = search_student(student_id)

    return render_template("search.html", student=student)


if __name__ == "__main__":
    app.run(debug=True)