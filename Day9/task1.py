class Person:
    def __init__(self, name, surname, birthdate, country, city, region, profession, gender):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.country = country
        self.city = city
        self.region = region
        self.profession = profession
        self.gender = gender

    def get_info(self):
        return f"""
Name --> {self.name}
Surname --> {self.surname}
Birthdate --> {self.birthdate}
Country--> {self.country}
City --> {self.city}
Region --> {self.region}
Profession --> {self.profession}
Gender --> {self.gender}
"""

class User(Person):
    def __init__(self, name, surname, birthdate, country, city, region, profession, gender, username, password1, password2):
        super().__init__(name, surname, birthdate, country, city, region, profession, gender)
        self.username = username
        self.password1 = password1
        self.password2 = password2

    def get_user_info(self):
        return f"{self.username},{self.password1}\n"

class UserManager:
    def __init__(self):
        self.filename = "file1.txt"

    def sign_up(self):
        name = input("Enter your name -->  ")
        surname = input("Enter your surname -->  ")
        birthdate = input("Enter your birthdate -->  ")
        country = input("Enter your country -->  ")
        city = input("Enter your city -->  ")
        region = input("Enter your region -->  ")
        profession = input("Enter your profession -->  ")
        gender = input("Enter your gender -->  ")
        username = input("Enter your username -->  ")
        password1 = input("Enter your password -->  ")
        password2 = input("Confirm your password -->  ")

        if password1 != password2:
            print("Password invalid")
            return
        new_user = User(name, surname, birthdate, country, city, region, profession, gender, username, password1, password2)

        with open(self.filename, "a") as file:
            file.write(new_user.get_user_info())
        print("User registered successfully!")
        
    def users_info(self):
        with open(self.filename, "r") as file:
            users = file.readlines()
            for user in users:
                print(user.strip())
    
    def login(self, username, password):
        with open(self.filename, "r") as file:
            users = file.readlines()
            for user in users:
                saved_username, saved_password = user.strip().split(",")
                if saved_username == username and saved_password == password:
                    print("You have successfully entered the system.")
                    return True
            print("Username or password is incorrect.")
            return False


manager = UserManager()
while True:
    choice = input("Enter your choice --> ")
    
    if choice == '1':
        manager.sign_up()
    elif choice == '2':
        manager.users_info()
    elif choice == '3':
        username = input("Enter your username to login --> ")
        password = input("Enter your password to login --> ")
        if manager.login(username, password):
            print("Login successful.")
            break
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

