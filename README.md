# Truthful-Calculator
## Description
This is a simple command-line calculator program written in Python. It can perform basic arithmetic operations like addition, subtraction, multiplication, and division on two numbers provided by the user. It also has the ability to store the result in memory and prompt the user if they want to continue calculating or exit the program.

## How it works
The program starts with a main loop that runs until the user chooses to exit.
It prompts the user to enter an equation in the form number operator number, where the operator is one of +, -, *, or /.
It checks if the input is valid and displays error messages if necessary.
If the input is valid, it checks for certain conditions using the check function and displays a message to the user based on those conditions.
It performs the arithmetic operation on the two numbers and displays the result to the user.
It prompts the user if they want to store the result in memory and if the result is a single digit, it asks the user if they want to store it again.
It prompts the user if they want to continue calculating or exit the program.
## Functions
## is_one_digit(v)
   Checks if a number is an integer and has only one digit.

## check(v1, v2, v3)
   Given three values, creates a message that will be displayed to the user based on specific conditions.

## Main Loop
The main loop of the program that prompts the user for input, performs calculations, and displays output.

## Messages
The program uses several messages to prompt the user for input, display errors, and provide feedback. These messages are stored in variables with names like msg_0, msg_1, etc.

## Memory
The program has a memory variable that can store a single number. If the user chooses to store the result of a calculation in memory, it will overwrite any previous value stored there. The value stored in memory can be used in subsequent calculations by entering M instead of a number in the input equation.

## Limitations
This calculator program is very simple and does not support advanced mathematical operations or functions. It also has limited error handling and may crash if provided with invalid input.
