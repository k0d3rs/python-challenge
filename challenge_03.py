# http://www.pythonchallenge.com/pc/def/equality.html

# Read file with data
file = open('challenge_03_data.txt', 'r') 
text_list = list(file.read())
file.close()

# Solution 1 - Traverse list and check if conditions are met

def meetsCriteria(index, list):
	if index<3 or index>len(list)-4: return False
	elif not list[index].islower(): return False
	elif (list[index-3].isupper() and list[index-2].isupper() and list[index-1].isupper() and list[index+1].isupper() and list[index+2].isupper() and list[index+3].isupper()):
		if (index==3 or list[index-4].islower()) and (index==len(list)-4 or list[index+4].islower()): return True
	else: return False
	
solution = []
for i in range(0, len(text_list)-1):
	if meetsCriteria(i, text_list): solution.append(text_list[i])

print("Solution: http://www.pythonchallenge.com/pc/def/" + ''.join(solution) + ".html")