import random

print("Welcome to the number guessing game!\n")
print("So today I will be thinking of a number and I will tell the range of numbers and I want you to guess the number.")
print("If you guess the number correctly, you win the game.")
print("You have 5 chances to guess the number correctly.")

while True:
    try:
        number = int(input("Enter the range of numbers you want to guess from: ")) # this is the range of numbers between which the random number will be generated
        if number > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Please enter a valid number.")

random_number = random.randint(1, number) # this generates a random number between 1 and the number entered by the user

print(f"I have thought of a number between 1 and {number}.")

guesses = 0

while guesses < 5:
    try:
        guess = int(input("Guess the number: "))
        guesses += 1

        if guess < random_number:
            print("Your guess is too low.")
        elif guess > random_number:
            print("Your guess is too high.")
        elif guess == random_number:
            print(f"You win! The number was {random_number}.")
            print(f"You guessed the number in {guesses} tries.")
            break
    except ValueError:
        print("That is not a valid guess. Please enter a number.")

if guesses == 5 and guess != random_number:
    print(f"Sorry, you've used all your chances. The number was {random_number}.")
