def chck_perm(st1,st2):
	if not len(st1)==len(st2):
		return False
	s_st1 = list(st1)
	s_st2 = list(st2)
	s_st1.sort()
	s_st2.sort()
	if s_st1==s_st2:
		return True
	return False

def chck_perm2(st1,st2):
	if not len(st1)==len(st2):
		return False
	chr_arr1 = [0]*128
	for i in st1:
		chr_arr1[ord(i)] +=1
	for i in st2:
		chr_arr1[ord(i)] -=1
		if(chr_arr1[ord(i)]<0):
			return False
	return True
