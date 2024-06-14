class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Creating an instance of Person class
person = Person("Alice", 30, "female")

# Calling the introduce method to display person's information
person.introduce()
