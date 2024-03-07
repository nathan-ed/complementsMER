# Créer sa propre série à partir des séries existantes
## Prérequis
Il est nécessaire de savoir compiler un document LaTeX avec la commade pdflatex. Une rapide introduction à LaTeX est disponible en suivant le lien https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes. 

## Généralités
### Structure du dossier

Le dossier avec les séries en format .tex est constitué de:
- Un dossier 9e qui contient les fichiers pour les séries de 9e. Il y a également dans ce dossier un sous-dossier média contenant les images qui sont intégrées dans les séries. Vous trouverez également dans ce dossier une série intitulée serie_personnalisee.tex qui est la série que l'on utiliser comme modèle dans ce tutoriel.
- Un dossier packages qui contient la classe à partir de laquelle les séries sont compilée.

### Différents types d'exercices  

Les fichiers .tex des séries recensent les exercices qui sont disponibles dans les séries sous format .pdf. Il y a plusieurs types d'exercices. Chaque type d'exercice est contenu entre une balise de début et de fin.
```
\begin{type de l'exercice}
Corps de l'exercice
\end{type de l'exercice}
```
Types d'exercices
-  Des exercices des MER (fichier et livre) entre les balises suivantes
	```
 	\begin{exol}
 	...
 	\end{exol}
 	```
	```
   	\begin{exof}
 	...
 	\end{exof}
 	```
- Des exercices à effectuer sur la série entre les balises suivantes
	```
 	\begin{exo}
 	...
 	\end{exo}
 	```
- Des exercices à effectuer dans le cahier/feuille à part entre les balises suivantes
	```
 	\begin{exop}
 	...
 	\end{exop}
 	```

## Compilation d'une série en ligne

Dans cette partie du tutoriel, nous allons utiliser la plateforme [Overleaf](overleaf.com) qui permet de compiler en ligne des documents LaTeX. Overleaf possède une [documentation très complète](https://www.overleaf.com/learn), donc n'hésitez pas à la consulter si vous rencontrez des difficultés.
1. Création d'un compte [Overleaf](overleaf.com) 
2. Télécharger le dossier avec les séries en format .tex
3. [Téléverser le dossier en format .zip sur Overleaf](https://www.overleaf.com/learn/how-to/Uploading_a_project)
4. Ouvrir le projet et ouvrir éditer le fichier serie_personnalisee.tex dans le dossier 9e
5. Modifier les variables:
	1. Titre de la série
	2. Année (9e, 10e, 11e)
6. Ajouter les exercices provenant des autres séries en copiant et collant le contenu entre chaque balise
7. Sauvegarder la série dans le même dossier que le dossier de base
8. Compiler la série

## Création d'une nouvelle série sur sa machine

### Prérequis - Logiciel à installer

Installation d'une version complète de MikTeX (Windows), TeX Live (Windows, macOS et Ubuntu) ou équivalent sur sa machine. 
Procédure à suivre pour l'installation: 
- Installation de MikTeX: https://miktex.org/howto/install-miktex 
- Procédure générale TeX Live: https://zestedesavoir.com/tutoriels/826/introduction-a-latex/1319_creer-vos-premiers-documents/5786_installation-et-premiers-pas/
- Procédure Windows: https://www.ibm.com/docs/en/strategicsm/10.1.3?topic=analysis-installing-tex-live-windows
- Procédure macOS: https://tug.org/mactex/
- Procédure Ubuntu: https://tex.stackexchange.com/questions/134365/installation-of-texlive-full-on-ubuntu-12-04
- Téléchargement de TeX Live: https://www.tug.org/texlive/acquire-netinstall.html
Il est important d'installer la version complète (avec tous les paquets) afin de ne pas à avoir à installer des paquets supplémentaires lors des compilations.  

### Marche à suivre afin de créer sa série

1. Télécharger le dossier avec les séries en format .tex
2. Extraire l'intégralité du dossier
3. Ouvrir le fichier serie_personnalisee.tex dans le dossier 9e  avec un éditeur LaTeX (TeXstudio,  TeXmaker, TeXworks, ...)
4. Modifier les variables:
	1. Titre de la série
	2. Année (9e, 10e, 11e)
5. Ajouter les exercices provenant des autres séries en copiant et collant le contenu entre chaque balise
6. Sauvegarder la série dans le même dossier que le dossier de base
7. Compiler la série
