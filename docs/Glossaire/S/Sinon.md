# "Sinon"

Les effets commençant par « sinon » ne se résolvent que si l'effet précédent ne s'est pas résolu.  

- Un effet « sinon » se résout si une ou plusieurs des conditions suivantes concernant l'effet précédent sont vraies :  
    - Il a une condition qui n'est pas vraie. (Par exemple, une capacité indique : « Si vous êtes en forme Héros, subissez 2 dégâts. Sinon, placez 2 menaces sur la manigance principale. » La partie « sinon » se résout si le joueur n'est pas en forme Héros.)  
    - Il possède un effet qui ne peut pas, au minimum, se résoudre partiellement. (Par exemple, une capacité indique : « Défaussez 2 cartes de votre main. Sinon, inclinez votre identité. » La partie « sinon » se résout si le joueur ne peut pas défausser au moins 1 carte de sa main.)  

- Si « sinon » est précédé d'un point‑virgule, « l'effet précédent » fait référence aux effets situés avant le point‑virgule dans la même phrase. Si l'effet « sinon » constitue sa propre phrase, « l'effet précédent » fait référence à la phrase placée directement avant la phrase « sinon ».  

_Voir aussi : [[EffetsDeRemplacement|Effets de remplacement]], [[Cible|Cible]]_  

<details class="source">
<summary>EN v1.7</summary>"OTHERWISE"
Effects beginning with "otherwise" resolve only if the preceding effect was not resolved.
• An "otherwise" effect will resolve if one or more of the following are true of the preceding effect:
» » It has a condition that is not true. (For example, an ability reads: "If you are in hero form, take 2 damage. Otherwise, place 2 threat on the main scheme." The "otherwise" portion resolves if the player is not in hero form.)
» » It has an effect that cannot at least partially resolve.
(For example, an ability reads: "Discard 2 cards from your hand. Otherwise, exhaust your identity."
The "otherwise" portion resolves if the player cannot discard at least 1 card from their hand.)
• If "otherwise" is preceded by a semicolon, the "preceding effect" refers to the effects before the semicolon in the same sentence. If the "otherwise" effect is its own sentence, the "preceding effect" refers to the sentence coming directly before the "otherwise" sentence.
See also: Replacement Effect, Target
</details>