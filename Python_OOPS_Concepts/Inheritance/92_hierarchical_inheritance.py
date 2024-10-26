class Human:
    def __init__(self, name, age):
        print("Calling Human class...")
        self.name = name
        self.age = age

    def show_details(self):
        print(f"name: {self.name}, age: {self.age}")

class Male(Human):
    def __init__(self, name, age, location):
        print("\nCalling Male class...")
        Human.__init__(self, name, age)
        self.location = location

    def display(self):
        print(f"I'm {self.name} and my age is {self.age}. I am from {self.location}.")


class Female(Human):
    def __init__(self, name, age, can_dance):
        print("\nCalling Female class...")
        super().__init__(name, age)
        self.know_dance = can_dance

    def display(self):
        Human.show_details(self)
        print(f"Know dance: {self.know_dance}")

female_1 = Female("Varsha", 25, True)
female_1.display()

male_1 = Male("Neeraj", 23, "TamilNadu")
male_1.display()



