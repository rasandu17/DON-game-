import random
from .Lifescore import generate_life_score
from .GamePrompt import display_game_prompt

def play_game():
    #Initializing variables
    sessionsave=[]
    
    player_name = input("Enter your name: ")#Getting user name as an input
    life_score = generate_life_score()
    attempts= 20
    count = 0

    #Looping the program for multiple attempts
    for attempt in range(1, attempts + 1):
        display_game_prompt(life_score, attempt,player_name)
        count = count + 1

        #Random number generate, generating 5 random numbers based on the attempt range
        if count >= 1 and count <= 5:
            numbers_to_fight = random.sample(range(15, 101),5)
            for i in numbers_to_fight:
                print(i,end=' ')
                
                
        elif count >= 6 and count <= 10:
            numbers_to_fight = random.sample(range(250, 2001),5)
            for i in numbers_to_fight:
                print(i,end=' ')
            
            
        
        elif count >= 11 and count <=15:
            numbers_to_fight = random.sample(range(3000, 10001),5)
            for i in numbers_to_fight:
                print(i,end=' ')
                
            

        elif count >= 16 and count <=20:
            numbers_to_fight = random.sample(range(20000, 100001),5)
            for i in numbers_to_fight:
                print(i,end=' ')
                
                
#Number selections
        #getting user input numbers as an input, other than print 'enemy'        
        try:
            print("")
            selected_number= int(input("Select a number to fight: "))
        except ValueError:
            print("No such enemy\n")
            #Recording a value error input attempt and endig the game
            sessionsave.append({
                'attempt': attempt,
                'life_score':life_score,
                'PresentedEnemies': f"{numbers_to_fight[0]} {numbers_to_fight[1]} {numbers_to_fight[2]} {numbers_to_fight[3]} {numbers_to_fight[4]}",
                'selected_number': selected_number,
                'FightStatus': 'Fight Lost'})
            break
        
        #Checking if the user selected number is in the given 5 random numbers 
        if selected_number in numbers_to_fight:
            #cheacking if the user selected number is less or equal to the lifescore
            if selected_number <= life_score:
                #updating the life score and recording a successful attempt
                print(f"{player_name} killed", selected_number)
                life_score += selected_number
                sessionsave.append({
                    'attempt': attempt,
                    'life_score':life_score,
                    'PresentedEnemies': f"{numbers_to_fight[0]} {numbers_to_fight[1]} {numbers_to_fight[2]} {numbers_to_fight[3]} {numbers_to_fight[4]}",
                    'selected_number': selected_number,
                    'FightStatus': 'Fight Won'})

                
            else:
                killed=f"{selected_number} killed {player_name}\n"
                print(killed)
                #Recording an unsuccessful attempt and ending the game
                sessionsave.append({
                    'attempt': attempt,
                    'life_score':life_score,
                    'PresentedEnemies': f"{numbers_to_fight[0]} {numbers_to_fight[1]} {numbers_to_fight[2]} {numbers_to_fight[3]} {numbers_to_fight[4]}",
                    'selected_number': selected_number,
                    'FightStatus': 'Fight Lost'})
                break
        else:
            noenemy=f"\nNo such enemy"
            print("No such enemy")
            #Recording an invalid selected number input and ending the game
            sessionsave.append({
                    'attempt': attempt,
                    'life_score':life_score,
                    'PresentedEnemies': f"{numbers_to_fight[0]} {numbers_to_fight[1]} {numbers_to_fight[2]} {numbers_to_fight[3]} {numbers_to_fight[4]}",
                    'selected_number': selected_number,
                    'FightStatus': 'Fight Lost'})
            break
    return  player_name,life_score, attempt,sessionsave
