# Echanger


Une instruction demandant d'échanger deux composants signifie qu'il faut intervertir l'emplacement de ces deux composants.

  - Un échange ne peut être effectué s'il n'y a pas de composant dans les deux emplacements.

    - Par exemple, vous ne pouvez pas "échanger une carte de votre main avec la carte du dessus de votre deck" si vous n'avez aucune carte en main.

  - Échanger une carte en main avec la carte du dessus d'un deck n'est pas considéré comme piocher cette carte.

  - Lors de l'échange d'une carte en zone de jeu avec une carte en zone hors-jeu, si ces deux cartes :

    - Partagent un titre, aucune des deux n'est considérée comme entrant ou quittant le jeu. Les pions, cartes attachées, cartes glissées dessous et cartes d'état de la carte précédemment en jeu sont transférés à l'autre carte, et celle-ci conserve l'état (prêt ou incliné) de la carte précédente. Si la carte échangée possède un compteur de points de vie associé, celui-ci conserve la même valeur.

    - Ne partagent pas de titre, la carte en jeu est considérée comme quittant le jeu et la carte hors-jeu est considérée comme entrant en jeu. Les pions, cartes attachées, cartes glissées dessous et cartes d'état ne sont pas transférés, et la nouvelle carte entre en jeu prête. Si elle possède un compteur de points de vie, celui-ci est réinitialisé à la valeur de points de vie imprimée de la nouvelle carte.

**Voir aussi** : Capacité, Cible


```
"SWAP"
An instruction to "swap" two components means to
exchange the location of those two components.

  - A swap cannot be completed if there is not a
component in both locations.

  - For example, you cannot "swap a card in your hand
with the top card of your deck" if you have no cards
in hand.

  - Swapping a card in hand with the top card of a deck
is not considered drawing that card.

  - When swapping a card in a play area with a card in an
out-of-play area, if those two cards:

  - Share a title, neither card is considered to enter or
leave play. Tokens, attached cards, tucked cards,
and status cards on the previously in-play card are
transferred to the other card and the other card
maintains the state (ready or exhausted) of the
previously in-play card. If the swapped card has an
associated hit point dial, that dial remains at the
same value.

  - Do not share a title, the in-play card is considered
to leave play and the out-of-play card is considered
to enter play. Tokens, attached cards, tucked cards,
and status cards on the previously in-play card are
not transferred to the other card and the other
card enters play ready. If the swapped card has an
associated hit point dial, that dial is reset to the
new card’s printed hit point value.


See also: Ability, Target
```