from datetime import datetime

from project import (
    calculate_average,
    sort_key,
    sort_planner,
    save_data,
    load_data,
    Course,
    Assignment,
    Exam
)


def test_calculate_average():
    courses = [
        Course("Math", 101, 3, "Ali"),
        Course("Python", 102, 2, "Ahmad")
    ]

    grades = {
        "math": 90,
        "python": 80
    }

    assert calculate_average(grades, courses) == "📊 Average: 86.00"
    assert calculate_average({}, []) == "❌ No grades found."

    courses = [Course("Math", 101, 3, "Ali")]
    assert calculate_average({"math": 95}, courses) == "📊 Average: 95.00"


def test_sort_key():
    assignment = Assignment(
        "Homework", "Math", "01/01/2026", "High", "Pending"
    )

    item = (
        "overdue",
        assignment,
        datetime.strptime(assignment.date, "%d/%m/%Y")
    )

    result = sort_key(item)

    assert result[0] == 0
    assert result[1] == item[2]
    assert result[2] == 1


def test_sort_planner():
    assignments = [
        Assignment("Homework", "Math", "01/01/2020", "High", "Pending")
    ]

    exams = [
        Exam("Python", "Midterm", "01/01/2030", "Hard")
    ]

    planner = sort_planner(assignments, exams)

    assert len(planner) == 2
    assert planner[0][0] == "overdue"
    assert any(item[0] == "exam" for item in planner)


def test_save_data():
    courses = [Course("Math", 101, 3, "Ali")]
    assignments = [
        Assignment("Homework", "Math", "01/01/2030", "High", "Pending")
    ]
    exams = [
        Exam("Math", "Midterm", "02/01/2030", "Hard")
    ]
    grades = {"math": 90}

    save_data(courses, assignments, exams, grades)

    loaded_courses, loaded_assignments, loaded_exams, loaded_grades = load_data()

    assert loaded_courses[0].name == "math"
    assert loaded_assignments[0].name == "homework"
    assert loaded_grades["math"] == 90


def test_load_data():
    courses = [Course("Math", 101, 3, "Ali")]
    assignments = [
        Assignment("Homework", "Math", "01/01/2030", "High", "Pending")
    ]
    exams = [
        Exam("Math", "Midterm", "02/01/2030", "Hard")
    ]
    grades = {"math": 90}

    save_data(courses, assignments, exams, grades)

    loaded_courses, loaded_assignments, loaded_exams, loaded_grades = load_data()

    assert isinstance(loaded_courses, list)
    assert isinstance(loaded_assignments, list)
    assert isinstance(loaded_exams, list)
    assert isinstance(loaded_grades, dict)
