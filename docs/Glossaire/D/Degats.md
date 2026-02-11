# Dégâts

![[pion_degat.png]] Les dégâts réduisent la santé d'un personnage. S'ils ne sont pas prévenus, les dégâts sont infligés à un personnage en plaçant un nombre de jetons de dégâts sur ce personnage égal à la quantité de dégâts infligés.  

- Si un personnage subit une quantité de dégâts égale ou supérieure à sa santé, le personnage est vaincu.  
- S'il est précisé qu'une capacité inflige des dégâts à un ou plusieurs personnages, ces dégâts ne peuvent pas être réduits par la valeur de DEF d'un personnage.  
- Les dégâts infligés par une attaque sont considérés comme des "dégâts d'attaque".  
- Les dégâts infligés par une capacité étiquetée comme une attaque sont également considérés comme des dégâts d'attaque.  
- Les dégâts infligés par une capacité non étiquetée comme une attaque ne sont pas des dégâts d'attaque, même si l'effet a été déclenché par une attaque.  
- Les dégâts infligés par un mot-clé (tel que `riposte`) ne sont pas des dégâts d'attaque.  
- Tout effet de carte qui "inflige" des dégâts est considéré comme une attaque si la capacité est étiquetée comme telle.  
- Si des dégâts sont infligés à une cible qui ne possède pas de valeur de santé (comme une manigance), ces dégâts sont ignorés.  
- Le mot "subit" ou "subit des dégâts" se réfère au moment où des dégâts non prévenus sont placés sur un personnage.  

<span class="new">- Quand des dégâts sont infligés à un personnage, ce personnage subit ces dégâts.  
    - Quand la quantité de dégâts qu’un effet inflige est modifiée, la quantité de dégâts subis par le personnage est modifiée de la même façon.  
    - Quand la quantité de dégâts qu’un personnage subit est modifiée (par exemple si des dégâts sont prévenus), la quantité de dégâts infligés n’est pas modifiée.  
    - <strong>Ordre de résolution</strong> :  
      1. Les capacités qui se déclenchent « quand [personnage] infligerait/subirait n’importe quelle quantité de dégâts... »  
      2. Les cartes d’état Tenace.  
      3. Les capacités qui se déclenchent « quand [personnage] serait sur le point de subir n’importe quelle quantité de dégâts... »  
      4. Les capacités qui se déclenchent « quand [personnage] subit n’importe quelle quantité de dégâts... »  
      5. Le placement des dégâts sur le personnage.  
      6. Les capacités qui se déclenchent « quand [personnage] serait vaincu... »  
      7. Les capacités qui se déclenchent « quand [personnage] est vaincu... »  
      8. Les capacités « Une fois vaincu ».  
      9. La défausse d’un personnage vaincu.  
      10. Les capacités qui se déclenchent « après que [personnage] inflige/subit n’importe quelle quantité de dégâts... » ou « après que [personnage] vainc/est vaincu... ».</span>  

**EN v1.7**:  
```
DAMAGE
![[pion_degat.png]]
Damage reduces a character’s hit points.
If a character has zero or fewer remaining hit points, it is defeated.
• Damage on an identity or villain is tracked by a hit point dial. If such a character takes damaged, reduce its dial by the amount of damage that it took.
• Damage on an ally or minion is tracked by damage tokens. If such a character takes damage, place the specified value of damage tokens on the character.
• When damage is dealt to a character, that character takes damage.
» » When the amount of damage an effect deals is modified, the amount of damage the character takes is similarly modified.
» » When the amount of damage a character takes is modified (such as by damage being prevented), the amount of damage dealt is not modified.
» » The order of resolution for effects surrounding the dealing and taking of damage are as follows:
1. Abilities that trigger "when [character] would deal/be dealt any amount of damage..."
2. Tough status cards.
3. Abilities that trigger "when [character] would take any amount of damage..."
4. Abilities that trigger "when [character] takes any amount of damage..."
5. Placing of damage on the character.
6. Abilities that trigger "when [character] would be defeated..."
7. Abilities that trigger "when [character] is defeated..."
8. "When Defeated" abilities.
9. Discarding of a defeated character.
10. Abilities that trigger "after [character] deals/is dealt/takes any amount of damage..." or "after [character] defeats/is defeated..."
See also: Component Limitations, Defeat, Hit Points, Indirect Damage, Move, Prevent, Tough
```


**FR v1.4**:  
```
DEGÂTS
Les dégâts réduisent les points de vie d’un personnage. Si un personnage tombe à zéro point de vie ou moins, il est vaincu.
• Les dégâts sur les héros/alter ego et le méchant sont indiqués via un compteur de points de vie. Si un tel personnage est blessé, diminuez la valeur de son compteur du montant de dégâts subis.
• Les dégâts sur les alliés et les sbires sont indiqués via des pions Dégât. Si un tel personnage est blessé, placez un nombre de pions Dégât correspondants sur ce personnage.
Voir aussi : Dégâts Indirects, Déplacer, Limitation du matériel (p. 4), Prévenir, Points de Vie, Vaincre/Déjouer
```