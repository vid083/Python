student_heights = input("Enter a list of student heights ").split()
for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

'''
total_height = sum(student_heights)
num_of_height = len(student_heights)

avg_height = round(total_height / num_of_height)
print(avg_height)

'''
total_height = 0
for heights in student_heights:
    total_height += heights

num_of_students = 0
for students in student_heights:
    num_of_students += 1

avg_height = round(total_height / num_of_students)
print(avg_height)



