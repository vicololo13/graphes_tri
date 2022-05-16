#**PROJET STRUCTURE DE DONNÉES ET ALGORITHMES AVANCÉS**

Ce document a pour but d'expliquer brièvement les différents programmes de notre projet.
Dans les programmes rendus, nous avons ajouté le Typing qui permet de bien voir ce que retourne chaque méthode.
Afin de pouvoir travailler ensemble dans les meilleures conditions, nous avons utilisé le plug-in CodeWithMe.

##1. Nouvelle classe pour les graphes

Dans cette partie, nous avons créé une classe python DirectedGraph qui nous permet de créer des graphes orientés grâce à l'ajout de sommets et d'arcs.
Nous avons également créer une sous-classe UndirectedGraph afin de créer des graphes non-orientés. Les principales différences sont aux niveaux des arcs qui deviennent des arêtes (cf [graph](graph.py)).
Les tests ont été passés avec succès. Pour tester la classe UndirectedGraph, nous avons utilisé les mêmes tests. (cf [test_graph](test_graph.py))

##2. Générer des graphes artificiellement


Dans cette partie, le but était de créer des méthodes permettant la generation de graphes aléatoires.
Dans un premier temps, nous avons implementé la méthode ```generate_random_graph```(cf [graph_generation](graph_generation.py)). Pour ce faire, nous générons un squelette reliant les sommets entre eux afin d'être certain que le graphe est connexe, puis sont ajoutés les arrêtes restantes aléatoirement.
Pour les tests, nous avons surtout essayé pour les cas extrêmes, et nous avons corrigé les erreurs dues à un trop gros nombre d'arêtes par rapport aux nombres de sommets en limitant le nombre d'arêtes (cf [test_graph_generation](test_graph_generation.py))
Nous avons adapté notre méthode ```generate_random_graph``` en ajoutant un argument booléen permettant d'orienter ou non notre graph aléatoire.
Enfin, nous avons étudié les graphes de communautés. Pour cela on crée les sommets puis on ajoute les arêtes en fonction des probabilités inter et intra données en argument de la fonction.
Nous avons ensuite testé ces graphes grâce aux intervalles de confiance et aux épreuves de Bernoulli.
Afin de mieux se rendre compte des résultats de nos algorithmes, nous avons créé une fonction ```draw``` dans la classe ```DirectedGraph``` qui permet de dessiner les graphes, et une fonction ```drawCummunityGraph``` (dans le fichier [test_graph_generation](test_graph_generation.py)) qui permet de dessiner les graphes de communauté avec les couleurs.
##3. Implémentation rapide de l'algorithme de Dijkstra

3.0 ```DirectedGraph.dijkstra```  
3.1 ```DirectedGraph.dijkstraTas```  
3.2 ```test_graph_generation.py```  
3.3 ```DirectedGraph.dijkstraSommet```  
3.4 ```DirectedGraph.bellman_Ford```

Dans un premier temps, nous implémentons l'algorithme de Dijkstra vu en cours. Par la suite, il a fallu l'optimiser pour obtenir des résultats plus rapidement.
Pour cela, nous avons utilisé des tas. Puis, nous avons ajouté différentes méthodes permettant de calculer le plus court chemin entre deux sommets choisis par exemple.
Toutes ces méthodes sont à retrouver ici [graph](graph.py) et les tests ici [test_graph](test_graph.py).
Nous avons également implémenté l'algorithme de Bellman-Ford en itératif, qui est une alternative à l'algorithme de Dijkstra, bien qu'il soit moins efficace, il permet de calculer le plus cours chemin sur des graphes avec des arêtes de poids négatifs.

##4. Experiences sur les graphes générés artificiellement

4.1 ```dijkstra_test_speed```  
4.2 ```dijkstra_test_speed_edges```  
4.3 ```statistic```  

Cette partie est orientée sur la comparaison de vitesse d'exécution entre nos différents algorithmes de Dijkstra.
Comme les temps d'exécutions sont assez longs, nous avons affiché le pourcentage d'exécution.
Nous avons commencé en comparant les vitesses des algorithmes avec et sans tas : ![](images/SPEED%204.1.png "Graphe")
On peut voir que pour certaines valeurs, le temps d'éxécution est plus élévé que ce qu'il devrait être : cela est dû au fait que, les graphes étant générés aléatoirement, il se peut que l'un d'eux est plus complexe que les autres, et ralentie artificiellement l'algorithme. Aussi, l'ordinateur a peut-être pris plus de temps pour l'exécuter parce qu'il était sur une autre tâche. 
Pour avoir des résultats concluants, nous avons donc lancé notre programme pour plusieurs graphes afin de limiter l'erreur,
ce qui nous a permis d'avoir des courbes plus régulières (cf [experiences_graphes](experiences_graphs.py)).

Ci-dessous, on peut voir le temps d'exécution minimum, moyen, median et maximun de l'algorithme de Dijkstra optimisé (avec les tas) entre deux sommets en fonction du nombres de sommets.

![](images/speed.png "Graphe")


##5. Experiences sur les données Reddit Hyperlink Network

5.1 ```nodeDegre```  
5.2 ```activity```  
5.3 ```chemins```  

Dans cette partie, nous avons appliqué notre programme à un cas concret : les subs reddit.
Nous avons donc téléchargé un [fichier](soc-redditHyperlinks-title.tsv) qui comporte les interactions entre différents subs Reddit, et l'avons converti en graphe (qui comporte plus de 50 000 sommets).
Le nombre d'intéractions d'un sub reddit est ainsi le degré du noeud correspondant, et pour trouver les liens les plus rapides entre les subs reddits, il suffit d'utiliser l'algorithme de Dijkstra.
Par exemple, pour passer de ```greenbaypackers``` à ```missouripolitics``` par le plus court chemin, il suffit de passer par le sub ```funny``` puis par ```electronic_cigarette```.

##6. Comparaison avec le modèle networkx

6.1 ```DirectedGraph.to_networkx```  
6.2 ```dijkstra_with_networkxx``` et ```dijkstra_comparaisons``` (fichier [experiences_graphes](experiences_graphs.py))  

Dans cette dernière partie, nous comparons notre projet avec le module python  ```networkx``` qui représente lui aussi des graphes orientés.
Pour cela, on réitère les experiences faites dans la partie 4, et on compare ces résultats avec les nôtres.
Ci-dessous les graphiques comparant les vitesses d'execution entre les fonctions du module ```networkx``` et les algorithmes de Dijkstra que nous avons codés.
![](images/dijkstra_comparaisons.png "Graphe")
Aussi, nous avons exécuté l'algorithme de Networkxx sur plusieurs graphes, comme précédemment, afin de déterminer les velurs minimales, maximales, moyennes et médiannes, dans le but de limiter les erreurs :
![](images/networkxxValues.png "Graphe")
