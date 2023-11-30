from tennis_player import TennisPlayer

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = TennisPlayer(player1_name)
        self.player2 = TennisPlayer(player2_name)

        self.scores = {
            "even": {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
                3: "Deuce"
            },
            "individual": {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty"
            }
        }

    def get_player_names(self):
        return [self.player1.name, self.player2.name]
    
    def get_player_points(self):
        return [self.player1.points, self.player2.points]

    def get_players_as_dict(self):
        return {
            self.player1.name: self.player1,
            self.player2.name: self.player2
        }

    def won_point(self, player_name):
        if player_name in self.get_player_names():
            player_dict = self.get_players_as_dict()
            player_dict[player_name].increment_points()

    def get_max_points_of_players(self):
        return max(self.player1.points, self.player2.points)
    
    def get_points_diff_of_players(self):
        return abs(self.player1.points - self.player2.points)
    
    def get_player_with_more_points(self):
        if self.player1.points == self.player2.points:
            return None
        return self.player1 if self.player1.points > self.player2.points else self.player2
    
    def points_are_even(self):
        points = self.get_player_points()

        return points[0] == points[1]
    
    def player_has_advantage(self):
        if self.get_points_diff_of_players() == 1 and self.get_max_points_of_players() >= 4:
            return True
        
        return False
    
    def get_even_score_based_on_points(self, points):
        if points > 3:
            points = 3
        return self.scores["even"][points]

    def player_has_won(self):
        if self.get_max_points_of_players() >= 4 and self.get_points_diff_of_players() >= 2:
            return True

        return False
    
    def get_score_when_no_even_or_advantage(self, points1, points2):
        p1_score = self.scores["individual"][points1]
        p2_score = self.scores["individual"][points2]

        return f"{p1_score}-{p2_score}"
    
    def get_score(self):

        if self.player_has_won():
            winner = self.get_player_with_more_points()
            
            return f"Win for {winner.name}"

        if self.points_are_even():
            return self.get_even_score_based_on_points(self.player1.points)
        
        if self.player_has_advantage():
            player = self.get_player_with_more_points()

            return f"Advantage {player.name}"
        
        return self.get_score_when_no_even_or_advantage(self.player1.points, self.player2.points)
