# The clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make the 'past' function return the time converted to milliseconds.
# More examples in the test cases below.

def past(h, m, s):
	# 1 hour in milliseconds is 3600000
	# 1 minute in milliseconds is 60000
	# 1 second in milliseconds is 1000
	time_ms = h*3600000 + m*60000 + s*1000

	return time_ms