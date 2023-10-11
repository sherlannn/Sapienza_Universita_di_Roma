from collections import namedtuple

n = int(input())  # Number of students

s = input().split()
S = namedtuple('Student', s) 

students = []

for i in range(n):
    s_data = input().split()
    student_obj = S(*s_data) 
    students.append(student_obj)

total = 0
for s in students:
    total += int(s.MARKS)

avg = total / n

print("{:.2f}".format(avg))
