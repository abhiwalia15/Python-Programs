def get_formatted_name(first,last):
  full_name=first+' '+last
  return full_name.title()
  
while True:
  
  print('\nEnter your name')
  print("(enter q to quit)")
  
  f_name=input('Full name: ')
  if f_name=='q':
    break
  
  l_name=input('Last name: ')
  if l_name=='q':
    break
  
  print('\nHello, {} !'.format(get_formatted_name('mrinal','walia')))