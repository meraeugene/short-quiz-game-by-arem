print("Welcome to my quiz game")
game = input("Do you want to play? ")


if game.lower() != 'yes':
    quit()

score = 0

print("Let's play")
answer1 = input("What does RAM stands for? ")
if answer1.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer2 = input("What does CPU stands for? ")
if answer2.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer3 = input("What does TV stands for? ")
if answer3.lower() == "television":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer4 = input("1+1= ")
if answer4 == "2":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer5 = input("10-5= ")
if answer5 == "5":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print()
print(f"Congrats you got {score} correct answers")
print(f"You got {score/5 * 100}%")







