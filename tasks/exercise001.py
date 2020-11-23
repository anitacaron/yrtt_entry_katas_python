# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
# Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15.
# More examples in the test cases below.

# Good luck!

def repeats(arr):
	dict_arr = dict()
	sum_unique = 0

	# count the occurrence of numbers using a dict
	for n in arr:
		if dict_arr.get(n) != None:
			dict_arr[n] += 1
		else:
			dict_arr[n] = 1

	# sum the numbers that occur once
	for key, item in dict_arr.items():
		if item == 1:
			sum_unique += key

	return sum_unique
