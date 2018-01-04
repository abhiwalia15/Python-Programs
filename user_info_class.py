class User():
  def __init__(self,first_name,last_name):
    self.first_name=first_name
    self.last_name=last_name
    
  def greet(self):
     print('\nWelcome-'+ self.first_name.title()+' '+self.last_name.title())
     
user=User('abbhi','walia')
print(user.first_name.title() +' '+ user.last_name.title() + ' is the man.')
user.greet()