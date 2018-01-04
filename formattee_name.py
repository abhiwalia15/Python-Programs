def formatted_name(first,last,middle=''):
  if middle:
    full_name=first + ' ' + middle + ' ' + last
  else:
    full_name=first+' '+last
  return full_name.title()
musician=formatted_name('jimi','hendrix')
print(musician)
musician=formatted_name('jimi','hendrix','lee')
print(musician)