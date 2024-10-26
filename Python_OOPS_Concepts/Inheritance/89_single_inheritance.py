class Human:
    def __init__(self, num_heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart

    def eat(self):
        print("I can Eat")

    def work(self):
        print("I can Work")

class Male(Human):
    def __init__(self, name, heart):
        super().__init__(heart)
        self.name = name

    def flirt(self):
        print("I can Flirt")

    def work(self):
        super().work() # using super we can access parent class method with same name in child class
        print("I can Code")

    def display(self):
        print(f"Hi, I am {self.name} and I have {self.num_heart} heart")

male_1 = Male("Neeraj", 1)
male_1.eat()
male_1.work()
print(male_1.name)
print(male_1.num_eyes) # if we have self def init in child class it will throw error ('Male' object has no attribute 'num_eyes')
# it the above code error will be fixed br adding super in self def (super().__init__())
print(male_1.num_heart)
male_1.display()