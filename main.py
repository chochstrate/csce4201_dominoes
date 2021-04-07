#from func import *
from array import *
import random
import math
import re

# Below minimax code from https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/?ref=rp

# Initial values of Alpha and Beta 
MAX, MIN = 1000, -1000 
  
# Returns optimal value for current player 
#(Initially called for root and maximizer) 
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta): 
    # Terminating condition. i.e leaf node is reached 
    if depth == 3: 
        return values[nodeIndex] 
    if maximizingPlayer: 
        best = MIN 
        # Recur for left and right children 
        for i in range(0, 2): 
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta) 
            best = max(best, val) 
            alpha = max(alpha, best) 
            # Alpha Beta Pruning 
            if beta <= alpha: 
                break 
        return best 
    else:
        best = MAX 
        # Recur for left and 
        # right children 
        for i in range(0, 2): 
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta) 
            best = min(best, val) 
            beta = min(beta, best) 
            # Alpha Beta Pruning 
            if beta <= alpha: 
                break 
        return best

def play(userInput):
    global doublePlayed
    global double
    global doubleSpots
    global turn
    global aiHandSize
    global player1HandSize
    global player2HandSize
    global player3HandSize
    global player4HandSize
    global player5HandSize
    global player6HandSize
    global player7HandSize
    global chickenYardAmount

    playedDomino = userInput.split(" ")
    if playedDomino[1] > playedDomino[2]:
        playedTemp = playedDomino[1]
        playedDomino[1] = playedDomino[2]
        playedDomino[2] = playedTemp

    if doublePlayed == True:
        if totalPlayed[double] > 10 and doubleSpots == 3:
            print("There are not enough", double,"'s left to complete the double, auto-drawing the remainder of the chicken yard")
            while chickenYardAmount > 0:
                draw()
            blockCheck = numPlayers + 1
        elif int(playedDomino[1]) == double:
            spotsPlayable[double] = spotsPlayable[double] - 1
            spotsPlayable[int(playedDomino[2])] = spotsPlayable[int(playedDomino[2])] + 1
            totalPlayed[double] = totalPlayed[double] + 1
            totalPlayed[int(playedDomino[2])] = totalPlayed[int(playedDomino[2])] + 1
            played[int(playedDomino[1])][int(playedDomino[2])] = 1
            doubleSpots = doubleSpots - 1
            blockCheck = 0
            if turn == 0:
                player1[int(playedDomino[1])][int(playedDomino[2])] = 0
                player1HandSize = player1HandSize - 1
                turn = 1
            elif numPlayers > 1 and turn == 1:
                player2[int(playedDomino[1])][int(playedDomino[2])] = 0
                player2HandSize = player2HandSize - 1
                turn = 2
            elif numPlayers > 2 and turn == 2:
                player3[int(playedDomino[1])][int(playedDomino[2])] = 0
                player3HandSize = player3HandSize - 1
                turn = 3
            elif numPlayers > 3 and turn == 3:
                player4[int(playedDomino[1])][int(playedDomino[2])] = 0
                player4HandSize = player4HandSize - 1
                turn = 4
            elif numPlayers > 4 and turn == 4:
                player5[int(playedDomino[1])][int(playedDomino[2])] = 0
                player5HandSize = player5HandSize - 1
                turn = 5
            elif numPlayers > 5 and turn == 5:
                player6[int(playedDomino[1])][int(playedDomino[2])] = 0
                player6HandSize = player6HandSize - 1
                turn = 6
            elif numPlayers > 6 and turn == 6:
                player7[int(playedDomino[1])][int(playedDomino[2])] = 0
                player7HandSize = player7HandSize - 1
                turn = 7
            elif turn == numPlayers:
                ai[int(playedDomino[1])][int(playedDomino[2])] = 0
                aiHandSize = aiHandSize - 1
                turn = 0
        elif int(playedDomino[2]) == double:
            spotsPlayable[double] = spotsPlayable[double] - 1
            spotsPlayable[int(playedDomino[1])] = spotsPlayable[int(playedDomino[1])] + 1
            totalPlayed[double] = totalPlayed[double] + 1
            totalPlayed[int(playedDomino[1])] = totalPlayed[int(playedDomino[1])] + 1
            played[int(playedDomino[1])][int(playedDomino[2])] = 1
            doubleSpots = doubleSpots - 1
            blockCheck = 0
            if turn == 0:
                player1[int(playedDomino[1])][int(playedDomino[2])] = 0
                player1HandSize = player1HandSize - 1
                turn = 1
            elif numPlayers > 1 and turn == 1:
                player2[int(playedDomino[1])][int(playedDomino[2])] = 0
                player2HandSize = player2HandSize - 1
                turn = 2
            elif numPlayers > 2 and turn == 2:
                player3[int(playedDomino[1])][int(playedDomino[2])] = 0
                player3HandSize = player3HandSize - 1
                turn = 3
            elif numPlayers > 3 and turn == 3:
                player4[int(playedDomino[1])][int(playedDomino[2])] = 0
                player4HandSize = player4HandSize - 1
                turn = 4
            elif numPlayers > 4 and turn == 4:
                player5[int(playedDomino[1])][int(playedDomino[2])] = 0
                player5HandSize = player5HandSize - 1
                turn = 5
            elif numPlayers > 5 and turn == 5:
                player6[int(playedDomino[1])][int(playedDomino[2])] = 0
                player6HandSize = player6HandSize - 1
                turn = 6
            elif numPlayers > 6 and turn == 6:
                player7[int(playedDomino[1])][int(playedDomino[2])] = 0
                player7HandSize = player7HandSize - 1
                turn = 7
            elif turn == numPlayers:
                ai[int(playedDomino[1])][int(playedDomino[2])] = 0
                aiHandSize = aiHandSize - 1
                turn = 0
        else:
            print("There is a double", double, "in play, you must play a", double)
        if doubleSpots == 0:
            doublePlayed = False
    elif playedDomino[1] == playedDomino[2]:
        if spotsPlayable[int(playedDomino[1])] > 0:
            played[int(playedDomino[1])][int(playedDomino[2])] = 1
            doublePlayed = True
            double = int(playedDomino[1])
            doubleSpots = 3
            spotsPlayable[int(playedDomino[1])] = spotsPlayable[int(playedDomino[1])] + 2 # -1 for played domino, +3 for double
            totalPlayed[int(playedDomino[1])] = totalPlayed[int(playedDomino[1])] + 1
            blockCheck = 0
            if turn == 0:
                player1[int(playedDomino[1])][int(playedDomino[2])] = 0
                player1HandSize = player1HandSize - 1
                turn = 1
            elif numPlayers > 1 and turn == 1:
                player2[int(playedDomino[1])][int(playedDomino[2])] = 0
                player2HandSize = player2HandSize - 1
                turn = 2
            elif numPlayers > 2 and turn == 2:
                player3[int(playedDomino[1])][int(playedDomino[2])] = 0
                player3HandSize = player3HandSize - 1
                turn = 3
            elif numPlayers > 3 and turn == 3:
                player4[int(playedDomino[1])][int(playedDomino[2])] = 0
                player4HandSize = player4HandSize - 1
                turn = 4
            elif numPlayers > 4 and turn == 4:
                player5[int(playedDomino[1])][int(playedDomino[2])] = 0
                player5HandSize = player5HandSize - 1
                turn = 5
            elif numPlayers > 5 and turn == 5:
                player6[int(playedDomino[1])][int(playedDomino[2])] = 0
                player6HandSize = player6HandSize - 1
                turn = 6
            elif numPlayers > 6 and turn == 6:
                player7[int(playedDomino[1])][int(playedDomino[2])] = 0
                player7HandSize = player7HandSize - 1
                turn = 7
            elif turn == numPlayers:
                ai[int(playedDomino[1])][int(playedDomino[2])] = 0
                aiHandSize = aiHandSize - 1
                turn = 0
        else:
            print("There is no open spot to play that domino")
    else:
        if spotsPlayable[int(playedDomino[1])] > 0 and spotsPlayable[int(playedDomino[2])] == 0:
            played[int(playedDomino[1])][int(playedDomino[2])] = 1
            spotsPlayable[int(playedDomino[1])] = spotsPlayable[int(playedDomino[1])] - 1
            spotsPlayable[int(playedDomino[2])] = spotsPlayable[int(playedDomino[2])] + 1
            totalPlayed[int(playedDomino[1])] = totalPlayed[int(playedDomino[1])] + 1
            totalPlayed[int(playedDomino[2])] = totalPlayed[int(playedDomino[2])] + 1
            blockCheck = 0
            if turn == 0:
                player1[int(playedDomino[1])][int(playedDomino[2])] = 0
                player1HandSize = player1HandSize - 1
                turn = 1
            elif numPlayers > 1 and turn == 1:
                player2[int(playedDomino[1])][int(playedDomino[2])] = 0
                player2HandSize = player2HandSize - 1
                turn = 2
            elif numPlayers > 2 and turn == 2:
                player3[int(playedDomino[1])][int(playedDomino[2])] = 0
                player3HandSize = player3HandSize - 1
                turn = 3
            elif numPlayers > 3 and turn == 3:
                player4[int(playedDomino[1])][int(playedDomino[2])] = 0
                player4HandSize = player4HandSize - 1
                turn = 4
            elif numPlayers > 4 and turn == 4:
                player5[int(playedDomino[1])][int(playedDomino[2])] = 0
                player5HandSize = player5HandSize - 1
                turn = 5
            elif numPlayers > 5 and turn == 5:
                player6[int(playedDomino[1])][int(playedDomino[2])] = 0
                player6HandSize = player6HandSize - 1
                turn = 6
            elif numPlayers > 6 and turn == 6:
                player7[int(playedDomino[1])][int(playedDomino[2])] = 0
                player7HandSize = player7HandSize - 1
                turn = 7
            elif turn == numPlayers:
                ai[int(playedDomino[1])][int(playedDomino[2])] = 0
                aiHandSize = aiHandSize - 1
                turn = 0
        elif spotsPlayable[int(playedDomino[2])] > 0 and spotsPlayable[int(playedDomino[1])] == 0:
            played[int(playedDomino[1])][int(playedDomino[2])] = 1
            spotsPlayable[int(playedDomino[2])] = spotsPlayable[int(playedDomino[2])] - 1
            spotsPlayable[int(playedDomino[1])] = spotsPlayable[int(playedDomino[1])] + 1
            totalPlayed[int(playedDomino[1])] = totalPlayed[int(playedDomino[1])] + 1
            totalPlayed[int(playedDomino[2])] = totalPlayed[int(playedDomino[2])] + 1
            blockCheck = 0
            if turn == 0:
                player1[int(playedDomino[1])][int(playedDomino[2])] = 0
                player1HandSize = player1HandSize - 1
                turn = 1
            elif numPlayers > 1 and turn == 1:
                player2[int(playedDomino[1])][int(playedDomino[2])] = 0
                player2HandSize = player2HandSize - 1
                turn = 2
            elif numPlayers > 2 and turn == 2:
                player3[int(playedDomino[1])][int(playedDomino[2])] = 0
                player3HandSize = player3HandSize - 1
                turn = 3
            elif numPlayers > 3 and turn == 3:
                player4[int(playedDomino[1])][int(playedDomino[2])] = 0
                player4HandSize = player4HandSize - 1
                turn = 4
            elif numPlayers > 4 and turn == 4:
                player5[int(playedDomino[1])][int(playedDomino[2])] = 0
                player5HandSize = player5HandSize - 1
                turn = 5
            elif numPlayers > 5 and turn == 5:
                player6[int(playedDomino[1])][int(playedDomino[2])] = 0
                player6HandSize = player6HandSize - 1
                turn = 6
            elif numPlayers > 6 and turn == 6:
                player7[int(playedDomino[1])][int(playedDomino[2])] = 0
                player7HandSize = player7HandSize - 1
                turn = 7
            elif turn == numPlayers:
                ai[int(playedDomino[1])][int(playedDomino[2])] = 0
                aiHandSize = aiHandSize - 1
                turn = 0
        elif spotsPlayable[int(playedDomino[1])] > 0 and spotsPlayable[int(playedDomino[2])] > 0:
            played[int(playedDomino[1])][int(playedDomino[2])] = 1
            totalPlayed[int(playedDomino[1])] = totalPlayed[int(playedDomino[1])] + 1
            totalPlayed[int(playedDomino[2])] = totalPlayed[int(playedDomino[2])] + 1
            blockCheck = 0
            #if turn < numPlayers: #uncomment when ai is implemented
            print("Would you like to play it on a", playedDomino[1], "or a", playedDomino[2])
            userInput = input()
            if userInput == playedDomino[1]:
                spotsPlayable[int(playedDomino[1])] = spotsPlayable[int(playedDomino[1])] - 1
                spotsPlayable[int(playedDomino[2])] = spotsPlayable[int(playedDomino[2])] + 1
            else:
                spotsPlayable[int(playedDomino[2])] = spotsPlayable[int(playedDomino[2])] - 1
                spotsPlayable[int(playedDomino[1])] = spotsPlayable[int(playedDomino[1])] + 1
            if turn == 0:
                player1[int(playedDomino[1])][int(playedDomino[2])] = 0
                player1HandSize = player1HandSize - 1
                turn = 1
            elif numPlayers > 1 and turn == 1:
                player2[int(playedDomino[1])][int(playedDomino[2])] = 0
                player2HandSize = player2HandSize - 1
                turn = 2
            elif numPlayers > 2 and turn == 2:
                player3[int(playedDomino[1])][int(playedDomino[2])] = 0
                player3HandSize = player3HandSize - 1
                turn = 3
            elif numPlayers > 3 and turn == 3:
                player4[int(playedDomino[1])][int(playedDomino[2])] = 0
                player4HandSize = player4HandSize - 1
                turn = 4
            elif numPlayers > 4 and turn == 4:
                player5[int(playedDomino[1])][int(playedDomino[2])] = 0
                player5HandSize = player5HandSize - 1
                turn = 5
            elif numPlayers > 5 and turn == 5:
                player6[int(playedDomino[1])][int(playedDomino[2])] = 0
                player6HandSize = player6HandSize - 1
                turn = 6
            elif numPlayers > 6 and turn == 6:
                player7[int(playedDomino[1])][int(playedDomino[2])] = 0
                player7HandSize = player7HandSize - 1
                turn = 7
            elif turn == numPlayers: #make automated with actual AI
                ai[int(playedDomino[1])][int(playedDomino[2])] = 0
                aiHandSize = aiHandSize - 1
                turn = 0
        else:
            print("There is no open spot to play that domino")

