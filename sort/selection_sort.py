def selection_sort(arr): #defination the selction_sort longs
	for i in range(len(arr)): # i is staring index
		min_index = i
		for j in range(i+1,len(arr)): # j is index 0,1,2,3,4--90,67,13,78,45
			if arr[j] < arr[min_index]: # comparing
				min_index=j
		arr[i],arr[min_index]=arr[min_index],arr[i] # swap
	return arr
test_arr=[90,67,13,78,45] # test 
selection_sort(test_arr)
print(test_arr)
