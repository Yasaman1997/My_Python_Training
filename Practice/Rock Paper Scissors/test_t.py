import  sys


user1=input("what's your name?")
user2=input("and yours?")

user1_ans=input("%s ,rock, paper or scissors?" %user1)
user2_ans=input("%s ,rock, paper or scissors?" %user2)

def compare(u1,u2):
    if u1 == u2:
        return ("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return ("Rock wins!")
        else:
            return ("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return ("Scissors win!")
        else:
            return ("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return ("Paper wins!")
        else:
            return ("Scissors win!")
    else:
        return ("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()


print(compare(user1_ans,user2_ans))
