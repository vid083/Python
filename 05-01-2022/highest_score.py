student_score = input("Enter a list of student scores: ").split()
for n in range(len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

#print(max(student_score))


for i in range(len(student_score)):
    # print("ï = ",i)
    for j in range(len(student_score)):
        # print(j)
        if student_score[i] > student_score[j] and i != j:
            highest_score = student_score[i]
print(f"The hightest score in the class is {highest_score}")


# highest_score = 0
# for score in student_score:
#     if score > highest_score:
#         highest_score = score
# print(f"The hightest score in the class is {highest_score}")
