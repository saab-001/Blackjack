import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def start():
    
    start_select = input("Do you want to play Blackjack? Type 'y' or 'n': ").capitalize()
    
    if start_select == "Y":
        print(logo)
    if start_select == "N":
        exit()
    if start_select != "Y" and "N":
        print("\nInvalid input!\n")
        start()

start()

def play(Colect_user,Colect_bot):

    Cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    Card_Drawn_user = [random.choice(Cards)]
    Card_Drawn_bot = [random.choice(Cards)]
    bot_points = sum(Colect_bot) + Card_Drawn_bot[0]
    user_points = sum(Colect_user) + Card_Drawn_user[0]
    
    if Card_Drawn_bot[0] == 11 and bot_points>10:
        Card_Drawn_bot[0] = 1

    if Card_Drawn_user[0] == 11 and user_points>10:
        Card_Drawn_user[0] = 1
    
    Colect_bot += Card_Drawn_bot
    Colect_user += Card_Drawn_user
    user_points = sum(Colect_user)
    bot_points = sum(Colect_bot)

    if len(Colect_user) == 1:
        play(Colect_user, Colect_bot)

    if user_points > 21:
        print("\nYour final hand: " + str(Colect_user) + "\t\t|\tFinal score: " + str(user_points))
        print("Computer's final hand: " + str(Colect_bot[0]) + "\t\t|\tFinal score: " + str(user_points))
        print("\nYou went over 21.\nYou Lose!!!")
        exit()
        
    print("Your cards: " + str(Colect_user) + "\t|\tCurrent score: " + str(user_points))
    print("Computer's first card: " + str(Colect_bot[0]))

    def Keep_playing(Colect_bot):
        selection = input("type 'y' to deal or 'n' to pass: ").capitalize()
        
        if selection == "Y":
            play(Colect_user,Colect_bot)

        if selection == "N":
            user_points = sum(Colect_user)
            bot_points = sum(Colect_bot)  

            while bot_points < 17:
                Colect_bot += [random.choice(Cards)]
                bot_points = sum(Colect_bot)
              
            if user_points < bot_points:
                print("\nYour final hand: " + str(Colect_user) + "\t|\tFinal score: " + str(user_points))
                print("Computer's final hand: " + str(Colect_bot[0]) + "\t|\tFinal score: " + str(bot_points))
                print("\n\tYou Lose!!!")
                exit()

            if user_points == bot_points:
                print("\nYour final hand: " + str(Colect_user) + "\t|\tFinal score: " + str(user_points))
                print("Computer's final hand: " + str(Colect_bot[0]) + "\t|\tFinal score: " + str(bot_points))
                print("\n\tit's a Draw!!!")
                exit()

            if user_points > bot_points:
                print("\nYour final hand: " + str(Colect_user) + "\t|\tFinal score: " + str(user_points))
                print("Computer's final hand: " + str(Colect_bot[0]) + "\t|\tFinal score: " + str(bot_points))
                print("\n\tYou Win!!!")
                exit()
            
        if selection != "Y" and selection != "N":
            print("\nInvalid input!\n")
            Keep_playing(Colect_bot)

    Keep_playing(Colect_bot)

play([],[])
