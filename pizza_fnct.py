def make_pizza(*toppings):
  print('\nThe following are the toppings you ordered-')
  for topping in toppings:
    print(topping)
  
make_pizza('chicken','bbq','cheese','peperroni')
make_pizza('egg')