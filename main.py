#from func import *
from array import *
import random
import re

def play(userInput):
    global doublePlayed
    global double
    global doubleSpots
    global turn

    playedDomino = userInput.split(" ")
    if playedDomino[1] > playedDomino[2]:
        playedTemp = playedDomino[1]
        playedDomino[1] = playedDomino[2]
        playedDomino[2] = playedTemp

    if doublePlayed == True:
        if totalPlayed[double] > 10 and doubleSpots == 3:
            print("There are not enough", double,"'s left to complete the double, auto-drawing the remainder of the chicken yard")
            while chickenYardAmount > 0:
                domino1 = random.randint(0,9)
                domino2 = random.randint(0,9)
                if domino1 > domino2:
                    dominoTemp = domino1
                    domino1 = domino2
                    domino2 = dominoTemp

                if chickenYard[domino1][domino2] == 1:
                    chickenYard[domino1][domino2] == 0
                    chickenYardAmount = chickenYardAmount - 1
                    if turn == 0:
                        player[domino1][domino2] = 1
                        playerHandSize = playerHandSize + 1
                        turn = 1
                    elif turn == 1:
                        ai[domino1][domino2] = 1
                        aiHandSize = aiHandSize + 1
                        turn = 0
            blockCheck = 2
        elif int(playedDomino[1]) == double:
            spotsPlayable[double] = spotsPlayable[double] - 1
            spotsPlayable[int(playedDomino[2])] = spotsPlayable[int(playedDomino[2])] + 1
            totalPlayed[double] = totalPlayed[double] + 1
            totalPlayed[int(playedDomino[2])] = totalPlayed[int(playedDomino[2])] + 1
            played[int(playedDomino[1])][int(playedDomino[2])] = 1
            doubleSpots = doubleSpots - 1
            blockCheck = 0
            if turn == 0:
                player[int(playedDomino[1])][int(playedDomino[2])] = 0
                turn = 1
            elif turn == 1:
                ai[int(playedDomino[1])][int(playedDomino[2])] = 0
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
                player[int(playedDomino[1])][int(playedDomino[2])] = 0
                turn = 1
            elif turn == 1:
                ai[int(playedDomino[1])][int(playedDomino[2])] = 0
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
                player[int(playedDomino[1])][int(playedDomino[2])] = 0
                turn = 1
            elif turn == 1:
                ai[int(playedDomino[1])][int(playedDomino[2])] = 0
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
                player[int(playedDomino[1])][int(playedDomino[2])] = 0
                turn = 1
            elif turn == 1:
                ai[int(playedDomino[1])][int(playedDomino[2])] = 0
                turn = 0
        elif spotsPlayable[int(playedDomino[2])] > 0 and spotsPlayable[int(playedDomino[1])] == 0:
            played[int(playedDomino[1])][int(playedDomino[2])] = 1
            spotsPlayable[int(playedDomino[2])] = spotsPlayable[int(playedDomino[2])] - 1
            spotsPlayable[int(playedDomino[1])] = spotsPlayable[int(playedDomino[1])] + 1
            totalPlayed[int(playedDomino[1])] = totalPlayed[int(playedDomino[1])] + 1
            totalPlayed[int(playedDomino[2])] = totalPlayed[int(playedDomino[2])] + 1
            blockCheck = 0
            if turn == 0:
                player[int(playedDomino[1])][int(playedDomino[2])] = 0
                turn = 1
            elif turn == 1:
                ai[int(playedDomino[1])][int(playedDomino[2])] = 0
                turn = 0
        elif spotsPlayable[int(playedDomino[1])] > 0 and spotsPlayable[int(playedDomino[2])] > 0:
            played[int(playedDomino[1])][int(playedDomino[2])] = 1
            totalPlayed[int(playedDomino[1])] = totalPlayed[int(playedDomino[1])] + 1
            totalPlayed[int(playedDomino[2])] = totalPlayed[int(playedDomino[2])] + 1
            blockCheck = 0
            if turn == 0:
                player[int(playedDomino[1])][int(playedDomino[2])] = 0
                turn = 1
                print("Would you like to play it on a", playedDomino[1], "or a", playedDomino[2])
                userInput = input()
                if userInput == playedDomino[1]:
                    spotsPlayable[int(playedDomino[1])] = spotsPlayable[int(playedDomino[1])] - 1
                    spotsPlayable[int(playedDomino[2])] = spotsPlayable[int(playedDomino[2])] + 1
                else:
                    spotsPlayable[int(playedDomino[2])] = spotsPlayable[int(playedDomino[2])] - 1
                    spotsPlayable[int(playedDomino[1])] = spotsPlayable[int(playedDomino[1])] + 1
            elif turn == 1: #make automated with actual AI
                ai[int(playedDomino[1])][int(playedDomino[2])] = 0
                turn = 0
                print("Would you like to play it on a", playedDomino[1], "or a", playedDomino[2])
                userInput = input()
                if userInput == playedDomino[1]:
                    spotsPlayable[int(playedDomino[1])] = spotsPlayable[int(playedDomino[1])] - 1
                    spotsPlayable[int(playedDomino[2])] = spotsPlayable[int(playedDomino[2])] + 1
                else:
                    spotsPlayable[int(playedDomino[2])] = spotsPlayable[int(playedDomino[2])] - 1
                    spotsPlayable[int(playedDomino[1])] = spotsPlayable[int(playedDomino[1])] + 1
        else:
            print("There is no open spot to play that domino")

