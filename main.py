from mesClasses import *


if __name__ == '__main__':
    restart_game = ""
    while True:
        ia_or_not = ''
        player_1 = Player(input("player_1 choisis ton pseudo: \n"))
        while ia_or_not != 'y' and ia_or_not != 'n':
            ia_or_not = input("Voulez vous jouer avec une ia ?(y/n)")
            if ia_or_not == 'y':
                player_2 = Ia()
            elif ia_or_not == 'n':
                player_2 = Player(input("player_2 choisis ton pseudo: \n"))
        start_game = MyGame(player_1, player_2)
        restart_game = input("rejouer ?(y/n)")
        if restart_game == 'n':
            break
