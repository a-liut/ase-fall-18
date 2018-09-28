# Calculator modue for customers

# must perform n increments to the value of m and return the result
def sum(m, n):
	if n < 0:
		for i in range(abs(n)):
			m -= 1
	else:
		for i in range(n):
			m = m + 1
	return m

# must subtract n from m until it gets to 0 and return the result
# ITS WRONG!
def divide(m, n):
	result = 0
	isnegative = m > 0 and n < 0 or m < 0 and n > 0

	for i in range(n), m - n >= 0:
		m -= n
		result += 1

	result = -result if isnegative else result

	return result


print sum(10, 3) #13
print sum(-1, 3) #2
print sum(10, -3) #7
print sum(-10, -3) #-13

print divide(10, 3) #1
print divide(-1, 3) #
print divide(10, -3) #
print divide(-10, -3) #