class Human:
    can_breath = True
    def __init__(self, num_heart):
        print("Calling Human Class")
        self.num_nose = 1
        self.num_eyes = 2
        self.num_heart = num_heart

    def eat(self):
        print("I can Eat")

    def work(self):
        print("I can Work")


class Male(Human):
    def __init__(self, name):
        print("Calling Male Class")
        self.name = name

    def flirt(self):
        print("I can Flirt")

    def work(self):
        super().work()
        print("I can Code")


class Boy(Male):
    def __init__(self, name, heart, can_dance):
        print("Calling Boy Class")
        Human.__init__(self, heart)
        Male.__init__(self, name)
        self.know_dance = can_dance

    def sleep(self):
        print("I can Sleep")

    def work(self):
        Human.work(self)
        Male.work(self)
        print("I can Test")

boy_1 = Boy("Neeraj", 1, True)
print(boy_1.num_eyes)
print(boy_1.name)
print(boy_1.know_dance)
print(boy_1.can_breath)

boy_1.work()
boy_1.flirt()
boy_1.eat()
boy_1.sleep()
print(Boy.mro())

