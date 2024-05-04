def add(num1,num2):
    total = num1+num2
    print(total)

def min(num1,num2):
    total = num1-num2
    print(total)

def multi(num1,num2):
    total = num1*num2
    print(total)

def div(num1,num2):
    total = num1/num2
    print(total)

print("addition")
print("minus")
print("multiplication")
print("division")
print("Exit")
choice = input("Enter the choice: ")
choice.lower()

    
while choice!="exit" :
    while choice not in ["addition", "minus", "multiplication", "division"]:
        print()
        choice = input("Please re-enter the information correctly: ").lower()
        
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    
    if choice=="addition":
        add(num1,num2)
    elif choice=="minus":
        min(num1,num2)
    elif choice=="multiplication":
        multi(num1,num2)
    else:
        div(num1,num2)
        
    print()
    print("addition")
    print("minus")
    print("multiplication")
    print("division")
    print("Exit")
    choice = input("Enter the choice: ")
    choice.lower()
print("Thank you for using us,Goodbye")