import json
import jsonlines


with open("full_bga.json", "r") as f:
    data = json.loads(f.read())


def json_refiner(z):
    for game in z:
        refined_game = {}

        for x in game:

            if len(game[x]) == 0:
                refined_game[x] = None

            if x in ["num_of_games_played", "duration"]:
                replacement = ""
                for y in game[x]:
                    if y.isdigit():
                        replacement += y
                refined_game[x] = int(replacement)


            elif x in ["complexity", "strategy", "luck", "interaction", "year_released"]:
                if len(game[x]) == 0:
                    refined_game[x] = None
                else:
                    refined_game[x] = int(game[x])

            elif x == "available_since":
                vari = game[x][-4:] + "-" + game[x][0:2] + "-" + game[x][5:7]
                refined_game[x] = vari

            elif x == "num_of_players":
                if len(game[x]) == 1:
                    refined_game["min_players"] = int(game["num_of_players"])
                    refined_game["max_players"] = int(game["num_of_players"])
                elif len(game[x]) >= 6:
                    if game[x][-2].isdigit():
                        refined_game["min_players"] = int(game["num_of_players"][0])
                        refined_game["max_players"] = int(game["num_of_players"][-2:])
                    else:
                        refined_game["min_players"] = int(game["num_of_players"][0])
                        refined_game["max_players"] = int(game["num_of_players"][-1])

                else:
                    refined_game["min_players"] = int(game["num_of_players"][0])
                    refined_game["max_players"] = int(game["num_of_players"][-1])

            else:
                refined_game[x] = game[x]

        yield refined_game


with jsonlines.open("output.jsonl", mode='w') as writer:
    for item in json_refiner(data):
        writer.write(item)
