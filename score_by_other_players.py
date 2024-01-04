    def score_by_other_players(self, game: Game) -> dict:
        """Return a dictionary mapping the score of each game connected to a player that likes the given game.
            Key: game, value: the game's score

        >>> game_ids = [id for id in graph.games]
        >>> with_reviews = [graph.games[id] for id in game_ids if graph.games[id].reviewed_by != {}]
        >>> graph.score_by_other_players(with_reviews[0])
        {True: 1}

        """
        other_games_so_far = {}  #maps games to its score, which is the number of players who liked it

        for key in game.reviewed_by:
            player_tup = game.reviewed_by[key]
            if player_tup[1]:  # if player likes the game

                for other_game in player_tup[0].games_reviewed:
                    reviewed_game = player_tup[0].games_reviewed[other_game]

                    # if player likes other game and this game is not the same one as the parameter 'game'
                    if reviewed_game[1] and reviewed_game[0] is not game:
                        # compute score
                        if reviewed_game[0] not in other_games_so_far:
                            other_games_so_far[reviewed_game[0]] = 1
                        else:
                            other_games_so_far[reviewed_game[0]] += 1

        return other_games_so_far
