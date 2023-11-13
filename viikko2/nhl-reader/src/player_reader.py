import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        json_response = requests.get(self.url).json()

        players = []

        for dict in json_response:
            player = Player(dict)
            players.append(player)

        return players