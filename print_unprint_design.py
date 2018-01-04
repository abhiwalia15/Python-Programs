unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_designs=[]

while unprinted_designs:
  
  current_designs=unprinted_designs.pop()
  print('current designs :'+current_designs)
  completed_designs.append(current_designs)
  
for completed_design in completed_designs:
  print('completed designs :'+completed_design)