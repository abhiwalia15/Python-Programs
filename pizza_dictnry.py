pizza={
	'base':'thick',
	'toppings':['bbq','cheese','chicken'],
	}
print("You ordered a pizza with "+pizza['base'].title() + " base and with this all toppings-")
for topping in pizza['toppings']:
	print(topping.title()) 
