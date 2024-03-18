inventory = []
atk_player = 8
hp_player = 10
money_player = 15
username = ""

import random


def new_game():
  print("Menu principal :")
  print("1. Nouvelle partie")
  print("2. Charger une partie")
  print("3. A propos")
  print("4. Quitter")
  choice_user = input()
  if choice_user == "1":
    game()
  elif choice_user == "2":
    print("Vous n'avez pas de partie sauvegardée")
    new_game()
  elif choice_user == "3":
    about()
    new_game()
  elif choice_user == "4":
    print("A bientôt")
    return


def about():
  print(
    "Ce jeu est une travail réalisé par Avidan Benguigui, Michael Yap et Léonie Laurent"
  )
  new_game()


def game():
  global username
  print("Bienvenue dans ce jeu !")
  print("Commencez par définir votre nom de joueur")
  username = input()
  print("Bon courage", username, "pour cette aventure !")
  village()


def american_drop():
  global money_player, atk_player, hp_player
  D = random.randint(1, 10)
  if D == 1:
    inventory.append("matraque")
    print("Une matraque a été placée dans votre inventaire.")
  elif D == 2:
    inventory.append("pistolet")
    print("Un pistolet a été placé dans inventaire.")
  elif D == 3:
    inventory.append("trousse de secours")
    print("Une trousse de secours a été placé dans votre inventaire.")
  elif D == 4:
    inventory.append("bouclier anti-émeute")
    print("Un bouclier anti-émeute a été placé dans votre inventaire.")
  elif D == 5:
    inventory.append("casque")
    print("Un casque a été placé dans votre inventaire.")
  elif D == 6:
    inventory.append("fusil d'assaut")
    print("Un fusil d'assault a été placé dans votre inventaire.")
  elif D == 7:
    inventory.append("billet de 20$")
    money_player += 20
    print("Tu trouves 20$")
  elif D == 8:
    inventory.append("billet de 50$")
    money_player += 50
    print("Tu trouves 50$")
  elif D == 9:
    inventory.append("gilet pare-balle")
    print("Un gilet pare-balle a été placé dans votre inventaire")
  elif D == 10:
    inventory.append("fumigène")
    print("Un fumigène a été placé dans votre inventaire.")


def player_inventory_fight():
  global atk_player, hp_player
  print("Vous avez", atk_player, "points d'attaque et", hp_player,
        "points de vie.")
  print("Vous avez ces objets :", inventory)
  print("Quel objet voulez-vous utiliser ?")
  choice_user = input()
  if choice_user == "matraque":
    hp_player += 10
    print("Votre attaque est désormais de ", hp_player)
    inventory.remove("matraque")
    print(inventory)
  elif choice_user == "pistolet":
    atk_player += 10
    print("Votre attaque est désormais de", atk_player)
    inventory.remove("pistolet")
    print(inventory)
  elif choice_user == "trousse de secours":
    hp_player += 20
    print("Vous avez", hp_player, "points de vie")
    inventory.remove("trousse de secours")
    print(inventory)
  elif choice_user == "fusil d'assaut":
    atk_player += 20
    print("Votre attaque est de", atk_player)
    inventory.remove("fusil d'assaut")
    print(inventory)
  elif choice_user == "bouclier anti-émeute":
    hp_player += 25
    print("Vous avez", hp_player, "points de vie")
    inventory.remove("bouclier anti-émeute")
    print(inventory)
  elif choice_user == "casque":
    hp_player += 10
    print("Vous avez", hp_player, "points de vie")
    inventory.remove("casque")
    print(inventory)
  elif choice_user == "fumigène":
    atk_player += 5
    print("Vous avez", atk_player, "atk")
    inventory.remove("fumigene")
    print(inventory)
  elif choice_user == "gilet pare-balle":
    hp_player += 10
    print("Vous avez", hp_player, "points de vie")
    inventory.remove("gilet pare-balle")
    print(inventory)
  elif choice_user == "couteau":
    atk_player += 10
    print("Vous avez", atk_player, "points d'attaque")
    inventory.remove("couteau")
    print(inventory)
  elif choice_user == "kit de survie":
    hp_player += 15
    print("Vous avez", atk_player, "points de vie")
    inventory.remove("kit de survie")
    print(inventory)
  elif choice_user == "billet de 20$" or "billet de 50$":
    print("Tu ne peux pas utiliser cet item durant un combat.")
  else:
    print("Commande non conforme")

    player_inventory_fight()


