aliens=[]
for alien_number in range(0,30):
	new_alien={'color':'green','speed':'low','point':5}
	aliens.append(new_alien)
for alien in aliens[:5]:
	if alien['color']=='green':
		alien['color']='yellow'
		alien['speed']='medium'
		alien['point']=10
for alien in aliens[:10]:
	print(alien)
print("....")
print("The total number of aliens are " + str(len(aliens)))
