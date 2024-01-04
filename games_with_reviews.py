    def games_with_reviews(self) -> list[Game]:
        """Return a list of games with at least one review."""
        game_ids = [game_id for game_id in self.games]
        return [self.games[game_id] for game_id in game_ids if self.games[game_id].reviewed_by != {}]
