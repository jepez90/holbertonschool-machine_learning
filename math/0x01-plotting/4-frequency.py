#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# your code here
plt.hist(student_grades, bins=np.arange(10, 101, 10), edgecolor="black")
plt.axis([0, 100, 0, 30])
plt.title("Project A")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.xticks(np.arange(0, 101, step=10))
plt.yticks(np.arange(0, 30, step=5))
plt.show()
