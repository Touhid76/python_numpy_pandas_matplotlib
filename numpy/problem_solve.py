import numpy as np

# Data
marks = np.array([
    [45, 60, 75],
    [80, 55, 70],
    [90, 85, 88],
    [30, 40, 50],
    [70, 75, 80]
])

# 1. Total marks of each student
total_marks = np.sum(marks, axis=1)
print("Total marks:", total_marks)

# 2. Average marks of each student
avg_marks = np.mean(marks, axis=1)
print("Average marks:", avg_marks)

# 3. Highest scorer (student index + marks)
top_index = np.argmax(total_marks)
print("Top student index:", top_index)
print("Top student total marks:", total_marks[top_index])

# 4. Average marks per subject
subject_avg = np.mean(marks, axis=0)
print("Subject-wise average:", subject_avg)

# 5. Students who scored >70 in ALL subjects
good_students = marks[np.all(marks > 70, axis=1)]
print("Students scoring >70 in all subjects:\n", good_students)

# 6. Add 5 grace marks (broadcasting)
grace_marks = marks + 5
print("Marks after adding grace:\n", grace_marks)

# 7. Grade system
grades = np.where(marks >= 80, 'A',
         np.where(marks >= 60, 'B',
         np.where(marks >= 40, 'C', 'F')))
print("Grades:\n", grades)

# 8. Normalization (0 to 1 scaling)
min_val = np.min(marks)
max_val = np.max(marks)

normalized = (marks - min_val) / (max_val - min_val)
print("Normalized marks:\n", normalized)