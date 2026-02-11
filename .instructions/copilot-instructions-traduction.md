# Instructions

## Contexte
Créer un référentiel du jeu Marvel Champions LCG, avec des définitions et des explications pour les termes et mécaniques du jeu. Le contenu est en français et vise à aider les joueurs à mieux comprendre les règles et les interactions du jeu. Les règles existantes sont en v1.7 en Anglais uniquement, et le but est de fournir une traduction et une adaptation complètes en français.


## Projet technique
Projet MkDocs utilisant le thème Material for MkDocs. Le contenu est écrit en Markdown avec une structure de dossiers organisée pour les différentes sections du guide de référence. Le fichier mkdocs.yml configure le site, y compris le nom, l'URL, le thème, les extensions Markdown et les plugins utilisés.
Hébergé sur GitHub Pages pour un accès facile et une distribution publique.



## Instructions de traduction
Le but est de traduire le bloc `EN v1.7` en n'oubliant aucune phrase.

Etapes à suivre de 1 à 11 :

1. Ne pas toucher aux blocs `**EN v1.7**` et `**FR v1.4**`.
2. Si la traduction existe dans le bloc `**FR v1.4**`, il faut la réutiliser pour être fidèle à la version précédente.
3. Traduire intégralement le bloc EN v1.7 en français entre le titre (#TITLE) et le bloc EN v1.7 La traduction doit être complète et fidèle au texte original, en respectant les termes spécifiques du jeu et en utilisant un langage clair et précis.
4.  Ne pas préfixer la traduction par le titre en majuscule (éviter DUPLICATION).
5. A partir de la traduction produite: remplacer les listes à puces `•` par un retour de ligne + tiret `\n-` et les chevrons `» »` par un tiret précédé d'un retour de ligne + 4 espaces `\n    -`. Respecter l'indentation des sub-bullets
6. Pour tout texte non présent dans le bloc FR v1.4, l'englober par `<span class="new">...</span>` pour indiquer que ce texte a été ajouté dans la nouvelle version.
7. Précéder les phrases `Voir` et `Voir aussi` d'une ligne vide et englober cette phrase en italique. Exemple: `_Voir aussi: Keyword1, keyword2_`. ATTENTION:Ne pas englober cette section dans un <span class="new">...</span>. Créer les liens markdowns de type [[Page|Title]]
8. Remplacer les icones par l'image correspondantes (voir section Correspondance Icone) 
9. Ajouter 2 espaces en fin de ligne pour assurer un bon rendu markdown.
10. Vérifier les correspondances (voir chapitre) pour vérifier les traductions sur certains mots-clés. Exemple le mot `villainous`doit se traduire `vilenie`
11. Executer les contrôles de validation (voir chapitre Contrôles) pour s'assurer que la traduction est complète et conforme aux attentes. Sinon recommencer à partir de l'étape 3.


# Contrôles ✅
- Vérifier que le texte EN v1.7 a été intégralement traduit, si il manque une phrase ou une partie de phrase, refuser la traduction et recommencer à partir de l'étape 3.
- Vérifier que le nombre de puces (top level et sous-puces et numérotation) dans la traduction produite correspond au nombre exact de puces dans le bloc EN v1.7.
- S’assurer que chaque phrase du bloc EN est soit présente textuellement en FR v1.4, soit présente dans <span class="new"> (comparer phrases normalisées).
- Rechercher et refuser les traductions préfixées par le titre MAJUSCULE.

## Correspondance Icone

-  = ![[icone_energie.jpg|15]]  
-  = ![[icone_mentale.jpg|15]]  
-  = ![[icone_physique.jpg|15]]  
-  = ![[icone_libre.jpg|15]]  
-  = ![[icone_acceleration.jpg|15]]  
-  = ![[icone_amplification.jpg|15]]  
-  = ![[icone_crise.jpg|15]]  
-  = ![[icone_aleas.jpg|15]]  
-  = ![[icone_boost.jpg|15]]  
-  = ![[icone_etoile.jpg|15]]  
-  = ![[icone_joueur.jpg|15]]  
-  = ![[icone_unique.jpg|15]]  
-  = ![[icone_consecutif.jpg|15]]  


## Correspondance 
Pour traduire les termes et expressions spécifiques au jeu, se référer aux mots correspondants de la version francaise:

- minions = sbires
- treachery = traîtrise
- attachment = attachement
- ally = allié
- event = évènement
- upgrade = amélioration
- support = support
- hero = héros
- alter-ego = alter-ego
- encounter = rencontre
- villain = méchant
- side scheme = manigance secondaire
- wild resource = ressource libre
- boost = boost
- interrupt = interruption
- response = réponse
- forced response = réponse Forcée
- forced interrupt = interruption Forcée
- setup = mise en place
- twart = contrer
- attack = attaque
- damage = dégâts
- health = santé
- defend = défendre
- steady = solide
- stalwart = robuste
- stunned = sonné
- confused = désorienté
- form = forme
- exhausted = incliné
- ready = prêt
- guard = garde
- hinder = entrave
- incite = incitation
- linked = lié
- overkill = déferlement
- patrol = patrouille
- peril = péril
- permanent = permanent
- piercing = perçant
- quickstrike = coup rapide
- ranged = à distance
- requirement (resources) = exigence (ressources)
- restricted = restreint
- retaliate = riposte
- team-up = en équipe
- teamwork = collaboration
- tough = tenace
- temporary = temporaire
- uses (X "type") = utilisations (X "type")
- victory X = victoire X
- villainous = vilenie
- surge = renfort
- alliance = alliance
- assault = assaut
- find = trouver
- vulnerable = vulnérable
- target = cible
- when revealed = une fois révélée
- when defeated = une fois vaincu
- when completed = une fois déjouée
- alteration effect = effet d'altération
- cancel = annuler
- Status Cards = Cartes d'état
- delayed effect = effet retardé
- enter play = entrer en jeu
- in play and out of play = en jeu et hors-jeu
- initiating abilities = Initier des Capacités
- labeled ability = capacité référentielle
- lasting effects = effets persistants
- qualifiers = Qualificatifs
- resource ability = Ressource (capacité)
- simultaneous resolution = résolution simultanée
- special = spécial 
- character = personnage
- consequential damage = dégâts consécutifs
- excess damage = dégâts en excès
- « peut » = pouvoir
- aspect card = carte d'affinité
- basic card = carte basique
- double-faced card = carte double-face
- encounter card = carte de rencontre
- identity-specific card = carte spécifique à l'identité
- player card = carte joueur
- resource card = carte ressource
- scenario-specific card = carte spécifique au scénario
- deal damage = infliger des dégâts
- deal a card = attribuer une carte
- discard a card = défausser une carte
- hazard = aléa
- copy = exemplaire
- counter = jeton
- Target Threat = Seuil de Menace
- Defait = Vaincre
- Triggering Condition = "Etre censé"
- round = round
- phase = phase
- THW = CTR
- ATK = ATQ
- HP = PV
- DEF = DEF
- REC = REC
- SCH = MNG
