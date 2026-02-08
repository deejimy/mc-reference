# Effets persistants


Certaines capacités créent des effets persistants. Ces effets ont une durée spécifiée (telle que "jusqu'à la fin de la phase" ou "pour ce round") et restent actifs pour cette durée.

  - Un effet persistant expire à la fin de sa durée, quel que soit l'état de la carte qui l'a créé. (Par exemple, si une amélioration crée un effet persistant qui dure jusqu'à la fin du round et que cette amélioration est défaussée, l'effet persiste jusqu'à la fin du round.)

  - Un effet persistant affecte l'état du jeu et les cartes au fur et à mesure qu'ils entrent en jeu, tant que la durée de l'effet est active.

**Voir aussi** : Capacité


```
LASTING EFFECTS
Some card abilities create effects or conditions that affect
the game for a specified duration (such as "until the end of
the phase" or "until the end of this attack"). Such effects are
known as lasting effects.

  - A lasting effect persists beyond the resolution of the
ability that created it, for the duration specified by
the effect. The effect continues to affect the game for
the specified duration whether or not the card that
created the lasting effect is in play.

  - For the specified duration of a lasting effect, it is
treated as if it was a constant ability and has the same
timing priority as a constant ability.

  - Lasting effects update whenever the game state
updates. (For example, a lasting effect of "until the
end of the phase, your hero gets +1 ATK for each
minion in play" changes the affected hero’s ATK any
time a minion enters or leaves play during that phase.)

  - If a card enters play (or changes status to meet the
criteria of a specified set of affected cards) after the
creation of a lasting effect, it is still affected by that
lasting effect.

  - A lasting effect expires as soon as the timing point
specified by its duration is reached. This means that
an "until the end of the round" lasting effect expires
just before an "at the end of the round" ability or
delayed effect may initiate.

  - A lasting effect that expires at the end of a specified
time period can only be initiated during that time
period.


See also: Ability, Enters Play
```