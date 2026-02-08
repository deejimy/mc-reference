# Elimination de Joueur


Un joueur est éliminé de la partie si son identité est vaincue. Cela se produit généralement lorsque les points de vie restants du personnage tombent à zéro.
Lorsqu'un joueur est éliminé, effectuez les étapes suivantes dans l'ordre :  

1. Si le joueur éliminé possède le pion de premier joueur, il le passe au joueur suivant dans le sens des aiguilles d'une montre.  

2. S'il y a des sbires engagés avec le joueur éliminé, chacun de ces sbires engage le joueur suivant dans le sens des aiguilles d'une montre, en conservant ses pions, cartes attachées, cartes de boost, cartes glissées dessous et cartes d'état.  

3. Pour chaque carte dans la zone de jeu du joueur éliminé qui n'appartient pas à ce joueur, faites ce qui suit :  

  - S'il s'agit d'un attachement avec le mot-clé `permanent`, résolvez son texte "attachez à". S'il n'en a pas ou si ce texte n'a pas de cible valide, retirez l'attachement de la partie.
  - Retirez de la partie chaque carte non-attachement possédant le mot-clé `permanent`.
  - Placez chaque autre carte dans la pile de défausse de son propriétaire.

4. Placez chaque carte appartenant au joueur éliminé dans sa pile de défausse.  

5. Retirez de la partie la zone de jeu du joueur éliminé et tout autre élément de jeu qu'elle contient (main, deck, pile de défausse, cartes en jeu, compteur de points de vie, etc.).
Lorsqu'un joueur est éliminé, les joueurs restants continuent la partie. Les joueurs éliminés ne participent plus mais sont considérés comme gagnants ou perdants avec le reste du groupe.  

  - Si tous les joueurs sont éliminés, la partie se termine et les joueurs perdent.
  - Si un joueur est éliminé pendant la résolution d'une capacité, terminez la résolution de l'intégralité de la capacité.
  - Les effets qui font référence aux joueurs en jeu ignorent les joueurs éliminés, sauf pour l'icône par joueur (![[icone_joueur.jpg|15]]).

**Voir aussi** : Capacité, Distribuer, Engager, Élément de jeu, Points de vie, Identité, Sbire, Icône par joueur, Joueur, Carte de joueur, Deck de joueur, Zone de jeu d'un joueur, Vaincre la partie


```
PLAYER ELIMINATION
A player is eliminated from the game if their identity
is defeated. This usually occurs when the character’s
remaining hit points are reduced to zero.
When a player is eliminated, perform the following in order:
1. If the eliminated player has the first player token, they
pass it to the next clockwise player.
2. If there are minions engaged with the eliminated player,
each of those minions engages the next clockwise
player, retaining any tokens, attached cards, boost
cards, tucked cards, and status cards on them.
3. For each card in the eliminated player’s play area that
are not owned by that player, do the following:

  - If that card is an attachment with the permanent
keyword, resolve its "attach to" text. If it has none
or that text does not have a valid target, remove the
attachment from the game.

  - Remove each non-attachment card with the
permanent keyword from the game.

  - Place each other card in its owner’s discard pile.
4. Place each card owned by the eliminated player in the
eliminated player’s discard pile.
5. Remove the eliminated player’s play area and each
other game element within it (hand, deck, discard pile,
cards in play, hit point dial, etc.) from the game.
When a player is eliminated, the remaining players continue
to play the game. Eliminated players no longer participate
in the game but are considered to win or lose along with the
rest of the group, depending on how they finish.

  - If all players are eliminated, the game ends and the
players lose.

  - If a player is eliminated partway through the
resolution of an ability, resolve the entire ability.

  - Effects that refer to the players in the game ignore
eliminated players, except for the per player icon ().


See also: Ability, Deal, Engage, Game Element, Hit Points,
Identity, Minion, Per Player Icon, Player, Player Card, Player
Deck, Player’s Play Area, Winning the Game
```