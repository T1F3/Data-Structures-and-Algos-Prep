#find No occurrences of chars in string, return max
def max_char(string):
	chars = {i:0 for i in list(string)}
	for i in string:
		chars[i]+=1
	return max(chars,key=chars.get)

#check if string only has unique characters
def chr_unq(string):
	chr_arr = list(string)
	unq_chr_arr = list(set(chr_arr))
	if len(unq_chr_arr)==len(chr_arr):
		return True
	else:
		return False

#compare all values, O(n^2) time, O(1) space
def chr_unq1(string):
	n = 0
	j = 1
	while n<len(string)-1:
		while j< len(string)-n:
			if string[n]==string[n+j]:
				return False
			j+=1
		j = 1
		n+=1
	return True

#use array with indices as ascii codes, O(n) time, O(1) space(bigger const space though)
def chr_unq2(string):
	#if more chars than ASCII char set, has to repeat at least once
	if len(string)>128:
		return False
	#ASCII character set number
	char_arr = [None]*128
	for i in string:
		#get ASCII code
		asc = ord(i)
		#if that index not None, an earlier char has changed it
		if char_arr[asc]:
			return False
		#set value at index of ascii code to not None
		char_arr[asc] = 1
	return True

#sort first, then all duplicates should be adjacent
def chr_unq3(string):
	string_arr = list(string)
	string_arr.sort()
	n = 0
	while n<len(string_arr)-1:
		if string_arr[n]==string_arr[n+1]:
			return False
		n+=1
	return True
		
