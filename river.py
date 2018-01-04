data={'nile':'egypt',
	'yamuna':'india',
	'ganga':'india',
	'kaveri':'india',
	'yamnotri':'india'
	}
for river,country in data.items():
	print("The "+river.title()+ " runs through "+country.title() +".")
