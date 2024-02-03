def display_game_prompt(life_score,attempt,player_name):
    "Function for display the game prompt"
    
    content= f"\nAttempt : {attempt}" 
    print(content) #print the attempt number 
    content=f"\n{player_name}'s life score is:{life_score} "
    print(content) #print the players lifescore value

