# Perform simple arithmetic encoded in an input string:
# '1 + 2' -> 3, or '1 - 2' -> -1.
def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y
def power(x, y):
    return x**y

def calculator():
    while True:
        print("___Simple Python Calculator___")
        print("Selecet and option")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Exit")
        choice = input("Select one of the above option")
        if choice == '6':
            print("Closing the app...\n")
            print(".......\n")
            break
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid operation")
            return
    try:
        num1 = float(input("Enter your first number:"))
        num2 = float(input("Enter your second number:"))
    except ValueError:
                     print("Invalid Error!")
                     return
        if choice == '1':
                     print(f"Result: add{num1, num2}")
        elif choice == '2':
                     print(f"Result: subtract{num1, num2}")
        elif choice == '3':
                     print(f"Result: multiply{num1, num2}")
        elif choice == '4':
                     print(f"Result: divide{num1, num2}")
        elif choice == '5':
                      print(f"Result: power{num1, num2}")
if __name__ == "__main__":
                     culculator()
                    




