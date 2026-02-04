def SearchingChallenge(strParam):
	#Checking length
	if len(strParam) < 4 or len(strParam) > 25:
		strParam = "false"
	#Check whether first char is a letter
	elif not strParam[0].isalpha():
		strParam = "false"
	#Check whether last char is underscore
	elif strParam[-1] == "_":
		strParam = "false"
	#Check that all char are letters, numbers or underscore
	else:
		valid = True
		for char in strParam:
			if not (char.isalnum() or char == "_"):
				valid = False
				break
		if valid:
			strParam = "true"
		else:
			strParam = "false"
	return strParam
print(SearchingChallenge("John_Doe"))
print(SearchingChallenge("3Jogn"))
print(SearchingChallenge("Jane_"))
print(SearchingChallenge("A"))
