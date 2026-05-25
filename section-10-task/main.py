import art

print(f"{art.logo}")

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    num1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        for key in operations:
            print(key)
            
        op = input("Pick an operation: ")
        
        num2 = float(input("what's the next number?: "))
        
        result = operations[op](num1, num2)
        print(f"{num1} {op} {num2} = {result}")
        
        y_or_n = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to start a new calculation: ").lower()
        
        if y_or_n == "y":
            num1 = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()