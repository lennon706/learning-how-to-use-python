import random
number = random.randint(1, 100)
count = 0
# print(number)
mode = ""
while mode != "E" and mode != "H":
    mode = input("which mode do you want: E for easy H for hard: "). upper ()
    if mode == "E":
        max_guesses = 10
else:
    max_guesses = 5
guess = int(input("guess the number: "))
while guess != number and count < 10:
    count += 1
    if guess < number:
        guess = int(input("to low try again: "))
    else:
        guess = int(input("to high try again: "))
if guess == number:
        print("you got it in", {count}, "guesses!")
else:
    print("you couldnt get it")
