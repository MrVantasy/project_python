import time
import random

print("\nNumber Guessing\n")
time.sleep(1)

while True:
    valid = int(input("Press 1 for ready! "))
    if valid == 1:
        time.sleep(0.5)
        num = random.randrange(1, 10)
        while True:
            num_guess = int(input("Any Guess? "))
            if num_guess == num:
                time.sleep(0.75)
                print("Wow, you're so good at guessing!")
                break
            else: 
                time.sleep(0.75)
                print("Try again!\n")
        break
    else:
        time.sleep(0.5)
        print("You have to be ready!\n")