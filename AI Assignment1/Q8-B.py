# Q.B) Make a class called User. Create two attributes called first_name and last_name, and then
# create several other attributes that are typically stored in a user profile. Make a method called
# describe_user() that prints a summary of the user’s information. Make another method called
# greet_user() that prints a personalized greeting to the user. Create several instances representing
# different users, and call both method for each user.

class User:
    def __init__(self,first_name,last_name,age,email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email =email
    
    def describe_user(self):
        print(f'First name : {self.first_name}')
        print(f'Last name : {self.last_name}')
        print(f'Age : {self.age}')
        print(f'Email : {self.email}')

    def greet_user(self):
        print(f'Hello, {self.first_name} {self.last_name}\nWelcome Back!!')

user1 = User('Sukhmanpreet','Singh',20,'abc@thapar.edu')
user2 = User('Eshaan','Singla',21,'ab23c@thapar.edu')
user3 = User('Arshdeep','Singh',19,'ab54c@thapar.edu')

user1.describe_user()
user1.greet_user()
print('\n')

user2.describe_user()
user2.greet_user()
print('\n')

user3.describe_user()
user3.greet_user()
print('\n')
