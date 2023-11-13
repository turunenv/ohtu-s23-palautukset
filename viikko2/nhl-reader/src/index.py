from player import Player
import requests

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    fin_players = [player for player in players if player.nationality == 'FIN']

    print("Players from FIN:")

    for player in fin_players:
        print(player)

if __name__ == "__main__":
    main()
