class Player:
    def __init__(self, pseudo):
        self.pseudo = pseudo


    def _verify_int(self, grille):
        choice_user = input("Quelle allumettre voulez vous enlevez: \n")
        try:
            choice_user = int(choice_user)
            if choice_user < 0 or choice_user >= len(grille):
                print("merci de rentrez un indice valide\n")
                return self._verify_int(grille) 
            return choice_user
        except:
            print("merci de rentrez un entier\n")
            return self._verify_int(grille)


    def choix_allumette(self, pseudo_player, grille):
        print("{} choisis une allumete que tu veux prendre\n".format(pseudo_player))
        for i in range(len(grille)):
            print("{} - {}".format(i, grille[i]))
        choice_user = self._verify_int(grille)
        return choice_user


class MyGame:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.liste_player = [self.player_1, self.player_2]
        self._start_game()

    def _verify_nb_allumette(self, grille):
        choice_user = input("combien d'allumettre voulez vous enlevez: \n")
        try:
            choice_user = int(choice_user)
            if ((len(grille) - choice_user) < 0) or (choice_user < 0) or (choice_user > 3):
                print("tu ne peux pas prendre autant d'allumette!\n")
                return self._verify_nb_allumette(grille)
            return choice_user
        except:
            print("merci de rentrez un entier\n")
            return self._verify_nb_allumette(grille)


    def _tour_player(self,tour):
        tour_player = tour
        print("c'est au tour de {} de jouer".format(self.liste_player[tour_player].pseudo))
        return tour_player
    
    
    def _grille_allumettre(self, grille:list)->str:
        for i in range(len(grille)):
            print("{}".format(grille[i]), end="")
    

    def _start_game(self):
        grille = ['|'] * 15
        tour = 0
        while len(grille) >= 2:
            self._grille_allumettre(grille)
            print("\n\n")
            a_qui_le_tour = self._tour_player(tour)
            if a_qui_le_tour == 0:
                tour += 1
            else:
                tour -= 1
            print("{} choisis combien d'allumete tu veux prendre\n".format(self.liste_player[a_qui_le_tour].pseudo))
            combien_dallumete = self._verify_nb_allumette(grille)
            for i in range(combien_dallumete):
                del grille[self.liste_player[a_qui_le_tour].choix_allumette(self.liste_player[a_qui_le_tour].pseudo, grille)]
        if self.liste_player[a_qui_le_tour - 1].pseudo == self.player_1.pseudo:
            print("Le player 2 gagne")
        else:
            print("Le player 1 gagne")
        return