def village():
  global atk_player
  print("Tu veux partir vers les Etats-unis pour avoir un meilleur avenir")
  print("Tu prends quelques affaires avant de partir.")
  inventory.append("couteau")
  inventory.append("kit de survie")
  print("Un couteau et un kit de survie ont été ajouté à ton inventaire")
  print(inventory)
  print("Tu te dirige vers la frontière et tu rencontres un membre d'une ONG.")
  PNJ_ong()


def PNJ_ong():
  global money_player
  print("Bonjour tu veux passer le mur ?")
  user_choice = input()
  if user_choice == "oui":
    print(
      "Sais-tu que de nombreux dangers se dresseront sur ton chemin? Et qu'une fois le mur franchi tu devras le combattre !"
    )
    print("Qui? Tu ne sais donc pas ?")
    print(
      "Celui-dont-on-ne-prononce-pas-le-nom... es-tu sur de vouloir y aller ? "
    )
    user_choice2 = input()
    if user_choice2 == "oui":
      print(
        "Dans ce cas, tu auras besoin d'un peu d'argent, voila 20 dollars.")
      money_player += 20
      print("Tu as", money_player, "dollars sur toi.")
      print(
        "Méfies-toi des gardes frontières, ils ne sont pas tendres avec nous, et n'hésites pas à parler aux passeurs sur ton chemin si tu as besoin de quoi que ce soit. Un conseil important, avant de commencer à attaquer les ennemis n'oublie pas de t'équiper, les lois des Américains les obligent à attendre que tu sois prêt(e)...Bon courage!"
      )
      print("Tu continues ton chemin et tombe sur un garde-frontière.")
      fight_border_guard()
    elif user_choice2 == "non":
      print(
        "Pas de problème, beaucoup y renoncent en prenant conscience de la difficulté qui les attendent."
      )
      return
    else:
      print("Je n'ai pas compris ce que tu as dit.")
      PNJ_ong()
  else:
    print(
      "Pas de problème, tu pourras réessayer une autre fois lorsque tu seras prêt !."
    )
    return


def fight_border_guard():
  hp_border_guard = 15
  atk_border_guard = 5
  global hp_player, atk_player, money_player
  print(
    "Vous vous faites controler par des gardes frontières et en voyant votre couteau ils vous attaquent !"
  )
  while hp_player >= 0 or hp_border_guard >= 0:
    print("Vos stats sont :", hp_player, "points de vie et", atk_player,
          "points d'attaque")
    print("Les stats de l'ennemi sont :", hp_border_guard, "points de vie et",
          atk_border_guard, "points d'attaque")
    print("1 - Attaque physique. 2 - Inventaire.")
    choice = input()
    if choice == "1":
      hp_border_guard = hp_border_guard - atk_player
      print("Les points de vie du garde frontière passent à ", hp_border_guard)
      if hp_border_guard <= 0:
        print("Victoire !")
        print("Le garde a fait tomber des objets")
        inventory.append("pistolet")
        inventory.append("gilet pare-balle")
        money_player += 10
        print(
          "Un pistolet et un gilet pare-balle sont placés dans votre inventaire."
        )
        print("Tu trouves 10$, tu as en tout", money_player, "dollars sur toi")
        print("Tu continues ton chemin, et tu rencontres un passeur.")
        PNJ_passeur_marchand_un()
      elif hp_border_guard > 0:
        print("Le garde frontière t'attaque !")
        hp_player = hp_player - atk_border_guard
        print("Vos points de vie passent à ", hp_player)
      elif hp_player <= 0:
        restart()
        return
    elif choice == "2":
      player_inventory_fight()


