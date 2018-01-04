class Car():
	
	def __init__(self,make,model,year):
		self.make=make 
		self.model=model
		self.year=year
		self.oddometer=0
		
	def get_name(self):
		f_name=self.make+' '+str(self.year)+' '+self.model
		return f_name.title()
			
	def read_oddometer(self):
		"""print a statement showing cars milege"""
		print('The car has '+str(self.oddometer)+' miles on it.')
		
	def update_oddometer(self,milege):
		self.oddometer=milege
		print('My car has a milege of '+str(self.oddometer))
		
	def increment_oddometer(self,miles):
		self.oddometer += miles
		

		
		
