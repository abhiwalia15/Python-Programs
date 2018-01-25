world_heritage_locations = {(13.4125, 103.866667): "Angkor Wat",
                            (25.73333, 32.6): "Ancient Thebes",
                            (30.330556, 35.4433330): "Petra",
                            (-13.116667, -72.583333): "Machu Picchu"}
                            
for latilongi,place in world_heritage_locations.items():
	
	latitude = latilongi[0]
	print(str(latitude) + ' is latitude of ' + place )
	
	longitude = latilongi[1]
	print(str(longitude) + ' is longitude of ' + place )
	
	