def PNJ_passeur_marchand_un():
  global money_player
  print(
    "Alors tu veux tenter de passer aux Etats-Unis ? Regarde ce que je vends, ça pourra t'être utile."
  )
  print("pistolet - 15 $", "gilet pare-balle - 15 $", "casque - 10 $",
        "kit de survie - 10 $", "trousse de secours - 20 $", "fumigene - 10 $")
  print("Que voulez-vous ? Vous avez", money_player, "$")
  user_choice = input()
  if user_choice == "pistolet":
    prix_pistolet = 15
    money_player = money_player - prix_pistolet
    if money_player < 0:
      print("Vous n'avez pas assez de $")
    else:
      print("Il vous reste", money_player, "$")
      inventory.append("pistolet")
      print(user_choice, "a été mis dans votre inventaire")
      print(inventory)
  elif user_choice == "gilet pare-balle":
    prix_gilet_pare_balle = 15
    money_player = money_player - prix_gilet_pare_balle
    if money_player < 0:
      print("Vous n'avez pas assez de $")
    else:
      print("Il vous reste", money_player, "$")
      inventory.append("gilet pare-balle")
      print(user_choice, "a été mis dans votre inventaire")
      print(inventory)
  elif user_choice == "casque":
    prix_casque = 10
    money_player = money_player - prix_casque
    if money_player < 0:
      print("Vous n'avez pas assez de $")
    else:
      print("Il vous reste", money_player, "$")
      inventory.append("casque")
      print(user_choice, "a été mis dans votre inventaire")
      print(inventory)
  elif user_choice == "kit de survie":
    prix_kit_survie = 10
    money_player = money_player - prix_kit_survie
    if money_player < 0:
      print("Vous n'avez pas assez de $")
    else:
      print("Il vous reste", money_player, "$")
      inventory.append("kit de survie")
      print(user_choice, "a été mis dans votre inventaire")
      print(inventory)
  elif user_choice == "trousse de secours":
    prix_trousse_secours = 20
    money_player = money_player - prix_trousse_secours
    if money_player < 0:
      print("Vous n'avez pas assez de $")
    else:
      print("Il vous reste", money_player, "$")
      inventory.append("trousse de secours")
      print(user_choice, "a été mis dans votre inventaire")
      print(inventory)
  elif user_choice == "fumigene":
    prix_fumigene = 10
    money_player = money_player - prix_fumigene
    if money_player < 0:
      print("Vous n'avez pas assez de $")
    else:
      print("Il vous reste", money_player, "$")
  print("Voulez-vous acheter autre chose ? oui/non")
  user_choice1 = input()
  if user_choice1 == "oui":
    PNJ_passeur_marchand_un()
  elif user_choice1 == "non":
    print("Très bien, j... qu'est-ce que c'est ?")
    print(
      "Vous entendez du bruit venant de l'extérieur, des policiers ont trouvés la planque du passeur et vous foncent dessus !"
    )
    print(
      "Vite! Tu peux : 1- Te battre avec les policiers, 2-Sortir par la gauche de la planque, 3-Sortir par la droite de la planque"
    )
    user_road = int(input())
    if user_road == 1:
      fight_policeman()
    elif user_road == 2:
      chemin_secondaire_gauche()
    elif user_road == 3:
      chemin_secondaire_droite()
  else:
    print("Je n'ai pas compris")
    PNJ_passeur_marchand_un()


def fight_policeman():
  hp_policeman = 30
  atk_policeman = 15
  global hp_player, atk_player
  print("Un policier a repéré sur la planque et te prend en chasse !")
  while hp_player > 0 or hp_policeman > 0:
    print("Vos stats", hp_player, "points de vie et", atk_player,
          "points d'attaque")
    print("Les stats de l'ennemi :", hp_policeman, "points de vie et",
          atk_policeman, "points d'attaque")
    print("1 - Attaque physique. 2 - Inventaire.")
    choice = input()
    if choice == "1":
      hp_policeman = hp_policeman - atk_player
      print("Les hp du policier passent à", hp_policeman)
      if hp_policeman <= 0:
        print("Victoire !")
        print("Le policier a fait tomber des objets")
        american_drop()
        american_drop()
        american_drop()
        print("Super je me rapproche de la frontière")
        print("Vous avancez vers le mur et apercevez un passeur.")
        last_passeur()
      elif hp_policeman > 0:
        print("Le policier t'attaque !")
        hp_player = hp_player - atk_policeman
      elif hp_player <= 0:
        restart()
    elif choice == "2":
      player_inventory_fight()


