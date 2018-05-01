import pandas as pd
import numpy as np
import matplotlib.pyplot as plott


def show_info(data):
    create_type_pie_chart(data)
    create_genre_pie_chart(data)
    create_rating_to_price(data)
    create_recommendation_to_price(data)
    create_player_count_to_price(data)
    create_player_count_to_recommendation(data)
    create_player_count_to_rating(data)
    main(data)



def create_type_pie_chart(data):
    free_count = data[data['IsFree'] == True].count()
    paid_count = data[data['IsFree'] == False].count()
    temp = {'': pd.Series([free_count[1], paid_count[1]],
                          index=['Free games', 'Paid games'])}
    free_paid_df = pd.DataFrame(temp)
    free_paid_df.plot(kind='pie', title='Type of games', figsize=(6, 6), subplots=True)
    plott.savefig("./type_of_games.png", bbox_inches='tight')
    plott.close()


def create_genre_pie_chart(data):
    non_game_count = data[data['GenreIsNonGame'] == True].count()
    indie_game_count = data[data['GenreIsIndie'] == True].count()
    action_game_count = data[data['GenreIsAction'] == True].count()
    adventure_game_count = data[data['GenreIsAdventure'] == True].count()
    casual_game_count = data[data['GenreIsCasual'] == True].count()
    strategy_game_count = data[data['GenreIsStrategy'] == True].count()
    rpg_game_count = data[data['GenreIsRPG'] == True].count()
    simulation_game_count = data[data['GenreIsSimulation'] == True].count()
    early_access_game_count = data[data['GenreIsEarlyAccess'] == True].count()
    free_to_play_game_count = data[data['GenreIsFreeToPlay'] == True].count()
    sports_game_count = data[data['GenreIsSports'] == True].count()
    racing_game_count = data[data['GenreIsRacing'] == True].count()
    massive_mp_game_count = data[data['GenreIsMassivelyMultiplayer'] == True].count()
    temp = {'': pd.Series([non_game_count[1], indie_game_count[1], action_game_count[1],
                           adventure_game_count[1], casual_game_count[1], strategy_game_count[1],
                           rpg_game_count[1], simulation_game_count[1], early_access_game_count[1],
                           free_to_play_game_count[1], sports_game_count[1], racing_game_count[1],
                           massive_mp_game_count[1]],
                          index=['Non game', 'Indie', 'Action', 'Adventure', 'Casual',
                                 'Strategy', 'RPG', 'Simulation', 'Early Access', 'Free To Play',
                                 'Sports', 'Racing', 'Massive Multiplayer'])}
    game_type_df = pd.DataFrame(temp)
    game_type_df.plot(kind='pie', title='Genre of games', figsize=(12, 12), subplots=True)
    plott.savefig("./genre_of_games.png", bbox_inches='tight')
    plott.close()


def create_rating_to_price(data):
    rating_to_price = plott.scatter(data['PriceInitial'], data['Metacritic'])
    plott.xlabel("Price in USD")
    plott.ylabel("Mean Rating")
    plott.xlim((0, 80))
    plott.ylim(20, 100)
    plott.savefig("./rating_to_price.png", bbox_inches='tight')
    plott.close()


def create_recommendation_to_price(data):
    recommendation_to_price = plott.scatter(data['PriceInitial'], data['RecommendationCount'])
    plott.xlabel("Price in USD")
    plott.ylabel("Recommendation count")
    plott.xlim((0, 100))
    plott.ylim((100,200000))
    plott.savefig("./recommendation_to_price.png", bbox_inches='tight')
    plott.close()


def create_player_count_to_price(data):
    player_count_to_price = plott.scatter(data['PriceInitial'], data['SteamSpyPlayersEstimate'])
    plott.xlabel("Price in USD")
    plott.ylabel("Player count")
    plott.xlim((0, 100))
    plott.ylim((0, 5000000))
    plott.savefig("./player_count_to_price.png", bbox_inches='tight')
    plott.close()


def create_player_count_to_recommendation(data):
    create_player_count_to_recommendation = plott.scatter(data['RecommendationCount'], data['SteamSpyPlayersEstimate'])
    plott.xlabel("Recommendation count")
    plott.ylabel("Player count")
    plott.xlim((0, 200000))
    plott.ylim((0, 5000000))
    plott.savefig("./player_count_to_recommendation.png", bbox_inches='tight')
    plott.close()


def create_player_count_to_rating(data):
    create_player_count_to_rating = plott.scatter(data['Metacritic'], data['SteamSpyPlayersEstimate'])
    plott.xlabel("Ratings")
    plott.ylabel("Player count")
    plott.xlim((1, 100))
    plott.ylim((0, 5000000))
    plott.savefig("./player_count_to_rating.png", bbox_inches='tight')
    plott.close()


def search(data):
    print('If you want to return to previous menu, please enter "null"')
    val = input('please enter the gamename you want to search: ')

    if val == 'null':
        main(data)

    res = data[data['Name'] == val][['ID', 'Name', 'ReleaseDate', 'Metacritic']]
    print(res)
    main(data)

def recommend(data):
    print('1. Give recommendation by your game habit')
    print('2. Give recommendation by specific game type')
    print('0. Return to previous menu')
    val = input('please select: ')

    if val == '0':
        main(data)
    elif val == '1':
        # TODO
        pass
    elif val == '2':
        pass
        # TODO
    else:
        print('Invalid input, please select again: ')
        recommend(data)
    main(data)

def rank(data):
    print('For "Overall Rank of sells", press "1"')
    print('For "Overall Rank of players", press "2"')
    print('For "New Release Rank", press "3"')
    print('For returning to previous menu， press "0"')
    val = input('please select: ')
    if val == '0':
        main(data)
    else:
        print('Invalid input, please select again: ')
        rank(data)
    main(data)



def main(data):
    print('############################################################')
    print('Welcome to use game box!!!')
    print('1. Basic info(Overview)')
    print('2. Search information by name')
    print('3. Recommendation')
    print('4. Rank Board')
    print('0. Exit')
    print('############################################################')
    val = input("Please enter the function you like (eg: 1): ")

    if val == '1':
        show_info(data)
    elif val == '2':
        search(data)
    elif val == '3':
        recommend(data)
    elif val == '4':
        rank(data)
    elif val == '0':
        print('Thank you for using our product!')
        exit()
    else:
        print('Invalid input, please select again: ')
        main(data)

if __name__ == "__main__":
    data = pd.read_excel("./data.xlsx", 'processed')
    main(data)
