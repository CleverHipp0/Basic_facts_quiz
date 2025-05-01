def count_list(list_to_count, to_count=("yes", "no", "close")):
    """Counts the amount of times items occur in a list"""

    # sets up a list for the response
    number_of_times = []

    # for every item in the list of things to find, add it to the response list
    for i in to_count:
        number_of_times.append(list_to_count.count(i))

    # Return the response list
    return number_of_times


def find_percentage(list_to_find, answers=("Correct", "Incorrect", "Close")):
    """Finds the percentage of items in a list"""

    for index, number in enumerate(list_to_find):

        # if the number of times an item occurs in a list is more than zero
        if number != 0:

            # finds the decimal
            number_decimal = number / sum(list_to_find)

            # finds fraction
            number_to_print = number_decimal * 100

            # rounds and prints it
            print(f"{answers[index]}: {number_to_print:.0f}%")

        # if the number of times an item occurs in a list is zero
        else:
            print(f"{answers[index]}: {number}")


def list_splitter(list_to_split, rounds_played, questions_per_round):
    """Splits list into sections and finds percentages"""

    round_stats = []

    for item in range(0, rounds_played):

        print(f"\nRound {item + 1}")

        for i in range(0, questions_per_round):
            # splits the list into the desired segments
            round_stats.append(list_to_split[item + i + 1])

        count = count_list(round_stats)
        find_percentage(count)
        round_stats.clear()


# Test list
my_list = ["yes", "no", "close", "yes", "yes", "no", "no", "no", "no"]

# How many groups to sort into (constant for testing)
list_splitter(my_list, 3, 3)
