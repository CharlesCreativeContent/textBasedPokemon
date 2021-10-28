#!/usr/bin/env python3
"""SC Research || Author: ShawnCharles@protonmail.com"""
"Pokemon Classes and useful dictionaries"
import crayons
import random
from assets.chadtricks import clear, print1by1, video
from assets.rooms import rooms
from assets.descriptions import descriptions
import json
#to start and stop music if we werent in virtual environment
import pygame.mixer
from pokemon.master import catch_em_all, get_pokemon
##ascii art

class Pokemon:
    def __init__(self,pokemonId,level):
        self.level = level
        self.id = pokemonId
        with open('assets/pokedex.txt',"r") as pokedex:
            stats = pokedex.readlines()
            self.name = stats[0].split("-")[pokemonId]
            self.attack = stats[1].split("-")[pokemonId]
            self.hp = {"base":int(stats[3].split("-")[pokemonId]), "max": (1+(level/25))*int(stats[3].split("-")[pokemonId]),"current":(1+(level/25))*int(stats[3].split("-")[pokemonId])}

            self.defense = stats[2].split("-")[pokemonId]
            self.speed = stats[4].split("-")[pokemonId]
            self.spAttack = stats[6].split("-")[pokemonId]
            self.spDefense = stats[5].split("-")[pokemonId]
            self.move1 = stats[7].split(".")[pokemonId]
            self.move2 = stats[8].split(".")[pokemonId]
            self.move3 = stats[9].split(".")[pokemonId]
            self.move4 = stats[10].split(".")[pokemonId]
            self.growth = 1+(level/25)

##Evolutions - nested Classes - Bulbasaur is-a Ivysaur, Ivysaur is-a Venusaur
##dont have ime to do

class Player:
    def __init__(self,room,inventory,badges,skills,pokemon):
        self.currentRoom = room
        self.inventory=inventory
        self.badges = badges
        self.skills = skills
        self.pokemon = pokemon
    def addItem(self,item):
        print(f'You obtained item {item}')
        self.inventory += [item]
    def takeItem(self,item):
        print(f'You lost the {item}')
        self.inventory.remove(item)
    def addSkill(self,newSkill):
        print(f'You obtained skill {newSkill}')
        self.skills += [newSkill]
    def earnedBadge(self):
        print(f'You obtained the {self.currentRoom}')
        self.badges += [self.currentRoom]
    def catchPokemon(self,poke):
        print(f'You obtained the {poke.name}')
        self.pokemon += [poke]
    

class Trainer(Player):
  def __init__(self, name, pokemon):
    super().__init__('',[],[],[],pokemon)
    self.name = name

#    start of save feature
#def loadPlayer(player):
   #"""load user data at start of game"""
    # Open the file in append & read mode ('a+')
    #with open("assets/user.txt", "a+") as user:
        # Move read cursor to the start of file.
        #user.seek(0)
        # If file is not empty then append '\n'
        #data = user.read(100)
        #if len(data) > 0:
        #user.write("\n")
        # Append text at the end of file
        #user.write("hello")

def validAction(action,player):
    currentPokemon = player.pokemon[0]
    validActions = {
            "R":True,
            "RUN":True,
            "C":True,
            "CATCH":True,
            "S":True,
            "SWITCH":True,
            currentPokemon.move1.upper():True,
            currentPokemon.move2.upper():True,
            currentPokemon.move3.upper():True,
            currentPokemon.move4.upper():True
            }
    if action in validActions:
        return True
    else:
        return False


