magicians_names=['abhi','lovee','anish','mrinal']
show_magicians=[]

while magicians_names:
  
  magicians=magicians_names.pop()
  print('Magicians are: '+magicians)
  show_magicians.append(magicians)
  
print('\nThe show magicians are as follows-')
for show_magician in show_magicians:
  print(show_magician)