class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def _average_rate(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
        average_rate = sum(all_grades) / len(all_grades)
        return round(average_rate, 1)
    
    def __str__(self) :
        result = f'Имя: {self.name}\n'
        result += f'Фамилия: {self.surname}\n'
        result += f'Средняя оценка за домашнии задания: {self._average_rate()}\n'
        result += f'Курсы в процессе обучения: {",".join(self.courses_in_progress)}\n'
        result += f'Завершенные курсы: {",".join(self.finished_courses)}'
        return result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_rate(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
        average_rate = sum(all_grades) / len(all_grades)
        return round(average_rate, 1)
    
    def __str__(self) :
        result = f'Имя: {self.name}\n'
        result += f'Фамилия: {self.surname}\n'
        result += f'Средняя оценка за лекции: {self._average_rate()}'
        return result


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
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result



