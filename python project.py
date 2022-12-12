import random

lower = int(input("Enter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))


# generating random number between
x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(3),
      " chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < (3):
    count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count <= (3):
    print("\nThe number is %d" % x)
    print("\tGame Over")
