# Modificateurs


Les modificateurs sont des capacités de carte ou des règles de jeu qui modifient les statistiques ou les capacités d'une carte.

  - Les modificateurs s'appliquent après avoir déterminé la valeur de base d'une statistique.

  - Si plusieurs modificateurs s'appliquent, appliquez d'abord les additions et soustractions, puis les multiplications et divisions.

**Voir aussi** : Valeur de base, Points de vie


```
MODIFIERS
The game constantly checks and (if necessary) updates the
count of any variable quantity that is being modified.
Any time a new modifier is applied or removed, the entire
quantity is recalculated from the start, considering the
unmodified base value and all active modifiers.

  - The "per player" icon () is not considered a modifier
and is applied before any modifiers are applied.

  - The calculation of a value treats all modifiers as being
applied simultaneously. However, while performing
the calculation, all additive and subtractive modifiers
are calculated before doubling and/or halving
modifiers are calculated.

  - If a value is "set" to a specific number, the set
modifier overrides all non-set modifiers. If multiple
set modifiers are in conflict, the most recently
resolved set modifier takes precedence.

  - After all active modifiers have been taken into
account, if a value is below zero, it is treated as zero:
a card cannot have "negative" icons, attributes, traits,
cost, or keywords.

  - Fractional values are rounded up after all modifiers
have been applied.

  - If a card ability causes a character to "get" a statistic
(such as +1 ATK or 4 hit points), the ability modifies
the character’s statistic while it is active.

  - If such an ability expires or otherwise becomes
inactive, the modified statistic reverts to the value
it would have without the modifier.

  - A value of a dash (–) cannot be modified.


See also: Base Value, Dash (Value), Printed
```