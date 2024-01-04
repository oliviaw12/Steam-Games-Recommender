"""CSC111 Winter 2023 Course Project Phase 2: Predictive Steam Game Reccomender

Summary
===============================

This module contains a collection of Python classes and functions that are used to
represent a SteamGraph.

"""
from __future__ import annotations
import random
from python_ta.contracts import check_contracts


# @check_contracts
class Game:
    """A node that represents a Steam video game in a SteamGraph.

    Instance Attributes:
    - game_name:
        The title of the game.
    - game_id:
        A unique identifier for the game.
    - game_tags:
        A set of the game tags for the game.
    - reviewed_by:
        A mapping containing players that have reviewed the game in the SteamGraph.
        Each key in this mapping is the id of the player,
        and the corresponding value is a tuple of the Player object and a string review of the game.

    Representation Invariants:
    # test3
    """
    game_name: str
    game_id: str
    game_tags: set[str]
    reviewed_by: dict[str, tuple[Player, bool]]

    def __init__(self, name: str, self_id: str, tags: set[str]) -> None:
        """Initialize a Game object with no reviews.

        Preconditions:
        ### need to find a way to say self_id is a unique id ###
        """
        self.game_name = name
        self.game_id = self_id
        self.game_tags = tags
        self.reviewed_by = {}


# @check_contracts
class Player:
    """A node that represents a Steam user in a SteamGraph.

    Instance Attributes:
    - player_id:
        A unique identifier for the player.
    - games_reviewed:
        A mapping containing the reviews the player has created for games in the SteamGraph.
        Each key in this mapping is the id of the reviewed game,
        and the corresponding value is a tuple of the Game object and a bool review of that game (True if liked game).

    Representation Invariants:

    """
    player_id: str
    games_reviewed: dict[str, tuple[Game, bool]]

    def __init__(self, self_id: str) -> None:
        """Initialize a Player object with no reviews

        Preconditions:
        ### need to find way to say self_id is a unique id ###
        """
        self.player_id = self_id
        self.games_reviewed = {}


# @check_contracts
class SteamGraph:
    """A graph that contains players and games.

    Instance Attributes:
    - players:
        A mapping of player ids and Player objects in this graph.
    - games:
        A mapping of game ids and Game objects in this graph.
    - reviewed_games:
        A list of games with at least one review
    - genre_games:
        A list of games with at least one genre tag

    Representation Invariants:
    ### each player has a unique id compared to other players in self.players ###
    ### each game has a unique id compared to other games in self.games ###
    """
    players: dict[str, Player]
    games: dict[str, Game]
    # reviewed_games: list[Game]
    # genre_games: list[Game]

    def __init__(self, all_games: list[Game]) -> None:
        """Initialize a SteamGraph with the game objects."""
        self.games = {}
        self.players = {}
        for game in all_games:
            self.games[game.game_id] = game

    def add_player(self, player: Player) -> None:
        """Add a player to this SteamGraph.
        """
        self.players[player.player_id] = player

    def add_review(self, player: Player, game_id: str, review: bool) -> None:
        """Add a review for this player, and update the corresponding Game object's reviewed_by attribute.

        Preconditons:
        - player.id in self.players
        - game_id in self.games
        """
        player.games_reviewed[game_id] = (self.games[game_id], review)
        self.games[game_id].reviewed_by[player.player_id] = (player, review)

    def compute_score(self, chosen_games: list[str]) -> float:
        """Compute a
        """
        raise NotImplementedError

    def score_by_other_players(self, game: Game) -> dict[Game, int]:
        """Return a dictionary mapping the score of each game connected to a player that likes the given game.
            Key: game, value: the game's score

        # run in console of steam_game_recommender.py
        >>> games = graph.games_with_reviews()
        >>> graph.score_by_other_players(games[0])
        {<player_game_classes.Game object at 0x00000199F71B7190>: 1}

        """
        other_games_so_far = {}  # maps games to its score, which is the number of players who liked it

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

    def score_by_genre(self, liked_genres: list[str]) -> dict[Game, int]:
        """Return a dictionary mapping each game to its score based on how many genres
        in like_genres it matches with."""

        with_genres = self.games_with_genres()
        genre_scores = {}  # key: a Game from with_reviews, value: its score

        for game in with_genres:
            # find how many liked_genres match with the game
            score = 0
            for liked_genre in liked_genres:
                if liked_genre in game.game_tags:
                    score += 1

            genre_scores[game] = score

        return genre_scores

    def generate_random_games(self, num_games: int) -> list[Game]:
        """Return a list of randomly generated games of length num_games."""

        games = []
        with_reviews = self.games_with_reviews()

        for _ in range(0, num_games):
            games.append(random.choice(with_reviews))

        return games

    def games_with_reviews(self) -> list[Game]:
        """Return a list of games with at least one review."""
        game_ids = [game_id for game_id in self.games]
        return [self.games[game_id] for game_id in game_ids if self.games[game_id].reviewed_by != {}]

    def games_with_genres(self) -> list[Game]:
        """Return a list of games with at least one game tag (genre)."""
        game_ids = [game_id for game_id in self.games]
        return [self.games[game_id] for game_id in game_ids if self.games[game_id].game_tags != set()]
