shit={
	'ganga':'india',
	'nile':'egypt',
	'yamuna':'america',
	}
for river,country in shit.items():
	print("The " + river.title() + " runs through " + country.title())
	
for river in shit.keys():
	print("\n"+river.upper())
	
for country in shit.values():
	print("\n"+country.upper())	
