dict = {
    "what does PSU stand for?" : "power supply",
    "what does RAM stand for?" : "random access memory",
    "What does CPU stand for? " : "central processing unit",
    "what does GPU stand for?" : "graphics processing unit",
}
def game():
    score = 0
    for k,v in dict.items():
        print(k)
        answer = input()
        if answer.lower() == v:
            print("correct")
            score += 1
        else:
            print("incorrect the answer is",v)
    return score

print("Welcome to my computer quizz !")
playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = game()
print("You got " + str(score)+ " questions correct !")
print("You got " + str((score/4)*100)+ " %.")

"""
        begineer version

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("what does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("what does RAM stand for?")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("what does PSU stand for?")
if answer.lower() == "power supply":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
"""






