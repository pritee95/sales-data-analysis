import numpy as np

marks = np.array([
    [78, 85, 90],   # Student 1
    [60, 70, 65],   # Student 2
    [88, 92, 95],   # Student 3
    [45, 50, 40],   # Student 4
    [70, 75, 80]    # Student 5
])

subjects = ["Math", "Science", "English"]

# Student average
student_avg = np.mean(marks, axis=1)
print(student_avg)

#Subject-wise Average
subject_avg = np.mean(marks, axis=0)
print(subject_avg)

#Topper Student
topper = np.argmax(student_avg)
print("Top Student:", topper + 1)

#Failed Students (average < 50)
failed = np.where(student_avg < 50)
print("Failed Students:", failed[0] + 1)
