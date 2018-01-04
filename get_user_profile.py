def build_profile(first,last,**user_info):
  
  profile={}
  profile['first name']=input(first).title()
  profile['last name']=input(last).title()
  
  for key,value in user_info.items():
    profile[key]=input(value)
  
  return profile
  
print(build_profile('first_name','last_name',location='location',age='age',interests='interests'))
    