def draw():
    global chickenYardAmount
    global player1HandSize
    global player2HandSize
    global player3HandSize
    global player4HandSize
    global player5HandSize
    global player6HandSize
    global player7HandSize
    global aiHandSize
    global turn
    global doublePlayed
    global double
    global blockCheck
    global numPlayers

    drawn = False # makes sure a valid domino is drawn

    if chickenYardAmount == 0:
        if turn == 0:
            turn = 1
            blockCheck = blockCheck + 1
        elif numPlayers > 1 and turn == 1:
            turn = 2
            blockCheck = blockCheck + 1
        elif numPlayers > 2 and turn == 2:
            turn = 3
            blockCheck = blockCheck + 1
        elif numPlayers > 3 and turn == 3:
            turn = 4
            blockCheck = blockCheck + 1
        elif numPlayers > 4 and turn == 4:
            turn = 5
            blockCheck = blockCheck + 1
        elif numPlayers > 5 and turn == 5:
            turn = 6
            blockCheck = blockCheck + 1
        elif numPlayers > 6 and turn == 6:
            turn = 7
            blockCheck = blockCheck + 1
        elif turn == numPlayers:
            turn = 0
            blockCheck = blockCheck + 1

    elif chickenYardAmount > 0:
        while drawn == False:
            domino1 = random.randint(0,9)
            domino2 = random.randint(0,9)
            if domino1 > domino2:
                dominoTemp = domino1
                domino1 = domino2
                domino2 = dominoTemp

            if chickenYard[domino1][domino2] == 1:
                chickenYard[domino1][domino2] = 0
                chickenYardAmount = chickenYardAmount - 1
                drawn = True

                userInput = " ".join(["play", str(domino1), str(domino2)])
   
                if doublePlayed == True:
                    if domino1 == double or domino2 == double:
                        play(userInput)
                        break
                elif spotsPlayable[domino1] > 0 or spotsPlayable[domino2] > 0:
                        play(userInput)
                        break
                if turn == 0:
                    player1[domino1][domino2] = 1
                    player1HandSize = player1HandSize + 1
                    turn = 1
                elif numPlayers > 1 and turn == 1:
                    player2[domino1][domino2] = 1
                    player2HandSize = player2HandSize + 1
                    turn = 2
                elif numPlayers > 2 and turn == 2:
                    player3[domino1][domino2] = 1
                    player3HandSize = player3HandSize + 1
                    turn = 3
                elif numPlayers > 3 and turn == 3:
                    player4[domino1][domino2] = 1
                    player4HandSize = player4HandSize + 1
                    turn = 4
                elif numPlayers > 4 and turn == 4:
                    player5[domino1][domino2] = 1
                    player5HandSize = player5HandSize + 1
                    turn = 5
                elif numPlayers > 5 and turn == 5:
                    player6[domino1][domino2] = 1
                    player6HandSize = player6HandSize + 1
                    turn = 6
                elif numPlayers > 6 and turn == 6:
                    player7[domino1][domino2] = 1
                    player7HandSize = player7HandSize + 1
                    turn = 7
                elif turn == numPlayers:
                    ai[domino1][domino2] = 1
                    aiHandSize = aiHandSize + 1
                    turn = 0

