# Classification des Tweets 

> Introduction


Les postes publiés sur Twitter reflètent l’interaction d’utilisateurs avec les événements réels qui se déroulent dans le monde, comme les élections,
les événements sportifs et culturels, les catastrophes naturelles, etc. Ces événements réels ont un impact direct sur la quantité de tweets mises en ligne.

Le suivi de ces événements sur les réseaux sociaux généralement et sur Twitter plus précisément est un défi audacieux pour les chercheurs, tout d’abord parce
qu’un sujet sur Twitter est caractérisé par plusieurs termes (ces termes peuvent être des hashtags) qui peuvent changer dynamiquement où certains peuvent
devenir moins utilisés et d’autres peuvent apparaître. Donc il est incontournable de trouver un moyen pour couvrir tous ces termes utilisés pendant le processus d’analyse. Cela représente l’un de nos objectifs dans ce travail. Mais avant de chercher les nouveaux termes, il faut pouvoir identifier les ensembles de tweets
qui parlent du même sujet et qui représentent un fil de discussion, ce qui définit l’objectif principal de notre travail.

> Préparation des tweets

Pour résoudre notre problème ,on collecte un ensemble des tweets à travers API twitter ,ce processus nessesaite de créar une application en "https://developer.twitter.com/en " a fin d'obtenir Api Keyet Access token 

> Préparation datasets 

une fois nous avons obtenir les credentials (identifiants) on peut collecter les datasets par thème (les catégories que nous avons le traitées sont:economic, culture, social , health , politics et sport ).

Exemple : a l'aide de fichier https://github.com/SabrineKassdallah/Classification-des-Tweets/blob/master/culture.ipynb ,on peut collecter les tweets de culture, chaque fichier a deux paramètres très nécessaires text_query et count , text_query correspondant au catégorie des tweets et count correspondant au  nombres des tweets.

Pour tous les restes des catégories on fait la même chose, à but d'exécuter n'importe quel fichier on a besoin deux librairies Tweepy et GetOldTweets3.

Installation 

!pip install tweepy

!pip install GetOldTweets3

> Concaténation de datasets

Le role de cette fichier https://github.com/SabrineKassdallah/Classification-des-Tweets/blob/master/Tweets_Classification.ipynb est de mettre tous les tweets en même fichier csv .

##  Analyse des tweets

Dans ce notebook on a tous les techniques nécessaires pour analyser les tweets https://github.com/SabrineKassdallah/Classification-des-Tweets/blob/master/Tweets_Classification.ipynb


> Classification du texte 

Dans cette partie on va Nettoyer les tweets et on applique les différentes techniques de NLTK tel que : lemmatisation, tokenisation, suppression des arrêts, ponctuations, hashtags et mentions, pratiquement nous avons appliqué des expressions regulieures.

>  Related Words

Dans cette partie on va définir l’ensemble des mots relies à chaque thème, pour effectuer ce processus on a utilisé Related Words.

Lien pour obtenir des mots connexes : https://relatedwords.org/


> Distance de Jaccard

La similitude Jaccard est bonne pour les cas où la duplication n'a pas d'importance, la similitude cosinus est bonne pour les cas où la duplication est importante lors de l'analyse de la similitude du texte. Pour deux descriptions de produits, il sera préférable d'utiliser la similitude Jaccard car la répétition d'un mot ne réduit pas leur similitude.

> KMeans Clustering

Pour traiter les données d'apprentissage, l'algorithme K-means dans l'exploration de données commence par un premier groupe de centres de gravité (centroids) sélectionnés au hasard, qui sont utilisés comme points de départ pour chaque cluster, puis effectue des calculs itératifs (répétitifs) pour optimiser les positions des centres de gravité (centroids).

> Clustered Datasets 

Dans cette partie on va étudier ou bien obtenir le tweet le plus représentatif de chaque catégorie.


* Kassdallah Sabine 

LinkedIn : https://www.linkedin.com/in/kassdallah-sabrine-a91601165/

Github : https://github.com/SabrineKassdallah

Mail : sabrinekasdallah2017@gmail.com

 

