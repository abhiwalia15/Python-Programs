def remove_duplicates(countries):
  target=[]
  for countrie in countries:
    if countrie not in target:
      target.append(countrie)
  return target
print(remove_duplicates(['Angola', 'Maldives', 'India', 'United States', 'India']))