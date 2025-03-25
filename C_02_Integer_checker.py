def int_check(question, low=None):
    """Checks for a number more than 0, accepts <enter> for infinite"""

    # Sets up an error message
    if low is not None:
        error = f"Please enter an whole number larger than {low} or <xxx>."

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


number = "a"

while number != "xxx":
    number = int_check("Number to check: ")
    print(number)

