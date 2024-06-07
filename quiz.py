#for this we are to ask the use a bunch of questions and then give them a score based on their answers

print("Welcome to the quiz!")


playing = input("Do you want to play my quiz? answer yes or no: ")

if playing.lower() == "yes":
    print("Great! Let's play!")
else:
        print("That's too bad! Maybe next time!")
        quit()

score = 0

answer = input("What year was this code written? ")
if answer.lower() == "2024":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the name of the onwr of this code? ")
if answer.lower() == "enoch":
    print("Correct!")
    score += 1
else:
        print("Incorrect!")

answer = input("What is the name of the language used to write this code? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the name of the onwr of this code? ")
if answer.lower() == "enoch":
    print("Correct!")
    score += 1
else:
        print("Incorrect!")

answer = input("what is the enoch's favorite color? ")
if answer.lower() == "blue":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("your total score is " + str(score))