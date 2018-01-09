def bmi(weight,height):
	bmi=weight/(height**2)
	print(bmi)

mom=[60,1.57]
bmi(mom[0],mom[1])

abhi=[76,1.79]
bmi(*abhi)
