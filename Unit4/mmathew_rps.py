import random

#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    print("r = Rock \np = Paper \ns = Scissors")
    p1move = input("Pick from above [r|p|s]: ")
    if p1move == "r":
        return 'r'
    elif p1move == "p":
        return 'p'
    elif p1move == "s":  
        return 's'
#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    cmove = random.randint(1,3)
    if cmove == 1:
        return 'r'
    elif cmove == 2:
        return 'p'
    elif cmove == 3:
        return 's'

# for x in range(10):
#     print(get_comp_move())

#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    num_rounds = input("The numbers of rounds from 1 to 9: ")
    return int(num_rounds)
    
    
    

#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's a tie
def get_round_winner(p1move,cmove):
    if p1move == "r" and cmove == "p":
        return "Player Won"
    elif p1move == "p" and cmove == "r":
        return "Player Won"
    elif p1move == "r" and cmove == "s":
        return "Player Won"
    elif p1move == "s" and cmove == "r":
        return "Computer Won"
    elif p1move == "p" and cmove == "s":
        return "Computer Won"
    elif p1move == "s" and cmove == "p":
        return "Player Won"
    elif p1move == "s" and cmove == "s":
        return "tie"
    elif p1move == "r" and cmove == "r":
        return "tie"
    elif p1move == "p" and cmove == "p":
        return "tie"

#function name: get_full_move
#   arguments: a single letter move 'r','p', or 's'
#   purpose: returns the "full" word of a given move
#   returns: returns a string based on the following:
#               "Rock" if given "r"
#               "Paper" if given "p"
#               "Scissors" if given "s"
def get_full_move(shortmove):
    if shortmove == 'r':
        return "Rock"
    elif shortmove == 'p':
        return "Paper" 
    elif shortmove == 's':
        return "Scissors"

#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(pscore, cscore, ties):
    print ("You have {} points \nThe computer has {} points\nYou guys tied {} times".format(pscore, cscore, ties))
    pscore == int(pscore) 
    cscore == int(cscore) 
    ties == int(ties) 

#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps():
    pscore = 0
    cscore = 0
    ties = 0
    round = get_rounds()
    for x in range(round):
        player = get_p1_move()
        computer = get_comp_move()
        print("player score {}".format(get_full_move(player)))
        get_round_winner(player,computer)
        print("Computer score {}".format(get_full_move(computer)))
        winner = get_round_winner(player,computer)
        print(winner)
        if winner == "Player Won":
            print("Player 1 Wins the Round")
            pscore = pscore + 1
        elif winner == "Computer Won":
            print("Computer Wins the round")
            cscore = cscore + 1
        elif winner == "ties":  
            print("It was a tie")
            ties = ties + 1           
        print(pscore,cscore,ties)
    # player_score = 0
    # comp_score = 0
    # ties = 0
    # rounds = get_rounds()
    # for x in range(rounds):
    #     player_1 = get_p1_move()
    #     computer_1 = get_comp_move()
    #     winner = get_round_winner(player_1,computer_1)
    #     print(winner)
    #     if winner == "Player Won":
    #         player_score = player_score + 1
    #     elif winner == "Computer Won":
    #         comp_score = comp_score + 1
    #     elif winner == "tie":
    #         ties = ties + 1
    #     print_score(player_score, comp_score, ties)
        
    #     if player_score > rounds / 2:
    #         break
    #     elif comp_score > rounds / 2:
    #         break
    
    # if player_score > comp_score:
    #     print ("\nYOU WIN WITH {} POINTS".format(player_1))
    # elif comp_score > player_score:
    #     print ("\nYOU LOSS BY " + str(comp_score - player_score) + " POINTS!!!")
    # elif comp_score == player_score:
    #     print ("\nYOU TIED WITH THE COMPUTER!!!")
    
rps()