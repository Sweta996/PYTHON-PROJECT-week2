winning_number = 43
guess = 1
game_over = False

while True:
    number = int(input("guess a number between 1 and 100 : "))
    if number == winning_number:
        print(f"you win, and you guessed this number in {guess} times ")
        break
        game_over = True
    else:
        if number < winning_number:
            print("too low ")
            guess += 1
            number = int(input("guess again : "))
        else :
            print("too high")
            guess += 1
            continue
