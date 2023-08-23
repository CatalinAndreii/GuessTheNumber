import random

AI = random.randint(1, 10)
run = True

while run:
    player = int(input("Guess the number: "))

    if player == AI:
        print("Correct")
        run = False
    elif player > AI:
        print("Less")
    elif player < AI:
        print("More")


