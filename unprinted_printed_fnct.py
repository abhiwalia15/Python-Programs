def print_models(unprinted_designs,completed_designs):
  while unprinted_designs:
  
    current_designs=unprinted_designs.pop()
    print('current designs :'+current_designs)
    completed_designs.append(current_designs)

def show_completed_models(completed_designs):
  print('\nThe completed models are:')
  for completed_design in completed_designs:
    print(completed_design)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_designs=[]
print_models(unprinted_designs,completed_designs)
show_completed_models(completed_designs)