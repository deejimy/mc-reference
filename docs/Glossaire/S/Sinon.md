# Sinon

L'effet commençant par "**sinon**" se résolvent uniquement si l'effet précédent n'a pas été résolu.

- Un effet "sinon" se résoudra si une ou plusieurs des conditions suivantes sont vraies concernant l'effet précédent :
    - Sa condition n'est pas remplie. (Par exemple, une capacité indique : "Si vous êtes sous forme de héros, subissez 2 dégâts. Sinon, placez 2 menaces sur la manigance principale." La partie "sinon" se résout si le joueur n'est pas sous forme de héros.).
    - Il a un effet qui ne peut pas se résoudre au moins partiellement. (Par exemple, une capacité indique : "Défaussez 2 cartes de votre main. Sinon, épuisez votre identité." La partie "sinon" se résout si le joueur ne peut pas défausser au moins 1 carte de sa main.)

- Si "sinon" est précédé d'un point-virgule, "l'effet précédent" fait référence aux effets avant le point-virgule dans la même phrase. Si l'effet "sinon" constitue sa propre phrase, "l'effet précédent" fait référence à la phrase venant directement avant la phrase "sinon".

**Voir aussi** : Effet de remplacement, Cible.

```
"OTHERWISE"
Effects beginning with "otherwise" resolve only if the
preceding effect was not resolved.

  - An "otherwise" effect will resolve if one or more of
the following are true of the preceding effect:

  - It has a condition that is not true. (For example,
an ability reads: "If you are in hero form, take
2 damage. Otherwise, place 2 threat on the main
scheme." The "otherwise" portion resolves if the
player is not in hero form.)

  - It has an effect that cannot at least partially resolve.
(For example, an ability reads: "Discard 2 cards
from your hand. Otherwise, exhaust your identity."
The "otherwise" portion resolves if the player
cannot discard at least 1 card from their hand.)

  - If "otherwise" is preceded by a semicolon, the
"preceding effect" refers to the effects before the
semicolon in the same sentence. If the "otherwise"
effect is its own sentence, the "preceding effect"
refers to the sentence coming directly before the
"otherwise" sentence.


See also: Replacement Effect, Target
```