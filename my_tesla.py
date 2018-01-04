from car import ElectricCar

my_tes = ElectricCar('tesla','s',2019)

print(my_tes.get_name())
my_tes.battery.describe()
my_tes.battery.range()
