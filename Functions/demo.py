# import random 

# def flipCoin() :
#     #generate random number
#     if random.random() <=0.5 :
#         print("Heads")
#     else :
#         print("Tails")

# while 1  :
#     flipCoin()
#     ans = input("Do you want to play again press y otherwise n")
#     if(ans=='n'):
#         break

#with parameter

# def squareNumber(num):
#     return num*num

# print(squareNumber(10))
# print(squareNumber(20))
# print(squareNumber(30))
# print(squareNumber(40))


#mistakes while returning
# indentation shoule be watched

# *args will be tuple in in function
# **kwargs will be list in function argunment

#unpacking

def allSums(*args) :   
    print(args)
    total = 0
    for num in args :
        total = total + num
    print(total)

# nums = (1,2,3,4,5,6)
nums = [1,2,3,4,5,6]
allSums(*nums) #if pass without star it will consider all the tuple or list as a one num ex ((1,2,3,4,5,6),)