#usr/bin/env python3

def word_of_list_of_words(list_of_words):
	"""This function tkaes a list of words and concaneate a word with the position
	of n on the list of words"""
	if len(list_of_words) == 0:
		return ""
	word_complete = ""
	for n, w in enumerate(list_of_words):
		if len(w) > n:
			word_complete += w[n]
		else:
			word_complete += ""
	return word_complete



def word_of_list_of_words_refactor(list_of_words):
	"""This function tkaes a list of words and concaneate a word with the position
	of n on the list of words"""
	if len(list_of_words) == 0:
		return ""
	
	return "".join([w[n] for n, w in enumerate(list_of_words) if len(w) > n])


