def word_count(sentence):
	wordcount={}
	for word in sentence.split():
		if word not in wordcount:
			wordcount[word] = 1
		else:
			wordcount[word] += 1
	for item in wordcount.items():
		print("{}:\t{}".format(*item))
word_count("Worldbuilding Stack Exchange is a question and answer site for")