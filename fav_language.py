fav_lang={
	'mrinal':'python',
	'lovee':'r',
	'mummy':'c',
	'papa':'python',
	}
 
friend=['abhi','lovee','jat']
for name in fav_lang.keys():
    print(name.title())
    
    if name in friend:
        print("Thankyou " + name.title() + " for taking the poll")
    else:
        print(name.title()+" you should take the poll")
