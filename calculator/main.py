from art import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}

def calculate():
    print(logo)
    should_accumulate = True
    number_1 =  (float(input("Please type the first number: " )))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operator =  (input("Please type a mathematical operator: "))
        number_2 = (float(input("Please type the second number: ")))
        answer = operations[operator] (number_1, number_2)
        print(f"{number_1} {operator} {number_2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculations: ")

        if choice == "y":
            number_1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculate()

calculate()
