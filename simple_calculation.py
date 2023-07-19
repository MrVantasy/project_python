import time

print("\nQUIZZ!\n")
time.sleep(1)

print("1. What's the result of 5 + 5?")
ans_1 = int(input("Input your answer: "))
time.sleep(0.75)
if ans_1 == 10:
    print("You're correct!\n")
    ans_1 = 1
else:
    print("You're incorrect!\n")
    ans_1 = 0

print("2. What's the x of 4 < x < 7? ")
ans_2 = int(input("Input your answer: "))
time.sleep(0.75)
if ans_2 == 5 or 6:
    print("You're correct!\n")
    ans_2 = 1
else:
    print("You're incorrect!\n")
    ans_2 = 1

time.sleep(0.75)

ans = ans_1 + ans_2
if ans == 2:
    print("You're so good at this!")
elif ans == 1:
    print("Nice Try!")
else:
    print("It's okay!")