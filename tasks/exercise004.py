# Move the first letter of each word to the end of it, then add "ay" 
# to the end of the word. Leave punctuation marks untouched.

def pig_it(text):

	#split sentence with whitespace
	words = text.split(" ")

	punctuation = "!"

	# take first letter from each word, add 'ay' and put in the end
	for i, word in enumerate(words):
		first_l = word[0] + "ay"

		if punctuation in word:
			index = word.find(punctuation)
			words[i] = word[1:index] + first_l + word[index:]

		else:
			words[i] = word[1:] + first_l


	return ' '.join(words)