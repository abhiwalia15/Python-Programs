prompt='Enter any thing and i will repeat it after you'
prompt += "\nEnter 'quit' to exit the program"
active = True
while active:
	message=input(prompt)
	if message =='quit':
		active=False
	else:
		print(message)