def battle(player1, ai):
    """Battle Logic"""
    #stop the music
    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets/music/battle.mp3")

    pygame.mixer.music.play()

    emoticons = [crayons.red("Θ"),f"(╯°□°)╯",f"(╯°□°)╯︵{crayons.red('◓')}",f"{crayons.yellow('ϞϞ')}({crayons.red('๑')}⚈ ․ ⚈{crayons.red('๑')})∩","><(((o.^.o)","ଘ @(￣▵—▵￣)v(￣▵▵￣)@ ଓ",">(8☉)@@@oo<>","(>￣ー￣)"]
    vid = [f"(╯°□°)╯  "+ emoticons[7],f"(╯°□°)╯︵"+emoticons[7],f"(╯°□°)╯︵{crayons.red('◓')}",f"(╯°□°)╯ ︵{crayons.red('◓')}",f"(╯°□°)╯ {crayons.red('◓')}︵",f"(╯°□°)╯ ︵{crayons.red('◓')}",f"(╯°□°)╯ {crayons.red('◓')}︵",f"(╯°□°)╯ {crayons.red('◓')}"] 
    clear()
    defeated = []
    if len(ai.pokemon)<2:
        print(f"A wild {ai.pokemon[0].name} has appeared!")
        while True:
        #wild encounter
            currentPokemon = player1.pokemon[0]
            wildPokemon = ai.pokemon[0]

            if wildPokemon.hp["current"]<=0:
                clear()
                print("You won the battle!")
                player1.pokemon[0] = Pokemon(currentPokemon.id,currentPokemon.level+1)
                pygame.mixer.music.stop()
                pygame.mixer.music.load("assets/music/town.mp3")
                pygame.mixer.music.play()
                return player1
            elif currentPokemon.hp["current"]<=0:
                print(player1.pokemon[0].name,"has fainted!")
                player1.pokemon.sort(key=lambda poke:poke.hp["current"],reverse=True)
                if player1.pokemon[0].hp["current"]<=0:
                    ##All pokemon faint
                    clear()
                    print("You fainted!")
                    print("You wake up in Pallet Town!")
                    player1.currentRoom = "Pallet Town"
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets/music/town.mp3")
                    pygame.mixer.music.play()
                    return player1
                else:
                    choice = ''
                    while choice not in [pokemon.name for pokemon in player1.pokemon if pokemon.name==choice and pokemon.hp['current']>=0 ]:
                        choice = input(f"Choose your next pokemon to battle! {[pokemon.name for pokemon in player1.pokemon if pokemon.hp['current']>=0]}\n<{crayons.red('◓')}>").capitalize()
                    player1.pokemon = [pokemon for pokemon in player1.pokemon if pokemon.name==choice]+[pokemon for pokemon in player1.pokemon if pokemon.name!=choice]
        
            print('{0:<}              {1:>}'.format(currentPokemon.name,wildPokemon.name))
            print('{0:<}              {1:>}'.format(f"lvl: {currentPokemon.level}",wildPokemon.level))
            print('{0:<}              {1:>}'.format(f"hp:  {currentPokemon.hp['current']}",wildPokemon.hp["current"]))
            
            print(f"You can (R)un,\n use {player1.pokemon[0].move1}, {player1.pokemon[0].move2}, {player1.pokemon[0].move3}, {player1.pokemon[0].move4},\n or (S)witch pokemon\n  or try to (C)atch {ai.pokemon[0].name}")
            action = None
            while validAction(action,player1) == False:
                action = input(f"<{crayons.red('◓')}>").upper()
            if action=="S" or action=="SWITCH":
                choice = ''
                while choice not in [pokemon.name for pokemon in player1.pokemon if pokemon.name==choice]:
                    choice = input(f"Choose your next pokemon to battle! {[pokemon.name for pokemon in player1.pokemon if pokemon.hp['current']>=0]}\n<{crayons.red('◓')}>").capitalize()
                player1.pokemon = [pokemon for pokemon in player1.pokemon if pokemon.name==choice]+[pokemon for pokemon in player1.pokemon if pokemon.name!=choice]
                ##Deal Damage
                currentPokemon.hp["current"]-= int(wildPokemon.attack)*wildPokemon.growth
                clear()
                if currentPokemon.hp['current']<=0:
                    print(f"{currentPokemon.name} has fainted")
                print(f"{wildPokemon.name} dealt {int(wildPokemon.attack)*wildPokemon.growth} points of damage to {currentPokemon.name}")
            elif action=="R" or action=="RUN":
                clear()
                pygame.mixer.music.stop()
                pygame.mixer.music.load("assets/music/town.mp3")
                pygame.mixer.music.play()
                return player1
            elif action=="C" or action=="CATCH":
                video(vid)
                if random.random() > 0.5:
                    print(f"You caught {wildPokemon.name}")
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets/music/town.mp3")
                    pygame.mixer.music.play()
                    return player1
                else:
                    clear()
                    print(vid[0])
                    print(f"{wildPokemon.name} broke free!")
                    print()
                    ##Deal Damage
                    currentPokemon.hp["current"]-= int(wildPokemon.attack)*wildPokemon.growth
                    print(f"{wildPokemon.name} dealt {int(wildPokemon.attack)*wildPokemon.growth} points of damage to {currentPokemon.name}")
            else:
                ##Attack process
                wildPokemon.hp["current"]-= int(currentPokemon.attack)*currentPokemon.growth
                currentPokemon.hp["current"]-= int(wildPokemon.attack)*wildPokemon.growth
                clear()
                print(f"{currentPokemon.name} dealt {int(currentPokemon.attack)*currentPokemon.growth} points of damage")
                print(f"{wildPokemon.name} dealt {int(wildPokemon.attack)*wildPokemon.growth} points of damage")
    
    else:
            #trainer battle
        print(f"{ai.name} wants to battle!")
        while True:
            currentPokemon = player1.pokemon[0]

            if ai.pokemon[0].hp["current"]<=0:
                print(f"You defeated {ai.pokemon[0].name}!")
                ai.pokemon.remove(ai.pokemon[0])
                ##levelup Pokemon
                player1.pokemon[0] = Pokemon(currentPokemon.id,currentPokemon.level+1)
                print(f"{player1.pokemon[0].name} leveled up!")
            if len(ai.pokemon)<=0:
                clear()
                print(f"You defeated {ai.name}!")
                #levelup
                player1.pokemon[0] = Pokemon(currentPokemon.id,currentPokemon.level+1)
                pygame.mixer.music.stop()
                pygame.mixer.music.load("assets/music/town.mp3")
                pygame.mixer.music.play()
                return player1
            else:
                wildPokemon = ai.pokemon[0]
            #currentPokemon fainted

            if currentPokemon.hp["current"]<=0:
                print(player1.pokemon[0].name,"has fainted!")
                player1.pokemon.sort(key=lambda poke:poke.hp["current"],reverse=True)
                if player1.pokemon[0].hp["current"]<=0:
                    ##All pokemon faint
                    clear()
                    print("You fainted!")
                    print("You wake up in Pallet Town!")
                    player1.currentRoom = "Pallet Town"
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets/music/town.mp3")
                    pygame.mixer.music.play()
                    return player1
                else:
                    choice = ''
                    while choice not in [pokemon.name for pokemon in player1.pokemon if pokemon.name==choice and pokemon.hp['current']>=0 ]:
                        choice = input(f"Choose your next pokemon to battle! {[pokemon.name for pokemon in player1.pokemon if pokemon.hp['current']>=0]}\n<{crayons.red('◓')}>").capitalize()
                    player1.pokemon = [pokemon for pokemon in player1.pokemon if pokemon.name==choice]+[pokemon for pokemon in player1.pokemon if pokemon.name!=choice]

            wildPokemon = ai.pokemon[0]
            currentPokemon = player1.pokemon[0]
            print('{0:<}             {1:>}'.format(player1.pokemon[0].name,wildPokemon.name))
            print('{0:<}                  {1:>}'.format(f"lvl: {player1.pokemon[0].level}",wildPokemon.level))
            print('{0:<}              {1:>}'.format(f"hp:  {player1.pokemon[0].hp['current']}",wildPokemon.hp["current"]))
            action = None
            print(f"You can (R)un,\n use {player1.pokemon[0].move1}, {player1.pokemon[0].move2}, {player1.pokemon[0].move3}, {player1.pokemon[0].move4} \nor (S)witch pokemon")
            while validAction(action,player1) == False:
                action = input(f"<{crayons.red('◓')}>").upper()
                if action == "C" or action=="CATCH":
                    action = ''
            if action=="R" or action=="RUN":
                clear()
                print("you can't run away")
            elif action=="S" or action=="SWITCH":
                choice = ''
                while choice not in [pokemon.name for pokemon in player1.pokemon if pokemon.name==choice and pokemon.hp['current']>=0]:
                    choice = input(f"Choose your next pokemon to battle! {[pokemon.name for pokemon in player1.pokemon if pokemon.hp['current']>=0]}\n<{crayons.red('◓')}>").capitalize()
                player1.pokemon = [pokemon for pokemon in player1.pokemon if pokemon.name==choice]+[pokemon for pokemon in player1.pokemon if pokemon.name!=choice]
                ##Deal Damage
                currentPokemon.hp["current"]-= int(wildPokemon.attack)*wildPokemon.growth
                clear()
                if currentPokemon.hp['current']<=0:
                    print(f"{currentPokemon.name} has fainted")
                print(f"{wildPokemon.name} dealt {int(wildPokemon.attack)*wildPokemon.growth} points of damage to {currentPokemon.name}")
            else:
                ##Attack process
                wildPokemon.hp["current"]-= int(currentPokemon.attack)*currentPokemon.growth
                currentPokemon.hp["current"]-= int(wildPokemon.attack)*wildPokemon.growth
                clear()
                print(f"{currentPokemon.name} dealt {int(currentPokemon.attack)*currentPokemon.growth} points of damage")
                print(f"{wildPokemon.name} dealt {int(wildPokemon.attack)*wildPokemon.growth} points of damage")
                

