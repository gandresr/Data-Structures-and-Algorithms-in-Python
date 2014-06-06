from time import time
import numpy as np
import matplotlib.pyplot as plt

def counterTime(x):
	start_time = time()
	sum = 0;
	for i in range(x):
		sum += i
	end_time = time()
	return end_time-start_time

# x = [counterTime(i) for i in range(10000)]
# plt.plot(x,'o')
# plt.show()

def approxLog(a, b):
	logV = 0
	while a > 1:
		a = a/float(b)
		logV += 1
	return logV

y = [approxLog(i,2) for i in range(0,100)]
x = [i for i in range(0,100)]
plt.plot(x)
plt.plot(y)
plt.show()