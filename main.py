from mesClasses import *


if __name__ == '__main__':
    player_1 = Player(input("player_1 choisis ton pseudo: \n"))
    player_2 = Player(input("player_2 choisis ton pseudo: \n"))
    start_game = MyGame(player_1, player_2)