from datetime import datetime
import json

class Course:
    def __init__(self,name,code,credits,instructor):
        self.name=name
        self.code=code
        self.credits=credits
        self.instructor=instructor

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")

        if not value.strip():
            raise ValueError("Name cannot be empty")

        self._name = value.lower().strip()


    @property
    def code(self):
        return self._code
    @code.setter
    def code(self,value):
        if not isinstance(value, int):
            raise TypeError("Code must be a integer")

        if value <=0 :
            raise ValueError("Code must be greater than 0")

        self._code = value


    @property
    def credits(self):
        return self._credits
    @credits.setter
    def credits(self,value):
        if not isinstance(value, int):
            raise TypeError("Credits must be a integer")

        if value not in [1, 2, 3]:
            raise ValueError("Credits must be 1, 2, or 3")

        self._credits = value


    @property
    def instructor(self):
        return self._instructor
    @instructor.setter
    def instructor(self,value):
        if not isinstance(value, str):
            raise TypeError("Instructor must be a string")

        if not value.strip():
            raise ValueError("Instructor cannot be empty")

        self._instructor = value.lower().strip()

class Assignment:
    def __init__(self,name,course,date,priority,status):
        self.name=name
        self.course=course
        self.date=date
        self.priority=priority
        self.status=status

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")

        if not value.strip():
            raise ValueError("Name cannot be empty")

        self._name = value.lower().strip()

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        if not isinstance(value, str):
            raise TypeError("Course must be a string")

        if not value.strip():
            raise ValueError("Course cannot be empty")

        self._course = value.lower().strip()

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("Date must be a string")

        if not value.strip():
            raise ValueError("Date cannot be empty")

        try:
            datetime.strptime(value.strip(), "%d/%m/%Y")
        except ValueError:
            raise ValueError("Invalid date! Use DD/MM/YYYY")

        self._date = value.strip()

    @property
    def priority(self):
        return self._priority
    @priority.setter
    def priority(self,value):
        if not isinstance(value, str):
            raise TypeError("Priority must be a string")

        if not value.strip():
            raise ValueError("Priority cannot be empty")

        if value.lower().strip() not in ["low", "medium", "high"]:
            raise ValueError("Priority must be low, medium, or high")

        self._priority = value.lower().strip()

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if not isinstance(value, str):
            raise TypeError("Status must be a string")

        if not value.strip():
            raise ValueError("Status cannot be empty")

        if value.lower().strip() not in ["pending", "completed"]:
            raise ValueError("Status must be pending or completed")

        self._status = value.lower().strip()

class Exam:
    def __init__(self, course, name, date, difficulty):
        self.course = course
        self.name = name
        self.date = date
        self.difficulty = difficulty

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        if not isinstance(value, str):
            raise TypeError("Course must be a string")

        if not value.strip():
            raise ValueError("Course cannot be empty")

        self._course = value.strip().lower()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")

        if not value.strip():
            raise ValueError("Name cannot be empty")

        self._name = value.strip().lower()

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("Date must be a string")

        if not value.strip():
            raise ValueError("Date cannot be empty")

        try:
            datetime.strptime(value.strip(), "%d/%m/%Y")
        except ValueError:
            raise ValueError("Invalid date! Use DD/MM/YYYY")

        self._date = value.strip()

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        if not isinstance(value, str):
            raise TypeError("Difficulty must be a string")

        if not value.strip():
            raise ValueError("Difficulty cannot be empty")

        if value.strip().lower() not in ["easy", "medium", "hard"]:
            raise ValueError("Difficulty must be easy, medium, or hard")

        self._difficulty = value.strip().lower()



