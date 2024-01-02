# IA capable de gagner à tous les couts au Tic Tac Toe (Morpion)

## Comment utiliser le programme ?
- Exécuter le programme *tic-tac-toe.py*, un plateau de jeu 3x3 va s'ouvrir.
- Vous pouvez jouer en cliquant sur les cases que vous souhaiter. Vous jouez en bleu et l'ordinateur en rouge.

![Plateau de jeu](/Images/plateau-de-jeu.png)

- Quand le jeu est terminé soit par une victoire soit par un match nul une fenêtre s'ouvre vous annonçant l'issue du jeu et vous permet de quitter ou de recommencer.

![Fenêtre de fin](/Images/fenetre-de-fin.png)

## Comment ça fonctionne ?

Le programme utilise l'algorithme Minimax, c'est une technique utilisée dans les jeux à deux joueurs à somme nulle, où le gain d'un joueur correspond à la perte de l'autre. Son objectif est de trouver le meilleur mouvement possible pour un joueur, en évaluant toutes les possibilités de mouvements jusqu'à une certaine profondeur dans l'arbre de recherche du jeu.

1. **Arbre de Recherche** : L'algorithme représente le jeu sous la forme d'un arbre de recherche, où chaque nœud représente un état possible du jeu, et chaque branche représente un coup possible.

2. **Évaluation des Feuilles** : Les feuilles de l'arbre sont évaluées en fonction d'une fonction d'évaluation qui mesure la qualité de la position du jeu pour le joueur.

3. **Alternance des Joueurs** : Les joueurs sont alternés à chaque niveau de l'arbre, car l'un cherche à maximiser son score (Max), tandis que l'autre cherche à minimiser le score (Min).

4. **Rétropropagation** : Le score est propagé vers le haut de l'arbre, en utilisant la logique du Min et du Max. À chaque nœud, le joueur Max prend le maximum des scores de ses nœuds enfants, tandis que le joueur Min prend le minimum.

5. **Meilleur Coup** : Une fois l'arbre évalué, le meilleur coup est choisi en fonction du score obtenu à la racine de l'arbre.

Dans le contexte de notre programme Python, l'algorithme Minimax a été implémenté pour évaluer tous les mouvements possibles du joueur et de l'IA. La fonction d'évaluation attribue des scores à chaque configuration du jeu, et l'algorithme cherche à maximiser ou minimiser ces scores en fonction du joueur actuel.

L'efficacité de l'algorithme Minimax réside dans sa capacité à explorer l'ensemble des possibilités, garantissant ainsi une prise de décision optimale dans le contexte d'un jeu à deux joueurs.

![Représentation de l'algorithme](/Images/minimax.png)
