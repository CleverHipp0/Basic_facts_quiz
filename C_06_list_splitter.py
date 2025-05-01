# Test list
my_list = ["apple", "banana", "pear", "burger", "sandwich", "wrap", "chicken", "pork", "lamb"]

# The 3 groups
fruit = []
lunch = []
meat = []

# How many groups to sort into (constant for testing)
questions_per_round = 3

# Splits the list per group
for item in range(0, questions_per_round):

    # group 1 starts at the beginning of the list
    fruit.append(my_list[item])
    # group 2 starts at were the first left off by adding how many per group
    lunch.append(my_list[item + questions_per_round])
    # group 2 starts at were the first left off by adding how many per group times 2
    meat.append(my_list[item + questions_per_round * 2])

print(my_list)
print(fruit)
print(lunch)
print(meat)

