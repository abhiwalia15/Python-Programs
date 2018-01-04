class Dog():
  
  def __init__(self,name,age):
    self.name= name
    self.age= age
    
  def sit(self):
    print(self.name.title() +' is sitting now.')
    
  def roll_over(self):
    print(self.name.title() +' rolled now !')

my_dog = Dog('moti', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()