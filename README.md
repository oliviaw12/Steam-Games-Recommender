# Steam-Games-Recommender
CSC111 Final Course Project

*Based on a player’s game history and Steam community
reviews, how can we recommend new Steam video games to them that suit their interests?

In community reviews on Steam, a user can like or dislike a game or provide a descriptive word review (Steam, 2023). So, in this problem, we will be examining the positive and negative reviews from a subset of these Steam reviews to predict what games a person who plays certain Steam games could potentially like or dislike (McAuley). Our project aims at people who play Steam video games (or people who play games on Steam across multiple platforms), which will return results based on said player’s favourite games and game genres that they either like or want to try out next! To do this, we will take an input of games liked by the user, and list of genres they like or want to try out, create a graph called a SteamGraph that connects Steam game objects and player objects, and run algorithms on our SteamGraph and the user’s input to narrow down the best possible game recommendations. The use of Steam reviews and the user’s input will help us filter video games to make predictions in choosing what other games may suit a gamer’s enjoyment. 

## How to Run
1. Download our three datasets found in the Datasets package.
2. Unzip the files and make sure the Datasets folder (unzipped from the zipped file) is in the same folder as main.py and all
of our other modules
3. Run the **`main.py`** file.

## Other details 
1.  **`steam_game_creatory.py`** opens our datasets and creates our SteamGraph
2.   **`tkinter_classes.py`** creates our GUI, takes all input, calls all algorithms and produces all outputs. 