def draw():
    global chickenYardAmount
    global playerHandSize
    global aiHandSize
    global turn
    global doublePlayed
    global double
    global blockCheck

    draw = False # makes sure a valid domino is drawn

    if chickenYardAmount == 0:
        if turn == 0:
            turn == 1
            blockCheck = blockCheck + 1
        elif turn == 1:
            turn == 0
            blockCheck = blockCheck + 1
    elif chickenYardAmount > 0:
        while draw == False:
            domino1 = random.randint(0,9)
            domino2 = random.randint(0,9)
            if domino1 > domino2:
                dominoTemp = domino1
                domino1 = domino2
                domino2 = dominoTemp

            if chickenYard[domino1][domino2] == 1:
                chickenYard[domino1][domino2] == 0
                chickenYardAmount = chickenYardAmount - 1
                draw = True

                userInput = " ".join(["play", str(domino1), str(domino2)])
   
                if doublePlayed == True:
                    if domino1 == double or domino2 == double:
                        play(userInput)
                    else:
                        if turn == 0:
                            player[domino1][domino2] = 1
                            playerHandSize = playerHandSize + 1
                            turn = 1
                        elif turn == 1:
                            ai[domino1][domino2] = 1
                            aiHandSize = aiHandSize + 1
                            turn = 0
                elif spotsPlayable[domino1] > 0 or spotsPlayable[domino2] > 0:
                        play(userInput)

round = 9 # what double to start round with, starting with 9
playerScore = 0
aiScore = 0

