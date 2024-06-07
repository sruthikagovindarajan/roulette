import random

check_list = [i for i in range(1, 37)]
red, black = list(), list()
even=0

for i in range(10):
    if(i%2==0):
        red.append(check_list[i])
    else:
        black.append(check_list[i])
for i in range(18,28,1):
    if(i%2==0):
        red.append(check_list[i])
    else:
        black.append(check_list[i])
for i in range(10,18,1):
    if(i%2==0):
        black.append(check_list[i])
    else:
        red.append(check_list[i])
for i in range(28,36,1):
     if(i%2==0):
        black.append(check_list[i])
     else:
        red.append(check_list[i])
red.sort()
black.sort()


def Manque(bet,c,total):
    a =c
    if a>0 and a<19:
        print("YOU'VE WON THE BET!\n")
        print("RETURN = $" + str(computeReturn(bet)))
        total=computeReturn(bet)+total
        print("Your total=",total)
        
    else:
        print("YOU'VE LOST!\n")
        print("You have lost $" + str(loss(bet)))
        total=total-(loss(bet))
        print("Your total=",total)
    return total

def Passe(bet, c,total):
    a=c;
    if a>19 and a<37: 
        print("YOU'VE WON THE BET!\n")
        print("RETURN = $" + str(computeReturn(bet)))
        total=computeReturn(bet)+total
        print("Your total=",total)
    else:
        print("YOU'VE LOST!\n")
        print("You have lost $" + str(loss(bet)))
        total=total-(loss(bet))
        print("Your total=",total)
    return total

def Rouge(bet,c, total):
    a = c
    if a in red:
        print("YOU'VE WON THE BET!\n")
        print("RETURN = $" + str(computeReturn(bet)))
        total = total + computeReturn(bet)
        print("Your total=",total)
    else:
        print("YOU'VE LOST!\n")
        print("You have lost $" + str(loss(bet)))
        total=total-(loss(bet))
        print("Your total=",total)
    return total

def Noir(bet,c, total):
    a = c
    if a in black:
        print("YOU'VE WON THE BET!\n")
        print("RETURN = $" + str(computeReturn(bet)))
        total=computeReturn(bet)+total
        print("Your total=",total)
    else:
        print("YOU'VE LOST!\n")
        print("You have lost $" + str(loss(bet)))
        total=total-(loss(bet))
        print("Your total=",total)
    return total

def returnRandomNumber():
    return random.choice(check_list)

def computeReturn(bet):
    return (bet*2)

def Pair(bet, c,total):
    a = c
    if a%2 == 0:
        print("YOU'VE WON THE BET!\n")
        print("RETURN = $" + str(computeReturn(bet)))
        total=computeReturn(bet)+total
        print("Your total=",total)
    else:
        print("YOU'VE LOST!\n")
        print("You have lost $" + str(loss(bet)))
        total=total-(loss(bet))
        print("Your total=",total)
    return total

def Impair(bet, c,total):
    a = c
    if a%2!=0:
        print("YOU'VE WON THE BET!\n")
        print("RETURN = $" + str(computeReturn(bet)))
        total=computeReturn(bet)+total
        print("Your total=",total)
    else:
        print("YOU'VE LOST!\n")
        print("You have lost $" + str(loss(bet)))
        total=total-(loss(bet))
        print("Your total=",total)
    return total
 
def ball():
    n=returnRandomNumber()
    print("The ball landed in",n)
    return n;

def loss(bet):
    return(bet/2)

def initiate():
    choice = 0
    total = 0
    c=0;
    print("                                 THE ROULETTE\n")
    print("Welcome to the Roulette")
    print("Minimum bet:$5  Maximum bet:$1000")
    print("__________\n| 1| 2| 3|\n__________\n| 4| 5| 6|\n__________\n| 7| 8| 9|\n__________\n|10|11|12|\n__________\n|13|14|15|\n__________\n|16|17|18|\n__________\n|19|20|21|\n__________\n|22|23|24|\n__________\n|25|26|27|\n__________\n|28|29|30|\n__________\n|31|32|33|\n__________\n|34|35|36|\n__________")

    while(choice < 7):
        choice = int(input('\n\nPick one of the outside bets:\n1.Manque(1-18)\n2.Passe(19-36)\n3.Rouge\n4.Noir\n5.Pair\n6.Impair\n7.Exit the game\n\n'))
        if choice == 7:
            print("You have a total of",total,"\nThank you for playing!\n\n")
            break
        
        bet = int(input("\n\nPlace bet : "))
        if bet>5 and bet<1000:
            
            if choice == 1:
                total=bet
                c=ball()
                total = Manque(bet,c, total)
        
            elif choice == 2:
                c=ball()
                total = Passe(bet,c, total)
    
            elif choice == 3:
                c=ball()
                total = Rouge(bet,c, total)
    
            elif choice == 4:
                c=ball()
                total = Noir(bet,c, total)
    
            elif choice == 5:
                c=ball()
                total = Pair(bet,c, total)
    
            elif choice == 6:
                c=ball()
                total = Impair(bet,c, total)
    
            else:
                break
        
        else:
            print("Bet again!\n\n")
            continue
        

initiate()
