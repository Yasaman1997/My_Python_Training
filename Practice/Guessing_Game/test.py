import random

number =random.randint(1,9)
guess=0
count=0


while guess !=number and guess!="exit":
    guess=input("What is your guess?")

    if guess=="exit":
        break


    guess=int(guess)
    count+=1


    if guess<number:
      print "too low!"

    elif  guess>number:
     print "Too high!"

    else:
         print "that is it!"

         print "it only took you",count,"tries!"
exit(3)