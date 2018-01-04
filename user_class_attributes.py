class Admin():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts = 0

    def login_attempt(self,attempts):
        self.login_attempt=attempts

    def increment_number_served(self):
        self.login_attempts += 1
        print('The number of attempts are now '+str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts =0
        print('The number of login attempts are again '+str(self.login_attempts))

    def greet_user(self):
        print('Welcome- '+self.first_name.title() +' '+ self.last_name.title())
        
    def show_privilege(self,privileges):
		self.privileges=[]
		self.privileges += ['can add post','can ban user','can delete post']
		for self.privilege in self.privileges:
			print(self.privilege)	    

user=Admin('abhi','walia')
user.login_attempts=23
user.increment_number_served()
user.greet_user()
user.reset_login_attempts()
user.show_privilege()
