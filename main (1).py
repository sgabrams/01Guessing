import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False
range = 100

while not quit:
    random_number = random.randint(1,range)
    count = 1
    number = -1
    while number != random_number:
        number = input("Pick a number between 1 and {}: ".format(range))
        if not number.isdigit():
            print("make sure to pick a real number")
        else:
            number = int(number)
            count = count +1
            print("Incorrect!")
            if number > random_number:
                print("Too high try again")
            elif number < random_number:
                print("Too low try again")
    print("You are correct")
    print("You guessed correctly in {} tries!".format(count))
    play_again = input("Try Again? (Yes or No?)")
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y":
        quit = False
    else:
        quit = True

print("Thanks for Playing")
