class Username:
    name = ""

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Welcome to iQuadra:" + self.name)


User1 = Username("Shraddha")
User1.sayHello()