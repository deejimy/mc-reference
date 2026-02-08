# Trouver


Lorsqu'un joueur reçoit l'instruction de trouver une carte, il cherche dans chaque zone de jeu où cette carte pourrait se trouver (zone de jeu, zone de mise de côté, deck de joueur, pile de défausse, deck Rencontre, etc.).

  - Les joueurs ne devraient pas chercher inutilement dans les zones de jeu s'ils savent où se trouve la carte qu'ils recherchent.

  - Toutes les zones de jeu sont sujettes à la recherche lors de la résolution d'une instruction "trouver", à l'exception des suivantes :

    - Les cartes de rencontre face cachée dans n'importe quelle zone de jeu en jeu (que cette carte soit elle-même en jeu ou non). (Par exemple, toutes les cartes de rencontre distribuées à un joueur ou données à un personnage comme carte de boost.)

    - La pile de victoire.

    - Les cartes qui ont été retirées de la partie.

  - Si un joueur reçoit l'instruction de "trouver et révéler" un sbire qui est déjà en jeu, ce joueur engage ce sbire et résout tous les mots-clés et/ou capacités déclenchées qui se résolvent suite à la révélation de ce sbire (comme la capacité "Une fois révélé" de ce sbire).

    - Ce sbire conserve tous les attachements et jetons sur lui.

    - Ce sbire n'est pas considéré comme entrant en jeu.

    - Ce sbire est considéré comme engageant ce joueur, à moins qu'il ne soit déjà engagé avec ce joueur.
Voir aussi : Chercher, Retiré de la partie, Pile de victoire


```
FIND
When instructed to find a card, a player searches each game
area where that card could be found (play area, set-aside
area, player deck, discard pile, encounter deck, etc.).

  - Players should not unnecessarily search game areas if
they know where the card they are looking for can be
found.

  - All game areas are subject to search when resolving a
"find" instruction, with the following exceptions:

  - Facedown encounter cards in any in-play game
area (whether that card is in play itself). (For
example, any encounter cards dealt to a player or
given to a character as a boost card.)

  - The victory display.

  - Cards that have been removed from the game.

  - If a player is instructed to "find and reveal" a minion
that is already in play, that player engages that minion
and resolves any keywords and/or triggered abilities
that resolve as a result of that minion being revealed
(such as that minion’s "When Revealed" ability).

  - That minion retains all attachments and tokens on it.

  - That minion is not considered to be entering play.

  - That minion is considered to engage that player
unless it was already engaged with that player.


See also: Search, Removed from the Game, Victory Display
```