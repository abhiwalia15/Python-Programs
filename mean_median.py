def median(numbers):
	numbers.sort()
	if len(numbers)%2!=0:
		middle_index=int(len(numbers)/2)	
		return numbers[middle_index]
	else:
		right_of_middle=int(len(numbers)/2)
		left_of_middle = right_of_middle - 1
		return (numbers[right_of_middle]+numbers[left_of_middle])/2
print(median([1,2,5,3,6,7,8,2]))