def add(a,b):
    answer = a + b
    print(str(a)+" + "+str(b)+" = "+str(answer) + "\n")
    
def sub(a,b):
    answer = a - b
    print(str(a)+" - "+str(b)+" = "+str(answer)+ "\n")

def mul(a,b):
    answer = a * b
    print(str(a)+" * "+str(b)+" = "+str(answer)+ "\n")

def div(a,b):
    answer = a / b
    print(str(a)+" / "+str(b)+" = "+str(answer)+ "\n")
while True:    
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    choice = input("Enter your choice: ")

    if choice == "A" or choice == "a":
        print("Aditions")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        add(a,b)
    elif choice == "B" or choice == "b":
        print("Subtraction")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        sub(a,b)
    elif choice == "C" or choice == "c":
        print("Multiplication")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        mul(a,b)
    elif choice == "D" or choice == "d":
        print("Division")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        div(a,b)
    elif choice == "E" or choice == "e":
        print("Exiting...")
        quit()
    else:
        print("Invalid choice")
        