def grass(player):
    """simulates random encounters"""
    if random.random()>0.5:
        pokemonId = random.choice(rooms[player.currentRoom]["pokemon"]["ids"])
        roomLevel = rooms[player.currentRoom]["pokemon"]["level"]
        level = random.randrange(roomLevel[0],roomLevel[1])
        player = battle(player,Trainer("chad",[Pokemon(pokemonId,level)]))
        return player
    else:
        return player

def gymBattle(player):
    """returns player after running Gym Battle"""
    gyms = {
            "Cinnabar Island": Trainer("Blaine",[Pokemon(78,60),Pokemon(38,75),Pokemon(136,59),Pokemon(59,60),Pokemon(6,65),Pokemon(146,75)]),
            "Cerulean City": Trainer("Misty",[Pokemon(55,56),Pokemon(148,75),Pokemon(134,1),Pokemon(121,60),Pokemon(130,60),Pokemon(9,70)]),
            "Pewter City": Trainer("Brock",[Pokemon(95,51),Pokemon(111,56),Pokemon(141,51),Pokemon(139,56),Pokemon(142,51),Pokemon(76,51)]),
            "Saffron City": Trainer("Sabrina",[Pokemon(122,60),Pokemon(124,56),Pokemon(97,51),Pokemon(80,56),Pokemon(103,60),Pokemon(65,70)]),
            "Vermillion City": Trainer("Lt. Surge",[Pokemon(101,60),Pokemon(135,56),Pokemon(125,51),Pokemon(82,56),Pokemon(127,70),Pokemon(26,65)]),
            "Celadon City": Trainer("Erika",[Pokemon(114,60),Pokemon(47,56),Pokemon(103,51),Pokemon(71,56),Pokemon(3,70),Pokemon(45,65)]),
            "Lavender Town": Trainer("Gary",[Pokemon(18,60),Pokemon(65,65),Pokemon(112,60),Pokemon(130,64),Pokemon(103,70),Pokemon(59,65)]),
            "Fuschia City": Trainer("Janine",[Pokemon(49,60),Pokemon(89,56),Pokemon(110,51),Pokemon(42,56),Pokemon(33,70),Pokemon(73,65)]),
            "Viridian City": Trainer("Giovanni",[Pokemon(111,45),Pokemon(51,42),Pokemon(31,44),Pokemon(34,45),Pokemon(111,50),Pokemon(150,150)]),
            "Indigo Plateau":[ Trainer("",[Pokemon(1,1)]),Trainer("",[Pokemon(1,1)])],
            "Santa's House": Trainer("Santa",[Pokemon(9,100),Pokemon(144,100)]),
            }
    
    player = battle(player,gyms[player.currentRoom])
    if player.pokemon[0].hp['current']>=0 and player.currentRoom not in player.badges:
        player.badges += [player.currentRoom]
        if player.currentRoom == "Pewter City":
            print('You obtained the skill flash')
            player.skills+=['flash']
        if player.currentRoom == "Cerulean City":
            print('You obtained the skill cut')
            player.skills+=['cut']
        if player.currentRoom == "Celadon City":
            print('You obtained the skill strength')
            player.skills+=['strength']
        if player.currentRoom == 'Saffron City':
            print('You obtained the skill surf')
            player.skills+=['surf']
    return player

