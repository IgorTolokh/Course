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
def func1(x):
	return x + 2

def func2(x):
	return x > 5



# minmax
def minmax(lst):
	return(min(lst))
	return(max(lst))


# year
def year_vis(year):
	if year % 100 != 0:
		if year %4 == 0:
			return('True')
		else: return('False')
	else: return('False')



# season
def season(x):
	if (x == 1 or x == 2 or x ==12):
		return('winter')
	elif (5>=x>=3):
		return('spring')
	elif (8>=x>=6):
		return('summer')
	elif (11>=x>=9):
		return('autumn')
	else:
		return('error')



# date
def date(*args):
	d = int(input('input day: '))
	m = int(input('input mounth: '))
	y = int(input('input year: '))
	v = year_vis(y)
	if  (m == 1 or m == 3 or m == 5 or m == 7 or m ==8 or m == 10 or m == 12):
		if (1<=d<=31):
			print('True')
		else: print('False')
	elif (m == 4 or m == 6 or m == 9 or m == 11):
		if (1<=d<=30):
			print('True')
		else: print('False')
	elif m == 2:
		if v == 'False':
			if (28>= d >= 1): return('True')
			else: return('False')
		else : 
			if (29>= d >= 1): return ('True')
			else : return('False')	



# lst
def sort(lst):
	lst1 = []
	for i in lst:
		if type(i) == int or type(i) == float:
			lst1.append(i)
		else: continue
	lst1 = sorted(lst1)
	return lst1
# output
print(mult(2))
print(parity(7))
print(check_10(11, 2))
print(g(11,2))
hello()
print(list(map(func1, [16, 12, 2, 4, 5, 11, 22])))
print(list(filter(func2, [16, 12, 2, 4, 5, 11, 22])))
print(minmax([16, 12, 2, 4, 5, 11, 22]))
print(year_vis(2016))
print(season(5))
print(date())
print(sort([16,-17, 2, 78.7, False, False, {'True' : True}, 555, 12, 23, 42, 'DD']))
