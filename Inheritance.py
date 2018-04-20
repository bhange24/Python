class BaseClass:
    def addition(self, numb1, numb2):
        add = numb1+numb2
        print("Addition of two numbers=", add)

    def Substation(self, numb1, numb2):
        sub = numb1-numb2
        print("Substation of two numbers=", sub)


class ChildClass(BaseClass):
    def method2(self):
        print("childClass method2")


def main():
    # exercise the class methods
    obj1 = ChildClass()
    obj1.Substation(12, 34)
    obj1.addition(52, 63)
    obj1.method2()


if __name__ == "__main__":
    main()