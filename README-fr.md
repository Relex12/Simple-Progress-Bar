# Simple-Progress-Bar
Une barre de progression très simple en Python, copie-collable et personnalisable, aucun import requis.
A very simple copy-pasteable and customizable progress bar in Python, no import needed.

![](https://img.shields.io/badge/status-Finished-green) ![](https://img.shields.io/github/license/Relex12/Simple-Progress-Bar) ![](https://img.shields.io/github/repo-size/Relex12/Simple-Progress-Bar) ![](https://img.shields.io/github/languages/top/Relex12/Simple-Progress-Bar) ![](https://img.shields.io/github/last-commit/Relex12/Simple-Progress-Bar) ![](https://img.shields.io/github/stars/Relex12/Simple-Progress-Bar)

Regarder sur GitHub

[![Markdown-Table-of-Contents](https://github-readme-stats.vercel.app/api/pin/?username=Relex12&repo=Simple-Progress-Bar)](https://github.com/Relex12/Simple-Progress-Bar)

[Read in English.](https://relex12.github.io/Simple-Progress-Bar)

---

## Sommaire

* [Simple-Progress-Bar](#simple-progress-bar)
    * [Sommaire](#sommaire)
    * [Qu'est-ce que c'est ?](#qu'est-ce-que-c'est-)
    * [Pourquoi devriez-vous utiliser celle-ci ?](#pourquoi-devriez-vous-utiliser-celle-ci-)
    * [À quoi ça ressemble](#à-quoi-ça-ressemble)
    * [Le code](#le-code)
    * [Utilisation](#utilisation)
    * [Qu'est-ce qui est personnalisable ?](#qu'est-ce-qui-est-personnalisable-)
    * [Qu'est-ce qui *n'est pas* personnalisable ?](#qu'est-ce-qui-n'est-pas-personnalisable-)
    * [Spécifications](#spécifications)
    * [License](#license)

<!-- table of contents created by Adrian Bonnet, see https://Relex12.github.io/Markdown-Table-of-Contents for more -->



## Qu'est-ce que c'est ?

C'est une barre de progression que vous pouvez utiliser dans n'importe quel type de projet en Python, sans avoir besoin d'installer quoique ce soit.



## Pourquoi devriez-vous l'utiliser ?

Parce que

*   elle a été faite avec le cœur
*   elle est facile à utiliser, il suffit de copier-coller le code
*   elle est très légère, **seulement quatre lignes**
*   elle est personnalisable



## À quoi ça ressemble

La barre de progression par défaut ressemble à ceci

![default bar](https://raw.githubusercontent.com/Relex12/Simple-Progress-Bar/main/img/default_bar.png)



## Le code

Voici ce que vous avez besoin de copier-coller dans votre code

```python
import sys

def progress_bar(count,total,size=100,sides="[]",full='#',empty='.',prefix=""):
    x = int(size*count/total)
    sys.stdout.write("\r" + prefix + sides[0] + full*x + empty*(size-x) + sides[1] + ' ' + str(count).rjust(len(str(total)),' ')+"/"+str(total))
    if count==total:
        sys.stdout.write("\n")
```



## Utilisation

Voici un exemple de comment l'utiliser

```python
for i in range(1,101):
	progress_bar(count=i,total=100)
    time.sleep(0.01) # place you job here
```

Notez que pour un meilleur résultat, le dernier appel doit être fait avec `count` et `total` étant égaux.



## Qu'est-ce qui est personnalisable ?

Vous pouvez personnaliser le **préfixe**, les caractères sur les **côtés**, les caractères de la **partie achevée** et de la **partie restante** ainsi que la **largeur** de la barre, par exemple

```python
progress_bar(count=i,total=100,size=40,sides="||",full='█',empty=' ',prefix="working...")
```

donne la barre suivante

![custom bar](https://raw.githubusercontent.com/Relex12/Simple-Progress-Bar/main/img/custom_bar.png)



## Qu'est-ce qui *n'est pas* personnalisable ?

Un **préfixe dynamique** comme dans les système Unix, les **couleurs** et l'**avancement** au format `i/n` ne peuvent être modifiés sans changer le code de la fonction. N'hésitez pas à faire un fork du projet ou créer une pull request si vous souhaitez ajouter ces fonctionnalités.



## Spécifications

Vous pouvez trouver ces spécifications dans la docstring de la fonction dans le code source

* **count** (*int*) : l'avancement actuel (doit être plus petit ou égal à *total*)
* **total** (*int*) : la quantité totale
* **size** (*int*) : la largeur de la barre de progression, sans les crochets ou le préfixe
* **sides** (*str*) : les caractères à afficher au début et à la fin de la barre de progression (doit faire au moins deux caractères de long)
* **full** (*str*) : le caractère à afficher dans la partie achevée de la barre (doit faire un caractère de long)
* **empty** (*str*) : le caractère à afficher dans la partie restante de la barre (doit faire un caractère de long)
* **prefix** (*str*) : le préfixe à afficher avant la barre de progression



## License

Ce projet est un petit projet. Le code source est donné librement à la communauté GitHub, sous la seule licence MIT, qui n'est pas trop restrictive.
