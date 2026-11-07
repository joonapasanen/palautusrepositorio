class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = filter(lambda p: p.nationality == nationality, self.players)
        players = sorted(players, reverse=True, key=lambda p: p.goals + p.assists)
        return players

    def top_scorers_by_team(self, team):
        players = filter(lambda p: p.team == team, self.players)
        players = sorted(players, reverse=True, key=lambda p: p.goals + p.assists)
        return players

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa
        maalimäärän mukaan laskevassa järjestyksessä.
        """
        players = sorted(self.players, reverse=True, key=lambda p: p.goals)
        return players[:how_many]
