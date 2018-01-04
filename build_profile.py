def build_profile(first,last,**user_info):
  profile={}
  profile['first name']=first
  profile['last name']=last
  
  for key,value in user_info.items():
    profile[key] = value
  return profile
  
user=build_profile('albert', 'einstein', location='delhi',field='physics')
print(user)