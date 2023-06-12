name = input("Type your name : ")
print("welcome", name, "to this adventure")

answer = input(
    "You have come to an end , you can go left or right , which way you want to go ? :"
).lower()

if answer == "left":
    answer = input(
        "you come to a river, you can walk around it or you can swim , type walk to walk around or swim to swin across ? "
    ).lower()

    if answer == "swim":
        print("you swan across and were eaten by alligator :(")
    elif answer == "walk":
        print("You walked for many miles and you ran out of water and lost!!")
    else:
        print("Not a valid option ")

elif answer == "right":
    print("You come to a bridge , it looks wobbly, do want to cross it or head back ? ")

    if answer == "back":
        print("you go back and lose.")
    elif answer == "cross":
        print(
            "you cross the bridge and meet the stranger, do want to talk to them Yes/No ?"
        )

        if answer == "Yes":
            print("You talk to stranger and they give you gold .. You WON!!")
        elif answer == "No":
            print("you ign the stranger and they killed you :(")
        else:
            print("Not a valid line")
else:
    print("Not a valid line")