def chemin_secondaire_gauche():
  hp_thief = 5
  atk_thief = 10
  print(
    "Vous avancez sur un chemin calme quand tout à coup vous voyez quelqu'un au loin"
  )
  print(
    "La personne se rapproche vite de vous et vous attaque pour vous détrousser!"
  )
  global hp_player, atk_player, money_player
  print("Les stats de l'ennemi sont de", hp_thief, "points de vie et",
        atk_thief, "points d'attaque")
  while hp_player >= 0 or hp_thief >= 0:
    print("Vos stats sont de ", hp_player, "points de vie et ", atk_player,
          "points d'attaque")
    print("1 - Attaque physique. 2 - Inventaire. 3 - fuite.")
    choice = input()
    if choice == "1":
      hp_thief = hp_thief - atk_player
      print("Les points de vie du racketteur passent à ", hp_thief)
      if hp_thief <= 0:
        print("Victoire")
        print("Le racketteur a fait tomber des objets")
        american_drop()
        american_drop()
        american_drop()
        print("Je touche presque au but !")
        print("Vous avancez vers le mur et apercevez un passeur.")
        last_passeur()
        return
      elif hp_player <= 0:
        restart()
      elif hp_thief > 0:
        print("Le racketteur t'attaque !")
        hp_player = hp_player - atk_thief
        print("Vos points de vie passent à ", hp_player)
    elif choice == "2":
      player_inventory_fight()
    elif choice == "3":
      A = flee()
      if A > 1:
        print("Fuite Réussie")
        return
      if A <= 1:
        print("Fuite ratée")


def fight_maria():
  hp_maria = 3
  atk_maria = 1
  global hp_player, atk_player
  while hp_player >= 0 or hp_maria >= 0:
    print("Vos stats sont de", hp_player, "points de vie et", atk_player,
          "points d'attaque")
    print("Les stats de l'ennemi :", hp_maria, "points de vie et", atk_maria,
          "points d'attaque")
    print("1 - Attaque physique. 2 - Inventaire.")
    choice = input()
    if choice == "1":
      hp_maria = hp_maria - atk_player
      print("Les points de vie de Maria passent à ", hp_maria)
      print("Maria t'attaque !")
      hp_player = hp_player - atk_maria
      print("Vos points de vie passent à ", hp_player)
      if hp_maria <= 0:
        print("Victoire !")
        print("Maria a fait tomber des objets")
        american_drop()
        american_drop()
        american_drop()
        print("Super, je me rapproche de la frontière !")
        print(
          "Vite il faut partir d'ici avant qu'elle ne revienne à la charge.")
        last_passeur()
        return
      elif hp_player <= 0:
        restart()
        return
    elif choice == "2":
      player_inventory_fight()


