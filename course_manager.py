from main import *

def average_students_grade_by_course(students, course):
    average_rates = []
    for student in students:
        if course in student.courses_in_progress:
            average_rates.append(student.average_rate())
    result = sum(average_rates) / len(average_rates)
    return round(result, 1)


def average_lecturer_grade_by_course(lecturers, course):
    average_rates = []
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            average_rates.append(lecturer.average_rate())
    result = sum(average_rates) / len(average_rates)
    return round(result, 1)
        
