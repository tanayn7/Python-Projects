import random

def main():
    print("\n\t ---------- Welcome to Dice Game ------------ \n")
    player1 = input("Enter player 1 name : ")
    print("Hello , "+ player1)
    player2 = input("Enter player 2 name : ")
    print("Hello , "+ player2) 
    print("\nLet's start game.")
   
    
    rounds=0
    count_rounds_player1=0
    count_rounds_player2=0
    
    total_rounds = int(input("How many rounds you want to play : "))
    while rounds != total_rounds :
        player1_score = roll_dice()
        print("\nPlayer 1 score = " + str(player1_score))
        player2_score = roll_dice()
        print("Player 2 score = " + str(player2_score))
        
        if player1_score > player2_score :
            print("Winner : " + player1)
            count_rounds_player1 += 1
        elif player1_score < player2_score :
            print("Winner : " + player2)
            count_rounds_player2 += 1
        else :
            print("Winner : Draw")
        
        rounds = rounds + 1

    print("\033[1m" + '\n\nResult :')
    if (count_rounds_player1 > count_rounds_player2):
        print("\tCONGRATULATION!!!!!! " + player1 + " you won game.\n")
    elif (count_rounds_player1 < count_rounds_player2):
        print("\tCONGRATULATION!!!!!! " + player2 + " you won game.\n")
    else :
        print("\tSorryyy!!! " + "It's Draw.\n")
    
    print("Thank You For Playing!!!!!. Have a good day. See you soon.\n")
        



def roll_dice():
    dice = random.randint(1, 6)
    return dice

main()


