# Serait


Le mot "devrait" (ou "serait") est utilisé pour définir la condition de déclenchement de certaines capacités d'interruption, et établit une priorité de timing plus élevée pour ces capacités que pour les interruptions au même déclencheur ne possédant pas le mot "devrait".

  - Si une interruption à une condition de déclenchement qui "devrait" se produire modifie la nature de ce qui est sur le point d'arriver (par exemple via un effet de remplacement), aucune autre interruption au déclencheur original ne peut être utilisée car la résolution de ce déclencheur n'est plus valide.
Par exemple, une interruption qui indique "quand un personnage devrait être vaincu" se déclenche avant une interruption qui indique "quand un personnage est vaincu".

**Voir aussi** : Interruption, Effet de remplacement, Capacité déclenchée

