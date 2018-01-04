req_tops=['chicken','bbq','olives','french fries']
available_tops=['chicken','bbq','sausages','tatti','gobar']
for req_top in req_tops:
	if req_top in available_tops:
		print("adding - "+req_top)
	else:
		print("sorry , we don't have "+ req_top)
print("finished adding your toppings")
