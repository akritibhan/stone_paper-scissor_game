import random
print("YOU ARE PLAYING WITH THE COMPUTER!")
def gamewin(comp,you):
    if comp==you:
        print("\n\nThe game is a tie!\n\n")
    elif comp=='stone':
        if you=='paper':
            print("\n\nCONGRATS! you win.Your paper wrapped the stone!\n\n")
        elif you=='scissor':
            print("\n\nOOPS! you lose.Your scissor has been hit hard by the stone !\n\n")
    elif comp=='paper':
        if you=='stone':
            print("\n\nOOPS! you lose. Paper wrapped up your stone!\n\n")
        elif you=='scissor':
            print("\n\nCONGRATS! you win.Your scissor has cut the paper.\n\n")
    elif comp=='scissor':
        if you=='paper':
            print("\n\nOOPS! you lose.The scissor has cut your paper\n\n")
        elif you=='stone':
            print("\n\nCONGRATS! you win. Your stone has hit the weak scissor!\n\n")

print("its computer's turn. The computer has chosen.")
randomno = random.randint(1,3)
if randomno==1:
    comp='stone'
elif randomno==2:
    comp='paper'
elif randomno==3:
    comp='scissor'

while True:
    you = input("Your turn : choose stone,paper or scissor? (enter nothing to stop)")
    if you=="":
        break
    gamewin(comp,you)

    print(f"Computer chose : {comp}")
    print("\n")
    print(f"You chose : {you}")
    print("\n")
    print('\n')
    print("lets play again\n")
