import random


def calculate(level, random_low, random_high, numbers_3="no"):
    """does the equation"""

    # Sets up numbers
    a = random.randint(random_low, random_high)
    b = random.randint(random_low, random_high)
    c = random.randint(random_low, random_high)

    # Stopped me from getting a yellow line
    answer = 0

    operation_style = random.randint(1, level)

    # Forms the equations based on difficulty
    # Easy Peasy
    if operation_style == 1:

        equation = f"{a} + {b}"

    # Easy
    elif operation_style == 2:
        equation = f"{a} - {b}"

    # Medium
    elif operation_style == 3:
        equation = f"{a} * {b}"

    # Hard
    elif operation_style == 4:
        # Works the equation backwards so it always gets an integer
        c = a * b
        equation = f"{c} / {b}"

        # Sets the answer as we already know it
        answer = a

    # Legendary P:1
    elif operation_style == 5:
        equation = f"{a} + {b} * {c}"

    # Legendary P:2
    else:
        equation = f"{a} - {b} * {c}"

    # Solves the equation to find the answer unless it is doing division as that ia already done
    if operation_style != 4:
        answer = eval(equation)

    # Prints the equation and answer
    print(f"{equation} = {answer}")

    # Returns the answer
    return answer


def int_check(question, low=None):
    """Checks for a number more than 0, accepts <enter> for infinite"""

    # Sets up an error message
    if low is not None:
        error = f"Please enter an whole number larger than {low - 1} or <xxx>."

    else:
        error = f"Please enter an whole number or <xxx>."

    while True:

        # Asks the question
        answer = input(question)

        # Returns if they input <xxx>
        if answer == "xxx":
            return answer

        # Checks to see if they entered an integer
        try:
            answer = int(answer)

            # If there is a low print an error if the answer is smaller
            if low is not None and answer < low:
                print(error)

            else:
                return answer

        # If an integer was not inputted it will print the error
        except ValueError:

            print(error)


# Main routine
# For testing
current_level = int_check("Level: ")
correct_answer = calculate(current_level, 1, 10)
user_answer = int_check("Answer? ")

if user_answer == correct_answer:
    # Replace with statement generator
    print("CORRECT!!!!")

elif correct_answer in range(user_answer - 5, user_answer + 5) and user_answer != correct_answer:
    # Replace with statement generator
    print("SO CLOSE!!!!")
    # Prints the correct answer
    print(correct_answer)

else:
    # Replace with statement generator
    print("---INCORRECT---")
    # Prints the correct answer
    print(correct_answer)

