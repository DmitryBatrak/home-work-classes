class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lection(self, lecturer,  course, grade) -> None:
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Error"

    def get_rating(self) -> float:
        all_grades = []
        for course_name, grades in self.grades.items():
            for grade in grades:
                all_grades.append(int(grade))
        if len(all_grades) > 0:
            average_rating = sum(all_grades) / len(all_grades)
        else:
            average_rating = 0
        return average_rating

    def __str__(self):
        average_rating = self.get_rating()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_rating}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}")

    def __eq__(self, student):
        return self.get_rating() == student.get_rating()

    def __ne__(self, student):
        return self.get_rating() != student.get_rating()

    def __lt__(self, student):
        return self.get_rating() < student.get_rating()

    def __gt__(self, student):
        return self.get_rating() > student.get_rating()

    def __le__(self, student):
        return self.get_rating() <= student.get_rating()

    def __ge__(self, student):
        return self.get_rating() >= student.get_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_rating(self) -> float:
        all_grades = []
        for course_name, grades in self.grades.items():
            for grade in grades:
                all_grades.append(int(grade))
        if len(all_grades) > 0:
            average_rating = sum(all_grades) / len(all_grades)
        else:
            average_rating = 0
        return average_rating

    def __str__(self):
        average_rating = self.get_rating()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_rating}"

    def __eq__(self, lecturer):
        return self.get_rating() == lecturer.get_rating()

    def __ne__(self, lecturer):
        return self.get_rating() != lecturer.get_rating()

    def __lt__(self, lecturer):
        return self.get_rating() < lecturer.get_rating()

    def __gt__(self, lecturer):
        return self.get_rating() > lecturer.get_rating()

    def __le__(self, lecturer):
        return self.get_rating() <= lecturer.get_rating()

    def __ge__(self, lecturer):
        return self.get_rating() >= lecturer.get_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade) -> None:
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Error"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def average_hw_grade(*, students_list: list, course_name: str) -> float:
    """
    The program calculates the average homework grade for all students within a specific course
    :return: average scores
    """
    all_grades = []
    for student in students_list:
        for grade in student.grades[course_name]:
            all_grades.append(int(grade))
    if len(all_grades) > 0:
        average_rating = sum(all_grades) / len(all_grades)
    else:
        average_rating = 0
    return average_rating


def average_lection_grade(*, lecturers_list: list, course_name: str) -> float:
    """
    The program calculates the average score for lectures of all lecturers within the course
    :return: average scores
    """
    all_grades = []
    for lecturer in lecturers_list:
        for grade in lecturer.grades[course_name]:
            all_grades.append(int(grade))
    if len(all_grades) > 0:
        average_rating = sum(all_grades) / len(all_grades)
    else:
        average_rating = 0
    return average_rating


student_one = Student("Bob", "White", "male")
student_two = Student("Roy", "Black", "male")
lecturer_one = Lecturer("Sam", "Johns")
lecturer_two = Lecturer("Ben", "Sherman")
reviewer_one = Reviewer("Ann", "Small")
reviewer_two = Reviewer("Katty", "Griffin")

student_one.courses_in_progress += ["Phyton"]
student_two.courses_in_progress += ["Phyton"]
lecturer_one.courses_attached += ["Phyton"]
lecturer_two.courses_attached += ["Phyton"]
reviewer_one.courses_attached += ["Phyton"]
reviewer_two.courses_attached += ["Phyton"]

student_one.finished_courses += ["JS"]
student_two.finished_courses += ["C#"]

reviewer_one.rate_hw(student_one, "Phyton", 10)
reviewer_one.rate_hw(student_one, "Phyton", 9)
reviewer_two.rate_hw(student_two, "Phyton", 8)
reviewer_two.rate_hw(student_two, "Phyton", 9)

student_one.rate_lection(lecturer_one, "Phyton", 10)
student_one.rate_lection(lecturer_one, "Phyton", 10)
student_two.rate_lection(lecturer_two, "Phyton", 10)
student_two.rate_lection(lecturer_two, "Phyton", 10)

students = [student_one, student_two]
lecturers = [lecturer_one, lecturer_two]

print(student_one.get_rating(), "\n")
print(student_two, "\n")
print(student_one < student_two, "\n")
print(lecturer_one.get_rating(), "\n")
print(lecturer_two, "\n")
print(lecturer_one == lecturer_two, "\n")
print(reviewer_one, "\n")
print(average_hw_grade(students_list=students, course_name="Phyton"), "\n")
print(average_lection_grade(lecturers_list=lecturers, course_name="Phyton"))






