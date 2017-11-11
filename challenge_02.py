# http://www.pythonchallenge.com/pc/def/ocr.html

# Read file with data
file = open('challenge_02_data.txt', 'r') 
text_list = list(file.read())
file.close()

# Let's see how many different symbols are there here
reps_dict = {}
for c in text_list:
	if c in reps_dict:
		reps_dict[c]=reps_dict[c]+1
	else:
		reps_dict[c]=1

# By inspection we realize there are very few 'rare' characters (with just one occurrence)
rare_list = [k for k, v in reps_dict.items() if v == 1]
	
# By combining them all, we've got the solution
solution = ''.join(rare_list)	

print("\nSolution: http://www.pythonchallenge.com/pc/def/" + solution + ".html")