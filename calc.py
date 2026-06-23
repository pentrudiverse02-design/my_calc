
class Calculator:
    def __init__(self):
        self.a=0
        self.b=0
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def setA(self):
        self.a=float(input("a:"))
    def setB(self):
        self.b=float(input("b:"))
    def sin(self):
        return math.sin(self.a/self.b)
    def pornesteCalculator(self):


        print(f"  a = {self.a}   b = {self.b}")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. setA")
        print("6. setB")
        print("7. Sin")
        a=int(input("Enter your choice:"))
        match a:
            case 1:
                print(self.add())
            case 2:
                print(self.sub())
            case 3:
                print(self.mul())
            case 4:
                print(self.div())
            case 5:
                self.setA()
            case 6:
                self.setB()
            case 7:
                self.sin()
        self.pornesteCalculator()

if __name__ == '__main__':
    calculator=Calculator()
    calculator.pornesteCalculator()