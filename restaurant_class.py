class Restro():
  def __init__(self,restro_type,cuisine_type):
    self.restro_type=restro_type
    self.cuisine_type=cuisine_type
    
  def open_restaurant(self):
    print(self.restro_type.title()+' is open now.')
    
