from car import Car

class Battery():
	
	def __init__(self,battery_size=70):
		self.battery_size=battery_size
		
	def describe(self):
		print('This car has a battery of '+str(self.battery_size)+' -Kwh.')
				
	def range(self):
		if self.battery_size == 70:
			range=240
		elif self.battery_size == 80:
			range=280
		
		msg = 'This car has a'+str(range)
		msg += 'miles on full fuel.'
		print(msg)
		
		
class ElectricCar(Car):
	
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery=Battery()
		
