def nearest_square(limit):
  limit=limit**0.5
  y=int(limit)
  while y<limit:
    y=y*y
    return y
print(nearest_square(40))