#example output for minimax from geeksforgeeks (returns 5)
#values = [3, 5, 6, 9, 1, 2, 0, -1]
#print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))

aiTest = 0 #used to see if AI is playing against itself or not
round = 9 # what double to start round with, starting with 9
player1Score = 0
player2Score = 0
player3Score = 0
player4Score = 0
player5Score = 0
player6Score = 0
player7Score = 0
aiScore = 0

p1Name = "Player 1"
p2Name = "Player 2"
p3Name = "Player 3"
p4Name = "Player 4"
p5Name = "Player 5"
p6Name = "Player 6"
p7Name = "Player 7"

numPlayers = 0
while numPlayers < 1:
    numPlayers = input("How many human players (1-7): ")
    if numPlayers == "aiTest":
        aiTest = 1
        numPlayers = 0
    numPlayers = int(numPlayers)
    if numPlayers < 0 or numPlayers > 7: #error checking
        numPlayers = 0

if aiTest == 0:
    names = input("Would you like to enter a name/names for the human player(s)? (yes/no): ")
    if names == "yes":
        p1Name = input("Enter Player 1's name: ")
        if numPlayers > 1:
            p2Name = input("Enter Player 2's name: ")
        if numPlayers > 2:
            p3Name = input("Enter Player 3's name: ")
        if numPlayers > 3:
            p4Name = input("Enter Player 4's name: ")
        if numPlayers > 4:
            p5Name = input("Enter Player 5's name: ")
        if numPlayers > 5:
            p6Name = input("Enter Player 6's name: ")
        if numPlayers > 6:
            p7Name = input("Enter Player 7's name: ")

