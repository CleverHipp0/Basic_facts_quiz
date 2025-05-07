import random


def statement_generator(decoration, decoration_time, statement):
    """Makes a statement fancy by adding decorative characters"""

    print(f"{decoration * decoration_time} {statement} {decoration * decoration_time}")


def calculate(level, random_low, random_high):
    """does the equation"""

    # Sets up numbers
    a = random.randint(random_low, random_high)
    b = random.randint(random_low, random_high)
    c = random.randint(random_low, random_high)

    # Stopped me from getting a yellow line
    answer = 0

    if level != 6:
        operation_style = level

    else:
        operation_style = random.randint(6, 7)

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
    elif operation_style == 6:
        equation = f"{a} + {b} * {c}"

    # Legendary P:2
    else:
        equation = f"{a} - {b} * {c}"

    # Solves the equation to find the answer unless it is doing division as that ia already done
    if operation_style != 4:
        answer = eval(equation)

    # Prints the equation and answer
    print(f"{equation} = ")

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


def cal_lives(answer, modifier, current_lives):
    """Finds the correct amount of lives to add or subtract"""
    # If the user got it right, and it is a healing round, +1 life
    if answer == "yes" and modifier == "🔼❤️🔼 Healing Round 🔼❤️🔼" and current_lives != 3:
        change_in_lives = 1

    # If the user got it close, and it is a double damage round, -1 life
    elif answer == "close" and modifier == "🔼⚔️🔼 Double Damage 🔼⚔️🔼":
        change_in_lives = -1

    # If the user got it wrong, and it is a double damage round, -2 life
    elif answer == "no" and modifier == "🔼⚔️🔼 Double Damage 🔼⚔️🔼":
        change_in_lives = -2

    # If the user got it wrong, and it is a normal round, -1 life
    elif answer == "no" and modifier != "🔼⚔️🔼 Double Damage 🔼⚔️🔼":
        change_in_lives = -1

    # If it is a normal round and the user got it close or correct, don't change lives
    else:
        change_in_lives = 0

    return change_in_lives


def find_percentage(list_to_find, answers=("Correct", "Incorrect", "Close")):
    """Finds the percentage of items in a list"""

    for index, number in enumerate(list_to_find):

        # if the number of times an item occurs in a list is more than zero
        if number != 0:

            # finds the decimal by dividing by the
            number_decimal = number / sum(list_to_find)

            # finds percentage by multiplying by 100
            number_to_print = number_decimal * 100

            # rounds and prints it
            print(f"{answers[index]}: {number_to_print:.0f}%")

        # if the number of times an item occurs in a list is zero
        else:
            print(f"{answers[index]}: {number}")


def count_list(list_to_count, to_count=("yes", "no", "close")):
    """Counts the amount of times items occur in a list"""

    # sets up a list for the response
    number_of_times = []

    # for every item in the list of things to find, add it to the response list
    for i in to_count:
        number_of_times.append(list_to_count.count(i))

    # Return the response list
    return number_of_times


def list_splitter(list_to_split, rounds_played, questions_per_round, name_list=None):
    """Splits list into sections and finds percentages"""

    # clears the list
    round_stats = []

    # cycles through levels
    for up_to_level in range(0, rounds_played):

        # shows the level
        if name_list is not None:
            print(f"\nLevel {name_list[up_to_level]}")

        else:
            print(f"\nLevel {up_to_level + 1}")

        # cycles through questions
        for i in range(0, questions_per_round):

            # splits the list into the desired segments
            round_stats.append(list_to_split[(up_to_level * 2) + i])

        # does the counting
        count = count_list(round_stats)

        # finds the percentages
        find_percentage(count)

        # clears the list
        round_stats.clear()


# Main routine
# TITLE
statement_generator("🔮", 3, "Magic Maths Quiz")
print()

# Asks the user if they want instructions
want_instructions = yes_no("Do you want instructions? ")

# If they do want the instructions then print them
if want_instructions == "yes":
    print()
    statement_generator("🧾", 3, "Instructions")
    print('''
1. You will be granted 3 lives
2. Answer questions correctly to keep your lives
3. if you are close only half a life will be deducted
4. If you are incorrect a whole life will be deducted
5. You will re-gain one life at the beginning of each level

            |   Good luck maths wizard  |
    ''')

# asks how many questions the user wants to answer per round
questions = int_check("How many Questions per round? ", 1)

