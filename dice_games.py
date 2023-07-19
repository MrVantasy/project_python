import random
import time

print("")
print("DICE GAMES!\n")
time.sleep(1)

me_score = 0
bot_score = 0

while True:
    input("Your Turn! Please press enter! ")
    me = random.randint(1, 6)
    time.sleep(0.5)
    me_value = print(f"You rolled {me}.")
    time.sleep(0.2)
    print("Now, it's Bot Turn!")
    bot = random.randint(1,6)
    time.sleep(0.5)
    bot_value = print(f"Bot rolled {bot}.")
    
    time.sleep(1.5)
    
    if me > bot:
        print("You win!")
        me_score = me_score + 1
    elif me < bot:
        print("You lose!")
        bot_score = bot_score + 1
    else:
        print("Draw!")
    
    valid = int(input("Press 1 for Continue or 2 for Done! "))
    if valid == 1:
        continue
    else:
        print(f"\nYour score is {me_score} and the bot score is {bot_score}")
        break

time.sleep(0.5)
print("Thank You For Playing!")

