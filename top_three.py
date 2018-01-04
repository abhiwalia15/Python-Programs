def top_three(input_list):
	sorted_list=sorted(input_list)
	top_three=sorted_list[-3:]
	return top_three
print(sorted(top_three([2,3,5,6,8,4,2,1]),reverse=True))