def main():

    courses, assignments, exams, grades = load_data()

    option=-1

    while option!=0:

        print("""
🎓 STUDENT COMMAND CENTER
─────────────────────────
1. 📚  Courses
2. 📝  Assignments
3. 📅  Exams
4. 📊  Grades & AVERAGE
5. 🧠  Smart Planner
6. 📈  Dashboard
─────────────────────────
0. 🚪  Exit
""")
        try:
            option = int(input("❯ Select an option: "))
        except ValueError:
            print("❌ Please enter a number.")
            continue

        if option==1:

            print("""
📚 COURSES
─────────────────────────
[1] ➕ Add Course
[2] 📋 View Courses
[3] ✏️  Edit Course
[4] 🗑️  Delete Course
[5] 🔎 Search Course
[0] ↩️  Back
─────────────────────────
""")
            try:
                option1 = int(input("❯ Select an option: "))
            except ValueError:
                print("❌ Please enter a number.")
                continue

            if option1 == 1:
                print("""
📚 ADD COURSE
─────────────────────────
""")

                name1=input("❯ The name of the course: ").lower().strip()

                found1=0

                for course in courses:
                    if course.name == name1:
                        print("❌ Course already exists.")
                        found1=1
                        break

                if found1==1:
                    continue

                try:
                    code1=int(input("❯ The code of the course: "))
                except ValueError:
                    print("❌ Code must be a number.")
                    continue

                code_exists=0

                for course in courses:
                    if course.code == code1:
                        code_exists=1
                        break

                if code_exists==1:
                    print("❌ Course code already exists.")
                    continue

                try:
                    credits1=int(input("❯ The credits of the course: "))
                except ValueError:
                    print("❌ Credits must be a number.")
                    continue

                instructor1=input("❯ The instructor of the course: ").lower().strip()

                try:
                    course1=Course(
                        name1,
                        code1,
                        credits1,
                        instructor1
                    )

                except (ValueError, TypeError) as e:
                    print(f"❌ {e}")
                    continue

                courses.append(course1)

                print("✅ Course added successfully!")
            elif option1 == 2:
                print("""
📚 YOUR COURSES
─────────────────────────────────
""")
                if not courses:
                    print("📚 No courses found.")

                else:


                    for i, course in enumerate(courses):
                        print(f"""
{i+1}. 📚 {course.name}
🔢 Code: {course.code}
🎓 Credits: {course.credits}
👨‍🏫 Instructor: {course.instructor}
""")
            elif option1 == 3:
                print("""
✏️ EDIT COURSE
─────────────────────────
""")

                if not courses:
                    print("❌ No courses found.")

                else:
                    course_name=input(
                        "❯ Enter course name to edit: "
                    ).strip().lower()

                    found=False

                    for index1, course in enumerate(courses):

                        if course.name == course_name:
                            found=True

                            old_name=course.name

                            new_name=input(
                                "❯ Enter new course name: "
                            ).strip().lower()

                            duplicate=False

                            for i, other_course in enumerate(courses):

                                if i != index1 and other_course.name == new_name:
                                    duplicate=True
                                    break

                            if duplicate:
                                print("❌ Another course already has this name.")
                                break

                            try:
                                new_code=int(
                                    input("❯ Enter new course code: ")
                                )

                                code_exists=0

                                for i, other_course in enumerate(courses):

                                    if i != index1 and other_course.code == new_code:
                                        code_exists=1
                                        break

                                if code_exists==1:
                                    print("❌ Another course already has this code.")
                                    break

                                new_credits=int(
                                    input("❯ Enter new course credits: ")
                                )

                                new_instructor=input(
                                    "❯ Enter new instructor: "
                                )

                                new_course=Course(
                                    new_name,
                                    new_code,
                                    new_credits,
                                    new_instructor
                                )

                                for assignment in assignments:

                                    if assignment.course == old_name:
                                        assignment.course=new_name

                                for exam in exams:

                                    if exam.course == old_name:
                                        exam.course=new_name

                                if old_name in grades:
                                    grades[new_name]=grades[old_name]
                                    del grades[old_name]

                                courses[index1]=new_course

                                print("✅ Course updated successfully.")

                            except (ValueError, TypeError) as e:
                                print(f"❌ Error: {e}")

                            break

                    if not found:
                        print("❌ Course not found.")

            elif option1 == 4:
                print("""
🗑️ DELETE COURSE
─────────────────────────
""")
                if not courses:
                    print("❌ No courses found.")

                else:



                    course_name = input("Enter course name to delete: ").strip().lower()

                    found = False

                    for course in courses:

                        if course.name == course_name:

                            found = True

                            print("⚠️ This will delete the course and all related assignments, exams, and grade.")

                            confirmation = input("Are you sure? (y/n): ").strip().lower()

                            if confirmation != "y":
                                print("❌ Deletion cancelled.")
                                break

                            for assignment in assignments[:]:

                                if assignment.course == course_name:
                                    assignments.remove(assignment)

                            for exam in exams[:]:

                                if exam.course == course_name:
                                    exams.remove(exam)

                            if course_name in grades:
                                del grades[course_name]

                            courses.remove(course)

                            print("✅ Course and all related data deleted successfully.")

                            break

                    if not found:
                        print("❌ Course not found.")

            elif option1 == 5:
                print("""
🔎 SEARCH COURSE
─────────────────────────
""")
                if not courses:
                    print("📚 No courses found.")

                else:

                    name = input("❯ Enter course name to search: ").strip().lower()

                    for course in courses:
                        if course.name.lower() == name:
                            print(f"""
🔎 COURSE FOUND
─────────────────────────────

📚 Name:       {course.name}
🔢 Code:       {course.code}
🎓 Credits:    {course.credits}
👨‍🏫 Instructor: {course.instructor}
        """)
                            break
                    else:
                        print("❌ Course not found.")

            elif option1 == 0:
                continue

            else:
                print("❌ Invalid option. Please choose a valid option.")



        elif option == 2:

            print("""
📝 ASSIGNMENTS
─────────────────────────
[1] ➕ Add Assignment
[2] 📋 View Assignments
[3] ✏️  Edit Assignment
[4] 🗑️  Delete Assignment
[5] ✅ Mark as Completed
[6] 🔎 Sort / Filter
[0] ↩️  Back
─────────────────────────
""")
            try:
                option2 = int(input("❯ Select an option: "))
            except ValueError:
                print("❌ Please enter a number.")
                continue

            if option2==1:
                print("""
📝 ADD ASSIGNMENT
─────────────────────────
""")
                found2=0

                course2=input("❯ The course of the assignment:").lower().strip()

                found_course=0
                for course in courses:
                    if course.name == course2:
                        found_course=1
                        break

                if found_course==0:
                    print("❌ Course not found.")
                    continue

                name2=input("❯ The name of the assignment:").lower().strip()

                for assignment in assignments:
                    if assignment.name == name2 and assignment.course == course2:
                        print("❌ Assignment already exists for this course.")
                        found2=1
                        break

                if found2==1:
                    continue

                date2=input("❯ The due date of the assignment:").strip()
                priority2=input("❯ The priority of the assignment:").lower().strip()
                status2=input("❯ The status of the assignment:").lower().strip()

                try:
                    assignment1=Assignment(name2,course2,date2,priority2,status2)
                except (ValueError, TypeError) as e:
                    print(f"❌ {e}")
                    continue

                assignments.append(assignment1)
                print("✅ Assignment added successfully!")

            elif option2 == 2:
                print("""
📋 YOUR ASSIGNMENTS
─────────────────────────
""")
                if not assignments:
                    print("📝 No assignments found.")

                else:


                    for i, assignment in enumerate(assignments):
                        print(f"""
{i+1}. 📝 {assignment.name}
📚 Course: {assignment.course}
📅 Date: {assignment.date}
🎯 Priority: {assignment.priority}
📌 Status: {assignment.status}
""")

            elif option2 == 3:
                print("""
✏️ EDIT ASSIGNMENT
─────────────────────────
""")

                if not assignments:
                    print("📝 No assignments found.")

                else:
                    course_name=input("❯ Enter course name: ").strip().lower()
                    assignment_name=input("❯ Enter assignment name: ").strip().lower()

                    found=False

                    for index1, assignment in enumerate(assignments):

                        if assignment.course == course_name and assignment.name == assignment_name:
                            found=True

                            try:
                                new_name=input("❯ Enter new assignment name: ").strip().lower()
                                new_course=input("❯ Enter new course name: ").strip().lower()

                                course_exists=False

                                for course in courses:
                                    if course.name == new_course:
                                        course_exists=True
                                        break

                                if not course_exists:
                                    print("❌ Course not found.")
                                    break

                                duplicate=False

                                for i, other_assignment in enumerate(assignments):

                                    if i != index1:
                                        if other_assignment.name == new_name and other_assignment.course == new_course:
                                            duplicate=True
                                            break

                                if duplicate:
                                    print("❌ Assignment already exists for this course.")
                                    break

                                new_date=input("❯ Enter new date (DD/MM/YYYY): ").strip()

                                new_priority=input(
                                    "❯ Enter new priority (low/medium/high): "
                                ).strip().lower()

                                new_status=input(
                                    "❯ Enter new status (pending/completed): "
                                ).strip().lower()

                                new_assignment=Assignment(
                                    new_name,
                                    new_course,
                                    new_date,
                                    new_priority,
                                    new_status
                                )

                                assignments[index1]=new_assignment

                                print("✅ Assignment updated successfully.")

                            except (ValueError, TypeError) as e:
                                print(f"❌ Error: {e}")

                            break

                    if not found:
                        print("❌ Assignment not found.")

            elif option2 == 4:
                print("""
🗑️ DELETE ASSIGNMENT
─────────────────────────
""")

                if not assignments:
                    print("📝 No assignments found.")

                else:
                    course_name=input("❯ Enter course name: ").strip().lower()
                    assignment_name=input("❯ Enter assignment name: ").strip().lower()

                    found=False

                    for assignment in assignments:

                        if assignment.course == course_name and assignment.name == assignment_name:
                            found=True

                            assignments.remove(assignment)

                            print("✅ Assignment deleted successfully.")
                            break

                    if not found:
                        print("❌ Assignment not found.")

            elif option2 == 5:
                print("""
✅ MARK AS COMPLETED
─────────────────────────
""")

                if not assignments:
                    print("📝 No assignments found.")

                else:
                    course_name=input("❯ Enter course name: ").strip().lower()
                    assignment_name=input("❯ Enter assignment name: ").strip().lower()

                    found=False

                    for assignment in assignments:

                        if assignment.course == course_name and assignment.name == assignment_name:
                            found=True

                            assignment.status="completed"

                            print("✅ Assignment marked as completed.")
                            break

                    if not found:
                        print("❌ Assignment not found.")
            elif option2 == 6:
                print("""
🔎 SORT / FILTER ASSIGNMENTS
─────────────────────────
""")
                if not assignments:
                    print("📝 No assignments found.")

                else:
                    pending_assignments = []

                    for assignment in assignments:
                        if assignment.status != "completed":
                            pending_assignments.append(assignment)

                    if not pending_assignments:
                        print("✅ No pending assignments found.")

                    else:
                        priority_order = {
                            "high": 1,
                            "medium": 2,
                            "low": 3
                        }

                        pending_assignments.sort(key=lambda assignment:
                                                (datetime.strptime(assignment.date, "%d/%m/%Y"),priority_order[assignment.priority])
                                                )

                        print("""
📋 PENDING ASSIGNMENTS
─────────────────────────
""")

                        for i, assignment in enumerate(pending_assignments):
                            print(f"""
{i+1}. 📝 {assignment.name}
📚 Course: {assignment.course}
📅 Date: {assignment.date}
🎯 Priority: {assignment.priority}
📌 Status: {assignment.status}
""")
            elif option2 == 0:
                continue
            else:
                            print("❌ Invalid option. Please choose a valid option.")


        elif option == 3:

            print("""
📅 EXAMS
─────────────────────────
[1] ➕ Add Exam
[2] 📋 View Exams
[3] ✏️  Edit Exam
[4] 🗑️  Delete Exam
[5] 📅 View Upcoming Exams
[0] ↩️  Back
─────────────────────────
""")
            try:
                option3 = int(input("❯ Select an option: "))
            except ValueError:
                print("❌ Please enter a number.")
                continue

            if option3==1:
                print("""
📅 ADD EXAM
─────────────────────────
""")
                course3=input("❯ The course of the exam:").lower().strip()
                found_course=0
                for course in courses:
                    if course.name == course3:
                        found_course=1
                        break

                if found_course==0:
                    print("❌ Course not found.")
                    continue

                name3=input("❯ The name of the exam:").lower().strip()
                found3=0

                for exam in exams:
                    if exam.name == name3 and exam.course == course3:
                        print("❌ Exam already exists for this course.")
                        found3=1
                        break

                if found3==1:
                    continue

                date3=input("❯ The date of the exam:").strip()
                difficulty3=input("❯ The difficulty of the exam:").lower().strip()

                try:
                    exam1=Exam(course3,name3,date3,difficulty3)
                except (ValueError, TypeError) as e:
                    print(f"❌ {e}")
                    continue

                exams.append(exam1)
                print("✅ Exam added successfully!")

            elif option3 == 2:
                print("""
📋 YOUR EXAMS
─────────────────────────
""")
                if not exams:
                    print("📅 No exams found.")

                else:


                    for i, exam in enumerate(exams):
                        print(f"""
{i+1}. 📅 {exam.name}
📚 Course: {exam.course}
📅 Date: {exam.date}
🎯 Difficulty: {exam.difficulty}
""")

            elif option3 == 3:
                print("""
✏️ EDIT EXAM
─────────────────────────
""")

                if not exams:
                    print("📅 No exams found.")

                else:
                    course_name=input("❯ Enter course name: ").strip().lower()
                    exam_name=input("❯ Enter exam name: ").strip().lower()

                    found=False

                    for index1, exam in enumerate(exams):

                        if exam.course == course_name and exam.name == exam_name:
                            found=True

                            try:
                                new_course=input("❯ Enter new course name: ").strip().lower()

                                course_exists=False

                                for course in courses:
                                    if course.name == new_course:
                                        course_exists=True
                                        break

                                if not course_exists:
                                    print("❌ Course not found.")
                                    break

                                new_name=input("❯ Enter new exam name: ").strip().lower()

                                duplicate=False

                                for i, other_exam in enumerate(exams):

                                    if i != index1:
                                        if other_exam.name == new_name and other_exam.course == new_course:
                                            duplicate=True
                                            break

                                if duplicate:
                                    print("❌ Exam already exists for this course.")
                                    break

                                new_date=input("❯ Enter new date (DD/MM/YYYY): ").strip()

                                new_difficulty=input(
                                    "❯ Enter new difficulty (easy/medium/hard): "
                                ).strip().lower()

                                new_exam=Exam(
                                    new_course,
                                    new_name,
                                    new_date,
                                    new_difficulty
                                )

                                exams[index1]=new_exam

                                print("✅ Exam updated successfully.")

                            except (ValueError, TypeError) as e:
                                print(f"❌ Error: {e}")

                            break

                    if not found:
                        print("❌ Exam not found.")

            elif option3 == 4:
                print("""
🗑️ DELETE EXAM
─────────────────────────
""")

                if not exams:
                    print("📅 No exams found.")

                else:
                    course_name=input("❯ Enter course name: ").strip().lower()
                    exam_name=input("❯ Enter exam name: ").strip().lower()

                    found=False

                    for exam in exams:

                        if exam.course == course_name and exam.name == exam_name:
                            found=True

                            exams.remove(exam)

                            print("✅ Exam deleted successfully.")
                            break

                    if not found:
                        print("❌ Exam not found.")

            elif option3 == 5:
                print("""
📅 UPCOMING EXAMS
─────────────────────────
""")
                if not exams:
                    print("📅 No exams found.")

                else:


                    upcoming_exams=[]

                    for exam in exams:
                        exam_date=datetime.strptime(exam.date,"%d/%m/%Y")
                        today=datetime.combine(datetime.now().date(), datetime.min.time())

                        if exam_date >= today:
                            upcoming_exams.append(exam)

                    if not upcoming_exams:
                        print("📅 No upcoming exams found.")

                    else:
                        upcoming_exams.sort(
                            key=lambda exam: datetime.strptime(
                                exam.date,"%d/%m/%Y"
                            )
                        )

                        for i, exam in enumerate(upcoming_exams):
                            print(f"""
{i+1}. 📅 {exam.name}
📚 Course: {exam.course}
📅 Date: {exam.date}
🎯 Difficulty: {exam.difficulty}
""")

            elif option3 == 0:
                continue
            else:
                print("❌ Invalid option. Please choose a valid option.")

        elif option == 4:

            print("""
📊 GRADES & AVERAGE
─────────────────────────
[1] ➕ Add Grade
[2] 📋 View Grades
[3] ✏️  Edit Grade
[4] 🗑️  Delete Grade
[5] 🧮 Calculate AVERAGE
[0] ↩️  Back
─────────────────────────
""")
            try:
                option4 = int(input("❯ Select an option: "))
            except ValueError:
                print("❌ Please enter a number.")
                continue

            if option4==1:
                print("""
                ➕ ADD GRADE
                ─────────────────────────
                """)
                if not courses:
                    print("📚 No courses found.")

                else:


                    course4=input("❯ The course of the grade:").lower().strip()

                    found_course=0
                    for course in courses:
                        if course.name == course4:
                            found_course=1
                            break

                    if found_course==0:
                        print("❌ Course not found.")
                        continue

                    if course4 in grades:
                        print("❌ Grade for this course already exists.")
                        continue

                    try:
                        grade4=int(input("❯ The grade: "))
                    except ValueError:
                        print("❌ Grade must be a number.")
                        continue

                    if grade4 < 0 or grade4 > 100:
                        print("❌ Grade must be between 0 and 100.")
                        continue

                    grades[course4]=grade4
                    print("✅ Grade added successfully!")

            elif option4 == 2:
                print("""
📋 YOUR GRADES
─────────────────────────
""")
                if not grades:
                    print("📊 No grades found.")

                else:


                    for course, grade in grades.items():
                        print(f"""
📚 Course: {course}
📊 Grade: {grade}
""")

            elif option4 == 3:
                print("""
✏️ EDIT GRADE
─────────────────────────
""")
                if not grades:
                    print("📊 No grades found.")

                else:


                    course4=input("❯ The course of the grade:").lower().strip()

                    found_course=0
                    for course in courses:
                        if course.name == course4:
                            found_course=1
                            break

                    if found_course==0:
                        print("❌ Course not found.")
                        continue

                    if course4 not in grades:
                        print("❌ No grade found for this course.")
                        continue

                    try:
                        grade4=int(input("❯ The new grade: "))
                    except ValueError:
                        print("❌ Grade must be a number.")
                        continue

                    if grade4 < 0 or grade4 > 100:
                        print("❌ Grade must be between 0 and 100.")
                        continue

                    grades[course4]=grade4
                    print("✅ Grade edited successfully!")

            elif option4 == 4:
                print("""
🗑️ DELETE GRADE
─────────────────────────
""")
                if not grades:
                    print("📊 No grades found.")

                else:


                    course4=input("❯ The course of the grade:").lower().strip()

                    if course4 not in grades:
                        print("❌ Grade not found.")
                        continue

                    del grades[course4]
                    print("✅ Grade deleted successfully!")

            elif option4 == 5:

                print(calculate_average(grades, courses))

            elif option4 == 0:
                continue
            else:
                print("❌ Invalid option. Please choose a valid option.")

        elif option == 5:

            print("""
🧠 SMART PLANNER
─────────────────────────
""")

            planner = sort_planner(assignments, exams)

            if not planner:
                print("✅ No upcoming tasks or exams.")

            else:
                print("""
📋 YOUR PLAN
─────────────────────────
""")

                for i, item in enumerate(planner):

                    item_type = item[0]
                    item_object = item[1]

                    if item_type == "overdue":

                        print(f"""
{i+1}. ⚠️ OVERDUE ASSIGNMENT
📝 Name:       {item_object.name}
📚 Course:     {item_object.course}
📅 Due Date:   {item_object.date}
🎯 Priority:   {item_object.priority}
""")

                    elif item_type == "exam":

                        print(f"""
{i+1}. 📅 EXAM
📝 Name:       {item_object.name}
📚 Course:     {item_object.course}
📅 Date:       {item_object.date}
🎯 Difficulty: {item_object.difficulty}
""")

                    else:

                        print(f"""
{i+1}. 📝 ASSIGNMENT
📝 Name:       {item_object.name}
📚 Course:     {item_object.course}
📅 Date:       {item_object.date}
🎯 Priority:   {item_object.priority}
""")

        elif option == 6:

            print("""
╔══════════════════════════════════════════════╗
║              📊 STUDENT DASHBOARD            ║
╚══════════════════════════════════════════════╝
""")

            total_courses = len(courses)
            total_credits = 0

            for course in courses:
                total_credits += course.credits

            total_assignments = len(assignments)
            completed_assignments = 0
            pending_assignments = 0

            for assignment in assignments:
                if assignment.status == "completed":
                    completed_assignments += 1
                else:
                    pending_assignments += 1

            total_exams = len(exams)
            upcoming_exams = 0
            today=datetime.combine(datetime.now().date(), datetime.min.time())

            for exam in exams:
                exam_date = datetime.strptime(exam.date, "%d/%m/%Y")

                if exam_date >= today:
                    upcoming_exams += 1

            total_grades = len(grades)

            total = 0
            total_grade_credits = 0

            for course_name, grade in grades.items():

                for course in courses:

                    if course.name == course_name:
                        total += grade * course.credits
                        total_grade_credits += course.credits

            if total_grade_credits == 0:
                average = 0
            else:
                average = total / total_grade_credits

            print(f"""
📚 COURSES
─────────────────────────
Total Courses:        {total_courses}
Total Credits:        {total_credits}

📝 ASSIGNMENTS
─────────────────────────
Total Assignments:    {total_assignments}
✅ Completed:          {completed_assignments}
⏳ Pending:            {pending_assignments}

📅 EXAMS
─────────────────────────
Total Exams:          {total_exams}
🔜 Upcoming Exams:    {upcoming_exams}

📊 GRADES
─────────────────────────
Grades Recorded:      {total_grades}
📈 Average:            {average:.2f}

══════════════════════════════════════════════
🎓 STUDENT COMMAND CENTER
══════════════════════════════════════════════
""")

        elif option == 0:
            save_data(courses, assignments, exams, grades)

            print("💾 Data saved successfully!")
            print("👋 Goodbye!")

        else:
            print("❌ Invalid option. Please choose 0-6.")