def articunoBattle(player):
    """returns player after running Legendary Battle"""
    player = battle(player,Trainer("Legendary",[Pokemon(144,65)]))
    return player

def zapdosBattle(player):
    """returns player after running Legendary Battle"""
    player = battle(player,Trainer("Legendary",[Pokemon(145,65)]))
    return player

def moltresBattle(player):
    """returns player after running Legendary Battle"""
    player = battle(player,Trainer("Legendary",[Pokemon(146,65)]))
    return player

def mewTwoBattle(player):
    """returns player after running Legendary Battle"""
    player = battle(player,Trainer("Legendary",[Pokemon(150,65)]))
    return player

def mewBattle(player):
    """returns player after running Legendary Battle"""
    player = battle(player,Trainer("Legendary",[Pokemon(151,65)]))
    return player
def heal(player):
    for pokemon in player.pokemon:
        pokemon.hp['current']=pokemon.hp['max']
    clear()
    print("Your pokemon have been healed!")
    return player

def showInstructions():
    ##write good instructions

  #print a main menu and the commands
    print('''
Pokemon
========
Commands:
  go [direction]
  get [item]
  talk [person]
  [skill]
  q (quit)
''')
##Starting intro music and 
def intro():

    pygame.mixer.init()
    pygame.mixer.music.load("assets/music/intro.mp3")
    pygame.mixer.music.play()

    starter= [Pokemon(25,5),Pokemon(1,5),Pokemon(4,5),Pokemon(7,5)]
    chosen = ''
    while chosen not in [pokemon.name for pokemon in starter]:
        chosen = input(f"Professor Oak: What Pokemon would you like? {[pokemon.name for pokemon in starter]}\n<{crayons.red('◓')}>").title()
    ##Super God Pikachu!!
    player = Player("Pallet Town", [],[],["climb","fly","dig","surf","cut","strength","hidden power","flash"],[Pokemon(25,1000)]) 
    # Actual Starter Player = Player("Pallet Town", [],[],[],[])
    player.catchPokemon([pokemon for pokemon in starter if pokemon.name == chosen][0])
    pygame.mixer.music.stop()
    return player

