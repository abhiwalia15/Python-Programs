def make_great(magicians_names,show_magicians):
  
  while magicians_names:
  
    magicians=magicians_names.pop()
    print('Magicians are: '+magicians.title())
    show_magicians.append(magicians)
  
def the_show_magicians(show_magicians):
  print('\nThe show magicians are as follows-')
  for show_magician in show_magicians:
    print('the great '+show_magician.title())

show_magicians=[]
magicians_names=['abhi','lovee','anish','mrinal']
make_great(magicians_names,show_magicians)
the_show_magicians(show_magicians)