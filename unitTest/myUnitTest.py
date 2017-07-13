def is_palindrom(str):
	'''
 		return true iff the string is palindrom
	'''
	return str==str[::-1]

def is_leap_year(year):
	'''
 		return true iff the year is leap year
	'''
	if year % 4 != 0:
		return False
	elif year % 100 !=0:
		return True
	elif year % 400 !=0:
		return False
	else:
		return True
def reverse(str):
	'''
 		return reverse string
	'''
	return str[::-1]

''' #################################################
    #                 PYTEST CASES                  #
	#################################################
'''
def test_palindrome():
	value = is_palindrom('dad') 
	assert value == True

def test_leapyear():
	value = is_leap_year(2016) 
	assert value == True
	value = is_leap_year(2011) 
	assert value == False

def test_reverse():
	value = reverse("abc") 
	assert value == "cba"
	value = reverse([1,2,3]) 
	assert value == [3,2,1]
    