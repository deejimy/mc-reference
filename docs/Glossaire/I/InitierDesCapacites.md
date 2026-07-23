# Initier des Capacités, Jouer des cartes  

Quand un joueur souhaite jouer une carte ou initier une capacité déclenchée, ce joueur doit d'abord déclarer son intention.  
Ensuite, il vérifie les conditions suivantes dans l'ordre :  

1. Si une carte est jouée, le joueur place cette carte face visible devant lui sur la table. (Cette carte n'est pas en jeu.)  
2. Vérifier les restrictions de jeu : la carte peut‑elle être jouée ou la capacité initiée à ce moment ?  
    - Si la carte ou la capacité précise une ou plusieurs cibles, vérifiez qu'il existe au moins une cible valide. Si la carte ou la capacité n'a pas au moins une cible valide, elle ne peut pas être jouée ni initiée.  
    - <span class="new">Si la carte ou la capacité a une exigence de forme (par exemple, « Forme héros uniquement » ou « Action héroïque »), la forme du joueur qui joue cette carte ou initie cette capacité est vérifiée maintenant.</span>  
3. Déterminer le coût (ou les coûts) pour jouer la carte ou initier la capacité et la capacité du joueur à les payer, en prenant en compte les modificateurs.  
    - <span class="new">Si une carte a un coût en ressources exprimé par X, le joueur qui la joue choisit la valeur de X lors de cette étape.</span>  
Si ces deux conditions sont remplies, accomplissez les étapes suivantes, dans l'ordre :  
4. Appliquez tous les modificateurs au(x) coût(s).  
5. Payez le ou les coûts. Si cette étape est atteinte et que le(s) coût(s) ne peuvent pas être payés, mettez fin à ce processus sans payer aucun coût.  
6. La carte commence à être jouée, ou les effets de la capacité tentent de s'initier.  
7. La carte est jouée ou la capacité (si elle n'a pas été annulée à l'étape précédente) est résolue. La carte entre en jeu ou, s'il s'agit d'une carte Événement, ses effets sont résolus puis elle est placée dans la pile de défausse de son propriétaire.

Si :  

- n'importe laquelle des étapes ci‑dessus devait remplir la condition de déclenchement d'une capacité d'interruption, cette capacité peut être initiée juste avant que cette condition ne soit remplie.  
- n'importe laquelle des étapes ci‑dessus devait remplir la condition de déclenchement d'une capacité de réponse, cette capacité peut être initiée immédiatement après que cette condition ait été remplie.  
- la capacité initiée se trouve sur une carte en jeu, la séquence ne s'interrompt pas si la carte quitte le jeu pendant la séquence, à moins que le fait que la carte quitte le jeu n'empêche un coût requis d'être payé.  

_Voir aussi : [[Capacite|Capacité]], [[Cible]], [[Cout|Coût]], [[RestrictionsEtPermissionsDeJeu|Restrictions et Permissions de Jeu]]_  

<details class="source">
<summary>EN v1.8</summary>INITIATING ABILITIES
When a player wishes to play a card or initiate a triggered ability, that player first declares their intent. Then, the player checks the following conditions in order:
1. If playing a card, the player places that card faceup on the table in front of them. (This card is not in play.)
2. Check play restrictions: can the card be played, or the ability initiated, at this time?
» If the card or ability specifies one or more targets, check that it has at least one valid target. If the card or ability does not have at least one valid target, it cannot be played or initiated.
» If the card or ability has a form requirement (for example, "Hero form only" or "Hero Action"), the form of the player playing that card or initiating that ability is checked now.
3. Determine the cost (or costs) to play the card or initiate the ability and the player’s ability to pay them, taking modifiers into account.
» If a card has a resource cost of X, the player playing that card chooses the value of X during this step.
If both conditions are met, follow these steps in order:
4. Apply any modifiers to the cost(s).
5. Pay the cost(s). If this step is reached and the cost(s) cannot be paid, abort this process without paying any costs.
6. The card commences being played, or the effects of the ability attempt to initiate.
</details>

<details class="source">
<summary>EN v1.7</summary>INITIATING ABILITIES
When a player wishes to play a card or initiate a triggered ability, that player first declares their intent. Then, the player checks the following conditions in order:
1. Check play restrictions: can the card be played, or the ability initiated, at this time?
» » If the card or ability specifies one or more targets, check that it has at least one valid target. If the card or ability does not have at least one valid target, it cannot be played or initiated.
2. Determine the cost (or costs) to play the card or initiate the ability and the player's ability to pay them, taking modifiers into account.
» » If a card has a resource cost of X, the player playing that card chooses the value of X during this step.
If both conditions are met, follow these steps in order:
3. If playing a card, the player places that card faceup on the table in front of them. (This card is not in play.)
4. Apply any modifiers to the cost(s).
5. Pay the cost(s). If this step is reached and the cost(s) cannot be paid, abort this process without paying any costs.
6. The card commences being played, or the effects of the ability attempt to initiate.
7. The card is played or the ability (if not canceled in the previous step) resolves. The card enters play or, if it is an event card, its effects resolve and it is then placed in its owner's discard pile.
• If any of the above steps would make the triggering condition of an interrupt ability true, that ability may be initiated just before that triggering condition becomes true.
• If any of the above steps would make the triggering condition of a response ability true, that ability may be initiated immediately after that triggering condition becomes true.
• If the ability being initiated is on a card that is in play, the sequence does not stop from completing if that card leaves play during this sequence unless the card leaving play prevents a required cost from being paid.
See also: Ability, Cost, Play Restrictions and Permissions, Target
</details>


<details class="source">
<summary>FR v1.4</summary>INITIER DES CAPACITES, JOUER DES CARTES
Quand un joueur souhaite jouer une carte ou initier une capacité déclenchée, ce joueur doit d'abord déclarer son intention.
Ensuite, il vérifie les conditions suivantes dans l'ordre :
1. Vérifier les restrictions de jeu : la carte peut-elle être jouée ou la capacité initiée à ce moment ? (Cela inclut la vérification que la résolution ou l'effet est en mesure de modifier l'état de la partie.)
2. Déterminer le coût (ou les coûts) pour jouer la carte ou initier la capacité en prenant en compte les modificateurs.
Si ces deux conditions sont remplies, accomplissez les étapes suivantes, dans l'ordre :
3. Appliquez tous les modificateurs au(x) coût(s).
4. Payez le ou les coûts. Si le ou les coûts ne peuvent plus être payés quand cette étape est atteinte, mettez fin au processus sans payer aucun coût.
5. Faites tous les « choix » requis pour résoudre la carte.
6. La carte commence à être jouée ou les effets de la capacité tentent de s'initier.
7. La carte est jouée ou la capacité (si elle n'a pas été annulée en étape 6) est résolue. La carte entre en jeu ou, s'il s'agit d'une carte Evénement, ses effets sont résolus et elle est placée dans la pile de défausse de son propriétaire.
• Si n'importe laquelle des étapes ci-dessus est censée remplir la condition de déclenchement d'une capacité d'interruption, cette capacité peut être initiée juste avant que la condition de déclenchement ne soit remplie.
• Si n'importe laquelle des étapes ci-dessus est censée remplir la condition de déclenchement d'une capacité de réponse, cette capacité peut être initiée immédiatement après que la condition de déclenchement a été remplie.
• Si la capacité initiée se trouve sur une carte en jeu, la séquence ne s'interrompt pas si la carte quitte le jeu pendant la séquence, à moins que le fait que la carte quitte le jeu n'empêche un coût requis d'être payé.
Voir aussi : Capacité, Coût, Restrictions et Permissions de Jeu
</details>