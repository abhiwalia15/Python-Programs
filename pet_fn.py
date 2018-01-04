def pet(pet_type,pet_name):
  print ('\nI have a {}'.format(pet_type))
  return "My {}'s name is {}.".format(pet_type,pet_name)
print(pet('dog','moti'))
print(pet('cat','jerry'))