class  Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def sum(self):
        print("_"*10)
        
        return f"""
The first number is:{self.num1}
The operation is: +
The second number is: {self.num2}
Sum = {self.num1+self.num2}
    """
        print("_"*10)

    def minus(self):
        print("_"*10)
        return f"""
The first number is:{self.num1}
The operation is: -
The second number is: {self.num2}
Minus = {self.num1+self.num2}
    """    
        print("_"*10)
        
    def Multiplication(self):
        print("_"*10)
        return f"""
The first number is:{self.num1}
The operation is: *
The second number is: {self.num2}
Minus = {self.num1+self.num2}
    """    
        print("_"*10)
        
    def Division(self):
        print("_"*10)
        return f"""
The first number is:{self.num1}
The operation is: /
The second number is: {self.num2}
Minus = {self.num1+self.num2}
    """    
        print("_"*10)


while True:
    print("\n1. Sum")
    print("2. Minus")
    print("3. Multiplication")
    print("4. Devision")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    match choice:
        case "1":
            calc1=Calculator(int(input("Enter num1 --> ")), int(input("Enter num2 --> ")))
            print(calc1.sum())
            
        case "2":
            calc1=Calculator(int(input("Enter num1 --> ")), int(input("Enter num2 --> ")))
            print(calc1.minus())
            
        case "3":
            calc1=Calculator(int(input("Enter num1 --> ")), int(input("Enter num2 --> ")))
            print(calc1.Multiplication())
       
        case "4":
            calc1=Calculator(int(input("Enter num1 --> ")), int(input("Enter num2 --> ")))
            print(calc1.Division())     
            
        case "5":
            break