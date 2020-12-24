import random
print("YOU ARE PLAYING WITH THE COMPUTER!")
def gamewin(comp,you):
    if comp==you:
        print("The game is a tie!")
    elif comp=='stone':
        if you=='paper':
            print("CONGRATS! you win.Your paper wrapped the stone!")
        elif you=='scissor':
            print("OOPS! you lose.Your scissor has been hit hard by the stone !")
    elif comp=='paper':
        if you=='stone':
            print("OOPS! you lose. Paper wrapped up your stone!")
        elif you=='scissor':
            print("CONGRATS! you win.Your scissor has cut the paper.")
    elif comp=='scissor':
        if you=='paper':
            print("OOPS! you lose.The scissor has cut your paper")
        elif you=='stone':
            print("CONGRATS! you win. Your stone has hit the weak scissor!")

print("its computer's turn. The computer has chosen.")
randomno = random.randint(1,3)
if randomno==1:
    comp='stone'
elif randomno==2:
    comp='paper'
elif randomno==3:
    comp='scissor'


you = input("Your turn : choose stone,paper or scissor? ")

a=gamewin(comp,you)

print(f"Computer chose : {comp}")
print(f"You chose : {you}")

