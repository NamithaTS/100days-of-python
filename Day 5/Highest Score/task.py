student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(sum(student_scores))
t=0
m=0
for score in student_scores:
    t+=score
    if score>m:
        m=score
print(m)

print(t)
print(max(student_scores))