class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades[course].append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Student(Mentor):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = None

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course not in self.grades:
                self.grades[course] = []
            self.grades[course].append(grade)
            self.update_average_grade()
        else:
            return 'Ошибка'

    def update_average_grade(self):
        self.average_grade = sum(grade for grades in self.grades.values() for grade in grades) / len(
            self.grades) if self.grades else 0

    def __str__(self):
        average_grade = sum(grade for grades in self.grades.values() for grade in grades) / len(
            self.grades) if self.grades else 0
        return f'Имя: {self.name}\nФамилия: {self.surname}\nПол: {self.gender}\nСредняя оценка за домашние задания: {average_grade:.2f}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade == other.average_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade > other.average_grade


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.average_grade = None

    def __str__(self):
        average_grade = sum(grade for grades in self.grades.values() for grade in grades) / len(
            self.grades) if self.grades else 0
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.2f}\nПрисоединенные курсы: {", ".join(self.courses_attached)}'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade == other.average_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade > other.average_grade


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nПрисоединенные курсы: {", ".join(self.courses_attached)}'

    def __eq__(self, other):
        if not isinstance(other, Reviewer):
            return NotImplemented
        return self.name == other.name and self.surname == other.surname

    def __lt__(self, other):
        if not isinstance(other, Reviewer):
            return NotImplemented
        return self.name < other.name

    def __gt__(self, other):
        if not isinstance(other, Reviewer):
            return NotImplemented
        return self.name > other.name


student = Student('Some', 'Buddy', 'male')
lecturer = Lecturer('Alice', 'Smith')
reviewer = Reviewer('Bob', 'Johnson')

reviewer.courses_attached.append('Python')
reviewer.courses_attached.append('Git')
some_reviewer = Reviewer('Some', 'Buddy')
some_student = Student('Ruoy', 'Eman', 'male')
some_lecturer = Lecturer('Some', 'Buddy')

student.courses_in_progress.append('Python')
student.courses_in_progress.append('Git')
lecturer.courses_attached.append('Python')
lecturer.courses_attached.append('Git')

student.rate_lecturer(lecturer, 'Python', 10)
student.rate_lecturer(lecturer, 'Git', 9)


print(some_reviewer)
print(some_lecturer)
print(some_student)

print(student)
print(lecturer)
print(reviewer)