
from random import randint
answer = None

number = randint(1, 10)
print(number)

while True:
    answer = input(("write the nymber between 1 and 9: "))
    answer = int(answer)
    if number > answer:
        print("to low")
    elif number < answer:
        print("to high")
    else:
        print("Well done, you guys.")
        break
