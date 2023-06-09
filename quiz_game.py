print("welcome to quiz game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay let's play :)")

score = 0

answer = input("Why are You here? ")
if answer.lower() == "idk":
    print("correct")
    score += 1
else:
    print("That's incorrect")

answer = input("what is your Name? ")
if answer.lower() == "funny":
    print("correct")
    score += 1
else:
    print("That's incorrect")


print("you got " + str(score) + " question correct")
print("you got " + str((score / 2) * 100) + "%")
