#Importing modules
from GameModules.StartGame import play_game
from GameModules.Gamestatus import gamestatus
from GameModules.GameSave import gamesave
   
#Intializing variables
player_name=''
attempt=0
life_score=0
numbers_to_fight=[]
selected_number=''
killed=0
noenemy=0
sessionsave=[]

#----------------Main Program--------------------

#call the function part
player_name, life_score, attempt,sessionsave= play_game()

cont=gamestatus(player_name,attempt,life_score)
gamesave(sessionsave,cont,player_name)