while round >= 0:
    dealt = 0
    neededDealt = 41 #number of dominos needed to be dealt before starting
    player1HandSize = 0
    player2HandSize = 1 #must be > 0 if not an actual player
    player3HandSize = 1 #must be > 0 if not an actual player
    player4HandSize = 1 #must be > 0 if not an actual player
    player5HandSize = 1 #must be > 0 if not an actual player
    player6HandSize = 1 #must be > 0 if not an actual player
    player7HandSize = 1 #must be > 0 if not an actual player
    aiHandSize = 0
    numPlayed = 0 # used to test for number of #'s played (e.g. number of 6's played)
    doublePlayed = False
    double = round # double that needs to be played
    doubleSpots = 6 # how many spots of the double still need to be filled
    chickenYardAmount = 55
    turn = 0
    blockCheck = 0

    chickenYard = [[1 for i in range(10)] for j in range(10)]
    player1 = [[0 for i in range(10)] for j in range(10)]
    ai = [[0 for i in range(10)] for j in range(10)]
    played = [[0 for i in range(10)] for j in range(10)]
    spotsPlayable = [0 for i in range(10)]
    totalPlayed = [0 for i in range(10)]

    if numPlayers > 1:
        player2 = [[0 for i in range(10)] for j in range(10)]
        player2HandSize = 0
    if numPlayers > 2:
        player3 = [[0 for i in range(10)] for j in range(10)]
        player3HandSize = 0
        neededDealt = 44
    if numPlayers > 3:
        player4 = [[0 for i in range(10)] for j in range(10)]
        player4HandSize = 0
        neededDealt = 40
    if numPlayers > 4:
        player5 = [[0 for i in range(10)] for j in range(10)]
        player5HandSize = 0
    if numPlayers > 5:
        player6 = [[0 for i in range(10)] for j in range(10)]
        player6HandSize = 0
    if numPlayers > 6:
        player7 = [[0 for i in range(10)] for j in range(10)]
        player7HandSize = 0
        neededDealt = 40

    # game setup    
    while doublePlayed == False:
        draw()
        dealt = dealt + 1
        if dealt > neededDealt:
            if player1[double][double] == 1:
                doublePlayed = True
                turn = 1
                player1[double][double] = 0
                played[double][double] = 1
                spotsPlayable[double] = spotsPlayable[double] + 6
                totalPlayed[double] = totalPlayed[double] + 1
                player1HandSize = player1HandSize - 1
                print(p1Name, "had double", double)
            elif numPlayers > 1 and player2[double][double] == 1:
                doublePlayed = True
                turn = 2
                player2[double][double] = 0
                played[double][double] = 1
                spotsPlayable[double] = spotsPlayable[double] + 6
                totalPlayed[double] = totalPlayed[double] + 1
                player2HandSize = player2HandSize - 1
                print(p2Name, "had double", double)
            elif numPlayers > 2 and player3[double][double] == 1:
                doublePlayed = True
                turn = 3
                player3[double][double] = 0
                played[double][double] = 1
                spotsPlayable[double] = spotsPlayable[double] + 6
                totalPlayed[double] = totalPlayed[double] + 1
                player3HandSize = player3HandSize - 1
                print(p3Name, "had double", double)
            elif numPlayers > 3 and player4[double][double] == 1:
                doublePlayed = True
                turn = 4
                player4[double][double] = 0
                played[double][double] = 1
                spotsPlayable[double] = spotsPlayable[double] + 6
                totalPlayed[double] = totalPlayed[double] + 1
                player4HandSize = player4HandSize - 1
                print(p4Name, "had double", double)
            elif numPlayers > 4 and player5[double][double] == 1:
                doublePlayed = True
                turn = 5
                player5[double][double] = 0
                played[double][double] = 1
                spotsPlayable[double] = spotsPlayable[double] + 6
                totalPlayed[double] = totalPlayed[double] + 1
                player5HandSize = player5HandSize - 1
                print(p5Name, "had double", double)
            elif numPlayers > 5 and player6[double][double] == 1:
                doublePlayed = True
                turn = 6
                player6[double][double] = 0
                played[double][double] = 1
                spotsPlayable[double] = spotsPlayable[double] + 6
                totalPlayed[double] = totalPlayed[double] + 1
                player6HandSize = player6HandSize - 1
                print(p6Name, "had double", double)
            elif numPlayers > 6 and player7[double][double] == 1:
                doublePlayed = True
                turn = 7
                player7[double][double] = 0
                played[double][double] = 1
                spotsPlayable[double] = spotsPlayable[double] + 6
                totalPlayed[double] = totalPlayed[double] + 1
                player7HandSize = player7HandSize - 1
                print(p7Name, "had double", double)
            elif ai[double][double] == 1:
                doublePlayed = True
                turn = 0
                ai[double][double] = 0
                played[double][double] = 1
                spotsPlayable[double] = spotsPlayable[double] + 6
                totalPlayed[double] = totalPlayed[double] + 1
                aiHandSize = aiHandSize - 1
                print("AI had double", double)

    if aiTest == 0:
        if round == 9:
            print("Type 'help' to list commands")
            print("Type 'play # #', where the #s are replaced by the domino you wish to play")
            print("Type 'doubles' to list the doubles that have been played so far")
            print("Type 'dominos' or 'dominoes' to list the number of each type of domino that has been played so far & how many dominoes remain in the chicken yard")
            print("Type 'draw' to draw a domino from the chicken yard")
            print("Type 'places' to list available places to play")
            print("Type 'score' to list the scores of the players")
            print("Type 'quit' to quit the game")

    # game starting
    while player1HandSize > 0 and player2HandSize > 0 and player3HandSize > 0 and player4HandSize > 0 and player5HandSize > 0 and player6HandSize > 0 and player7HandSize > 0 and aiHandSize > 0:
        if turn == 0:
            print(p1Name,"'s Turn", sep = '')
            for i in range(10): # print hand to player 1
                for j in range(10):
                    if player1[i][j] == 1:
                        print("[",i,"|",j,"]", sep='', end='')
        elif numPlayers > 1 and turn == 1:
            print(p2Name,"'s Turn", sep = '')
            for i in range(10): # print hand to player 2
                for j in range(10):
                    if player2[i][j] == 1:
                        print("[",i,"|",j,"]", sep='', end='')
        elif numPlayers > 2 and turn == 2:
            print(p3Name,"'s Turn", sep = '')
            for i in range(10): # print hand to player 3
                for j in range(10):
                    if player3[i][j] == 1:
                        print("[",i,"|",j,"]", sep='', end='')
        elif numPlayers > 3 and turn == 3:
            print(p4Name,"'s Turn", sep = '')
            for i in range(10): # print hand to player 4
                for j in range(10):
                    if player4[i][j] == 1:
                        print("[",i,"|",j,"]", sep='', end='')
        elif numPlayers > 4 and turn == 4:
            print(p5Name,"'s Turn", sep = '')
            for i in range(10): # print hand to player 5
                for j in range(10):
                    if player5[i][j] == 1:
                        print("[",i,"|",j,"]", sep='', end='')
        elif numPlayers > 5 and turn == 5:
            print(p6Name,"'s Turn", sep = '')
            for i in range(10): # print hand to player 6
                for j in range(10):
                    if player6[i][j] == 1:
                        print("[",i,"|",j,"]", sep='', end='')
        elif numPlayers > 6 and turn == 6:
            print(p7Name,"'s Turn", sep = '')
            for i in range(10): # print hand to player 7
                for j in range(10):
                    if player7[i][j] == 1:
                        print("[",i,"|",j,"]", sep='', end='')
        elif turn == numPlayers:
            print("AI's Turn") # for testing
            for i in range(10): # print hand to player ai for testing
                for j in range(10):
                    if ai[i][j] == 1:
                        print("[",i,"|",j,"]", sep='', end='')
        print()
        if doublePlayed == True:
            print("Double", double, "in play,", doubleSpots, "spots remaining on it")
        else:
            available = []
            numAvailable = []
            for i in range (10):
                if spotsPlayable[i] > 0:
                    available.append(i)
                    numAvailable.append(spotsPlayable[i])
            if len(available) == 1:
                print(available, "is available to play on")
                print(numAvailable, "is how many of it is available")
            else:
                print(available, "are available to play on")
                print(numAvailable, "is how many of each are available")
        #if(turn < numPlayers): #make player only after implementing ai
        userInput = input("Enter move: ")
        if userInput == "help":
            print("Type 'help' to list commands")
            print("Type 'play # #', where the #s are replaced by the domino you wish to play")
            print("Type 'doubles' to list the doubles that have been played so far")
            print("Type 'dominos' or 'dominoes' to list the number of each type of domino that has been played so far & how many dominoes remain in the chicken yard")
            print("Type 'draw' to draw a domino from the chicken yard")
            print("Type 'places' to list available places to play")
            print("Type 'score' to list the scores of the players")
            print("Type 'quit' to quit the game")
        elif re.search("play ", userInput):
            playedDomino = userInput.split(" ")
            if turn == 0 and player1[int(playedDomino[1])][int(playedDomino[2])] == 1:
                play(userInput)
            elif numPlayers > 1 and turn == 1 and player2[int(playedDomino[1])][int(playedDomino[2])] == 1:
                play(userInput)
            elif numPlayers > 2 and turn == 2 and player3[int(playedDomino[1])][int(playedDomino[2])] == 1:
                play(userInput)
            elif numPlayers > 3 and turn == 3 and player4[int(playedDomino[1])][int(playedDomino[2])] == 1:
                play(userInput)
            elif numPlayers > 4 and turn == 4 and player5[int(playedDomino[1])][int(playedDomino[2])] == 1:
                play(userInput)
            elif numPlayers > 5 and turn == 5 and player6[int(playedDomino[1])][int(playedDomino[2])] == 1:
                play(userInput)
            elif numPlayers > 6 and turn == 6 and player7[int(playedDomino[1])][int(playedDomino[2])] == 1:
                play(userInput)
            elif turn == numPlayers and ai[int(playedDomino[1])][int(playedDomino[2])] == 1:
                play(userInput)
            else:
                print("You do not have that domino")
        elif userInput == "doubles":
            available = []
            for i in range(10):
                if played[i][i] == 1:
                    available.append(i)
            if len(available) == 1:
                print("Double", available, "played")
            else:
                print("Doubles", available, "played")
        elif userInput == "dominos" or userInput == "dominoes":
            print("[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
            print(totalPlayed, "have been played of each")
            print(chickenYardAmount, "dominoes left in chicken yard")
        elif userInput == "draw":
            #draw(chickenYardAmount, turn, blockCheck, chickenYard, doublePlayed, double, player, playerHandSize, ai, aiHandSize, spotsPlayable)
            draw()
        elif userInput == "places":
            available = []
            numAvailable = []
            for i in range (10):
                if spotsPlayable[i] > 0:
                    available.append(i)
                    numAvailable.append(spotsPlayable[i])
            if len(available) == 1:
                print(available, "is available to play on")
                print(numAvailable, "is how many of it is available")
            else:
                print(available, "are available to play on")
                print(numAvailable, "is how many of each are available")
        elif userInput == "score":
            print(p1Name,"'s score is ", player1Score, sep = '')
            if numPlayers > 1:
                print(p2Name,"'s score is ", player2Score, sep = '')
            if numPlayers > 2:
                print(p3Name,"'s score is ", player3Score, sep = '')
            if numPlayers > 3:
                print(p4Name,"'s score is ", player4Score, sep = '')
            if numPlayers > 4:
                print(p5Name,"'s score is ", player5Score, sep = '')
            if numPlayers > 5:
                print(p6Name,"'s score is ", player6Score, sep = '')
            if numPlayers > 6:
                print(p7Name,"'s score is ", player7Score, sep = '')
            print("AI's score is", aiScore)
        elif userInput == "quit":
            quit()
        elif userInput == "block": # debug command to test blocked game
            blockCheck = numPlayers + 1
        elif userInput == "win": # debug command to test winning
            for i in range(10):
                for j in range(10):
                    if turn == 0:
                        player1[i][j] = 0
                        player1HandSize = 0
                    elif numPlayers > 1 and turn == 1:
                        player2[i][j] = 0
                        player2HandSize = 0
                    elif numPlayers > 2 and turn == 2:
                        player3[i][j] = 0
                        player3HandSize = 0
                    elif numPlayers > 3 and turn == 3:
                        player4[i][j] = 0
                        player4HandSize = 0
                    elif numPlayers > 4 and turn == 4:
                        player5[i][j] = 0
                        player5HandSize = 0
                    elif numPlayers > 5 and turn == 5:
                        player6[i][j] = 0
                        player6HandSize = 0
                    elif numPlayers > 6 and turn == 6:
                        player6[i][j] = 0
                        player6HandSize = 0
                    elif turn == numPlayers:
                        ai[i][j] = 0
                        aiHandSize = 0
            
        if blockCheck > numPlayers or player1HandSize == 0 or player2HandSize == 0 or player3HandSize == 0 or player4HandSize == 0 or player5HandSize == 0 or player6HandSize == 0 or player7HandSize == 0 or aiHandSize == 0: # round end tests
            break

    for i in range(10): # calc score
        for j in range(10): 
            if player1[i][j] == 1:
                player1[i][j] = 0
                if i == 0 and j == 0:
                    player1Score = player1Score + 50
                else:
                    player1Score = player1Score + i
                    player1Score = player1Score + j
            elif numPlayers > 1 and player2[i][j] == 1:
                player2[i][j] = 0
                if i == 0 and j == 0:
                    player2Score = player2Score + 50
                else:
                    player2Score = player2Score + i
                    player2Score = player2Score + j
            elif numPlayers > 2 and player3[i][j] == 1:
                player3[i][j] = 0
                if i == 0 and j == 0:
                    player3Score = player3Score + 50
                else:
                    player3Score = player3Score + i
                    player3Score = player3Score + j
            elif numPlayers > 3 and player4[i][j] == 1:
                player4[i][j] = 0
                if i == 0 and j == 0:
                    player4Score = player4Score + 50
                else:
                    player4Score = player4Score + i
                    player4Score = player4Score + j
            elif numPlayers > 4 and player5[i][j] == 1:
                player5[i][j] = 0
                if i == 0 and j == 0:
                    player5Score = player5Score + 50
                else:
                    player5Score = player5Score + i
                    player5Score = player5Score + j
            elif numPlayers > 5 and player6[i][j] == 1:
                player6[i][j] = 0
                if i == 0 and j == 0:
                    player6Score = player6Score + 50
                else:
                    player6Score = player6Score + i
                    player6Score = player6Score + j
            elif numPlayers > 6 and player7[i][j] == 1:
                player7[i][j] = 0
                if i == 0 and j == 0:
                    player7Score = player7Score + 50
                else:
                    player7Score = player7Score + i
                    player7Score = player7Score + j
            elif ai[i][j] == 1:
                ai[i][j] = 0
                if i == 0 and j == 0:
                    aiScore = aiScore + 50
                else:
                    aiScore = aiScore + i
                    aiScore = aiScore + j

    if round == 0:
        if player1Score < aiScore and player1Score < player2Score and player1Score < player3Score and player1Score < player4Score and player1Score < player5Score and player1Score < player6Score and player1Score < player7Score:
            print(p1Name, "won with a score of", player1Score)#, "compared to the AI's", aiScore)
        elif player2Score < aiScore and player2Score < player1Score and player2Score < player3Score and player2Score < player4Score and player2Score < player5Score and player2Score < player6Score and player2Score < player7Score:
            print(p2Name, "won with a score of", player2Score)
        elif player3Score < aiScore and player3Score < player1Score and player3Score < player2Score and player3Score < player4Score and player3Score < player5Score and player3Score < player6Score and player3Score < player7Score:
            print(p3Name, "won with a score of", player3Score)
        elif player4Score < aiScore and player4Score < player1Score and player4Score < player2Score and player4Score < player3Score and player4Score < player5Score and player4Score < player6Score and player4Score < player7Score:
            print(p4Name, "won with a score of", player4Score)
        elif player5Score < aiScore and player5Score < player1Score and player5Score < player2Score and player5Score < player3Score and player5Score < player4Score and player5Score < player6Score and player5Score < player7Score:
            print(p5Name, "won with a score of", player5Score)
        elif player6Score < aiScore and player6Score < player1Score and player6Score < player2Score and player6Score < player3Score and player6Score < player4Score and player6Score < player5Score and player6Score < player7Score:
            print(p6Name, "won with a score of", player6Score)
        elif player7Score < aiScore and player7Score < player1Score and player7Score < player2Score and player7Score < player3Score and player7Score < player4Score and player7Score < player5Score and player7Score < player6Score:
            print(p7Name, "won with a score of", player7Score)
        elif aiScore < player1Score and aiScore < player2Score and aiScore < player3Score and aiScore < player4Score and aiScore < player5Score and aiScore < player6Score and aiScore < player7Score:
            print("The AI won with a score of", aiScore)#, "compared to player's", player1Score)
        elif player1Score == aiScore and player2Score == aiScore and player3Score == aiScore and player4Score == aiScore and player5Score == aiScore and player6Score == aiScore and player7Score == aiScore:
            print("Players and the AI tied with a score of", player1Score)
        else:
            print("There has been an error in the scoring")
        quit()
    else:
        round = round - 1
        blockCheck = 0