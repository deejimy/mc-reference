# Attaque (Activation des Ennemis)


Une attaque est un type d'activation d'ennemi. Lorsqu'un ennemi initie une attaque, il cible un joueur spécifique, puis résout cette attaque contre ce joueur.

- Les attaques d'ennemis sont toujours initiées à la fois contre un joueur et contre un personnage.
    - Normalement, le personnage attaqué est le héros du joueur, mais des capacités peuvent forcer un ennemi à attaquer l'alter-ego d'un joueur ou un allié que ce joueur contrôle. Dans tous ces cas, le joueur est toujours considéré comme étant attaqué.
    - Si un personnage autre que le personnage attaqué défend l'attaque, ce personnage devient la nouvelle cible de cette attaque.
    - Si un joueur autre que le joueur attaqué défend l'attaque avec un personnage qu'il contrôle, ce joueur devient la nouvelle cible de cette attaque.
    - Les capacités qui se déclenchent `Quand/Après que [ennemi] vous attaque` sont résolues quand/après qu'un joueur est attaqué, quel que soit le personnage qu'il contrôle qui a été attaqué. (Par exemple, Ultron I indique : `Réponse forcée : après qu'Ultron vous a attaqué, choisissez de soit placer 1 menace sur la manigance principale, soit de mettre la carte du dessus de votre deck en jeu face cachée, engagée avec vous en tant que sbire drone.` Cet effet se résout contre le joueur attaqué, peu importe si ce joueur a utilisé un allié pour défendre l'attaque.)

Pour résoudre une attaque d'ennemi, suivez ces étapes :

1. Si un méchant, ou un sbire avec le mot-clé `vilenie`, attaque, donnez-lui une carte de boost face cachée du deck Rencontre. (Si un sbire sans le mot-clé `vilenie` attaque, ignorez cette étape.)
2. Si un joueur souhaite défendre, ce joueur incline un héros ou un allié en tant que défenseur. Si un joueur autre que le joueur ciblé défend, le joueur défenseur devient le joueur cible pour cette attaque.
3. Résolvez chacune des cartes de boost de l'ennemi attaquant, une par une et dans l'ordre où elles ont été distribuées, en procédant comme suit :
    1. Retournez la carte de boost face visible.
    2. Résolvez toutes les capacités de `Boost`, indiquées par l'icône étoile (![[icone_etoile.jpg|15]]) dans la zone de boost. (Toutes les autres capacités sur la carte de boost sont ignorées.)
    3. Augmentez la valeur d'ATK de l'ennemi attaquant de 1 pour chaque icône de boost sur la carte.
    4. Défaussez la carte de boost.
    5. Si l'ennemi possède encore des cartes de boost, répétez ces étapes avec la carte suivante.
4. Infligez les dégâts de l'attaque égaux à la valeur d'ATK modifiée de l'ennemi, selon les cas suivants :
    - Si un héros effectue une défense de base contre l'attaque, la quantité de dégâts infligés est réduite de la valeur de DEF de ce héros, et les dégâts restants de l'attaque sont infligés à ce héros.
        - Le héros défenseur est considéré comme ayant été attaqué.
        - Si un héros avec un état tenace effectue une défense de base, les dégâts sont d'abord réduits par la valeur de DEF du héros. Si les dégâts sont réduits à 0, le héros conserve son état tenace.
    - Si un allié défend contre l'attaque, tous les dégâts de l'attaque sont infligés à l'allié. (Si l'allié est vaincu par l'attaque, les dégâts excédentaires ne sont pas reportés sur l'identité.)
        - L'allié défenseur est considéré comme ayant été attaqué.
        - Si l'allié défenseur quitte le jeu avant que les dégâts de l'attaque ne soient infligés, l'attaque est considérée comme n'ayant aucun personnage défenseur et l'identité du contrôleur de cet allié devient la cible de l'attaque.
    - Si aucun personnage ne défend contre l'attaque, l'attaque est considérée comme sans défense. Tous les dégâts de l'attaque sont infligés au personnage ciblé par l'attaque.
        - Le personnage ciblé est considéré comme ayant été attaqué.
