def data_type(data):
	if type(data)== str:
		return len(data)
	elif data == None:
		return "no value"
	elif type(data)== bool:
		return data
	elif type(data)== int:
		if data<200:
			return "less than 100"
		else:
			return "more than 100"
	elif type(data)== list:
		if len(data)>=3:
			return data[2]
		elif len(data)<3:
			print "None"
		elif len(data)<0:
			print "None"

data_type([])