# Student Command Center

#### Video Demo: https://youtu.be/tRFVZnr5N-0

#### Description:

Student Command Center is a Python command-line application designed to help students manage their academic information in one place. The application provides a simple menu-based interface for managing courses, assignments, exams, and grades. It also includes a Smart Planner and a Dashboard to give the student a clearer overview of their academic workload.

The Courses section allows the user to add, view, edit, delete, and search for courses. Each course contains a name, course code, credit hours, and instructor. The application validates the entered information and prevents duplicate course names and course codes.

The Assignments section allows the user to manage assignments associated with their courses. Each assignment has a name, course, due date, priority, and status. The user can add, view, edit, and delete assignments, as well as mark them as completed. The Sort / Filter option organizes pending assignments according to their due dates and priorities, helping the student identify tasks that need attention.

The Exams section provides similar functionality for exams. The user can add, view, edit, and delete exams and can also view upcoming exams. Each exam has a course, name, date, and difficulty level. The application validates the entered information and makes sure that the selected course exists.

The Grades & Average section allows the user to store grades for courses and calculate a weighted average based on course credit hours. The Dashboard provides a quick summary of the student's academic information, including the number of courses, total credits, assignments, completed and pending assignments, exams, grades, and average.

The Smart Planner combines assignments and exams into an organized list. Overdue assignments are identified separately, while upcoming assignments and exams are sorted by date. This provides the student with a single place to see upcoming academic tasks and overdue work.

The project uses object-oriented programming through three main classes: `Course`, `Assignment`, and `Exam`. I chose to use classes because each type of academic information has its own attributes and validation rules. Properties and setters are also used to validate data when objects are created or modified.

The application uses JSON for data persistence. The data is stored in `student_data.json` and is loaded when the application starts. The data is saved when the user exits the application. JSON was chosen instead of a database because the project is a command-line student management application and does not require the additional complexity of a database.

The main files in the project are `project.py`, `test_project.py`, `README.md`, and `requirements.txt`. `project.py` contains the classes, main menu, application logic, planner, dashboard, and data persistence functions. `test_project.py` contains pytest tests for the main custom functions. `README.md` documents the project, its functionality, and its design choices. `requirements.txt` lists external dependencies required by the project. This project currently uses Python's standard library, so no external packages are required.

Overall, Student Command Center was created to demonstrate Python programming, object-oriented programming, input validation, functions, JSON file handling, data persistence, and automated testing while solving a practical problem for students.
