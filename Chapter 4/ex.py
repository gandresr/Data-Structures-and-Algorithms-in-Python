#-*- coding: utf-8 -*-

def factorial(n):
	if (n == 0) or (n == 1):
		return 1
	else:
		return factorial(n-1)*n

# EX P-4.25
# n -> inches of the ruler
# tl -> tick length
def draw_english_ruler(n, tl): 
	'''Draw an English ruler of n inches -> n has to be an integer'''

	for i in range(int(8*n/tl+1)):
		if (i%(8/tl) == 0):
			print ('---- %d' % (i*tl/8))
		elif (i%(4/tl) == 0):
			print ('---')
		elif (i%(2/tl) == 0):
			print ('--')
		else:
			print ('-')

def bad_fibonacci(n):
	if (n == 0) or (n == 1):
		return 1
	else:
		return bad_fibonacci(n-1)+bad_fibonacci(n-2)

def good_fibonacci(n):
	if (n == 0) or (n == 1):
		return (n,0)
	else:
		(a, b) = good_fibonacci(n-1)
		return (a+b, a)

from time import time
import numpy as np
import matplotlib.pyplot as plt

# This algorithm is O(n), as it makes n+1 recursive calls
def power(x, n):
	if n == 0:
		return 1
	else:
		return x*power(x, n-1)

def power2(x, n):
	if n == 0:
		return 1
	else:
		partial = power(x, n/2)
		result = partial * partial
		if (n%2 != 0):
			result *= x
	return result

# EX R-4.1 # EX C-4.9
# Time Complexity: O(n)
# Space Usage: O(n)
def find_max(s):
	if len(s) == 1:
		return s[0]
	else:
		max_number = find_max(s[1:])
		if max_number > s[0]:
			result_max = max_number 
		else:
			result_max = s[0]
		if max_number < s[0]:
			result_min = max_number
		else:
			result_min = s[0]
		return result_min, result_max


# t1 = [0]*500
# t2 = [0]*500
# for i in range(500):
# 	start = time()
# 	power2(2,i)
# 	end = time()
# 	t2[i] = end-start
# for i in range(500):
# 	start = time()
# 	power(2,i)
# 	end = time()
# 	t1[i] = end-start
# plt.plot(range(500), t1)
# plt.plot(range(500), t2)
# plt.show()

# t = [0]*999
# for i in range(999):
# 	start = time()
# 	print (good_fibonacci(i)[1])
# 	end = time()
# 	t[i] = end-start
# plt.plot(range(999), t)
# plt.show()

# t = [0]*40
# for i in range(40):
# 	start = time()
# 	bad_fibonacci(i)
# 	end = time()
# 	t[i] = end-start
# plt.plot(range(40), t)
# plt.show()
