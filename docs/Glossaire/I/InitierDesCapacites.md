# Initier des Capacités


Lorsqu'un joueur souhaite jouer une carte ou initier une capacité déclenchée, ce joueur déclare d'abord son intention. Ensuite, le joueur vérifie les conditions suivantes dans l'ordre :

1. Vérifier les restrictions de jeu : la carte peut-elle être jouée, ou la capacité initiée, à ce moment-là ?

  - Si la carte ou la capacité spécifie une ou plusieurs cibles, vérifiez qu'elle possède au moins une cible valide.

2. Déterminer si la capacité peut être au moins partiellement résolue.

3. Payer tous les coûts associés (y compris les coûts en ressources, l'inclinaison de cartes et les coûts décrits dans le texte).

Une fois ces étapes franchies, la capacité est considérée comme initiée et commence sa résolution.

  - Lorsqu'un joueur joue une carte, cette carte est considérée comme ayant été jouée dès que ses coûts sont payés.
  - Lorsqu'un joueur utilise une capacité déclenchée, cette capacité est considérée comme ayant été utilisée dès que ses coûts sont payés.

**Voir aussi** : Capacité, Coût, Jouer, Résolution des capacités, Cible


```
INITIATING ABILITIES
When a player wishes to play a card or initiate a triggered
ability, that player first declares their intent. Then, the player
checks the following conditions in order:
1. Check play restrictions: can the card be played, or the
ability initiated, at this time?

  - If the card or ability specifies one or more targets,
check that it has at least one valid target. If the card
or ability does not have at least one valid target, it
cannot be played or initiated.
2. Determine the cost (or costs) to play the card or initiate
the ability and the player’s ability to pay them, taking
modifiers into account.

  - If a card has a resource cost of X, the player playing
that card chooses the value of X during this step.
If both conditions are met, follow these steps in order:
3. If playing a card, the player places that card faceup on
the table in front of them. (This card is not in play.)
4. Apply any modifiers to the cost(s).
5. Pay the cost(s). If this step is reached and the cost(s)
cannot be paid, abort this process without paying any
costs.
6. The card commences being played, or the effects of
the ability attempt to initiate.
7. The card is played or the ability (if not canceled in the
previous step) resolves. The card enters play or, if it is
an event card, its effects resolve and it is then placed in
its owner’s discard pile.

  - If any of the above steps would make the triggering
condition of an interrupt ability true, that ability may
be initiated just before that triggering condition
becomes true.

  - If any of the above steps would make the triggering
condition of a response ability true, that ability
may be initiated immediately after that triggering
condition becomes true.

  - If the ability being initiated is on a card that is in play,
the sequence does not stop from completing if that
card leaves play during this sequence unless the card
leaving play prevents a required cost from being
paid.


See also: Ability, Cost, Play Restrictions and Permissions,
Target
```