def chemin_secondaire_droite():
  global hp_player, atk_player, money_player
  hp_maria, atk_maria
  A = random.randint(1, 3)
  print("Vous avancez sur un chemin et apercevez une maison au loin.")
  print("Fatigué, vous décidez de vous y arrêter et de vous reposer.")
  hp_player += 30
  print("Vous avez gagné 30 points de vie.")
  if A == 1:
    print("Une femme entre dans la maison et vous aperçoit.")
    print(
      "Bonjour je m'appelle maria, ne vous inquiétez pas, je ne vais pas vous balancer aux policiers, reposez-vous autant que vous voulez et partez ensuite."
    )
    print("Vous décidez de partir le lendemain.")
    print("En vous dirigeant vers le mur et apercevez un passeur.")
    last_passeur()
  elif A == 2:
    print("Une femme entre dans la maison et vous aperçoit")
    print(
      "Bonjour je m'appelle maria, ne vous inquiétez pas, je ne vous balancerai pas si vous me donnez 30 dollars"
    )
    if money_player >= 30:
      money_player = money_player - 30
      print("Super, reposez-vous autant que vous voulez et partez.")
    else:
      print("Tu n'as pas d'argent? très bien, alors je préviens les policiers")
      print(
        "Les policiers sont en chemin, vous n'avez plus beaucoup de temps. Vous pouvez : 1-l'attaquer, 2-l'assommer ou 3-partir"
      )
      choice_user = input()
      if choice_user == "1":
        fight_maria()
      if choice_user == "2":
        print(
          "Vous lui donnez un coup derrière la tête et partez de la maison en courant"
        )
        print("Vous avancez vers le mur et apercevez un passeur.")
        last_passeur()
      if choice_user == "3":
        print(
          "Vous essayez de partir le plus vite possible mais Maria vous empèche de partir en vous filmant et les policiers vous rattrappent."
        )
        restart()
        return
  elif A == 3:
    print("Une femme entre dans la maison et vous aperçoit")
    print("OH MON DIEU UN ETRANGER DANS MON LIT J'APPELLE LA POLICE!!")
    print(
      "Les policiers arrivent vite et vous attrappent, ils vous ramènent dans votre village"
    )
    print("Vous avez perdu")
    restart()
    return


def last_passeur():
  print(
    "Avant de passer le mur est-ce que tu veux m'acheter quelque chose ? On ne connait pas les dangers qu'on peut rencontrer après."
  )
  user_choice = input()
  if user_choice == "oui":
    PNJ_passeur_marchand_deux()
    return
  else:
    print(
      "Ok, j'espère que tu es prêt, maintenant, tu vas devoir faire face à leur chef, le terrible Celui-Dont-On-Ne-Doit-Pas-Prononcer-Le-Nom. Je ne peux pas en dire plus, il y a trop de risques à rester ici à découvert."
    )
  user_choice = input("Es-tu prêt à passer ce mur et devenir libre ? ")
  if user_choice == "oui":
    print("Ok ! Suis-moi.")
    fight_trump()
  else:
    print("Je n'ai pas compris, suis-moi vite avant qu'on se fasse attraper.")
    fight_trump()


def fight_trump():
  global hp_player, atk_player, username
  hp_trump = 50
  atk_trump = 20
  print("Ennemi : QUI OSE ESSAYER DE RENTRER DANS MON PAYS ?")
  print("Passeur : Oh non ! Celui-Dont-On-Ne-Doit-Pas-Prononcer-Le-Nom !!")
  print(username, ": Voldemort?")
  print(
    "Ennemi : Mais non je suis Donald Trump ! Le 45ème président des Etats-Unis d'Amérique ! Homme d'affaires, animateur de télévision, homme d'État et milliardaire avec une fortune estimée à 2,500,000,000 de $ !"
  )
  print(
    "Passeur : C'est pour ça qu'on ne dit jamais son nom, il est vraiment insupportable et n'arrête plus de parler de lui une fois lancé."
  )
  print(
    "Trump : Puisque les forces de l'ordre n'ont pas réussi à vous arrêter, je vais le faire moi-même !"
  )
  while hp_player >= 0 or hp_trump >= 0:
    print("Vos stats sont de", hp_player, "points de vie et", atk_player,
          "points d'attaque")
    print("Les stats de l'ennemi :", hp_trump, "points de vie et", atk_trump,
          "points d'attaque")
    print("1 - Attaque physique. 2 - Inventaire.")
    choice = input()
    if choice == "1":
      hp_trump = hp_trump - atk_player
      print("Les points de vie de Trump passe à ", hp_trump)
      if hp_trump <= 0:
        print("Victoire")
        print(
          "Tu as vaincu le président, tu peux maintenant vivre ta vie aux Etats-Unis !"
        )
        end_game()
        break
      elif hp_player <= 0:
        print("Tu étais prêt de la fin, courage !")
        restart()
        return
      elif hp_trump > 0:
        print("Trump t'attaque !")
        hp_player = hp_player - atk_trump
        print("Vos points de vie passent à ", hp_player)
    elif choice == "2":
      player_inventory_fight()