# Set the lives to 3
lives = 3

# set up power ups
round_power_ups = ["🔼❤️🔼 Healing Round 🔼❤️🔼", "🔼⚔️🔼 Double Damage 🔼⚔️🔼", "🏰 Normal Round 🏰"]

# set history
history = []

# sets rounds played to 0
levels_played = 0

# sets level names
level_names = ["Easy Peasy", "Easy", "Medium", "Hard", "Legendary"]

# loops for the 5 levels
for current_level in range(1, 6):

    if current_level == 3 or current_level == 4:
        # Changes the range to get half a life taken away
        close_range = 3

    elif current_level == 5:

        # Changes the range to get half a life taken away
        close_range = 0

    else:
        # Changes the range to get half a life taken away
        close_range = 5

    # Prints the correct heading, uses -1 because the list starts a 0
    print()
    statement_generator("🚩", 3, level_names[current_level - 1])

    # Sets up the questions asked
    questions_asked = 0

    # Sets up an emergency exit if the user enters "xxx"
    emergency_exit = "no"

    # Loops until it has asked the desired amount of questions
    while questions_asked != questions and lives > 0:

        # Shows the user their lives at the beginning of each round
        print(f"Lives: ", lives * "❤️")

        # Picks the type of round randomly has a 1 in 10 chance of being a healing or double damage round
        # counting from zero makes it easier to select the power up meaning i need to subtract 1 from the to number
        round_type = random.randint(0, 10 - 1)

        if round_type == 0:
            # sets up the type of round as a healing round
            power_up = round_power_ups[round_type]

        elif round_type == 1:
            # sets up the type of round as a double damage round
            power_up = round_power_ups[round_type]

        else:
            # sets up the type of round as a normal round
            power_up = round_power_ups[2]

        print(power_up)
        correct_answer = calculate(current_level, 1, 10)
        user_answer = int_check("Answer? ")

        if user_answer == "xxx":
            # An emergency exit incase the user wants to quit
            emergency_exit = "yes"
            user_correct = "-"
            break

        elif user_answer == correct_answer:
            statement_generator("!", 3, "CORRECT")
            # Stores the status of the answer that the user gave to be used in lives and stats
            user_correct = "yes"

        elif correct_answer in range(user_answer - 5, user_answer + 5) and user_answer != correct_answer:
            statement_generator("!", 3, "SO CLOSE")
            # Stores the status of the answer that the user gave to be used in lives and stats
            user_correct = "close"
            # Prints the correct answer
            print(correct_answer)

        else:
            statement_generator("-", 3, "INCORRECT")
            # Stores the status of the answer that the user gave to be used in lives and stats
            user_correct = "no"
            # Prints the correct answer
            print(f"The correct answer was {correct_answer}")

        # adds spacing
        print()

        # adds the response to the history list
        history.append(user_correct)

        # calculates whether any lives need to be deducted or added
        lives += cal_lives(user_correct, power_up, lives)

        # adds 1 to the counter
        questions_asked += 1

    # exits the loop if the exit code is entered, or they die.
    if emergency_exit == "yes" or lives <= 0:
        levels_played = current_level
        break


# Makes sure the length of the list is compatible as if they don't finish the round it will break
if len(history) != levels_played * questions:

    # finds the amount of blanks to add (probably a better way)
    for n in range((levels_played * questions) - len(history)):

        # adds blanks
        history.append("-")

# asks if the user wants to see the stats
see_stats = yes_no("Do you want to see your statistics? ")

# if the user wants to see the stats show them if the user played any rounds
if see_stats == "yes" and len(history) != 0:

    # heading
    statement_generator("📊", 3, "Statistics")
    print()

    # sub heading
    print("Overall: ")

    # finds the overall percentage of correct incorrect and close responses
    find_percentage(count_list(history))
    print()

    # asks the user if they want to see the stats for every round
    see_stat_advanced = yes_no("Do you want to see your statistics for every round? ")

    # calculates each rounds statistics
    if see_stat_advanced == "yes" and levels_played != 0:
        # calculates the statistics for each round
        list_splitter(history, levels_played, questions)

    elif see_stat_advanced == "yes" and levels_played == 0:
        # max number of rounds is 5, calculates the statistics for each round
        list_splitter(history, 5, questions)

    else:
        # catch all error
        print("Error")

else:
    # if the user didn't play any rounds tell them so
    statement_generator("🐔", 3, "You played 0 rounds")
