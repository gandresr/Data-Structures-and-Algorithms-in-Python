
# EX R-1.1
def isMultiple(a, b):
	return a%b==0
# EX R-1.2
def isEven(k):

	if k == 0:
		return False

	s = str(k)
	last = int( s[-1] )

	if last in [0, 2, 4, 6, 8]:
		return True
	return False

# EX R-1.3
def minmax(data):

	max = data[0]
	min = data[0]

	for i in range(1,len(data)):
		if data[i] > max:
			max = data[i]
		elif data[i] < min:
			min = data[i]

	return (min, max)

# EX R-1.4
def squares(n):

	sq = 0
	for i in range(n):
		sq += i**2

	return sq

# EX R-1.5
def squares2(n):
	return sum([a**2 for a in range(n)])

# EX R-1.7
def squareodds(n):
	return sum([a**2 for a in range(0,n,2)])

# EX C-1.13
def reverseList(l):
	n = len(l)
	reversedList = range(n)
	for i in range( (n-1), -1, -1 ):
		reversedList[i] = l[(n-1)-i]
	return reversedList 

# EX C-1.14
def oddProduct(l):
	return sum([(a%2)!=0 for a in set(l)]) > 2

# EX C-1.15
def allDistinct(l):
	return len(set(l)) == len(l)

# EX C-1.24
def countVowels(s):
	vowels = 0
	for l in s.lower():
		if l in ['a','e','i','o','u']:
			vowels += 1
	return vowels

# EX C-1.25
def rmPunctuation(s):
	newS = ''
	for l in s:
		if l in ["'",',',';','.',':']:
			newS += ''
		else:
			newS += l
	return newS


# EX C-1.28
def norm(v, p=2):
	return (sum([a**p for a in v]))**(1/float(p))

# EX P-1.29
#from intertools import combinations
#def allStrings(s = ['c','a','t','d','o','g']):0
#	return [a for a in combinations(s, 1)]



