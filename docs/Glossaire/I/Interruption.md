# Interruption


Interruption est un type de capacité déclenchée. Une capacité d'interruption peut être exécutée chaque fois que sa condition de déclenchement est sur le point de se produire.

  - Une interruption interrompt le déroulement du jeu et se résout immédiatement avant sa condition de déclenchement.

  - Si une interruption est utilisée, la résolution de la condition de déclenchement est temporairement suspendue jusqu'à ce que l'interruption soit résolue.

**Voir aussi** : Capacité, Interruption forcée, Priorité temporelle, Capacité déclenchée


**EN v1.7**:  
```
INTERRUPT
An interrupt ability is a type of triggered ability, indicated by the bold "Interrupt" timing trigger. Interrupt abilities may be executed anytime the specified triggering condition occurs, as described in the interrupt’s ability text. The interrupt ability interrupts the resolution of the specified triggering condition, and resolves immediately before that triggering condition resolves.
• Players can only trigger interrupt abilities on cards they control or on encounter cards.
» » Players cannot trigger interrupt abilities on obligations in other players’ play areas.
• Multiple interrupts may be triggered by the same triggering condition, but each interrupt can only be triggered once per occurrence of the triggering condition.
» » Multiple copies of a card with an interrupt can each be triggered by the same triggering condition.
• An interrupt ability is executed when its triggering condition initiates, but before that triggering condition resolves.
» » Interrupts that use the word "would" resolve before its triggering condition initiates, when that condition becomes imminent.
• If an interrupt changes (via a replacement effect) or cancels an imminent triggering condition, further interrupts to the original triggering condition cannot be triggered.
• Once all players decide they do not wish to resolve any (further) interrupts to a triggering condition, (further) interrupts to that instance of that triggering condition cannot be used.
See also: Cancel, Replacement Effect, Triggered Ability, "Would"
```


**FR v1.4**:  
```
INTERRUPTION
Une capacité d’interruption est un type de capacité déclenchée signalé par l’indicatif de déclenchement « Interruption
» en gras. Les capacités d’interruption peuvent être exécutées chaque fois que les conditions de déclenchement spécifiées se produisent telles que décrites dans le texte de la capacité d’interruption. La capacité d’interruption interrompt la condition de déclenchement spécifiée et se résout immédiatement avant que cette condition de déclenchement ne se résolve.
• Plusieurs interruptions peuvent être déclenchées par la même condition de déclenchement.
• Une capacité d’interruption est exécutée quand sa condition de déclenchement devient imminente, mais avant qu’elle ne se résolve. Les opportunités d’interrompre ont lieu dans l’ordre des joueurs jusqu’à ce que tous les joueurs aient consécutivement passé.
• Une fois que tous les joueurs ont consécutivement passé leur opportunité d’interrompre une condition de déclenchement imminente, aucune autre interruption pour cette condition de déclenchement spécifique ne peut être utilisée.
• Si une interruption change (via un effet de remplacement) ou annule une condition de déclenchement imminente, d’autres interruptions à la condition de déclenchement originelle ne peuvent pas être déclenchées.
Voir aussi : Annuler, Capacité Déclenchée, Effets de Remplacement
```