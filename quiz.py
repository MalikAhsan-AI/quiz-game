highest_score = 0
question = 1
score = 0
print("welcome to the quiz competition")
print("today well ask you 10 questions related to science")
print("youll have 4 options and final score will be shown")
while question != 4:
    if question == 1:
        print("so this is your first question. Get ready")
        print("who was the scientist that discovered gravity")
        print("A.albert einstein")
        print("B.isac newton")
        print("C.galileo")
        print("D.charles darwin")
        while True:
            answer = input("enter either A,B,C,D").upper()
            if answer in ['A', 'B', 'C', 'D']:
                question += 1
                break
        else:
            print("wrong value input,try again")
        if answer == "B":
            print("good job right answer")
            score += 1
        else:
            print("wrong answer try again")
    elif question == 2:
        print("this is your second question")
        print("what is water made of")
        print("A.oxygen only")
        print("B.hydrogen only")
        print("C.salt and air")
        print("D.hydrogen and oxygen")
        while True:
            answer = input("enter either A,B,C,D").upper()
            if answer in ['A', 'B', 'C', 'D']:
                question += 1
                break
        else:
            print("wrong value input,try again")
        if answer == "D":
            print("good job right answer")
            score += 1
        else:
            print("wrong answer try again")
    elif question == 3:
        print("this is your third question")
        print("what do plants need to grow")
        print("A.moonlight")
        print("B.water sunlight and air")
        print("C.sand")
        print("D.plastic")
        while True:
            answer = input("enter either A,B,C,D").upper()
            if answer in ['A', 'B', 'C', 'D']:
                question += 1
                break
        else:
            print("wrong value input,try again")
        if answer == "B":
            print("good job right answer")
            score += 1
        else:
            print("wrong answer ")


print("your game has finished")
print(f"this is your score out of 3: {score}")
if score > highest_score:
    highest_score = score
print("congragulations ")
