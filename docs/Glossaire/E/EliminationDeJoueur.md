# Elimination de Joueur

Un joueur est éliminé de la partie si son identité est vaincue. Cela se produit généralement quand les points de vie restants du personnage tombent à zéro.

Quand un joueur est éliminé, effectuez les étapes suivantes dans l’ordre :
1. <span class="new">Si le joueur éliminé possède le jeton du premier joueur, il le passe au joueur suivant dans le sens horaire.</span>
2. Si des sbires sont engagés avec le joueur éliminé, chacun de ces sbires engage le joueur suivant dans le sens horaire en conservant tous leurs attachements, dégâts, jetons et cartes d’état.
3. S’il existe des cartes dans la zone de jeu du joueur éliminé dont ce joueur n’est pas le propriétaire :
- Si la carte est un attachement avec le mot-clé « Permanent », résolvez son texte « Attacher à ». Si elle n’en a pas ou si ce texte ne possède pas de cible valide, retirez l’attachement de la partie.
- Retirez de la partie chaque carte non-attachement qui possède le mot-clé « Permanent ».  
- Placez chaque autre carte dans la pile de défausse de son propriétaire.
4. Placez chaque carte appartenant au joueur éliminé dans la pile de défausse du joueur éliminé.
5. Retirez de la partie la zone de jeu du joueur éliminé et tous les autres éléments de jeu qui s’y trouvent (main, deck, pile de défausse, cartes en jeu, compteurs de points de vie, etc.).

Quand un joueur est éliminé, les joueurs restants continuent à jouer la partie. On considère que les joueurs éliminés gagnent ou perdent la partie en même temps que le reste de leur groupe, en fonction du résultat de celui-ci.
• Si tous les joueurs sont éliminés, la partie se termine et les joueurs ont perdu.
<span class="new">• Si un joueur est éliminé au milieu de la résolution d’une capacité, résolvez la capacité en entier.</span>
<span class="new">• Les effets qui font référence aux joueurs dans la partie ignorent les joueurs éliminés, sauf pour l’icône par joueur ().</span>

_Voir aussi : [[Capacite|Capacité]], [[Degats|Dégâts]], [[Engager|Engager]], [[ElementDeJeu|Élément de Jeu]], [[PointsDeVie|Points de Vie]], [[Identite|Identité]], [[Sbire|Sbire]], [[IconeParJoueur|Icône par joueur]], [[Joueur|Joueur]], [[CartesJoueur|Cartes Joueur]], [[DeckJoueur|Deck Joueur]], [[ZoneDeJeuDUnJoueur|Zone de Jeu d’un Joueur]], [[GagnerLaPartie|Gagner la Partie]]_  

**EN v1.7**:  
```
PLAYER ELIMINATION
A player is eliminated from the game if their identity is defeated. This usually occurs when the character’s remaining hit points are reduced to zero.
When a player is eliminated, perform the following in order:
1. If the eliminated player has the first player token, they pass it to the next clockwise player.
2. If there are minions engaged with the eliminated player, each of those minions engages the next clockwise player, retaining any tokens, attached cards, boost cards, tucked cards, and status cards on them.
3. For each card in the eliminated player’s play area that are not owned by that player, do the following:
• If that card is an attachment with the permanent keyword, resolve its "attach to" text. If it has none or that text does not have a valid target, remove the attachment from the game.
• Remove each non-attachment card with the permanent keyword from the game.
• Place each other card in its owner’s discard pile.
4. Place each card owned by the eliminated player in the eliminated player’s discard pile.
5. Remove the eliminated player’s play area and each other game element within it (hand, deck, discard pile, cards in play, hit point dial, etc.) from the game.
When a player is eliminated, the remaining players continue to play the game. Eliminated players no longer participate in the game but are considered to win or lose along with the rest of the group, depending on how they finish.
• If all players are eliminated, the game ends and the players lose.
• If a player is eliminated partway through the resolution of an ability, resolve the entire ability.
• Effects that refer to the players in the game ignore eliminated players, except for the per player icon ().
See also: Ability, Deal, Engage, Game Element, Hit Points, Identity, Minion, Per Player Icon, Player, Player Card, Player Deck, Player’s Play Area, Winning the Game
```


**FR v1.4**:  
```
ELIMINATION DE JOUEUR
Un joueur est éliminé de la partie si son identité est vaincue.
Cela se produit généralement quand les points de vie restants du personnage tombent à zéro.
Quand un joueur est éliminé, effectuez les étapes suivantes dans l’ordre :
14 Guide de Référence
1. Si des sbires sont engagés avec le joueur éliminé, chacun de ces sbires engage le joueur suivant dans le sens horaire en conservant tous leurs attachements, dégâts, jetons et cartes d’état.
2. S’il existe des cartes dans la zone de jeu du joueur éliminé dont ce joueur n’est pas le propriétaire, placez chacune de ces cartes dans la pile de défausse de son propriétaire (même si cette carte a le mot-clé Permanent).
3. Retirez de la partie la zone de jeu du joueur éliminé et tous les autres éléments de jeu qui s’y trouvent (main, deck, pile de défausse, cartes en jeu, compteurs de points de vie, etc.).
Quand un joueur est éliminé, les joueurs restants continuent à jouer la partie. On considère que les joueurs éliminés gagnent ou perdent la partie en même temps que le reste de leur groupe, en fonction du résultat de celui-ci.
• Si tous les joueurs sont éliminés, la partie se termine et les joueurs ont perdu.
Si un joueur est éliminé au milieu de la résolution d’une capacité, résolvez la capacité en entier.
Voir aussi : Attribuer, Capacité, Cartes Joueur, Deck Joueur, Engager, Gagner la Partie, Identité, Joueur, Points de Vie, Sbire, Zone de Jeu d’un Joueur
```