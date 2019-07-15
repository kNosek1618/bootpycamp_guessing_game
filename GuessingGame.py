
from random import randint
answer = None
quest = None

number = randint(1, 10)
print(number)

while True:
    answer = input(("write the nymber between 1 and 10: "))
    answer = int(answer)
    if number > answer:
        print("to low")
    elif number < answer:
        print("to high")
    else:
        print("Well done, you guys.")
        quest = input("Do you want to play again? (y/n) ")
        if quest == "y":
            number = None
            number = randint(1, 10)
        if quest == "n":
            print("thanks for that you played!")
            break
