def build_person(first_name,last_name,age='',occupation=''):
  person = {'first':first_name,'last':last_name}
  if age:
    person['age']=age
  
    person['occupation']=occupation
  return person
print(build_person('mrinal','walia',19,'developer'))