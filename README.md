# Classification des Tweets 

> Introduction

Live Demonstration
https://covid19-123.herokuapp.com/


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

Exemple : a l'aide de fichier https://github.com/SabrineKassdallah/Classification-des-Tweets/blob/master/culture.ipynb ,on peut collecter les tweets de culture, chaque fichier a deux paramètres très nécessaires text_query et count , text_query correspendent au catégorie des tweets  et count les nombres des tweets.
Pour tous les restes des catégories on fait la même chose, à but d'exécuter n'importe quel fichier on a besoin deux librairies Tweepy et GetOldTweets3.
Installation 

!pip install tweepy

!pip install GetOldTweets3

> Concaténation de datasets




* Kassdallah Sabine 

LinkedIn : https://www.linkedin.com/in/kassdallah-sabrine-a91601165/

Github : https://github.com/SabrineKassdallah

Mail : sabrinekasdallah2017@gmail.com

 