5. L'attaque finit de se résoudre et les types de capacités suivantes se déclenchent dans l'ordre :
    1. Le mot-clé `riposte X` (si le personnage attaqué est toujours en jeu).
    2. Les capacités forcées avec les déclencheurs suivants (dans n'importe quel ordre) :
        - `après que [personnage] attaque [et blesse/vainc] [vous/un allié]...`
        - `après que [personnage] est attaqué...`
        - `après que [personnage] défend [et ne subit aucun dégât]...`
        - `après que [personnage] [subit/inflige] des dégâts...`
    3. Les capacités non-forcées avec les déclencheurs listés ci-dessus.

Ces règles s'appliquent également aux attaques d'ennemis :

- Les interruptions qui se déclenchent `quand [nom de l'ennemi] attaque` ont le même timing que les interruptions qui se déclenchent `quand [le méchant/un ennemi] initie une attaque`.
- Si une attaque d'ennemi se termine avant que les dégâts ne soient infligés, les capacités qui se déclenchent après qu'un personnage défend une attaque se résolvent, mais les capacités qui se déclenchent après qu'un ennemi attaque ne se résolvent pas.

**Voir aussi** : Activation, Allié, Attaques contre des alliés, Boost, Dégâts, Défendre, Ennemi, Identité, Sbire, Modificateurs, Riposte X, Cible, Méchant, Vilenie


```
ATTACK (ENEMY ACTIVATION)
An attack is a type of enemy activation. When an enemy
initiates an attack, it targets a specific player, then resolves
that attack against that player.

  - Enemy attacks are always initiated against both a
player and a character.

  - Normally the attacked character is the player’s
hero, but abilities can instead cause an enemy to
attack a player’s alter-ego or an ally that player
controls. In all of these cases, the player is still
considered attacked.

  - If a character other than the attacked character
defends the attack, that character becomes the
new target of that attack.

  - If a player other than the attacked player defends
the attack with a character they control, that player
becomes the new target of that attack.

  - Abilities that trigger "When/After [enemy] attacks
you" are resolved when/after a player is attacked,
regardless of which character they control was
attacked. (For example, Ultron I reads: "Forced
Response: After Ultron attacks you, choose to
either place 1 threat on the main scheme or put the
top card of your deck into play facedown, engaged
with you as a drone minion." This effect resolves
against the attacked player regardless of if that
player used an ally to defend the attack.)
To resolve an enemy attack, follow these steps:
1. If a villain, or a minion with the villainous keyword, is
attacking, give it one facedown boost card from the
encounter deck. (If a minion without the villainous
keyword is attacking, skip this step.)
2. If a player wishes to defend, that player exhausts a hero
or ally as the defender. If a player other than the target
player defends, the defending player becomes the
target player for this attack.
3. Resolve each of the attacking enemy’s boost cards, one
at a time and in the order in which they were dealt, by
doing the following:
a. Flip the boost card faceup.
b. Resolve any "Boost" abilities, indicated by the star
icon in the boost area. (All other abilities on the
boost card are ignored.)
c. Increase the attacking enemy’s ATK value by one
for each boost icon on the card.
d. Discard the boost card.
e. If the enemy has any boost cards remaining, repeat
these steps with the next boost card.
4. Deal damage from the attack equal to the attacking
enemy’s modified ATK value, based on the following:

  - If a hero makes a basic defense against the attack,
the amount of damage dealt is reduced by that hero’s
DEF value, and the remaining damage from the attack
is dealt to that hero.

  - The defending hero is considered to have been
attacked.

  - If a hero with a tough status makes a basic defense,
the damage is first reduced by that hero’s DEF
value. If the damage is reduced to 0, the hero
keeps their tough status.

  - If an ally defends against the attack, all damage from
the attack is dealt to the ally. (If the ally is defeated by
the attack, additional damage does not carry over to
the identity.)

  - The defending ally is considered to have been
attacked.

  - If the defending ally leaves play prior to damage
from the attack being dealt, the attack is
considered to have no character defending and the
identity of that ally’s controller becomes the target
of the attack.

  - If no character defends against the attack, the attack
is considered undefended. All damage from the
attack is dealt to the character targeted by the attack.

  - The targeted character is considered to have been
attacked.
5. The attack finishes resolving and the following types of
abilities trigger in order:
a. The retaliate X keyword (if the attacked character
is still in play).
b. Forced abilities with the following triggers (in any
order):

  - "after [character] attacks [and damages/defeats]
[you/an ally]..."

  - "after [character] is attacked..."

  - "after [character] defends [and takes no
damage]..."

  - "after [character] [takes/deals] damage..."
c. Non-forced abilities with the triggers listed above.
These rules also apply to enemy attacks:

  - Interrupts that trigger "when [enemy name] attacks"
have the same timing as interrupts that trigger "when
[the villain/an enemy] initiates an attack."

  - If an enemy attack ends before damage is dealt,
abilities that trigger after a character defends an
attack resolve, but abilities that trigger after an
enemy attacks do not.


See also: Activation, Ally, Attacks Against Allies, Boost,
Damage, Defend, Enemy, Identity, Minion, Modifiers,
Retaliate X, Target, Villain, Villainous
```