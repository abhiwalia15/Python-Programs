my_pizza=['cheese','pep','bbq']
friends_pizza=my_pizza[:]
print("my pizza are:")
print(my_pizza)
print("my friends pizza are :")
print(friends_pizza)
my_pizza.append('farm')
friends_pizza=my_pizza[:] 
print("my pizza are:")
print(my_pizza)
print("my friends pizza are :")
print(friends_pizza)
my_pizza.append('nonveg')
print("my pizza are:")
print(my_pizza)
friends_pizza.append('veg')
print("my friends pizza are :")
print(friends_pizza)

