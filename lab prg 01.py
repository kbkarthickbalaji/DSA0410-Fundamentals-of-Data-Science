import numpy as np
student_scores = np.array([
    [80, 90, 85, 70],
    [75, 88, 78, 85],
    [92, 81, 86, 78],
    [88, 79, 90, 82]
])
subject_averages = np.mean(student_scores, axis=0)
max_index = np.argmax(subject_averages)
subjects = ["Math", "Science", "English", "History"]
highest_avg_subject = subjects[max_index]
print("Average scores per subject:", subject_averages)
print("Subject with highest average score:", highest_avg_subject)
