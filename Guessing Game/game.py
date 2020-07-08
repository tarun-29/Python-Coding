import random

randnum = random.randint(1,10);
guess = None
while randnum != guess :
    guess = input("Put one number between 1 to 10")
    guess = int(guess)
    if(guess<randnum):
        print("Too Low\n")
    elif(guess>randnum):
        print("Too High\n")
    else :
        print("You Won\n")
    
print(randnum)