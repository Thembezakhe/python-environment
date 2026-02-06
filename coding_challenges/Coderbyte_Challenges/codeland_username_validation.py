"""
Challenge: Codeland Username Validation (Coderbyte)

Goal:
Validate whether a given string qualifies as a valid username
based on a fixed set of rules involving length, allowed characters,
and positioning constraints.

Approach:
- Check length constraints
- Ensure the username starts with a letter
- Validate allowed characters only
- Ensure the username does not end with an underscore

Time Complexity:
O(n), where n is the length of the username

Space Complexity:
O(1), constant extra space
"""

def CodelandUsernameValidation(strParam):
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
print(CodelandUsernameValidation("John_Doe"))
print(CodelandUsernameValidation("3Jogn"))
print(CodelandUsernameValidation("Jane_"))
print(CodelandUsernameValidation("A"))

# Example test cases:
# Input: "aa_" → False
# Input: "u__hello_world123" → True

