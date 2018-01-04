class Restro():
  def __init__(self,restro_type,cuisine_type):
    self.restro_type=restro_type
    self.cuisine_type=cuisine_type
    
  def open_restaurant(self):
    print(self.restro_type.title()+' is open now.')
    
restaurant=Restro('punjabi dhaba','punjabi')
print(restaurant.restro_type.title()+ ' is a '+ restaurant.cuisine_type.title() + ' cuisine restaurant.')
restaurant.open_restaurant()

restaurants=Restro('dhaba','punjabi')
print('\n')
print(restaurants.restro_type.title()+ ' is a '+ restaurants.cuisine_type.title() + ' cuisine restaurant.')
restaurants.open_restaurant()

restaurantss=Restro('desi dhaba','punjabi')
print('\n')
print(restaurantss.restro_type.title()+ ' is a '+ restaurantss.cuisine_type.title() + ' cuisine restaurant.')
restaurantss.open_restaurant()
    