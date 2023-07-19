import random
import time

print("")
print("DICE GAMES!\n")
time.sleep(1)

while True:
    input("Your Turn! Please press enter! ")
    me = random.randint(1, 6)
    time.sleep(0.5)
    print("Now, it's Bot Turn!")
    bot = random.randint(1,6)
    
    time.sleep(0.75)
    
    if me > bot:
        print("You win!")
    elif me < bot:
        print("You lose!")
    else:
        print("Draw!")
    
    valid = int(input("Press 1 for Continue! "))
    if valid == 1:
        continue
    else:
        break

time.sleep(0.5)
print("")
print("Thank You For Playing!")

