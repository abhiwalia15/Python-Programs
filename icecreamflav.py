class restro():
	def __init__(self,type,cuisine):
		self.type=type
		self.cuisine=cuisine
		self.served=0
		
	def status(self):
		print(self.type.title()+' is OPEN')
		
	def serve(self,persons):
		self.served=persons
		print('The '+self.cuisine.title() +' can serve '+str(self.served)+' persons at a time.')
		
class icecreamstand(restro):
	def __init__(self,type,cuisine):
		super().__init__(type,cuisine)	
		
	def flavours(self):
		for flavour in flavours:
			print('your ice cream has '+self.flavour.title()+'.')
			
res=restro('punjabi','rajasthani')
print(res.type.title()+res.cuisine.title()+' theme restaurant.')
res.status()
res.serve(23)
flav=icecreamstand('butter_scotch','chcoclate','vanilla')
flav.flavours()