def main():
    clear()
    print("██████╗  ██████╗ ██╗  ██╗███████╗███╗   ███╗ ██████╗ ███╗   ██╗\n██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗████╗  ██║\n██████╔╝██║   ██║█████╔╝ █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║\n██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║\n██║     ╚██████╔╝██║  ██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║\n╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n")
    validCommands = ["get","go","use", "fly","cut","climb", "surf", "hidden power", "flash","dig"]
   
    player = intro()
    move= ""
    
    pygame.mixer.music.load("assets/music/town.mp3")
    pygame.mixer.music.play()
    storage = []
    emoticons = [crayons.red("Θ"),f"(╯°□°)╯",f"(╯°□°)╯︵{crayons.red('◓')}",f"{crayons.yellow('ϞϞ')}({crayons.red('๑')}⚈ ․ ⚈{crayons.red('๑')})∩","><(((o.^.o)","ଘ @(￣▵—▵￣)v(￣▵▵￣)@ ଓ",">(8☉)@@@oo<>","(>￣ー￣)"]
    vid = [f"(╯°□°)╯  "+ emoticons[7],f"(╯°□°)╯︵"+emoticons[7],f"(╯°□°)╯︵{crayons.red('◓')}","(╯°□°)╯ ︵{crayons.red('◓')}","(╯°□°)╯ {crayons.red('◓')}︵","(╯°□°)╯ ︵{crayons.red('◓')}","(╯°□°)╯ {crayons.red('◓')}︵",f"(╯°□°)╯ {crayons.red('◓')}"]
    #Didnt have time to finish saves
    #loadPlayer()
    def showStatus():
  #print the player's current status
  #remove items from map that are in inventory
        for item in player.inventory:
            if item in rooms[player.currentRoom]["items"]:
                rooms[player.currentRoom]["items"].remove(item)
        print('Inventory :',player.inventory)
        print('Locations :',rooms[player.currentRoom]["locations"])
        print('Badges :',player.badges)
        print('Skills:',[skill for skill in player.skills if skill in rooms[player.currentRoom]["skills"]])
        print("You can go", ", ".join(rooms[player.currentRoom]['directions']))
        print('---------------------------')
        print('You are in',player.currentRoom)
        with open("assets/descriptions.txt","r") as allDescriptions:
  #print the Current Room description
            objects = allDescriptions.read().splitlines()
            for index,obj in enumerate(objects):
                if obj.split(" : ")[0]== player.currentRoom:
                    print(objects[index].split(" : ")[1])
                elif obj.split(" : ")[0] in rooms[player.currentRoom]["items"]:
                    print(objects[index].split(" : ")[1])
                    
    #clear()
    #showInstructions()
    
    #plays music but server doesnt have speakers


    while True and move !="q":
        ##if fail, load found file into game - version2
        ##Battle Sequence and leveling pokemon - accomplished
        ##Route Logic making a pokemon appear conditional before status message- accomplished
        ##1Puzzle
        ##Skill directions
        ##Skill Event 
        ##1Gym - accomplished
        if player.currentRoom[0]=="R":
            player = grass(player)
        
        if player.currentRoom=="Mt. Silver" and "Iceroot Carrot" in player.inventory:
            player = articunoBattle(player)
        
        if player.currentRoom=="Power Plant" and "Electirizer" in player.inventory:
            player = zapdosBattle(player)
        
        if player.currentRoom=="Cinnibar Island" and "Ho-oh Feather" in player.inventory:
            player = moltresBattle(player)
        
        showStatus()
        move= ""
        while move == '':
            move=input(f"<{crayons.red('◓')}>")
        move = move.lower().split(" ", 1)

        #if they type 'go' first
        if move[0] == 'go':
    #check that they are allowed wherever they want to go
            if move[1] in rooms[player.currentRoom]["directions"]:
      #set the current room to the new room
                player.currentRoom = rooms[player.currentRoom]["directions"][move[1]]
                clear()
            elif move[1] in rooms[player.currentRoom]["locations"]:
                if move[1] == "gym":
                    player=gymBattle(player)
                if move[1] == "pokecenter":
                    player=heal(player)
            else:
                clear()
                print('You can\'t go that way!')
        
        
        elif move[0] == 'fly':
            if move[1].title() in rooms:
                player.currentRoom = move[1].title()
                clear()
            else:
                print('You can\'t fly there!')
        elif move[0] in rooms[player.currentRoom]['skills']:
            clear()
            if player.currentRoom == "Power Plant":
                player.addItem('Electirizer')
                print('You Hear a Huge Explosion as a Bird Falls Through the Ceiling')
                rooms[player.currentRoom]
            if player.currentRoom == "Viridian Forest":
                print('You swiftly Climb the tree and find at the top there is a shining feather')
                player.addItem('Ho-oh Feather')
                rooms[player.currentRoom]['items'].remove('Ho-oh Feather')
            if player.currentRoom == "Mt. Moon":
                print('You dug deep into the dirt and got some delicious Iceroot Carrot')
                player.addItem('Iceroot Carrot')
                rooms[player.currentRoom]['items'].remove('Iceroot Carrot')

            player.currentRoom = rooms[player.currentRoom]['skills'][move[0]]
        elif move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
            if move[1].title() in rooms[player.currentRoom]["items"]:
      #add the item to their player.inventory
                move[1] = move[1].title()
                player.inventory += [move[1]]
      #display a helpful message
                clear()
                print(f"You put {move[1]} in your inventory")
    
      #delete the item from the room
                rooms[player.currentRoom]['items'].remove(move[1])
    #otherwise, if the item isn't there to get
            else:
      #tell them they can't get it  
                clear()
                print('Can\'t get ' + move[1] + '!')

        elif move[0] == 'help' :
            clear()
            showInstructions()
        else:
            clear()
            print("Say That Again Please!")

if __name__=="__main__":
    main()

