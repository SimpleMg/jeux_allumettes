import re


class Ia:
    def __init__(self):
        self.pseudo = "Vincent Freeman"
        self.cas_fin = {1: 1, 2: 1, 3: 2}

    def _calcul_congruence(self, nbAllumette) -> int:
        """
        a ≡ b[n] <=> n / b-a
        b = nk + a
        """
        if (nbAllumette % 4) == (1 % 4):
            return 4
        return False

    def choix_nb_allumette(self, grille):
        if (y := len(grille)) in self.cas_fin:
            choice_nb_allumette = self.cas_fin[y]
        else:
            choice_nb_allumette = self._calcul_congruence(len(grille))
            if not choice_nb_allumette:
                with open('cerveau.txt', 'r') as f:
                    plus_commun = 0
                    dernier_ajout = 0
                    d = re.sub(r"\s+", "", f.read())
                    for i in d:
                        if d.count(i) > plus_commun:
                            plus_commun = int(i)
                        dernier_ajout = int(i)
                choice_nb_allumette = plus_commun
                cpt = 1
                while ((len(grille) - choice_nb_allumette) % 4) != (1 % 4):
                    if choice_nb_allumette >= 3:
                        choice_nb_allumette = dernier_ajout
                        break
                    choice_nb_allumette += cpt
                    cpt += 1
            if (len(grille) - choice_nb_allumette) == 5:
                choice_nb_allumette -= 1
            print(choice_nb_allumette)
        return choice_nb_allumette

    def choix_allumette(self):
        print("L'\IA {} choisis une allumette".format(self.pseudo))
        choice_ia = 0
        print("choiceIa = ", choice_ia)
        return choice_ia


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
        self.NB_ALLUMETTE = 16
        self.liste_player = [self.player_1, self.player_2]
        self._start_game()

    def _verify_nb_allumette(self, grille):
        choice_user = input("combien d'allumettre voulez vous enlevez: \n")
        try:
            choice_user = int(choice_user)
            if ((len(grille) - choice_user) < 0) or (choice_user < 0) or (choice_user > 4):
                print("tu ne peux pas prendre autant d'allumette!\n")
                return self._verify_nb_allumette(grille)
            return choice_user
        except:
            print("merci de rentrez un entier\n")
            return self._verify_nb_allumette(grille)

    def _tour_player(self, tour):
        tour_player = tour
        print("c'est au tour de {} de jouer".format(
            self.liste_player[tour_player].pseudo))
        return tour_player

    def _grille_allumettre(self, grille: list) -> str:
        for i in range(len(grille)):
            print("{}".format(grille[i]), end="")

    def _start_game(self):
        grille = ['|'] * self.NB_ALLUMETTE
        tour = 0
        while len(grille) >= 2:
            self._grille_allumettre(grille)
            print("\n\n")
            a_qui_le_tour = self._tour_player(tour)
            if a_qui_le_tour == 0:
                tour += 1
            else:
                tour -= 1
            print("{} choisis combien d'allumete tu veux prendre\n".format(
                self.liste_player[a_qui_le_tour].pseudo))
            if not isinstance(self.liste_player[a_qui_le_tour], Ia):
                combien_dallumete_user = self._verify_nb_allumette(grille)
                for i in range(combien_dallumete_user):
                    del grille[self.liste_player[a_qui_le_tour].choix_allumette(
                        self.liste_player[a_qui_le_tour].pseudo, grille)]
            else:
                with open('cerveau.txt', 'a') as f:
                    f.write(str(combien_dallumete_user))
                combien_dallumete = self.liste_player[a_qui_le_tour].choix_nb_allumette(
                    grille)
                for i in range(combien_dallumete):
                    del grille[self.liste_player[a_qui_le_tour].choix_allumette()]
        if self.liste_player[a_qui_le_tour - 1].pseudo == self.player_1.pseudo:
            print("Le player 2 {} gagne".format(self.player_2.pseudo))
        else:
            print("Le player 1 {} gagne".format(self.player_1.pseudo))
        return
