current_users=['abhi','lovee','anish','mrinal','jaat']
new_users=['shreya','anjali','abhi','lovee','charu']
for new_user in new_users:
	if new_user in current_users:
		print("your username " + new_user.title() + " is alrady taken ,choose a new username")
	else:
		print("this username "+ new_user.title()+" is available")
		
