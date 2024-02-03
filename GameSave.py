import random
import datetime

def gamesave(sessionsave,cont,player_name):
    "function for write output in a text file"
    
    CurrentDateTime=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    #generate a random number within the range of 0000 to 9999
    RandomNumber=random.randint(0,9999)
    
    FileName=f"{CurrentDateTime}_{RandomNumber:04d}.txt"
    
    TextFile=open(FileName,"w")
    
        # Write details for each attempt
    for session in sessionsave:
        TextFile.write(f"Attempt: {session['attempt']}\n")
        TextFile.write(f"{player_name}'s life score is: {session['life_score']}\n")
        TextFile.write(f"Presented Enemies: {session['PresentedEnemies']}\n")
        TextFile.write(f"Seleted Number: {session['selected_number']}\n")
        TextFile.write(f"{session['FightStatus']}\n\n")

    #writing the game status to the text file
    TextFile.write(cont)

    #Closing the Text File
    TextFile.close()
    return
