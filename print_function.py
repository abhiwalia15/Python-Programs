def print_models(unprinted_designs,completed_models):
  
  while unprinted_designs:
    
    complete=unprinted_designs.pop()
    print('unprinted designs: {}'.format(complete))
    completed_models.append(complete)
    
def show_completed_models(completed_models):
  print("\nThe following models have been printed:")
  for completed_model in completed_models:
    print(completed_model)
