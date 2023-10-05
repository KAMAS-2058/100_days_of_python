# making a program that calcualtes the highest score in the classe from user input
# not allowed to use the max function

student_scores = input("Please enter the scores from your class, we will tell you the highest score:").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

#manually making the max function from stack overflow
highest_score = None
for i in student_scores:
    if highest_score is None or i > highest_score: highest_score = i

print(highest_score)

# from course solution
top_score = 0

for score in student_scores:
    if score > top_score:
        top_score = score