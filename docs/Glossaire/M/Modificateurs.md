# Modificateurs


Les modificateurs sont des capacités de carte ou des règles de jeu qui modifient les statistiques ou les capacités d'une carte.

  - Les modificateurs s'appliquent après avoir déterminé la valeur de base d'une statistique.

  - Si plusieurs modificateurs s'appliquent, appliquez d'abord les additions et soustractions, puis les multiplications et divisions.

**Voir aussi** : Valeur de base, Points de vie


**EN v1.7**:  
```
MODIFIERS
The game constantly checks and (if necessary) updates the count of any variable quantity that is being modified.
Any time a new modifier is applied or removed, the entire quantity is recalculated from the start, considering the unmodified base value and all active modifiers.
• The "per player" icon () is not considered a modifier and is applied before any modifiers are applied.
• The calculation of a value treats all modifiers as being applied simultaneously. However, while performing the calculation, all additive and subtractive modifiers are calculated before doubling and/or halving modifiers are calculated.
• If a value is "set" to a specific number, the set modifier overrides all non-set modifiers. If multiple set modifiers are in conflict, the most recently resolved set modifier takes precedence.
• After all active modifiers have been taken into account, if a value is below zero, it is treated as zero: a card cannot have "negative" icons, attributes, traits, cost, or keywords.
• Fractional values are rounded up after all modifiers have been applied.
• If a card ability causes a character to "get" a statistic (such as +1 ATK or 4 hit points), the ability modifies the character’s statistic while it is active.
» » If such an ability expires or otherwise becomes inactive, the modified statistic reverts to the value it would have without the modifier.
• A value of a dash (–) cannot be modified.
See also: Base Value, Dash (Value), Printed
```


**FR v1.4**:  
```
MODIFICATEURS
Le jeu vérifie constamment et actualise (si nécessaire) le compte de toutes les variables qui sont modifiées.
Chaque fois qu’un nouveau modificateur est appliqué ou retiré, la valeur concernée est recalculée entièrement depuis le début en prenant en compte la valeur de base non modifiée et tous les modificateurs actifs.
• Le calcul d’une valeur considère tous les modificateurs comme étant appliqués simultanément. Cependant, lors du calcul, tous les modificateurs additifs ou soustractifs sont calculés avant les modificateurs multiplicatifs ou divisifs.
• Si une valeur est « fixée » à un nombre spécifique, le modificateur fixé supplante tous les autres modificateurs. Si plusieurs modificateurs fixant une valeur entrent en conflit, le modificateur le plus récent supplante les autres.
• Après que tous les modificateurs actifs ont été pris en compte, si une valeur est inférieure à zéro, elle est considérée comme étant égale à zéro. Une carte ne peut pas avoir de valeur « négative » d’icônes, d’attributs, de traits, de coût ou de mot-clé.
• Toutes les fractions sont arrondies au nombre supérieur après application de tous les modificateurs.
Voir aussi : Valeur de base, Imprimé
```