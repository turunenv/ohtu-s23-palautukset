from player import Player
import requests

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    fin_players = [player for player in players if player.nationality == 'FIN']

    #sort based on points
    fin_players.sort(
            key = lambda player: player.goals + player.assists,
            reverse = True
        )

    print("Players from FIN:\n")

    for player in fin_players:
        print(player)

if __name__ == "__main__":
    main()
