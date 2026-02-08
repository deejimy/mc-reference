# Attaque (Activation des Ennemis)


Une attaque est un type d'activation d'ennemi. Lorsqu'un ennemi initie une attaque, il cible un joueur spécifique, puis résout cette attaque contre ce joueur.

- Les attaques d'ennemis sont toujours initiées à la fois contre un joueur et contre un personnage.
    - Normalement, le personnage attaqué est le héros du joueur, mais des capacités peuvent forcer un ennemi à attaquer l'alter-ego d'un joueur ou un allié que ce joueur contrôle. Dans tous ces cas, le joueur est toujours considéré comme étant attaqué.
    - Si un personnage autre que le personnage attaqué défend l'attaque, ce personnage devient la nouvelle cible de cette attaque.
    - Si un joueur autre que le joueur attaqué défend l'attaque avec un personnage qu'il contrôle, ce joueur devient la nouvelle cible de cette attaque.
    - Les capacités qui se déclenchent `Quand/Après que [ennemi] vous attaque` sont résolues quand/après qu'un joueur est attaqué, quel que soit le personnage qu'il contrôle qui a été attaqué. (Par exemple, Ultron I indique : `Réponse forcée : après qu'Ultron vous a attaqué, choisissez de soit placer 1 menace sur la manigance principale, soit de mettre la carte du dessus de votre deck en jeu face cachée, engagée avec vous en tant que sbire drone.` Cet effet se résout contre le joueur attaqué, peu importe si ce joueur a utilisé un allié pour défendre l'attaque.)

Pour résoudre une attaque d'ennemi, suivez ces étapes :

1. Si un méchant, ou un sbire avec le mot-clé `vilenie`, attaque, donnez-lui une carte de boost face cachée du deck Rencontre. (Si un sbire sans le mot-clé `vilenie` attaque, ignorez cette étape.)
2. Si un joueur souhaite défendre, ce joueur incline un héros ou un allié en tant que défenseur. Si un joueur autre que le joueur ciblé défend, le joueur défenseur devient le joueur cible pour cette attaque.
3. Résolvez chacune des cartes de boost de l'ennemi attaquant, une par une et dans l'ordre où elles ont été distribuées, en procédant comme suit :
    1. Retournez la carte de boost face visible.
    2. Résolvez toutes les capacités de `Boost`, indiquées par l'icône étoile (![[icone_etoile.jpg|15]]) dans la zone de boost. (Toutes les autres capacités sur la carte de boost sont ignorées.)
    3. Augmentez la valeur d'ATK de l'ennemi attaquant de 1 pour chaque icône de boost sur la carte.
    4. Défaussez la carte de boost.
    5. Si l'ennemi possède encore des cartes de boost, répétez ces étapes avec la carte suivante.
4. Infligez les dégâts de l'attaque égaux à la valeur d'ATK modifiée de l'ennemi, selon les cas suivants :
    - Si un héros effectue une défense de base contre l'attaque, la quantité de dégâts infligés est réduite de la valeur de DEF de ce héros, et les dégâts restants de l'attaque sont infligés à ce héros.
        - Le héros défenseur est considéré comme ayant été attaqué.
        - Si un héros avec un état tenace effectue une défense de base, les dégâts sont d'abord réduits par la valeur de DEF du héros. Si les dégâts sont réduits à 0, le héros conserve son état tenace.
    - Si un allié défend contre l'attaque, tous les dégâts de l'attaque sont infligés à l'allié. (Si l'allié est vaincu par l'attaque, les dégâts excédentaires ne sont pas reportés sur l'identité.)
        - L'allié défenseur est considéré comme ayant été attaqué.
        - Si l'allié défenseur quitte le jeu avant que les dégâts de l'attaque ne soient infligés, l'attaque est considérée comme n'ayant aucun personnage défenseur et l'identité du contrôleur de cet allié devient la cible de l'attaque.
    - Si aucun personnage ne défend contre l'attaque, l'attaque est considérée comme sans défense. Tous les dégâts de l'attaque sont infligés au personnage ciblé par l'attaque.
        - Le personnage ciblé est considéré comme ayant été attaqué.
5. L'attaque finit de se résoudre et les types de capacités suivantes se déclenchent dans l'ordre :
    1. Le mot-clé `riposte X` (si le personnage attaqué est toujours en jeu).
    2. Les capacités forcées avec les déclencheurs suivants (dans n'importe quel ordre) :
        - `après que [personnage] attaque [et blesse/vainc] [vous/un allié]...`
        - `après que [personnage] est attaqué...`
        - `après que [personnage] défend [et ne subit aucun dégât]...`
        - `après que [personnage] [subit/inflige] des dégâts...`
    3. Les capacités non-forcées avec les déclencheurs listés ci-dessus.

Ces règles s'appliquent également aux attaques d'ennemis :

- Les interruptions qui se déclenchent `quand [nom de l'ennemi] attaque` ont le même timing que les interruptions qui se déclenchent `quand [le méchant/un ennemi] initie une attaque`.
- Si une attaque d'ennemi se termine avant que les dégâts ne soient infligés, les capacités qui se déclenchent après qu'un personnage défend une attaque se résolvent, mais les capacités qui se déclenchent après qu'un ennemi attaque ne se résolvent pas.

**Voir aussi** : Activation, Allié, Attaques contre des alliés, Boost, Dégâts, Défendre, Ennemi, Identité, Sbire, Modificateurs, Riposte X, Cible, Méchant, Vilenie