# Define an example numbers for sorting
numbers=[10,34,53,63,2,45]
n=len(numbers) # get the length of the array
for i in range(n): #Circular array lens
    for j in range(0,n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j] #to compare the second one and first one and cycleing
print(numbers)