def calculate_average(grades, courses):
    """
    take a dict of grades and a list of courses
    then calculate the Average
    """
    total = 0
    total_credits = 0
    for course_name, grade in grades.items():
        for course in courses:
            if course.name == course_name:
                total += grade * course.credits
                total_credits += course.credits

    if total_credits == 0:
        return("❌ No grades found.")
    else:
        average = total / total_credits
        return f"📊 Average: {average:.2f}"

def sort_key(item):

    item_type = item[0]
    item_object = item[1]
    item_date = item[2]

    difficulty_order = {
        "hard": 1,
        "medium": 2,
        "easy": 3
    }

    priority_order = {
        "high": 1,
        "medium": 2,
        "low": 3
    }

    if item_type == "overdue":
        return (
            0,
            item_date,
            priority_order[item_object.priority]
        )

    elif item_type == "exam":
        return (
            1,
            item_date,
            0,
            difficulty_order[item_object.difficulty]
        )

    else:
        return (
            1,
            item_date,
            1,
            priority_order[item_object.priority]
        )


def sort_planner(assignments, exams):

    today=datetime.combine(datetime.now().date(), datetime.min.time())

    planner = []

    for exam in exams:

        exam_date = datetime.strptime(
            exam.date,
            "%d/%m/%Y"
        )

        if exam_date >= today:
            planner.append(("exam", exam, exam_date))

    for assignment in assignments:

        if assignment.status != "completed":

            assignment_date = datetime.strptime(
                assignment.date,
                "%d/%m/%Y"
            )

            if assignment_date < today:
                planner.append(
                    ("overdue", assignment, assignment_date)
                )

            else:
                planner.append(
                    ("assignment", assignment, assignment_date)
                )

    planner.sort(key=sort_key)

    return planner

