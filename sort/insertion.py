numbers = [89, 80, 38, 908, 786, 13, 56]

def sortasc(arr):
	ii=0
	nn=len(arr)
	while ii<nn-1:
		#n = len(arr)
		#min_number=arr[5]
		i=0
		min_index=0
		min_number=arr[min_index]
		while  i<nn-ii-1:
			if min_number>arr[i+1]:
				min_number=arr[i+1]
				min_index=i+1
			i+=1
		tmp=arr[nn-ii-1] #56
		arr[nn-ii-1]=min_number
		arr[min_index]=tmp
		ii+=1
	return arr
rr=sortasc(numbers)
print(rr)

numbers = [89, 80, 38, 908, 786, 13, 56]

