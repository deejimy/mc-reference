# Attaque (Activation des Ennemis)

Une attaque est un type d’activation des ennemis. Lorsqu’un ennemi attaque, il cible un joueur spécifique. Ensuite, il résout cette attaque contre ce joueur.  

- <span class="new">Les attaques ennemies sont toujours initiées à la fois contre un joueur et contre un personnage.</span>  
    - <span class="new">Normalement, le personnage attaqué est le héros du joueur, mais des capacités peuvent faire en sorte qu’un ennemi attaque l’alter‑ego du joueur ou un allié contrôlé par ce joueur. Dans tous ces cas, le joueur est toujours considéré comme attaqué.</span>  
    - <span class="new">Si un personnage autre que le personnage attaqué défend l’attaque, ce personnage devient la nouvelle cible de l’attaque.</span>  
    - <span class="new">Si un joueur autre que le joueur attaqué défend l’attaque avec un personnage qu’il contrôle, ce joueur devient la nouvelle cible de l’attaque.</span>  
    - <span class="new">Les capacités qui se déclenchent « Quand/Après [ennemi] vous attaque » se résolvent quand/après qu’un joueur est attaqué, quel que soit le personnage qu’il contrôle qui a été attaqué. (Par exemple, Ultron I : « Réponse Forcée : Après qu’Ultron vous a attaqué, choisissez soit de placer 1 menace sur la manigance principale, soit de mettre la carte du dessus de votre deck en jeu face cachée, engagée avec vous comme sbire drone. » Cet effet se résout contre le joueur attaqué même si ce joueur a utilisé un allié pour défendre l’attaque.)</span>  

Pour résoudre une attaque ennemie, respectez les étapes suivantes :  

1. Si un méchant, ou un sbire ayant le mot‑clé vilenie, attaque, donnez‑lui une carte de boost face cachée prise sur le deck Rencontre. (Si un sbire sans le mot‑clé vilenie attaque, ignorez cette étape.)  
2. Si un joueur souhaite défendre, ce joueur incline un héros ou un allié comme défenseur. Si un joueur autre que le joueur ciblé défend, le joueur qui défend devient le nouveau joueur ciblé par cette attaque.  
3. <span class="new">Résolvez chacune des cartes de boost de l’ennemi attaquant, une à la fois et dans l’ordre dans lequel elles ont été distribuées, en procédant de la manière suivante :</span>  
    1.  <span class="new">Retournez la carte de boost face visible.</span>  
    2. <span class="new">Résolvez toute capacité « Boost : », indiquée par l’icône d’étoile dans le champ de boost. (Toutes les autres capacités imprimées sur la carte de boost sont ignorées.)</span>  
    3. <span class="new">Augmentez la valeur d’ATQ de l’ennemi attaquant de 1 pour chaque icône de boost sur la carte.</span>  
    4. <span class="new">Défaussez la carte de boost.</span>  
    5. <span class="new">Si l’ennemi a encore des cartes de boost, répétez ces étapes avec la carte suivante.</span>  

4. Infligez les dégâts de l’attaque égaux à la valeur d’ATQ modifiée de l’ennemi attaquant, selon les cas suivants :  
- Si un héros effectue une défense de base contre l’attaque, la quantité de dégâts infligés est réduite par la valeur de DEF de ce héros, et les dégâts restants sont infligés à ce héros.  
    - <span class="new">Le héros qui défend est considéré comme ayant été attaqué.</span>  
    - <span class="new">Si un héros ayant l’état Tenace effectue une défense de base, les dégâts sont d’abord réduits par la valeur DEF de ce héros. Si les dégâts sont réduits à 0, le héros conserve son état Tenace.</span>  
- Si un allié défend contre l’attaque, tous les dégâts de l’attaque sont infligés à l’allié. (Si l’allié est vaincu par l’attaque, les dégâts en excès ne sont pas infligés à l’identité.)  
    - <span class="new">Si l’allié défenseur quitte le jeu avant que les dégâts de l’attaque ne soient infligés, l’attaque est considérée comme n’ayant aucun personnage en défense et l’identité du contrôleur de cet allié devient la cible de l’attaque.</span>  
