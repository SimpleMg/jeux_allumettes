from mesClasses import *


if __name__ == '__main__':
    ia_or_not = input("Voulez vous jouer avec une ia ?(y/n)")
    player_1 = Player(input("player_1 choisis ton pseudo: \n"))
    if ia_or_not == 'y':
        player_2 = Ia()
    else:
        player_2 = Player(input("player_2 choisis ton pseudo: \n"))
    start_game = MyGame(player_1, player_2)
