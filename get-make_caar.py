def make_car(manufacture,car_model,**car_info):
  car={}
  car['manufacture']=input(manufacture).title()
  car['car_model']=input(car_model).title()
  
  for key,value in car_info.items():
    
    car[key]=input(value).title()
    
  return car
  
car=make_car('manufacture', 'car model', color='color', tow_package='tow package')
print(car)