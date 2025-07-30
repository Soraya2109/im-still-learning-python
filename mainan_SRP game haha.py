# 14. SCISSORS ROCK PAPER GAME

import random

rps = ("scissors", "rock", "paper")
player_win = 0
bot_win = 0


while True :
    player = None
    bot = random.choice(rps)


    print("--SCISSORS ROCK PAPER--")
    player = input("scissors/rock/paper : ").lower()
    if player not in rps and player != "quit" :
        print("Apaansih??")
        continue 

    elif player == "quit" :
        break
        

    print(f"You = {player}")
    print(f"Computer = {bot}")

    if player == bot :
        print("Seri!")
    elif player == "scissors" and bot == "paper" :
        print("You win!")
        player_win += 1
    elif player == "scissors" and bot == "rock" :
        print("You lose!")
        bot_win += 1
    elif player == "rock" and bot == "paper" :
        print("You lose!")
        bot_win += 1
    elif player == "rock" and bot == "scissors" :
        print("You win!")
        player_win += 1
    elif player == "paper" and bot == "scissors" :
        print("You lose!")
        bot_win += 1
    elif player == "paper" and bot == "rock" :
        print("You win!")
        player_win += 1


    print(f"Score saat ini = {player_win} vs {bot_win}")
    print("--------------------")

print(f"Score akhir = {player_win} vs {bot_win}")