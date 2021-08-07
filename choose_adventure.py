name = input("Type your name: ")
print("Welcome", name,"to this adventure")

answer = input("you are on a dirt road, it has come to an end and you can go left or right. Which way would like to go? ").lower()

if answer == "left":
    answer = input("you com to a river, you can walk auround it or swim accross ? Type walk to walk around and swim to swim accross: ")
    if answer == "swim":
        print("you swim accross and were eaten by an alligator")
    elif answer == "walk":
        print("you walked for many miles, run out of water and you lost the game.")
    else:
        print("not a valid option. You lose")
elif answer =="right":
    answer = input("you come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back)")
    if answer == "back":
        print("you go back and lose ")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer=="yes":
            print("you talk to the stranger and they give you gold . You WIN")
        elif answer=="no":
            print("you ignore the stranger and they are offended and you lose")
        else:
            print("not a valid option. You lose")
    else:
        print("not a valid option. You lose")
    print()
else: 
    print("not a valid option. You lose")

print("thank you for trying",name)