- Si aucun personnage ne défend contre l’attaque, l’attaque est considérée comme non défendue. Tous les dégâts de l’attaque sont infligés au personnage ciblé par l’attaque.  
    - <span class="new">Le personnage ciblé est considéré comme ayant été attaqué.</span>  

5. <span class="new">L’attaque termine sa résolution et les types de capacités suivants se déclenchent dans l’ordre :</span>  
    - <span class="new">Le mot‑clé Riposte X (si le personnage attaqué est toujours en jeu).</span>  
    - <span class="new">Les capacités forcées avec les déclencheurs suivants (dans n’importe quel ordre) :</span>  
        - <span class="new">"après que [personnage] attaque [et inflige/des dégâts/vainc] [vous/un allié]..."</span>  
        - <span class="new">"après que [personnage] est attaqué..."</span>  
        - <span class="new">"après que [personnage] défend [et ne subit aucun dégât]..."</span>  
        - <span class="new">"après que [personnage] [subit/ inflige] des dégâts..."</span>  
    - <span class="new">Les capacités non‑forcées avec les déclencheurs listés ci‑dessus.</span>  

<span class="new">Ces règles s’appliquent également aux attaques ennemies :</span>  

- <span class="new">Les Interruptions qui se déclenchent "quand [nom de l’ennemi] attaque" ont le même timing que les Interruptions qui se déclenchent "quand [le méchant/un ennemi] initie une attaque".</span>  
- <span class="new">Si une attaque ennemie se termine avant que les dégâts ne soient infligés, les capacités qui se déclenchent après qu’un personnage a défendu une attaque se résolvent, mais les capacités qui se déclenchent après qu’un ennemi attaque ne se résolvent pas.</span>  

_Voir aussi : [[Activation|Activation]], [[Allie|Allié]], [[AttaquesContreLesAllies|Attaques contre les Alliés]], [[BoostIconeDeBoost|Boost]], [[Degats|Dégâts]], [[DefendreDefense|Défendre]], [[Ennemi|Ennemi]], [[Identite|Identité]], [[Modificateurs|Modificateurs]], [[RiposteX|Riposte X]], [[Cible|Cible]], [[MechantDeckMechant|Méchant]], [[Sbire|Sbire]], [[Vilenie|Vilenie]]_  

<details class="source">
<summary>EN v1.7</summary>ATTACK (ENEMY ACTIVATION)
An attack is a type of enemy activation. When an enemy initiates an attack, it targets a specific player, then resolves that attack against that player.
• Enemy attacks are always initiated against both a player and a character.
» » Normally the attacked character is the player’s hero, but abilities can instead cause an enemy to attack a player’s alter-ego or an ally that player controls. In all of these cases, the player is still considered attacked.
» » If a character other than the attacked character defends the attack, that character becomes the new target of that attack.
» » If a player other than the attacked player defends the attack with a character they control, that player becomes the new target of that attack.
» » Abilities that trigger "When/After [enemy] attacks you" are resolved when/after a player is attacked, regardless of which character they control was attacked. (For example, Ultron I reads: "Forced Response: After Ultron attacks you, choose to either place 1 threat on the main scheme or put the top card of your deck into play facedown, engaged with you as a drone minion." This effect resolves against the attacked player regardless of if that player used an ally to defend the attack.) To resolve an enemy attack, follow these steps:
1. If a villain, or a minion with the villainous keyword, is attacking, give it one facedown boost card from the encounter deck. (If a minion without the villainous keyword is attacking, skip this step.)
2. If a player wishes to defend, that player exhausts a hero or ally as the defender. If a player other than the target player defends, the defending player becomes the target player for this attack.
3. Resolve each of the attacking enemy’s boost cards, one at a time and in the order in which they were dealt, by doing the following: 
  a. Flip the boost card faceup. 
  b. Resolve any "Boost" abilities, indicated by the star icon in the boost area. (All other abilities on the boost card are ignored.) 
  c. Increase the attacking enemy’s ATK value by one for each boost icon on the card. 
  d. Discard the boost card. 
  e. If the enemy has any boost cards remaining, repeat these steps with the next boost card.
