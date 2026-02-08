# Serait


Le mot "devrait" (ou "serait") est utilisé pour définir la condition de déclenchement de certaines capacités d'interruption, et établit une priorité de timing plus élevée pour ces capacités que pour les interruptions au même déclencheur ne possédant pas le mot "devrait".

  - Si une interruption à une condition de déclenchement qui "devrait" se produire modifie la nature de ce qui est sur le point d'arriver (par exemple via un effet de remplacement), aucune autre interruption au déclencheur original ne peut être utilisée car la résolution de ce déclencheur n'est plus valide.
Par exemple, une interruption qui indique "quand un personnage devrait être vaincu" se déclenche avant une interruption qui indique "quand un personnage est vaincu".

**Voir aussi** : Interruption, Effet de remplacement, Capacité déclenchée


```
"WOULD"
The word "would" is used to define the triggering condition
of some interrupt abilities, and establishes a higher timing
priority for those abilities than interrupts to the same
triggering condition without the word "would."

  - If an interrupt to a triggering condition that would
occur changes the nature of that which is about to
occur (such as through a replacement effect), no
further interrupts to the original trigger may be used
since the resolution of that trigger is no longer valid.
For example, an interrupt that states "when a character
would be defeated" triggers before an interrupt that states
"when a character is defeated."


See also: Interrupt, Replacement Effect, Triggered Ability
```