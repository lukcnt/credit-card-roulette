import random

# Take the names of everybody on the table.
names_string = input("Give me everybody's names, separated by a comma: ")

# Split string method.
names = names_string.split(",")

# The choice function of the random module was purposely not used for a better fixation of knowledge regarding indexes.
names_quantity = len(names)
names_index = names_quantity - 1
index_payer = random.randint(0, names_index)
payer_bill = names[index_payer]
print(f"{payer_bill} is going to buy the meal today!")