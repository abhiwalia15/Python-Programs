def add_number(*numbs):
	total=0
	for numb in numbs:
		total += numb
	return total

print(add_number(3,5,15,14,16))
