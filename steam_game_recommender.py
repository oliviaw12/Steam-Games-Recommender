"""CSC111 Winter 2023 Course Project Phase 2: Predictive Steam Game Reccomender

Summary
===============================

This module contains the code that will run our final Steam game reccomender.

"""
from python_ta.contracts import check_contracts
from player_game_classes import Player, Game, SteamGraph

import json
import gzip


# copied code from dataset source, used to open json file (which is uniquely formatted)
def parse(path):
    g = gzip.open(path, 'r')
    for l in g:
        yield eval(l)


@check_contracts
def json_games_and_reviews_formatter(json_reviews_file: str, json_games_file: str) -> tuple[list[dict], list[dict]]:
    """Create list of mappings based on the given json files.

    The file json_reviews_file will create a list of mappings of steam users,
    which contains another mapping of steam reviews, alongside other useful information.

    The file json_games_file will create a list of mappings of steam games,
    which contains other useful information.

    Preconditions:
    - json_reviews_file and json_games_files refers to a valid json file
    in the format described in the written report.
    """
    user_reviews = list(parse(json_reviews_file))
    steam_games = list(parse(json_games_file))

    return user_reviews, steam_games


def remove_duplicates(json_games_and_reviews: tuple[list[dict], list[dict]]) -> tuple[list[dict], list[dict]]:
    """Remove all games with duplicates. For example, if there's two games with the same name, remove both."""
    games = json_games_and_reviews[1]


def steamgraph_creator(json_games_and_reviews: tuple[list[dict], list[dict]]) -> SteamGraph:
    """Create a SteamGraph object based on the given data from a json file.

    Preconditions:
    - json_games_and_reviews is in the same format as described in the written report.
    """
    user_reviews = json_games_and_reviews[0]
    steam_games = json_games_and_reviews[1]

    games = []
    game_names_so_far = set()

    for game in steam_games:
        # there are 3 instances (out of 32135) in steam_games where this condition is not met (from our game dataset),
        # but those games are not reviewed by any players (from our reivew dataset).
        if 'id' in game and 'app_name' in game:
            # there is at least 39 instances (out of 32135) instances where this condition is not met (from our dataset)
            # if a Game object with a shared game name already exists (duplicate name),
            # then don't create an instance of this game. This prevents complications with user input for
            # our reccomendation algorithm.
            if game['app_name'] not in game_names_so_far:
                game_names_so_far.add(game['app_name'])
                tags = []
                # there are 163 instances (out 32135) in steam_games where this condition is not met (from our game dataset)
                if 'tags' in game:
                    tags = game['tags']
                # there are 3283 instances in steam_games where this condition is not met (from our game dataset)
                elif 'genres' in game:
                    tags = game['genres']

            games.append(Game(name=game['app_name'], self_id=game['id'], tags=tags))

    new_steam_graph = SteamGraph(games)

    for player in user_reviews:
        new_player = Player(player['user_id'])
        new_steam_graph.add_player(new_player)
        for review in player['reviews']:
            # there are 5317 reviews (out of 59305 reviews) that have no shared id in steam_games (from our datasets)
            # we will exclude those reviews
            if review['item_id'] in new_steam_graph.games:
                new_steam_graph.add_review(player=new_player, game_id=review['item_id'], review=review['recommend'])

    return new_steam_graph


if __name__ == '__main__':
    data = json_games_and_reviews_formatter('Datasets/australian_user_reviews_v1.json', 'Datasets/steam_games_v2.json')
    graph = steamgraph_creator(data)
