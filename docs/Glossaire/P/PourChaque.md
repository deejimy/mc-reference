# "Pour Chaque"


"Pour chaque" indique qu'un effet est répété en fonction du nombre d'un élément de jeu dénombrable.

  - Si un effet avec "pour chaque" nécessite une cible, cet effet s'applique à une seule cible à moins que la clause "pour chaque" n'inclue une instruction "choisissez".

    - Par exemple, un effet qui dit "Pour chaque traîtrise regardée de cette manière, retirez 1 menace d'une manigance" retire de la menace d'une seule manigance. À l'inverse, un effet qui dit "Pour chaque amélioration que vous contrôlez, choisissez un ennemi et infligez-lui 2 dégâts" vous permet de choisir un ennemi différent pour chaque amélioration que vous contrôlez.

  - Si un effet "pour chaque" sans instruction "choisissez" inflige des dégâts ou retire de la menace, il est considéré comme une instance unique de dégâts infligés ou de menace retirée, respectivement.

  - Si un effet "pour chaque" comporte une instruction "choisissez", chaque répétition de ce choix est considérée comme une instance distincte de cet effet, même si la même cible est choisie plusieurs fois.

    - L'état de la partie est mis à jour après chaque instance (par exemple, si un sbire ou une manigance annexe est vaincu).

    - Des réponses peuvent être déclenchées après chaque instance.

    - Par exemple, si un joueur est engagé avec un sbire avec garde et utilise un effet qui dit "pour chaque ressource que vous avez dépensée de cette manière, choisissez un ennemi et infligez-lui 2 dégâts", ce joueur peut vaincre le sbire avec garde avec une instance de 2 dégâts, rendant le méchant cible valide pour les instances suivantes. Ce joueur peut déclencher une capacité de réponse comme "Après avoir infligé des dégâts à un ennemi" après chaque instance.

  - Si une autre capacité modifie un effet "pour chaque", ce modificateur est appliqué à chaque instance de l'effet "pour chaque". (Par exemple, Rafale de Lames est un évènement qui possède l'effet : "Pour chaque Psi-Katana, choisissez un ennemi et infligez-lui 2 dégâts." S'il est modifié par un effet qui dit "cet évènement inflige 1 dégât supplémentaire", Rafale de Lames infligera 3 dégâts à chaque ennemi choisi.)

**Voir aussi** : Capacité, Cible


**EN v1.7**:  
```
"FOR EACH"
"For each" indicates an effect is repeated based on the number of a countable game element.
• If an effect with "for each" requires a target, that effect applies to a single target unless the "for each" clause includes a "choose" instruction.
» » For example, an effect that reads "For each treachery looked at this way, remove 1 threat from a scheme" removes threat from a single scheme.
Alternatively, an effect that reads "For each upgrade you control, choose an enemy and deal 2 damage to it" allows you to choose a different enemy for each upgrade you control.
• If a "for each" effect without a "choose" instruction deals damage or removes threat, it is considered a single instance of damage dealt or threat removed, respectively.
• If a "for each" effect has a "choose" instruction, each iteration of that choice is considered a separate instance of that effect, even if the same target is chosen multiple times.
» » The game state updates after each instance (for example, if a minion or side scheme is defeated).
» » Responses can be triggered after each instance.
» » For example, if a player is engaged with a guard minion and uses an effect that says "for each resource you spent this way, choose an enemy and deal 2 damage to it," that player can defeat the guard minion with one instance of 2 damage, making the villain a valid target for further instances. That player can trigger a response ability like "After you deal damage to an enemy" after each instance.
• If another ability modifies a "for each" effect, that modifier is applied to each instance of the "for each" effect. (For example, Flurry of Blades is an event that has the effect: "For each Psi-Katana, choose an enemy and deal 2 damage to it." If modified by an effect that says "that event deals 1 additional damage," Flurry of Blades deals 3 damage to each chosen enemy.) See also: Ability, Target
```