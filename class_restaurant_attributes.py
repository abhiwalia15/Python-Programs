class restaurant():

    def __init__(self,restro_type,cuisine_type):
        self.restro_type=restro_type
        self.cuisine_type=cuisine_type
        self.number_served=0

    def status(self):
        print('The restaurant-'+self.restro_type+' is open now.')

    def served(self,number):
        self.number_served=input(number)

rest=restaurant('punjabi dhaba','punjabi')
print(rest.restro_type.title()+ ' is a '+ rest.cuisine_type.title() + ' cuisine restaurant.')

rest.status()
rest.served('people')
print(rest.restro_type.title() +' can serve '+str(rest.number_served)+' people at a time.')
