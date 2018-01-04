def starbox(width, height):
  print("*" * width)
  for _ in range(height-2):
      print("*" + " " * (width-2) + "*")
  print("*" * width)
  
print("Test 1:")
starbox(5, 5)  
  
  
  
  