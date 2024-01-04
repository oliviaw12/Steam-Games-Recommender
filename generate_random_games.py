    def generate_random_games(self, num_games: int) -> list[Game]:
        """Return a list of randomly generated games of length num_games."""

        games = []
        with_reviews = self.games_with_reviews()

        for _ in range(0, num_games):
            games.append(random.choice(with_reviews))
            
        return games
