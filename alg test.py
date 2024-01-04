"""
calc recc.
"""

def calculate_alg(p_input: list[Game, Game, Game], score_type: str) -> ...:
    """
    main calc func

    Preconditions:
    - score_type in {'players', 'genre', 'players_genre'}
    """
    saved_recs = []

    for game in p_input:
        if score_type == 'players':
            saved_recs.append(Compute_score_simple(game))
        if score_type == 'genre':
            saved_recs.append(Compute_score_genre(game))
        if score_type == 'players_genre':
            saved_recs.append(compute_score_players_genre(game))

    # saved_recs now is a list of 3 elements, all the results from each call to compute_score
    # now, something to calculate final reccomendations based on reccom. From each game


def compute_score_simple(game: Game) -> ...:
    """
    simple calc
    """
    Other_games_so_far = {}
    for liked_by in game.liked_by:
        for reviewed in Liked_by.reviewed:
            # compute score
            if reviewed not in other_games_so_far:
                Other_games_so_far[reviewed] = 1
            else:
                Other_games_so_far[reviewed] += 1

    # other_games_so_far will be a dict of all reviewed games by players connected to Game,
    # the games that have the highest num in the dict other_games_so_far will be returned (?)


for key in game.reviewed_by:
    reviewed_by[key][0]
    if reviewed_by[key][1] = True:
