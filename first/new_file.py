import statistics


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


from statistics import mean
inp_lst_1 = [9.9, 9.9, 9.9]
list_avg_1 = mean(inp_lst_1)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.lectures = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def __gt__(self, other):
        return mean(self.grades[self.courses_attached[0]]) > mean(other.grades[other.courses_attached[0]])

    def __lt__(self, other):
        return mean(self.grades) < mean(other.grades)


from statistics import mean
inp_lst = [9.9, 9.9, 9.9]
list_avg = mean(inp_lst)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


pythonStr = 'Python'
javascriptStr = 'Javascript'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += [pythonStr, javascriptStr]
worst_student = Student('Artem', 'Petrov', 'male')
worst_student.courses_in_progress += [pythonStr, javascriptStr]

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += [pythonStr, javascriptStr]
bad_lecturer = Lecturer('Some', 'Buddy')
bad_lecturer.courses_attached += [pythonStr, javascriptStr]

best_student.rate_l(cool_lecturer, pythonStr, 10)
best_student.rate_l(cool_lecturer, javascriptStr, 9)

best_student.rate_l(bad_lecturer, pythonStr, 8)
best_student.rate_l(bad_lecturer, javascriptStr, 4)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += [pythonStr, javascriptStr]
cool_reviewer.rate_hw(best_student, pythonStr, 10)
cool_reviewer.rate_hw(best_student, javascriptStr, 10)

cool_reviewer.rate_hw(worst_student, pythonStr, 5)
cool_reviewer.rate_hw(worst_student, javascriptStr, 6)


def calculate_grades(student_list, course):
    grades = []
    for student in student_list:
        grades += student.grades[course]
    return mean(grades)


students = [best_student, worst_student]
print(calculate_grades(students, pythonStr))
print(calculate_grades(students, javascriptStr))


def calculate_lectures(lecturer_list, course):
    lectures = []
    for lecturer in lecturer_list:
        lectures += lecturer.lectures[course]
    return mean(lectures)


lecturers = [cool_lecturer, bad_lecturer]
print(calculate_lectures(lecturers, pythonStr))
print(calculate_lectures(lecturers, javascriptStr))


# print(cool_lecturer.grades)
cool_reviewer = Reviewer('Some', 'Buddy')
print(cool_reviewer.__str__())

# cool_lecturer = Lecturer('Some', 'Buddy')
print(cool_lecturer.__str__())
print(f"Средняя оценка за лекцию: {list_avg}\n")

best_student = Student('Ruoy', 'Eman', 'your_gender')
print(best_student.__str__())
print(f"Средняя оценка за домашнее задание: {list_avg_1}\n")


print(cool_lecturer.__gt__(bad_lecturer))
# print(cool_lecturer.grades)


