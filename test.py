from main import *
from course_manager import *


stud1 = Student('Anton', 'Veshkin', 'Male')
stud1.courses_in_progress += ['Python', 'Cpp']
stud1.finished_courses +=['Ангийский для разработчиков']

stud2 = Student('Ivan', 'Elnitsky', 'Male')
stud2.courses_in_progress += ['Python']

lect1 = Lecturer('Oleg', 'Buligin')
lect1.courses_attached = ['Python']

lect2 = Lecturer('Anna', 'Batitskaya')
lect2.courses_attached = ['Python', 'Cpp']

rev = Reviewer ('Aleksandr', 'Bardin')
rev.courses_attached = ['Python', 'Cpp']

rev2 = Reviewer('Ended', 'Fantasy')


stud1.rate_lect(lect1, 'Python', 10)
stud1.rate_lect(lect1, 'Python', 9)
stud1.rate_lect(lect1, 'Python', 7)
stud2.rate_lect(lect1, 'Python', 8)
stud2.rate_lect(lect1, 'Python', 8)


stud1.rate_lect(lect2, 'Python', 7)
stud1.rate_lect(lect2, 'Python', 7)
stud1.rate_lect(lect2, 'Python', 7)
stud2.rate_lect(lect2, 'Python', 5)
stud2.rate_lect(lect2, 'Python', 5)


rev.rate_hw(stud1, 'Python', 10)
rev.rate_hw(stud1, 'Python', 10)
rev.rate_hw(stud1, 'Python', 10)
rev2.rate_hw(stud1, 'Python', 2)

rev.rate_hw(stud2, 'Python', 7)
rev.rate_hw(stud2, 'Python', 6)
rev.rate_hw(stud2, 'Python', 10)
rev2.rate_hw(stud2, 'Python', 2)



print(stud1)
print(lect1)
print(rev)
print()
print(stud1 < stud2)
print(lect1 >= lect2)
print()
print(average_lecturer_grade_by_course([lect1, lect2], 'Python'))
print(average_students_grade_by_course([stud1, stud2], 'Python'))





