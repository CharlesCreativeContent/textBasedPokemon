#!/usr/bin/env python3
"Pokemon Classes and useful dictionaries"

class Pokemon:
    def __init__(self,pokemonId,lvl):
        self.lvl = lvl
        self.id = pokemonId
        with open('pokedex.txt',"r") as pokedex:
            stats = pokedex.readlines()
            self.name = stats[0].split("-")[pokemonId]
            self.attack = stats[1].split("-")[pokemonId]
            self.hp = stats[3].split("-")[pokemonId]
            self.defense = stats[2].split("-")[pokemonId]
            self.speed = stats[4].split("-")[pokemonId]
            self.spAttack = stats[6].split("-")[pokemonId]
            self.spDefense = stats[5].split("-")[pokemonId]
            self.move1 = stats[7].split("-")[pokemonId]
            self.move2 = stats[8].split("-")[pokemonId]
            self.move3 = stats[9].split("-")[pokemonId]
            self.move4 = stats[10].split("-")[pokemonId]

def main():
    hooh = Pokemon(5,50)
    print(hooh.name,hooh.move1)



#from playsound import playsound
#playsound('intro.mp3')

