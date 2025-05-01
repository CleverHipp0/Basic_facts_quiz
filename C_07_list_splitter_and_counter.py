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


# Test list
my_list = ["-", "no", "close", "yes", "yes", "no", "no", "no", "no"]

# The 3 groups
group_1 = []
group_2 = []
group_3 = []

# How many groups to sort into (constant for testing)
questions_per_round = 3

# Splits the list per group

for item in range(0, questions_per_round):

    # group 1 starts at the beginning of the list
    group_1.append(my_list[item])
    # group 2 starts at were the first left off by adding how many per group
    group_2.append(my_list[item + questions_per_round])
    # group 2 starts at were the first left off by adding how many per group times 2
    group_3.append(my_list[item + questions_per_round * 2])

my_list_counted = count_list(my_list)
group_1_counted = count_list(group_1)
group_2_counted = count_list(group_2)
group_3_counted = count_list(group_3)

print(my_list)

print(group_1)
print(group_1_counted)


print(find_percentage(my_list_counted))
