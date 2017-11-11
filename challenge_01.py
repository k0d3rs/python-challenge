# http://www.pythonchallenge.com/pc/def/map.html

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

first_letter = 97
num_letters = 26
caesars_offset = 2

# Solution 1 - map

print("\nSolution 1 - map\n")

f_subst = lambda c: chr( first_letter + ((ord(c) - first_letter + caesars_offset) % num_letters)) if (ord(c) >= first_letter and ord(c)<first_letter + num_letters) else c
decrypted_list1 = map(f_subst, list(text))
decrypted_text1 = ''.join(decrypted_list1)
print("\nHint for solution 1: " + decrypted_text1 + "\n")

new_url = "http://www.pythonchallenge.com/pc/def/" + ''.join(map(f_subst, list("map"))) + ".html"
print("Solution 1: " + new_url + "\n")


# Solution 2 - List comprehensions

print("Solution 2 - List comprehensions")

text_list = list(text)
def modify(c):
	if (ord(c) >= first_letter and ord(c)<first_letter + num_letters):
		return chr( first_letter + ((ord(c) - first_letter + 		caesars_offset) % num_letters))
	else:
		return c

decrypted_list2 = [modify(x) for x in text_list]
decrypted_text2 = ''.join(decrypted_list2)
print("\nHint for solution 2: " + decrypted_text2 + "\n")

new_url = "http://www.pythonchallenge.com/pc/def/" + ''.join([modify(x) for x in list("map")]) + ".html"
print("Solution 2: " + new_url + "\n")


# Solution 3 - str.maketrans

import string

print("Solution 3 - str.maketrans\n")

dict = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[caesars_offset:] + string.ascii_lowercase[0:caesars_offset])
decrypted_text3 = text.translate(dict)
print("\nHint for solution 3: " + decrypted_text3 + "\n")

new_url = "http://www.pythonchallenge.com/pc/def/" + "map".translate(dict) + ".html"
print("Solution 3: " + new_url + "\n")