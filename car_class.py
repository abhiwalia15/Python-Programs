class car():
    def __init__(self,make,year,model):
        self.make=make
        self.year=year
        self.model=model
        self.oddo_meter_reading=0

    def get_descriptive_name(self):
        full_name=self.make+' '+self.model+' '+str(self.year)
        return full_name.title()

    def read_oddometer(self):
        print('This car has '+str(self.oddo_meter_reading)+' miles on it.')

    def update_oddometer(self,milege):
        if milege>=self.oddo_meter_reading:
            self.oddo_meter_reading=(milege)
        else:
            print('you cant roll back the oddommeter.')

    def increment_oddometer(self, miles):
        self.oddo_meter_reading += miles

my_new_car=car('lamborigini',2017,'avenador')
print(my_new_car.get_descriptive_name())

my_new_car.update_oddometer(65)
my_new_car.read_oddometer()

my_new_car.increment_oddometer(100)
my_new_car.read_oddometer()
