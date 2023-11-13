class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = filter(
                        lambda player: player.nationality == nationality,
                        self.players
                    )
        
        #turn the iterator object into a list
        players = list(players)

        players.sort(
            key = lambda player: player.goals + player.assists,
            reverse = True
        )

        return players