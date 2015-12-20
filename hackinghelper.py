# Fallout 4 Hacking Helper
# purplehaze150

choices = 0		# initial number of passwords in ingame terminal
passwords = []		# list for storing each password
i = 0			# incremented in while loop for adding passwords to passwords list

def compare(str1, str2):    #input two strings, returns # of letters that match (location and character)
	count = 0
	x = 0
	if (len(str1) == len(str2)):
		while x < len(str1):
			if str1[x] == str2[x]:
				count += 1
			x += 1
		return count

choices = int(float(raw_input("Enter the number of choices available: ")))			# convert input string to integer
while (i < choices):
	passwords.append(raw_input("Enter password %s in all lowercase: " % (i+1)))		# input all passwords
	i += 1

while len(passwords) >= 1:									# while there are passwords left in list
	newpasswords = []									# fixes iterating through list problem
	tempchoice = ""										# temp location for each chosen password
	tempcomp = 0										# output of compare function
	diff = 0										# storage for likeness of tempchoice
	print "Your choices are:\n %s" % (passwords)						# print all choices
	tempchoice = raw_input("Input your choice: ")						# input first chosen password
	diff = int(float(raw_input("What is the likeness? ")))					# input number of similar characters 
	for words in passwords:
		tempcomp = compare(tempchoice, words)						# compare with each password
		print "There are %s similarities between %s and %s!" % (tempcomp, tempchoice, words)
		if diff == tempcomp:
			newpasswords.append(words)
	passwords = newpasswords
