# Limite


Le texte "Limite de X par [période]" restreint le nombre de fois qu'une capacité peut être déclenchée pendant la période spécifiée.

  - Si une capacité comporte une limite, chaque instance de cette capacité est comptée individuellement pour cette limite.

  - Si une capacité est déclenchée, elle est comptabilisée dans sa limite, même si l'effet de la capacité est annulé.

  - Le terme "par joueur" dans une limite signifie que chaque joueur possède sa propre limite pour cette capacité.

**Voir aussi** : Capacité, Max


```
LIMIT
"Limit X per [period]" is a limit that appears on some player
cards. These limits are card-specific. Each copy of an ability
with such a limit may be used X times per the specified
period, per instance of that ability.

  - If an effect with a limit is canceled, the card is
still considered to have been played or the ability
initiated, and it counts toward the limit.


See also: Player Card
```