def PNJ_passeur_marchand_deux():
  global money_player
  print("Voila ce que je vends, vous avez", money_player, " $")
  print("pistolet - 15 $", "gilet pare-balle - 15 $", "casque - 10 $",
        "kit de survie - 10 $", "trousse de secours - 20 $", "fumigène - 10 $")
  print("Que voulez-vous ?")
  user_choice = input()
  if user_choice == "pistolet":
    prix_pistolet = 15
    money_player = money_player - prix_pistolet
    if money_player < 0:
      print("Vous n'avez pas assez de $")
    else:
      print("Il vous reste", money_player, "$")
      inventory.append("pistolet")
      print(user_choice, "à été mis dans votre inventaire")
      print(inventory)

  elif user_choice == "gilet pare-balle":
    prix_gilet_pare_balle = 15
    money_player = money_player - prix_gilet_pare_balle
    if money_player < 0:
      print("Vous n'avez pas assez de $")
    else:
      print("Il vous reste", money_player, "$")
      inventory.append("gilet pare-balle")
      print(user_choice, "à été mis dans votre inventaire")
      print(inventory)

  elif user_choice == "casque":
    prix_casque = 10
    money_player = money_player - prix_casque
    if money_player < 0:
      print("Vous n'avez pas assez de $")
    else:
      print("Il vous reste", money_player, "$")
      inventory.append("casque")
      print(user_choice, "à été mis dans votre inventaire")
      print(inventory)

  elif user_choice == "kit de survie":
    prix_kit_survie = 10
    money_player = money_player - prix_kit_survie
    if money_player < 0:
      print("Vous n'avez pas assez de $")
    else:
      print("Il vous reste", money_player, "$")
      inventory.append("kit de survie")
      print(user_choice, "à été mis dans votre inventaire")
      print(inventory)

  elif user_choice == "trousse de secours":
    prix_trousse_secours = 20
    money_player = money_player - prix_trousse_secours
    if money_player < 0:
      print("Vous n'avez pas assez de $")
    else:
      print("Il vous reste", money_player, "$")
      inventory.append("trousse de secours")
      print(user_choice, "à été mis dans votre inventaire")
      print(inventory)

  elif user_choice == "fumigene":
    prix_fumigene = 10
    money_player = money_player - prix_fumigene
    if money_player < 0:
      print("Vous n'avez pas assez de $")
    else:
      print("Il vous reste", money_player, "$")
      inventory.append("fumigene")
      print(user_choice, "à été mis dans votre inventaire")
      print(inventory)
  else:
    print("je n'ai aps compris")
    PNJ_passeur_marchand_deux()

  print("Voulez-vous acheter autre chose ?")
  user_choice = input()
  if user_choice == "oui":
    PNJ_passeur_marchand_deux()
  else:
    last_passeur()


def end_game():
  print(
    "Félicitations ! Tu as réussi à finir notre jeu, n'hésites pas à nous mettre une super note ! Ce jeu est un travail collectif de Leonie Laurent, Michael Yap et Avidan Benguigui"
  )
  return


def restart():
  print("Tu es mort sans avoir réaliser ton rêve. Make Mexico Great Again ! ")
  new_game()


command = input("Voulez-vous commencer une partie ? ")
if command == "oui":
  new_game()

# possibilité de choisir le mode de difficulté du jeu au début, en modifiant les valeurs des objets au marché et la force des ennemis ?
# condition dans inventaire pour le quitter sans choisir si on s'est trompé de trouche.
# changer affichage pv si < 0, voir dans l'affichage pour mettre KO
# powsi objet plus dans l'inventaire, le code bug
# pb marchand 2 achat si plus de pièce, pas d'autre réponse que oui
