import random
secret_number = random.randint(1, 10)
print("I am thinking of a number between 1 and 10.")
while True:
    x = input("What is the number?: ")
    if int(x) < 5:
        print(str(x) + " is too low.")
    if int(x) > 5:
        print(str(x) + " is too high.")
    if int(x) == secret_number:
        print ("Yes! You Win!")
        break

y = Y 
n = N
answer = input("Do you want to play again (y or n): ")
    if answer == y:
        