4. Deal damage from the attack equal to the attacking enemy’s modified ATK value, based on the following:
• If a hero makes a basic defense against the attack, the amount of damage dealt is reduced by that hero’s DEF value, and the remaining damage from the attack is dealt to that hero.
» » The defending hero is considered to have been attacked.
» » If a hero with a tough status makes a basic defense, the damage is first reduced by that hero’s DEF value. If the damage is reduced to 0, the hero keeps their tough status.
• If an ally defends against the attack, all damage from the attack is dealt to the ally. (If the ally is defeated by the attack, additional damage does not carry over to the identity.)
» » The defending ally is considered to have been attacked.
» » If the defending ally leaves play prior to damage from the attack being dealt, the attack is considered to have no character defending and the identity of that ally’s controller becomes the target of the attack.
• If no character defends against the attack, the attack is considered undefended. All damage from the attack is dealt to the character targeted by the attack.
» » The targeted character is considered to have been attacked.
5. The attack finishes resolving and the following types of abilities trigger in order: a. The retaliate X keyword (if the attacked character is still in play). b. Forced abilities with the following triggers (in any order):
» » "after [character] attacks [and damages/defeats] [you/an ally]..."
» » "after [character] is attacked..."
» » "after [character] defends [and takes no damage]..."
» » "after [character] [takes/deals] damage..." c. Non-forced abilities with the triggers listed above.
These rules also apply to enemy attacks:
• Interrupts that trigger "when [enemy name] attacks" have the same timing as interrupts that trigger "when [the villain/an enemy] initiates an attack."
• If an enemy attack ends before damage is dealt, abilities that trigger after a character defends an attack resolve, but abilities that trigger after an enemy attacks do not.
See also: Activation, Ally, Attacks Against Allies, Boost, Damage, Defend, Enemy, Identity, Minion, Modifiers, Retaliate X, Target, Villain, Villainous
</details>


<details class="source">
<summary>FR v1.4</summary>ATTAQUE (ACTIVATION DES ENNEMIS)
Une attaque est un type d’activation des ennemis. Lorsqu’un ennemi attaque, il cible un joueur spécifique. Ensuite, il résout cette attaque contre ce joueur. Pour résoudre une attaque ennemie, respectez les étapes suivantes :
1. Si un méchant ou un sbire ayant le mot clé Vilenie attaque, donnez-lui une carte de boost face cachée prise sur le deck Rencontre. (Si un sbire sans le mot clé Vilenie attaque, ignorez cette étape.)
2. Si un joueur souhaite défendre, il incline un héros ou un allié en tant que défenseur. Si un joueur autre que le joueur ciblé défend, le joueur qui défend devient le nouveau joueur ciblé par cette attaque.
3. Retournez chaque carte de boost de l’ennemi attaquant face visible, une à la fois. (Si un sbire sans le mot clé Vilenie attaque, ignorez cette étape.) Puis dans cet ordre :
• Résolvez toute capacité « Boost : », indiquée par une icône d’étoile dans le champ de boost.
• Augmentez de 1 la valeur d’ATQ de l’ennemi attaquant pour chaque icône de boost sur la carte.
• Défaussez chaque carte de boost après sa résolution.
4. Infligez les dégâts de l’attaque. Ces derniers sont égaux à la valeur d’ATQ de l’ennemi attaquant modifiée de la manière suivante :
• Si un héros effectue une défense de base contre l’attaque, la quantité de dégâts infligés est réduite par la valeur de DEF de ce héros et les dégâts restants sont infligés à ce héros.
• Si un allié défend contre l’attaque, tous les dégâts de l’attaque sont infligés à cet allié. (Si l’allié est vaincu par l’attaque, les dégâts en excès ne sont pas infligés à l’identité.)
• Si aucun personnage ne défend contre l’attaque, l’attaque est considérée comme non défendue. Tous les dégâts de cette attaque sont infligés à l’identité du joueur ciblé (même si cette identité est sous sa forme d’alter ego).
Voir aussi : Activation, Allié, Boost, Cible, Défendre, Dégâts, Ennemi, Identité, Méchant, Sbire, Vilenie
</details>