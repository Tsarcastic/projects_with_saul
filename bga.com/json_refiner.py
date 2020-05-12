import json

data = []
for line in open("test.json", 'r'):
    data.append(json.loads(line))


#test = {"name": "Race for the Galaxy", "designer": "Tom Lehmann", "artist": "Claus Stephan & Martin Hoffmann", "publisher/editor": "Rio Grande Games", "developed_by": "Board Game Arena, Galehar ( galehar )", "num_of_games_played": "7 259 579", "complexity": "4", "strategy": "3", "luck": "2", "interaction": "1", "available_since": "11 / 30 / 2010", "release": "200214-1053", "year": "2007"},

def json_refiner(z):
    for game in z:
        for x in game:

            if len(game[x]) == 0:
                game[x] = None

            if x in ["num_of_games_played", "duration"]:
                replacement = ""
                for y in game[x]:
                    if y.isdigit():
                        replacement += y
                game[x] = int(replacement)


            elif x in ["complexity", "strategy", "luck", "interaction", "year_released"]:
                game[x] = int(game[x])

            elif x == "available_since":
                vari = game[x][-4:] + "-" + game[x][0:2] + "-" + game[x][5:7]
                game[x] = vari

            elif x == "num_of_players":
                if len(x) == 1:
                    game["min_players"] = x
                    game["max_players"] = x
                else:
                    game["min_players"] = int(game["num_of_players"[0]])
                    game["max_players"] = int(game["num_of_players"[-1]])
        print(game)

json_refiner(data)