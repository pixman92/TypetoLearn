# take in code
# code can be multi lined
# exit code when 2 enters are pressed

# soon to print array length in 
# strings bookended with \n

import sys

bookendsArray = []
savedCode = []
lineMe = ""
i = 1

#input for multilined code
#ends input with EOF text
print ("Insert Code here")
while True:
	rawCode=raw_input()
	if rawCode == "EOF":
		break
	if rawCode is None:
		rawCode = raw_input()
	savedCode.append(rawCode)

print("line?")
#prints Line? asks for line to skip to
#needs to 0 out when no number entered

#try except to find if not number
#if failed, try again

while True:
	try:
		lineMe = int(raw_input())
		if lineMe == "":
			i=0
			print(i)
			break
		else:
			i=lineMe
			break
		if lineMe =="\n\n\n":
			break
	except:
		i=0
		# print(i)
		print("Not a number!")
		break


	# print("i=")
	# print(i)
	# print(savedCode)




skip = False
#code to compare typed line to 
#line saved in array of Strings
while True:
	# print("I ran!")
	# print (i)
	print savedCode[i]
	x = raw_input()
	print("\nLine " + str(i))

	if x.isdigit()==True:		
		i = int(x)
		skip = True
		# print("i=x")
		# print(x, i)

	# print(i)
	if x==savedCode[i]:
		print ("\nCorrect!")
		i=i+1
	elif skip == False:
		print ("wrong!")
		skip = True
	if x == "done":
		break
	if savedCode[i] is "":
		print savedCode[i]
		i+=1
	if i > len(savedCode):
		print "All done! Good job!"
		break

                                    
