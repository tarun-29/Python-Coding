import random

randnum = random.randint(1,10);
guess = None
while 1 :
    guess = input("Put one number between 1 to 10")
    guess = int(guess)
    if(guess<randnum):
        print("Too Low\n")
    elif(guess>randnum):
        print("Too High\n")
    else :
        print("You Won\n")
        playAgain = input("If you want to play again press y otherwise n")
        if playAgain == 'y' :
            randnum = random.randint(1,10);
            guess = None
        else: 
            print("Thank You for playing")
            break
            
    
print(randnum)