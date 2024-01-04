    def score_by_genre(self, liked_genres: list[str]) -> dict[Game, int]:
        """Return a dictionary mapping each game to its score based on how many genres
        in like_genres it matches with."""

        with_genres = self.games_with_genres()
        genre_scores = {}  # key: a Game from with_reviews, value: its score
        liked_genres_len = len(liked_genres)

        for game in with_genres:
            # find how many liked_genres match with the game
            score = 0
            for liked_genre in liked_genres:
                if liked_genre in game.game_tags:
                    # genres are ordered starting with the most important, so those at the beginning of the list
                    # are weighted more.
                    significance = 0.5 * (liked_genres_len - 1 - liked_genres.index(liked_genre))
                    score += 1 + significance

            genre_scores[game] = score

        return genre_scores
