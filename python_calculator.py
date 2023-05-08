from art import logo

def input_number():
    while True:
        user_input = input("Please give a number:")
        try:
            if "." in user_input:
                user_input = float(user_input)
            else:
                user_input = int(user_input)
            return user_input
        except ValueError:
            print("Please give a number as integer or float.")


def operation(a: int | float, operation: str) -> int | float:
    b = input_number()
    if operation == "+":
        c = a + b
    elif operation == "-":
        c = a - b
    elif operation == "*":
        c = a * b
    elif operation == "/":
        c = a / b
    print(f"{a} {operation} {b} = {c} \n")
    return c


calculation_ongoing = True
print(logo)
print("Welcome to the pythonic calculator! \n")
operation_number = input_number()

while calculation_ongoing:
    print(f"Please choose an operation from below: \n"
          f"+\n"
          f"-\n"
          f"*\n"
          f"/\n"
          f"exit \n")
    chosen_operation = input("Chosen operation:")
    
    if chosen_operation == "exit":
        calculation_ongoing = False
    elif chosen_operation == "+" or \
        chosen_operation == "-" or \
        chosen_operation == "*" or \
        chosen_operation == "/":
        operation_number = operation(operation_number, chosen_operation)
    else:
        print("Unacceptable command.")
        continue

    print("Do you wish to continue on? yes/no")
    continue_on = input("Your choice:")
    if continue_on == "no":
        calculation_ongoing = False

print("goodbye!")
