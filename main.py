import random
number_list = list(range(1,101))
random_number = random.choice(number_list)

print("Disclaimer: **You will only have one chance to guess the number**")
num_guess = int(input("Guess the number: "))

if random_number == num_guess:
    print("You have guessed the number!")
elif random_number < num_guess:
    print("The number you have guessed is greater than the number chosen.")
else:
    print("The number you have guessed is less than the number chosen.")


