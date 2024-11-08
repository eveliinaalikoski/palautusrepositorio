

class PlayerStats:
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def _sort_by_points(self, players):
        sorted_players = sorted(
            players,
            reverse = True,
            key = lambda player: player.points()
        )

        return sorted_players

    def top_scorers_by_nationality(self, nationality):
        players_of_nat = filter(
            lambda player: player.nationality == nationality,
            self._players
        )
        
        result = self._sort_by_points(list(players_of_nat))

        return result