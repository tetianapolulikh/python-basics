class User:

    def __init__(self,first_name, last_name, age, sex, citizenship):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.citizenship = citizenship

    def describe_user(self):
        print('\nUSER PROFILE')
        print(f"\nName: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Citizenship: {self.citizenship}")   

    def greet_user(self):
        full_name = f'{self.first_name} {self.last_name}'
        print(f"\nHello {full_name}, welcome back")

users = [
    User('Teti', 'Pol', 19, 'female', 'Ukrainian'),
    User('Sam', 'Pav', 23, 'male', 'Brazilian'),
    User('Vicky', 'Kom', 20, 'female', 'German')
]

for user in users:
    user.describe_user()
    user.greet_user()

