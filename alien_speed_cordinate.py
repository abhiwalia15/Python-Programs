alien={'x_cord':0,'y_cord':25,'speed':'medium'}
print("the original x-coordinate of the alien is " + str(alien['x_cord']))
alien['speed']='fast'
if alien['speed']=='slow':
	x_increament=1
elif alien['speed']=='medium':
	x_increament=2
else:
    x_increament=5
alien['x_cord']=alien['x_cord']+x_increament
print("the new x-coordinate of the alien is "+ str(alien['x_cord']))


