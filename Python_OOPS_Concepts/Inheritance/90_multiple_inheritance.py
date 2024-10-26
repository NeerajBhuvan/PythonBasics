class Human:
    def __init__(self, num_heart):
        self.num_nose = 1
        self.num_eyes = 2
        self.num_heart = num_heart

    def eat(self):
        print("I can Eat")

    def work(self):
        print("I can Work")


class Male:
    def __init__(self, name):
        self.name = name

    def flirt(self):
        print("I can Flirt")

    def work(self):
        print("I can Code")


class Boy(Human, Male):
    def __init__(self, name, heart, language):
        Human.__init__(self, heart)
        Male.__init__(self, name)
        self.language = language

    def sleep(self):
        print("I can Sleep")

    def work(self):
        print("I can Test")

    def display(self):
        print(f"Hi I'm {self.name}, I am working in {self.language} programming language")


boy_1 = Boy("Neeraj", 1, "Python")
boy_1.eat()
boy_1.flirt()
boy_1.sleep()
boy_1.work()
Male.work(boy_1)
Human.work(boy_1)
print(Boy.mro()) #to check how classes are called in order [<class '__main__.Boy'>, <class '__main__.Human'>, <class '__main__.Male'>, <class 'object'>]
print(boy_1.name)
print(boy_1.num_heart)
boy_1.display()