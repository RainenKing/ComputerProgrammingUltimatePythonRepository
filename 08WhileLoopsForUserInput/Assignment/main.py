import random

#number = random.randint(0,10)
#response = int(input("enter a number"))
#while response < number:
    #print("to low")
    #response = int(input("enter a number"))
#while response > number:
    #print("to high")
#    response = int(input("enter a number"))
#else:
#    print("correct")


#number = random.randint(0,10)
#lives = 2
#response = int(input("enter a number"))
#while response < number and lives > 0:
#    print(lives, "lives, to low")
#    response = int(input("enter a number"))
#    lives = lives - 1
#while response > number and lives > 0:
#    print(lives, "lives, to high")
#    response = int(input("enter a number"))
#    lives = lives - 1


#if lives == 0:
#   print("out of lives you lose")
#else:
#    print("correct")



number = 50
print(number)
Total = True
while Total == True:
    amount_entered = int(input("enter your coins only 5, 10, and 25 cents"))
    if amount_entered != 10 and amount_entered != 5 and amount_entered != 25:
        print("invalid amount entered")
        Total = False
    elif number > 0:
        amount_entered == 10 and amount_entered == 5 and amount_entered == 25
        Total = True
        sub_amount = number - amount_entered
        number = sub_amount
        print(number)
    else:
        number == 0
        Total = False
        print("total due paid")
