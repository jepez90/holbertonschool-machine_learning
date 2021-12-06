#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# your code here
#  plt.figure(1, constrained_layout=True, )
# plt.subplots(nrows=3, ncols=2, gridspec_kw={"wspace":0.5, "hspace":0.5})

a_1 = plt.subplot(321)
a_1.plot(np.arange(0, 11), y0, 'r-')

a = plt.subplot(322)
a.scatter(x1, y1, c="magenta", s=5)
a.set_title("Men's Height vs Weight", fontsize="x-small")
a.set_xlabel("Height (in)", fontsize="x-small")
a.set_ylabel("Weight (lbs)", fontsize="x-small")

b = plt.subplot(323)
b.plot(x2, y2, 'b-')
b.set_yscale("log")
b.axis([0, 28650, None, None])
b.set_title("Exponential Decay of C-14", fontsize="x-small")
b.set_xlabel("Time (years)", fontsize="x-small")
b.set_ylabel("Fraction Remaining", fontsize="x-small")

c = plt.subplot(3, 2, 4)
c.plot(x3, y31, 'r--', label="C-14")
c.plot(x3, y32, 'g-', label="Ra226")
c.axis([0, 20000, 0, 1])
c.set_title("Exponential Decay of Radioactive Elements", fontsize="x-small")
c.set_xlabel("Time (years)", fontsize="x-small")
c.set_ylabel("Fraction Remaining", fontsize="x-small")
c.legend()

plt.subplot(3, 2, (5, 6))
plt.hist(student_grades, bins=np.arange(10, 101, 10), edgecolor="black")
plt.axis([0, 100, 0, 30])
plt.title("Project A", fontsize="x-small")
plt.xlabel("Grades", fontsize="x-small")
plt.ylabel("Number of Students", fontsize="x-small")
plt.xticks(np.arange(0, 101, step=10))
plt.yticks(np.arange(0, 30, step=5))

plt.suptitle('Big Suptitle')
plt.show()
