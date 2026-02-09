# Attaque (Activation du Joueur)

Certains effets de jeu et capacités de carte font référence à une attaque. Il existe plusieurs façons pour qu'une attaque se produise :

- Un héros ou un allié peut utiliser son pouvoir d'attaque de base pour attaquer un ennemi. Un personnage doit s'incliner pour utiliser ce pouvoir. Cela inflige des dégâts égaux à la valeur d'ATK du personnage à l'ennemi.
    - Un personnage ne peut initier une attaque de base que s'il y a un ennemi qui peut être attaqué par ce personnage ou si ce personnage est sonné.
- Si une capacité déclenchée est étiquetée comme une attaque — telle que `Action de Héros (attaque)` — la résolution de cette capacité est considérée comme attaquer la cible spécifiée. Sauf indication contraire dans le texte de la capacité, un héros ne s'incline pas lorsqu'il utilise une telle capacité.
    - Une capacité étiquetée comme une attaque est considérée comme une seule et unique attaque, même si cette attaque inflige plusieurs instances de dégâts.
    - Lorsqu'une capacité d'attaque voit ses dégâts augmentés par une autre capacité, chaque instance de dégâts de cette capacité d'attaque qui n'utilise pas le mot `supplémentaire` est augmentée du montant spécifié.
- Si une capacité indique `Effectuez les X attaques suivantes dans l'ordre`, suivies de deux instances de dégâts ou plus, chacune de ces instances est considérée comme une attaque distincte.
    - Une capacité qui augmente les dégâts d'une attaque n'augmente les dégâts que de l'une des attaques de cette capacité, bien qu'une telle capacité puisse être déclenchée séparément pour chaque attaque.

- Les attaques des héros et des alliés peuvent cibler n'importe quel ennemi, à moins qu'une capacité de carte (telle que Garde) n'empêche cet ennemi d'être attaqué.
- Lorsqu'une attaque cible plusieurs ennemis, le personnage attaquant est considéré comme ayant attaqué chacun de ces ennemis.
    - Chaque ennemi attaqué possédant le mot-clé `riposte X` qui est toujours en jeu après la résolution de l'attaque inflige ses dégâts de riposte au personnage attaquant.

- L'ordre de résolution des capacités déclenchées par la résolution d'une attaque est le suivant :
    1. Le mot-clé `riposte X` (si le personnage attaqué n'a pas été vaincu).
    2. Les capacités forcées avec les déclencheurs suivants (dans n'importe quel ordre) :
        - `après que [personnage] attaque [et blesse/vainc] [un ennemi/un sbire]...`
        - `après que [personnage] est attaqué...`
    3. Les capacités non-forcées avec les déclencheurs listés ci-dessus.
    4. Les dégâts consécutifs (pour les alliés).

Voir aussi : Allié, Pouvoir de base, Dégâts, Défendre, Ennemi, Identité, Capacité étiquetée, Sbire, Modificateurs, Riposte X, Cible, Méchant



**EN v1.7**:  
```
ATTACK (PLAYER ABILITY TYPE)
Some game effects and card abilities reference an attack.
There are a few different ways an attack can occur:
• A hero or ally can use their basic attack power to attack an enemy. A character must exhaust to use this power. This deals damage equal to the character’s ATK value to the enemy.
» » A character can only initiate a basic attack if there is an enemy that can be attacked by that character or if that character is stunned.
• If a triggered ability is labeled as an attack—such as "Hero Action (attack)"—resolving that ability is considered to attack the specified target. Unless specified by the ability’s text, a hero does not exhaust when using such an ability.
» » An ability labeled as an attack is considered a single attack, even if that attack deals multiple instances of damage.
» » When an attack ability has its damage increased by another ability, each instance of damage in that attack ability that does not use the word "additional" is increased by the specified amount.
• If an ability says "Make the following X attacks in order," followed by two or more instances of damage, each of those instances is considered a separate attack.
» » An ability that increases the damage of an attack only increases the damage of one of that ability’s attacks, though such an ability can be triggered separately for each attack.
• Hero and ally attacks can target any enemy, unless a card ability (such as guard) is preventing that enemy from being attacked.
• When an attack targets multiple enemies, the attacking character is considered to have attacked each of those enemies.
» » Each attacked enemy with the retaliate X keyword that is still in play after the attack resolves deals its retaliate damage to the attacking character.
• The order of resolution for abilities triggered by the resolution of an attack is as follows:
1. The retaliate X keyword (if the attacked character was not defeated).
2. Forced abilities with the following triggers (in any order):
» » "after [character] attacks [and damages/defeats] [an enemy/a minion]..."
» » "after [character] is attacked..."
3. Non-forced abilities with the triggers listed above.
4. Consequential damage (for allies).
See also: Ally, Basic Power, Damage, Defend, Enemy, Identity, Labeled Ability, Minion, Modifiers, Retaliate X, Target, Villain
```




**FR v1.4**:  
```
ATTAQUE, ATTAQUER
Certains effets de jeu et capacités de cartes parlent d’attaque.
Il y a différentes façons d’attaquer :
• Un héros peut utiliser son pouvoir de base d’attaque pour attaquer un ennemi. Un héros doit s’incliner pour utiliser ce pouvoir. Cela inflige à l’ennemi des dégâts égaux à la valeur d’ATQ du héros.
• Un allié peut utiliser son pouvoir de base d’attaque pour attaquer un ennemi. Cela inflige à l’ennemi des dégâts égaux à la valeur d’ATQ de cet allié.
• Si une capacité déclenchée est référencée en tant qu’attaque — comme « Action de héros (attaque) » — résoudre cette capacité est considéré comme une attaque contre la cible spécifiée. À moins que cela ne soit spécifiquement indiqué, un héros ne s’incline pas lorsqu’il utilise une telle capacité.
• Les attaques des héros et des alliés peuvent cibler n’importe quel ennemi, à moins qu’une capacité de carte (comme Garde) n’empêche cet ennemi d’être attaqué.
• Les ennemis peuvent attaquer lors de la deuxième étape de la phase du Méchant.
• Des capacités de cartes peuvent faire attaquer le méchant et/ou les sbires à d’autres moments si la capacité en question demande explicitement au méchant ou au sbire « d’attaquer ».
Voir aussi : Allié, Attaques des Ennemis, Cible, Défendre, Dégâts, Ennemi, Identité, Méchant, Pouvoir de Base, Sbire
```