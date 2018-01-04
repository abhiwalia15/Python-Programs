class Admin():
	
	privileges = []
	def __init__(self,privileges):
		self.privileges.append(['can add post','can delete post','can ban user'])
		for privilege in privileges:
			msg=('PRIVILEGES- '+privilege)
			
			return msg


