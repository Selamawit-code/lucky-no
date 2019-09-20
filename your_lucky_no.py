import random 
number=random.randint(1,9)
guess=0
count = 0

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
            print("excellent, only %s tries. " % count)
        elif count > 3 and count < 10:
            print("good, %s tries." % count)
        else:
            print("bad, more than %s tries." % count)
    count +=1