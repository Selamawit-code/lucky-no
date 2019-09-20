import random 
number=random.randint(1,9)
guess=0
Try = 0

print( "good luck")

while guess!=number and guess!= "exit":
    guess = input("guess a number: ")
    
    if guess == "exit" :
        break 
    
    guess=int(guess)
    if guess > number:
        print("too high")

        print("to low")
    
    elif guess == number:
        print("YES, you got it. your lucky nummber is, %s." % number)
        if count < 3:
            print("excellent, only %s tries. " % Try)
        elif Try > 3 and Try < 10:
            print("good, %s tries." % Try)
        else:
            print("bad, more than %s tries." % Try)
    Try +=1
