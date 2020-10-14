def printTitle():
    return('*************************\n * WELCOME TO REDDOG   *\n*************************')

def reddog():
    def displayCard():
        import random
        random.seed() # generate a new random seed each time the program is run
        a=((random.randint(1,13))) # pick a number between 1 and 13 (Ace to King)
        x = {1:'A', 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:'J', 12:'Q', 13:'K'}
        return x[a]
    
    def swapGreater(card1,card2): 
        card1,card2 = card2,card1 # Swaps the value of card1 and card2
        return card1,card2
        
    bank = 5000
    bet = int(input('Enter your bet: '))
    while bet > bank or bet <=0:
        print('Invalid bet. Please reenter.', end='')
        bet = int(input('Enter your bet: '))
    card1 = displayCard()
    print('Card 1:', card1)
    
    card2 = displayCard()
    print('Card 2:', card2)
    
    a = {'A':1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':11, 'Q':12, 'K':13}
    card1 = a[card1] # turn into int
    card2 = a[card2] # turn into int
    if card1 > card2: 
        (card1, card2) = swapGreater(card1,card2) # swap cards so that card2 is always bigger than card1
    if card2-card1 == 1:
        print('We push.')
        return bank
    elif card2==card1:
        card3 = displayCard()
        print('Card 3:', card3)
        card3 = a[card3]
        if card3==card2:
            bank += 11*bet
            return bank
        else:
            print('We push.')
            return bank
    else:
        if card2-card1 == 2:
            spread = 5
        elif card2-card1 == 3:
            spread = 4
        elif card2-card1 == 4:
            spread = 2
        else:
            spread = 1
        print('Spread is: ', spread, '-1', sep='')
        card3 = displayCard()
        print('Card 3:', card3)
        card3 = a[card3]
        if card1 <= card3 <= card2 or card2 <= card3 <= card1: # Check if card3 is in between or equal to card1 and card2
            print('You win!')
            bank += spread * bet
            return bank
        else:
            print('You lose!')
            bank -= bet
            return bank
        
# Main program starts here
title = printTitle()
print(title) 
play = 'y' # Sentinel for while loop
bank = 5000  
while play == 'y':
    print('You have $', bank, '.', sep= '', end='') 
    bank = reddog()
    print('You have $', bank, '.', sep= '', end='')
    if bank == 0:
        print('\nGAME OVER')
        break
    play = input('Play again (y/n):')

