class Calc:

    # def __init__(self):
    #     self.a = 0
    #     self.b = 0

    def input(self):
        self.a = int(input("Enter a number: "))
        self.b = int(input("Enter another number: "))

        return self.a + self.b

    def input1(self):
        self.a = int(input("Enter a number: "))
        self.b = int(input("Enter another number: "))

        return self.a - self.b

    def input2(self):
        self.a = int(input("Enter a number: "))
        self.b = int(input("Enter another number: "))

        return self.a * self.b

    def input3(self):
        self.a = int(input("Enter a number: "))
        self.b = int(input("Enter another number: "))

        return self.a / self.b


Dhruvil = Calc()
print(f"Sum is "+ str(Dhruvil.input()))
print(f"subtraction is " + str(Dhruvil.input1()))
print(f"multiplication is " + str(Dhruvil.input2()))
print(f"Divison is "+ str(Dhruvil.input3()))