def save_data(courses, assignments, exams, grades):

    data = {
        "courses": [],
        "assignments": [],
        "exams": [],
        "grades": grades
    }

    for course in courses:
        data["courses"].append({
            "name": course.name,
            "code": course.code,
            "credits": course.credits,
            "instructor": course.instructor
        })

    for assignment in assignments:
        data["assignments"].append({
            "name": assignment.name,
            "course": assignment.course,
            "date": assignment.date,
            "priority": assignment.priority,
            "status": assignment.status
        })

    for exam in exams:
        data["exams"].append({
            "course": exam.course,
            "name": exam.name,
            "date": exam.date,
            "difficulty": exam.difficulty
        })

    with open("student_data.json", "w") as file:
        json.dump(data, file, indent=4)


def load_data():

    try:

        with open("student_data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:

        return [], [], [], {}

    courses = []
    assignments = []
    exams = []
    grades = data.get("grades", {})

    for course in data.get("courses", []):

        course1 = Course(
            course["name"],
            course["code"],
            course["credits"],
            course["instructor"]
        )

        courses.append(course1)

    for assignment in data.get("assignments", []):

        assignment1 = Assignment(
            assignment["name"],
            assignment["course"],
            assignment["date"],
            assignment["priority"],
            assignment["status"]
        )

        assignments.append(assignment1)

    for exam in data.get("exams", []):

        exam1 = Exam(
            exam["course"],
            exam["name"],
            exam["date"],
            exam["difficulty"]
        )

        exams.append(exam1)

    return courses, assignments, exams, grades

if __name__ == "__main__":
    main()
