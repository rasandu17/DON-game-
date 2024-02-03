def gamestatus(player_name,attempt,life_score):
    "Provides the Game status"
    
    if attempt==20:
        cont = f"\n*** Game status ***\nPlayer name: {player_name}\nTotal attempts: {attempt}\nFinal life score: {life_score}\n{player_name} saved letter-kind!!"
        print(cont)
    else:
        cont = f"\n*** Game status ***\nPlayer name: {player_name}\nTotal attempts: {attempt}\nFinal life score: {life_score}\n{player_name} was Defeted!!!"
        print(cont)
    return cont
