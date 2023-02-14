def is_one_digit(v):
    # Checks if a number is an integer and has only one digit
    return v % 1 == 0 and -10 < v < 10

def check(v1, v2, v3):
    # Given three values, creates a message that will be displayed to the user based on specific conditions.
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        # If both values v1 and v2 are one-digit numbers, add the message associated with the code msg_6.
        msg += msg_6

    if v3 == "*" and (v1 == 1 or v2 == 1):
        # If the operation is multiplication and at least one of the values is equal to 1, add the message associated with the code msg_7.
        msg += msg_7

    if (v1 == 0 or v2 == 0) and (v3 != "/"):
        # If either of the values is 0 and the operation is not division, add the message associated with the code msg_8.
        msg += msg_8

    if msg:
        # If there is a message, add the message associated with the code msg_9 to the beginning of the message.
        msg = msg_9 + msg
        print(msg)

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

running = True
memory = 0

# Main loop
while running:
    print(msg_0)
    calc = input()

    # Split the input string into its components
    x, oper, y = calc.split()

    try:
        if x == "M":
            # If the first value is M, replace it with the value stored in memory
            x = memory
        if y == "M":
            # If the second value is M, replace it with the value stored in memory
            y = memory
        x = float(x)
        y = float(y)
    except ValueError:
        # If there is a ValueError, the input was not valid
        print(msg_1)
        continue

    valid_oper = "+-*/"
    if oper not in valid_oper:
        # If the operator is not valid, print an error message and continue to the next iteration of the loop
        print(msg_2)
        continue

    check(x, y, oper)

    # Initialize result to 0
    result = 0

    # Check the operator and calculate the result
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/":
        # Check if the second input is zero before dividing
        if y == 0.0:
            # Print an error message and continue with the next iteration
            print(msg_3)
            continue
        else:
            result = x / y

    # Print the result
    print(result)

    # Ask the user if they want to perform additional operations
    answer = ""
    while answer != "y" and answer != "n":
        # Prompt the user for input
        print(msg_4)
        answer = input()
        if answer == "y":
            # Check if the result is a single digit
            if is_one_digit(result):
                # Print additional messages for single-digit results
                msg_index = 10
                while msg_index < 13:
                    if msg_index == 10:
                        print(msg_10)
                    elif msg_index == 11:
                        print(msg_11)
                    else:
                        print(msg_12)
                    # Prompt the user for input
                    answer2 = input()
                    if answer2 == "y":
                        msg_index += 1
                    elif answer2 == "n":
                        break
                else:
                    # Save the result in memory if it is not a single digit
                    memory = result
            else:
                # Save the result in memory if it is not a single digit
                memory = result

    # Ask the user if they want to continue running the program
    answer = ""
    while answer != "y" and answer != "n":
        # Prompt the user for input
        print(msg_5)
        answer = input()
        if answer == "n":
            # Exit the program
            running = False