while round >= 0:
    deal = 0
    playerHandSize = 0
    aiHandSize = 0
    numPlayed = 0 # used to test for number of #'s played (e.g. number of 6's played)
    doublePlayed = False
    double = 0 # double that needs to be played
    doubleSpots = 6 # how many spots of the double still need to be filled
    chickenYardAmount = 55
    turn = 0
    blockCheck = 0

    chickenYard = [[1 for i in range(10)] for j in range(10)]
    player = [[0 for i in range(10)] for j in range(10)]
    ai = [[0 for i in range(10)] for j in range(10)]
    played = [[0 for i in range(10)] for j in range(10)]
    spotsPlayable = [0 for i in range(10)]
    totalPlayed = [0 for i in range(10)]

    # game setup
    while doublePlayed == False:
        double = round
        domino1 = random.randint(0,9)
        domino2 = random.randint(0,9)
        if domino1 > domino2:
            dominoTemp = domino1
            domino1 = domino2
            domino2 = dominoTemp

        if chickenYard[domino1][domino2] == 1:
            if deal % 2 == 0:
                player[domino1][domino2] = 1
                playerHandSize = playerHandSize + 1
            else:
                ai[domino1][domino2] = 1
                aiHandSize = aiHandSize + 1
            chickenYard[domino1][domino2] = 0
            chickenYardAmount = chickenYardAmount - 1
            deal = deal + 1
        if deal > 39:
            if player[double][double] == 1:
                doublePlayed = True
                turn = 1
                player[double][double] = 0
                played[double][double] = 1
                spotsPlayable[double] = spotsPlayable[double] + 6
                totalPlayed[double] = totalPlayed[double] + 1
                playerHandSize = playerHandSize - 1
                # print("Player had double", double)
            elif ai[double][double] == 1:
                doublePlayed = True
                turn = 0
                ai[double][double] = 0
                played[double][double] = 1
                spotsPlayable[double] = spotsPlayable[double] + 6
                aiHandSize = aiHandSize - 1
                # print("AI had double", double)
            else: # reset and draw again
                chickenYard = [[1 for i in range(10)] for j in range(10)]
                player = [[0 for i in range(10)] for j in range(10)]
                ai = [[0 for i in range(10)] for j in range(10)]
                deal = 0
                playerHandSize = 0
                aiHandSize = 0
                chickenYardAmount = 55

    if round == 9:
        print("Type 'help' to list commands")
        print("Type 'play # #', where the #s are replaced by the domino you wish to play")
        print("Type 'doubles' to list the doubles that have been played so far")
        print("Type 'dominos' or 'dominoes' to list the number of each type of domino that has been played so far & how many dominoes remain in the chicken yard")
        print("Type 'draw' to draw a domino from the chicken yard")
        print("Type 'places' to list available places to play")
        print("Type 'score' to list the scores of the players")
        # print("Type 'surrender' to surrender the current round") # maybe remove
        print("Type 'quit' to quit the game")

    # game starting
    while playerHandSize > 0 and aiHandSize > 0 and chickenYardAmount > 0:
        if turn == 0:
            print("Player's Turn") # for testing
            for i in range(10): # print hand to player
                for j in range(10):
                    if player[i][j] == 1:
                        print("[",i,"|",j,"]", sep='', end='')
            print()
        elif turn == 1:
            print("AI's Turn") # for testing
            for i in range(10): # print hand to player ai for testing
                for j in range(10):
                    if ai[i][j] == 1:
                        print("[",i,"|",j,"]", sep='', end='')
            print()
        if doublePlayed == True:
            print("Double", double, "in play,", spotsPlayable[double], "spots remaining")
        else:
            locations()
        userInput = input("Enter move: ") 
        if userInput == "help":
            print("Type 'help' to list commands")
            print("Type 'play # #', where the #s are replaced by the domino you wish to play")
            print("Type 'doubles' to list the doubles that have been played so far")
            print("Type 'dominos' or 'dominoes' to list the number of each type of domino that has been played so far & how many dominoes remain in the chicken yard")
            print("Type 'draw' to draw a domino from the chicken yard")
            print("Type 'places' to list available places to play")
            print("Type 'score' to list the scores of the players")
            # print("Type 'surrender' to surrender the current round") # maybe remove
            print("Type 'quit' to quit the game")
        elif re.search("play ", userInput):
            playedDomino = userInput.split(" ")
            if turn == 0 and player[int(playedDomino[1])][int(playedDomino[2])] == 1:
                play(userInput)
            elif turn == 1 and ai[int(playedDomino[1])][int(playedDomino[2])] == 1:
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
            print("Player's score is", playerScore)
            print("AI's score is", aiScore)
        elif userInput == "surrender":
            for i in range(10):
                for j in range(10):
                    if turn == 0:
                        ai[i][j] = 0
                        aiHandSize = 0
                    elif turn == 1:
                        player[i][j] = 0
                        playerHandSize = 0
            break
        elif userInput == "quit":
            quit()
        elif userInput == "block": # debug command to test blocked game
            blockCheck = 2
        elif userInput == "win": # debug command to test winning
            for i in range(10):
                for j in range(10):
                    if turn == 0:
                        player[i][j] = 0
                        playerHandSize = 0
                    elif turn == 1:
                        ai[i][j] = 0
                        aiHandSize = 0
            
        if blockCheck > 1 or playerHandSize == 0 or aiHandSize == 0: # round end tests
            break

    for i in range(10): # calc score
        for j in range(10): 
            if player[i][j] == 1:
                player[i][j] = 0
                if i == 0 and j == 0:
                    playerScore = playerScore + 50
                else:
                    playerScore = playerScore + i
                    playerScore = playerScore + j
            elif ai[i][j] == 1:
                ai[i][j] = 0
                if i == 0 and j == 0:
                    aiScore = aiScore + 50
                else:
                    aiScore = aiScore + i
                    aiScore = aiScore + j

    if round == 0:
        if playerScore < aiScore:
            print("Player won with a score of", playerScore, "compared to the AI's", aiScore)
        elif aiScore < playerScore:
            print("The AI won with a score of", aiScore, "compared to player's", playerScore)
        elif playerScore == aiScore:
            print("Player and the AI tied with a score of", playerScore)
        else:
            print("There has been an error in the scoring")
        quit()
    else:
        round = round - 1
        blockCheck = 0