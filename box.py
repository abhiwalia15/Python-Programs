def box(width,height,symbol='*'):
	#make a box of desired width and height and your own symbol
	
	print(symbol * width)
	
	for height in range(height - 2):
		
		print( symbol + " " * (width -2) + symbol )
		
	print(symbol * width)
	
box(7,7,'b')		
	
