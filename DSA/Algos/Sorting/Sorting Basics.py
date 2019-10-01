###O(n^2)
def BB_sort(arr):
	for j in range(len(arr)-1):
		for i in range(len(arr)-1-j):
			if arr[i]>arr[i+1]:
				arr[i],arr[i+1] = arr[i+1],arr[i]
	return arr

###O(n^2)m

def S_sort(arr):
	for j in range(len(arr)):
		min = sys.maxsize
		for i in range(len(arr)-j):
			if arr[i+j]<min:
				min_ind = i+j
				min = arr[i+j]
		arr[j],arr[min_ind] = arr[min_ind],arr[j]
	return arr

###O(n+m)f

def join(arr1,arr2):
	ret = []
	while len(arr1) and len(arr2):
		if arr1[0]<=arr2[0]:
			ret.append(arr1.pop(0))
		else:
			ret.append(arr2.pop(0))
	for i in arr1:
		ret.append(i)
	for i in arr2:
		ret.append(i)
	return ret
#O(n log(n) )

def M_sort(arr):
	if len(arr)==1:
		return(arr)
	L = M_sort(arr[:len(arr)//2])
	R = M_sort(arr[len(arr)//2:])
	return join(L,R)
###


#time O(nlogn)av, O(n^2)wrst,space o(1), randomize pivot choice to ensure O(nlogn) to high probablty

def pivot(arr,start,end):
	piv = random.randint(start, end)
	arr[piv],arr[end] = arr[end],arr[piv]
	PI = start
	LI = start
	while LI < end:
		if arr[LI]<arr[end]:
			arr[LI],arr[PI] = arr[PI],arr[LI]
			PI+=1
		LI+=1
	arr[end],arr[PI] = 	arr[PI],arr[end]
	return PI

def Q_sortH(arr,start,end):
	if start>=end:
		return
	PI = pivot(arr,start,end)
	Q_sortH(arr,start,PI-1)
	Q_sortH(arr,PI+1,end)
	return arr

def Q_sort(arr):
	return Q_sortH(arr,0,len(arr)-1)


####

M_sort([3,2,8,1,5])
S_sort([3,2,8,1,5])
BB_sort([3,2,8,1,5])
Q_sort([3,2,8,1,5])




