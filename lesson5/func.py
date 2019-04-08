# empty func
def empty():
	pass


# multiply
def mult(num):
	return num*2


# parity
def parity(num):
	if num % 2 == 0:
		return 'Yes'
	else:
		return 'No'


# check >10
def check_10(num1, num2):
	if num1 > 10:
		return 'Yes'
	else:
		return 'No'


# lambda
g = lambda num1, num2: num1 % num2


# my decor
def decor(func):
	def wrap():
		print('=========')
		print(func())
		print('=========')
	return wrap
@decor
def hello():
	return('Hello world!')


# map and filter
lst = [16, 12, 2, 4, 5, 11, 22]
def func1(x):
	return x + 2

def func2(x):
	return x > 5



# minmax
def minmax(lst):
	print(min(lst))
	print(max(lst))


# output
print(mult(2))
print(parity(7))
print(check_10(11, 2))
print(g(11,2))
hello()
print(list(map(func1, lst)))
print(list(filter(func2, lst)))
minmax(lst)
