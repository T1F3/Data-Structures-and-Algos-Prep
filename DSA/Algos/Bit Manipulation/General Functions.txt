def Getbit(num,index):
	return (num & (1<<index))>0

def Setbit(num, index):
	return num | (1<<index)

def Clrbit(num,index):
	return num & ~(1<<index)

def ClrUp2(num,index):
	return num & ( (1<<index) - 1)

def Clr4rm(num,index):
	return num & ( -1<<(index+1) )

def insert(num,index,val):
	upd_num = num & ~(1<<index)
	upd_num = upd_num | ( (1<<index) * val)
	return upd_num

def fit(N,M,j,i,bits):

def float_2_bin():
