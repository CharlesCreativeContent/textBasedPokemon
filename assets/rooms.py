rooms = {
        'Pallet Town' : { 
            'directions' : {"north": "Route 1"},
            'items'  : [  ],
            'locations': ['pokecenter'],
            'skills': {'surf':'Route 21'}
            },
        'Victory Road' : {
            'directions' : {"north": "Indigo Plateau","south": "Route 26"},
            'items'  : [  ],
            'locations': [],
            'skills': []
            },
        'Viridian Forest' : {
            'directions' : {"north": "Route 2","south": "Viridian City"},
            'items'  : [ "Ho-oh Feather" ],
            'locations': [],
            'skills': {'climb': 'Viridian Forest'}
            },
        'Mt. Moon' : {
            'directions' : {"west": "Route 3","east": "Route 4"},
            'items'  : [ "Iceroot Carrot" ],
            'locations': [],
            'skills': {'dig': 'Mt. Moon'}
            },
        'Rock Tunnel' : {
            'directions' : {"west": "Route 9","south": "Route 10"},
            'items'  : [ "Kings Rock" ],
            'pokemon': {'level': [2,5],
            'ids': [16,19,25]},
            'locations': [],
            'skills': []
            },
        'Power Plant' : {
            'directions' : {"north": "Route 10","south": "Lavender Town"},
            'items'  : [ "Electirizer" ],
            'locations': [],
            'skills': {'flash': 'Power Plant'}
            },
        'Radio Tower' : {
            'directions' : {"outside": "Lavender Town", "exit": "Lavender Town", "leave": "Lavender Town"},
            'items'  : [  ],
            'pokemon': {'level': [2,5],
            'ids': [16,19,25]},
            'locations': [],
            'skills': []
            },
        'Silph Co.' : {
            'directions' : {"outside": "Saffron City", "exit": "Saffron City", "leave": "Saffron City"},
            'items'  : [  ],
            'locations': [],
            'skills': []
            },
        'Seafoam Islands' : {
            'directions' : {"west": "Route 20","east": "Route 19"},
            'items'  : [  ],
            'locations': [],
            'skills': []
            },
        'Tohjo Falls' : {
            'directions' : {"east": "Route 27"},
            'items'  : [  ],
            'locations': [],
            'skills': []
            },
        "Diglett's Cave": {
            'directions' : {"south": "Route 11"},
            'items'  : [  "Dragon Fang"],
            'locations': [],
            'skills': {'dig':"Diglet's Cave"}
            },
        "Diglet's Cave": {
            'directions' : {"north": "Route 3"},
            'items'  : [  ],
            'locations': [],
            'skills': {'dig':"Diglett's Cave"}
            },
        'Mt. Silver' : {
            'directions' : {"east": "Route 28"},
            'items'  : [  ],
            'locations': [],
            'skills': []
            },
        'Indigo Plateau' : {
            'directions' : {"south": "Victory Road"},
            'items'  : [  ],
            'locations': [],
            'skills': []
            },
        "Bill's House" : {
            'directions' : {"west": "Route 25"},
            'items'  : [  ],
            'locations': [],
            'skills': []
            },
        'Route 1' : {
            'directions' : {"north": "Viridian City", "south": "Pallet Town"},
            'items'  : [  ],
            'pokemon': {'level': [2,5],
            'ids': [16,19,25]},
            'locations': [],
            'skills': [] 
            },
        'Viridian City' : {
            'directions' : {"north": "Viridian Forest", "south": "Route 1","west": "Route 22"},
            'items'  : [  ],
            'locations': ['gym','pokecenter','pokemart'],
            'skills': []
            },
        'Pewter City' : {
            'directions' : {"east": "Route 3", "south": "Route 2"},
            'items'  : [  ],
            'locations': ['gym','pokecenter','pokemart'],
            'skills': []
            },
        'Cerulean City' : {
            'directions' : {"north": "Route 24", "south": "Route 5", "east": "Route 9", "west": "Route 4"},
            'items'  : [  ],
            'locations': ['gym','pokecenter','pokemart'],
            'skills': []
            },
        'Celadon City' : {
            'directions' : {"west": "Route 16", "east": "Route 7"},
            'items'  : [  ],
            'locations': ['gym','pokecenter','pokemart'],
            'skills': []
            },
        'Saffron City' : {
            'directions' : {"north": "Route 5", "south": "Route 6", "east": "Route 8", "west": "Route 7"},
            'items'  : [  ],
            'locations': ['gym','pokecenter','pokemart'],
            'skills': []
            },
        'Lavender Town' : {
            'directions' : {"north": "Power Plant", "south": "Route 12", "west": "Route 8"},
            'items'  : [  ],
            'locations': ['gym','pokecenter','pokemart'],
            'skills': []
            },
        'Vermillion City' : {
            'directions' : {"north": "Route 6", "east": "Route 11"},
            'items'  : [  ],
            'locations': ['gym','pokecenter','pokemart'],
            'skills': []
            },
        'Fuschia City' : {
            'directions' : {"west": "Route 18", "east": "Route 15"},
            'items'  : [  ],
            'locations': ['gym','pokecenter','pokemart'],
            'skills': {'surf':'Route 19'}
            },
        'Cinnibar Island' : {
            'directions' : {"north": "Route 21", "east": "Route 20"},
            'items'  : [  ],
            'locations': ['gym','pokecenter','pokemart'],
            'skills': []
            },
        'Route 2' : {
            'directions' : {"north": "Pewter City", "south": "Viridian Forest"},
            'items'  : [  ],
            'pokemon': {'level': [4,6],
                'ids': [10,11,12,13,14,15,16,17,18,19,25,122, 23]},
            'locations': [],
            'skills': []
            },
        'Route 3' : {
            'directions' : {"west": "Pewter City","east": "Mt. Moon", "south": "Diglet's Cave"},
            'items'  : [  ],
            'pokemon': {'level': [6,9],
                'ids': [16,19,21,27,39,56,23,24,41,]},
            'locations': [],
            'skills': []
            },
        'Route 4' : {
            'directions' : {"east": "Cerulean City", "west": "Mt. Moon"},
            'items'  : [  ],
            'pokemon': {'level': [8,12],
                'ids': [19,21,23,27,56,129,60,118,54,98,119,]},
            'locations': [],
            'skills': []
            },
        'Route 5' : {
            'directions' : {"north": "Cerulean City"},
            'items'  : [  ],
            'pokemon': {'level': [10,15],
                'ids': [16,17,19,43,52,56,63,44,69,]},
            'locations': [],
            'skills': {'strength': 'Saffron City'}
            },
        'Route 6' : {
            'directions' : {"north": "Saffron City", "south": "Vermillion City"},
            'items'  : [  ],
            'pokemon': {'level': [12,18],
                'ids': [16,17,19,39,43,52,56,63,69,54,55,129,60,118,90,98,96,81,129]},
            'locations': [],
            'skills': []
            },
        'Route 7' : {
            'directions' : {"west": "Celadon City", "east": "Saffron City"},
            'items'  : [  ],
            'pokemon': {'level': [14,21],
                'ids': [16,17,19,37,39,43,52,56,58,63,69,20,21,53,]},
            'locations': [],
            'skills': []
            },
        'Route 8' : {
            'directions' : {"east": "Lavender Town", "west": "Saffron City"},
            'items'  : [  ],
            'pokemon': {'level': [16,24],
                'ids': [16,17,19,23,27,37,39,52,56,58,63,64,93]},
            'locations': [],
            'skills': []
            },
        'Route 9' : {
            'directions' : {"west": "Cerulean City", "east": "Rock Tunnel"},
            'items'  : [  ],
            'pokemon': {'level': [18,27],
                'ids': [19,20,21,22,23,27,29,30,33,41,48,49,57,56,105,118,119,129]},
            'locations': [],
            'skills': []
            },
        'Route 10' : {
            'directions' : {"north": "Rock Tunnel"},
            'items'  : [  ],
            'pokemon': {'level': [20,30],
                'ids': [19,20,21,23,27,29,32,66,81,100,129,60,118,79,98,99,116,22,49,48,41,105]},
            'locations': [],
            'skills': {'surf':'Power Plant'}
            },
        'Route 11' : {
            'directions' : {"north": "Diglett's Cave", "west": "Vermillion City", "east": "Route 12"},
            'items'  : [  ],
            'pokemon': {'level': [22,33],
                'ids': [16,17,19,20,21,23,27,96,129,60,118,72,90,98,116,30,51,52,81,96,97]},
            'locations': [],
            'skills': []
            },
        'Route 12' : {
            'directions' : {"north": "Lavender", "south": "Route 13", "west": "Route 11"},
            'items'  : [  ],
            'pokemon': {'level': [24,36],
                'ids': [16,17,43,44,48,69,70,83,79,80,129,60,118,72,98,116,117,143,73]},
            'locations': [],
            'skills': []
            },
        'Route 13' : {
            'directions' : {"north": "Route 12", "south": "Route 14"},
            'items'  : [  ],
            'pokemon': {'level': [26,39],
                'ids': [16,17,43,44,48,70,69,83,132,79,80,129,60,118,72,98,116,117,20,33,17,113]},
            'locations': [],
            'skills': []
            },
        'Route 14' : {
            'directions' : {"north": "Route 13", "south": "Route 15"},
            'items'  : [  ],
            'pokemon': {'level': [28,42],
                'ids': [16,17,43,44,48,49,69,70,132,129,60,118,30,33,113,17,48,49,98,120,99,142]},
            'locations': [],
            'skills': []
            },
        'Route 15' : {
            'directions' : {"north": "Route 14", "west": "Fuschia City"},
            'items'  : [  ],
            'pokemon': {'level': [30,45],
                'ids': [16,17,43,44,48,49,69,70,30,33,113,48,49]},
            'locations': [],
            'skills': []
            },
        'Route 16' : {
            'directions' : {"south": "Route 17","east": "Celadon City"},
            'items'  : [  ],
            'pokemon': {'level': [32,48],
                'ids': [19,20,21,22,143,88,89,]},
            'locations': [],
            'skills': []
            },
        'Route 17' : {
            'directions' : {"north": "Route 16", "south": "Route 18"},
            'items'  : [ ],
            'pokemon': {'level': [34,51],
                'ids': [20,21,22,77,84,85,129,60,118,72,90,98,]},
            'locations': [],
            'skills': []
            },
        'Route 18' : {
            'directions' : {"north": "Route 17","east": "Fuschia City"},
            'items'  : [  ],
            'pokemon': {'level': [36,54],
                'ids': [19,20,21,22,84,129,60,118,72,90,98,47,88,89]},
            'locations': [],
            'skills': []
            },
        'Route 19' : {
            'directions' : {"north": "Fuschia City", "west": "Seafoam Islands"},
            'items'  : [  ],
            'pokemon': {'level': [38,57],
                'ids': [72,129,60,118,73,90,116,118,120,98,99,]},
            'locations': [],
            'skills': []
            },
        'Route 20' : {
            'directions' : {"west": "Cinnibar Island", "east": "Seafoam Islands"},
            'items'  : [  ],
            'pokemon': {'level': [40,60],
                'ids': [72,129,60,118,73,90,]},
            'locations': [],
            'skills': []
            },
        'Route 21' : {
            'directions' : {"north": "Pallet Town","south": "Cinnibar Island"},
            'items'  : [  ],
            'pokemon': {'level': [42,63],
                'ids': [16,17,19,20,114,72,129,60,118,73,90,116,118,120]},
            'locations': [],
            'skills': []
            },
        'Route 22' : {
            'directions' : {"east": "Viridian City"},
            'items'  : [  ],
            'pokemon': {'level': [44,66],
                'ids': [19,21,29,32,56,129,77,]},
            'locations': [],
            'skills': {'cut':'Route 26'}
            },
        'Route 24' : {
            'directions' : {"north": "Route 25", "south": "Cerulean City"},
            'items'  : [  ],
            'pokemon': {'level': [48,72],
                'ids': [10,11,13,14,16,17,43,48,63,69,129,60,118,54,98,119,63,70,12,49,44]},
            'locations': [],
            'skills': []
            },
        'Route 25' : {
            'directions' : {"south": "Route 24", "east": "Bill's House"},
            'items'  : [  ],
            'pokemon': {'level': [50,75],
                'ids': [10,11,12,13,14,15,16,17,43,48,63,69,129,60,118,54,98,118,49,119]},
            'locations': [],
            'skills': []
            },
        'Route 26' : {
            'directions' : {"north": "Victory Road", "south": "Route 27","east": "Route 22", "west": "Route 28"},
            'items'  : [  ],
            'pokemon': {'level': [52,78],
                'ids': [20,24,28,77,84,72,129,90,129,73,15,102]},
            'locations': [],
            'skills': []
            },
        'Route 27' : {
            'directions' : {"north": "Route 26","west": "Tohjo Falls"},
            'items'  : [ ],
            'pokemon': {'level': [54,81],
                'ids': [20,24,28,85,73,12,15]},
            'locations': [],
            'skills': []
            },
        'Route 28' : {
            'directions' : {"east": "Route 26","west": "Mt. Silver"},
            'items'  : [  ],
            'pokemon': {'level': [56,84],
                'ids': [77,78,24,84,61,42]},
            'locations': [],
            'skills': []
            },
        }
