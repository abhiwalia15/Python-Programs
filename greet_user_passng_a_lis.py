def greet_users(names):
  for name in names:
    msg= 'Hello , {} !'.format(name)
    print(msg)
username=['abhi','lovee','mummy','dad']
print(greet_users(username))