# functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
    
# Main Function
def calculator():
    print("Select the operation you want to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")  

    choice = input("Enter the number of the operation(1/2/3/4): ")

    #Check if the the choise is valid
    if choice not in ['1', '2', '3', '4']:
        print("Invalid operation!")
        return
    #Ask for the numbers  