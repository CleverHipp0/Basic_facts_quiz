def statement_generator(decoration, decoration_time, statement):
    """Makes a statement fancy by adding decorative characters"""

    print(f"\n{decoration * decoration_time} {statement} {decoration * decoration_time}\n")


def yes_no(question):
    """Input question, out put whether they said yes or no"""
    while True:

        # Asks a yes or no question
        yes_no_raw = input(question).lower()

        # acceptable answers in lists
        yes_acceptable = ("yes", "y")
        no_acceptable = ("no", "n")

        # Checks the list to see if it's an acceptable answer and returns it
        if yes_no_raw in yes_acceptable:
            return yes_acceptable[0]

        elif yes_no_raw in no_acceptable:
            return no_acceptable[0]

        else:
            print("That is not an acceptable answer. Please answer with <yes> or <no>.")


# Main routine goes here
# Asks if the user wants the instructions
want_instructions = yes_no("Do you want instructions? ")

# If they do want the instructions then print them
if want_instructions == "yes":
    statement_generator("🧾", 3, "Instructions")
    print('''1. You will be granted 3 lives
2. Answer questions correctly to keep your lives
3. if you are close only half a life will be deducted
4. If you are incorrect a whole life will be deducted
5. You will re-gain one life at the beginning of each level

            |   Good luck maths wizard  |
    ''')
