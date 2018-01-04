user={
	'abhi':{
		'first':'mrinal',
		'last':'walia',
		'location':'ddn',
		},
	'lovee':{
		'first':'anish',
		'last':'walia',
		'location':'ddn',
		},
	}
for username,user_info in user.items():
 full_name=user_info['first']+" "+user_info['last']
 location=user_info['location']
 print("full name:"+ full_name.title())
 print("location:"+ location.title())
