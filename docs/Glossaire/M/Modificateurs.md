# Modificateurs

Le jeu vérifie constamment et actualise (si nécessaire) le compte de toute quantité variable qui est modifiée.  

Chaque fois qu'un nouveau modificateur est appliqué ou retiré, la valeur concernée est recalculée entièrement depuis le début en prenant en compte la valeur de base non modifiée et tous les modificateurs actifs.  

- L'icône « par joueur » ![[icone_joueur.jpg|15]] n'est pas considérée comme un modificateur et s'applique avant que les autres modificateurs ne soient pris en compte.  
- Le calcul d'une valeur considère tous les modificateurs comme étant appliqués simultanément. Cependant, lors du calcul, tous les modificateurs additifs ou soustractifs sont calculés avant les modificateurs multiplicatifs ou divisifs.  
- Si une valeur est « fixée » à un nombre spécifique, le modificateur fixé supplante tous les autres modificateurs qui ne sont pas fixés. Si plusieurs modificateurs fixant une valeur entrent en conflit, le modificateur fixé le plus récemment résolu prend la priorité.  
- Après que tous les modificateurs actifs ont été pris en compte, si une valeur est inférieure à zéro, elle est considérée comme étant égale à zéro : une carte ne peut pas avoir d'icônes, d'attributs, de traits, de coût ou de mots‑clé « négatifs ».  
- Toutes les valeurs fractionnaires sont arrondies au nombre supérieur après application de tous les modificateurs.  
- Si une capacité de carte fait qu'un personnage gagne une statistique (par exemple +1 ATQ ou 4 points de vie), la capacité modifie la statistique du personnage tant qu'elle est active.  
    - Si une telle capacité expire ou devient inactive pour une autre raison, la statistique modifiée revient à la valeur qu'elle aurait sans ce modificateur.  
- Une valeur représentée par un tiret (–) ne peut pas être modifiée.  

_Voir aussi : [[ValeurDeBase|Valeur de base]], [[TiretValeur|Tiret (Valeur)]], [[Imprime|Imprimé]]_  

<details class="source">
<summary>EN v1.7</summary>MODIFIERS
The game constantly checks and (if necessary) updates the count of any variable quantity that is being modified.
Any time a new modifier is applied or removed, the entire quantity is recalculated from the start, considering the unmodified base value and all active modifiers.
• The "per player" icon () is not considered a modifier and is applied before any modifiers are applied.
• The calculation of a value treats all modifiers as being applied simultaneously. However, while performing the calculation, all additive and subtractive modifiers are calculated before doubling and/or halving modifiers are calculated.
• If a value is "set" to a specific number, the set modifier overrides all non-set modifiers. If multiple set modifiers are in conflict, the most recently resolved set modifier takes precedence.
• After all active modifiers have been taken into account, if a value is below zero, it is treated as zero: a card cannot have "negative" icons, attributes, traits, cost, or keywords.
• Fractional values are rounded up after all modifiers have been applied.
• If a card ability causes a character to "get" a statistic (such as +1 ATK or 4 hit points), the ability modifies the character's statistic while it is active.
» » If such an ability expires or otherwise becomes inactive, the modified statistic reverts to the value it would have without the modifier.
• A value of a dash (–) cannot be modified.
See also: Base Value, Dash (Value), Printed
</details>


<details class="source">
<summary>FR v1.4</summary>MODIFICATEURS
Le jeu vérifie constamment et actualise (si nécessaire) le compte de toutes les variables qui sont modifiées.
Chaque fois qu'un nouveau modificateur est appliqué ou retiré, la valeur concernée est recalculée entièrement depuis le début en prenant en compte la valeur de base non modifiée et tous les modificateurs actifs.
• Le calcul d'une valeur considère tous les modificateurs comme étant appliqués simultanément. Cependant, lors du calcul, tous les modificateurs additifs ou soustractifs sont calculés avant les modificateurs multiplicatifs ou divisifs.
• Si une valeur est « fixée » à un nombre spécifique, le modificateur fixé supplante tous les autres modificateurs. Si plusieurs modificateurs fixant une valeur entrent en conflit, le modificateur le plus récent supplante les autres.
• Après que tous les modificateurs actifs ont été pris en compte, si une valeur est inférieure à zéro, elle est considérée comme étant égale à zéro. Une carte ne peut pas avoir de valeur « négative » d'icônes, d'attributs, de traits, de coût ou de mot-clé.
• Toutes les fractions sont arrondies au nombre supérieur après application de tous les modificateurs.
Voir aussi : Valeur de base, Imprimé
</details>