# Elimination de Joueur


Un joueur est éliminé de la partie si son identité est vaincue. Cela se produit généralement lorsque les points de vie restants du personnage tombent à zéro.
Lorsqu'un joueur est éliminé, effectuez les étapes suivantes dans l'ordre :
1. Si le joueur éliminé possède le pion de premier joueur, il le passe au joueur suivant dans le sens des aiguilles d'une montre.
2. S'il y a des sbires engagés avec le joueur éliminé, chacun de ces sbires engage le joueur suivant dans le sens des aiguilles d'une montre, en conservant ses pions, cartes attachées, cartes de boost, cartes glissées dessous et cartes d'état.
3. Pour chaque carte dans la zone de jeu du joueur éliminé qui n'appartient pas à ce joueur, faites ce qui suit :

  - S'il s'agit d'un attachement avec le mot-clé permanent, résolvez son texte "attachez à". S'il n'en a pas ou si ce texte n'a pas de cible valide, retirez l'attachement de la partie.

  - Retirez de la partie chaque carte non-attachement possédant le mot-clé permanent.

  - Placez chaque autre carte dans la pile de défausse de son propriétaire.
4. Placez chaque carte appartenant au joueur éliminé dans sa pile de défausse.
5. Retirez de la partie la zone de jeu du joueur éliminé et tout autre élément de jeu qu'elle contient (main, deck, pile de défausse, cartes en jeu, compteur de points de vie, etc.).
Lorsqu'un joueur est éliminé, les joueurs restants continuent la partie. Les joueurs éliminés ne participent plus mais sont considérés comme gagnants ou perdants avec le reste du groupe.

  - Si tous les joueurs sont éliminés, la partie se termine et les joueurs perdent.

  - Si un joueur est éliminé pendant la résolution d'une capacité, terminez la résolution de l'intégralité de la capacité.

  - Les effets qui font référence aux joueurs en jeu ignorent les joueurs éliminés, sauf pour l'icône par joueur ().

Voir aussi : Capacité, Distribuer, Engager, Élément de jeu, Points de vie, Identité, Sbire, Icône par joueur, Joueur, Carte de joueur, Deck de joueur, Zone de jeu d'un joueur, Vaincre la partie

