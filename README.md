# Simple-Progress-Bar
A very simple copy-pasteable and customizable progress bar in Python, no import needed.

![](https://img.shields.io/badge/status-Finished-green) ![](https://img.shields.io/github/license/Relex12/Simple-Progress-Bar) ![](https://img.shields.io/github/repo-size/Relex12/Simple-Progress-Bar) ![](https://img.shields.io/github/languages/top/Relex12/Simple-Progress-Bar) ![](https://img.shields.io/github/last-commit/Relex12/Simple-Progress-Bar) ![](https://img.shields.io/github/stars/Relex12/Simple-Progress-Bar)

Look it on GitHub

[![Markdown-Table-of-Contents](https://github-readme-stats.vercel.app/api/pin/?username=Relex12&repo=Simple-Progress-Bar)](https://github.com/Relex12/Simple-Progress-Bar)

[Lire en Français.](https://relex12.github.io/fr/Simple-Progress-Bar)

---

## Summary

* [Simple-Progress-Bar](#simple-progress-bar)
    * [Summary](#summary)
    * [What is it?](#what-is-it)
    * [Why should you use this one?](#why-should-you-use-this-one)
    * [What it looks like](#what-it-looks-like)
    * [The Code](#the-code)
    * [Usage](#usage)
    * [What is customizable?](#what-is-customizable)
    * [What is *not* customizable?](#what-is-not-customizable)
    * [Specifications](#specifications)
    * [License](#license)

<!-- table of contents created by Adrian Bonnet, see https://Relex12.github.io/Markdown-Table-of-Contents for more -->



## What is it?

It is a progress bar you can use in any king of projects in Python, without installing anything.



## Why should you use this one?

Because

*   it was made with heart
*   it is easy to use, you just have to coy-paste the code
*   it is very lightweight, **four lines long**
*   it is customizable



## What it looks like

The default progression bar looks like this

![default bar](https://raw.githubusercontent.com/Relex12/Simple-Progress-Bar/main/img/default_bar.png)



## The Code

This is what you will have to copy-paste in your code

```python
import sys

def progress_bar(count,total,size=100,sides="[]",full='#',empty='.',prefix=""):
    x = int(size*count/total)
    sys.stdout.write("\r" + prefix + sides[0] + full*x + empty*(size-x) + sides[1] + ' ' + str(count).rjust(len(str(total)),' ')+"/"+str(total))
    if count==total:
        sys.stdout.write("\n")
```



## Usage

Here is an example of how you can use it

```python
for i in range(1,101):
	progress_bar(count=i,total=100)
    time.sleep(0.01) # place you job here
```

Please note that, for better rendering, the last call should be done with `count` and `total` being equals.



## What is customizable?

You can customize the **prefix**, the **side** characters, the **done part** and the **remaining part** characters and the **width** of the bar, for example

```python
progress_bar(count=i,total=100,size=40,sides="||",full='█',empty=' ',prefix="working...")
```

gives the following bar

![custom bar](https://raw.githubusercontent.com/Relex12/Simple-Progress-Bar/main/img/custom_bar.png)



## What is *not* customizable?

A Unix-like **dynamic prefix**, **colors** and the `i/n` format **advancement** can't be modified without changing the function's code. Feel free to fork this project or create a pull request if you want to add those features.



## Specifications

You can find those specifications in the function's docstring in the source code

* **count** (*int*) : the current advancement (must be smaller or equal than *total*)
* **total** (*int*) : the total amount
* **size** (*int*) : the width of the progress bar, without the brackets and the prefix
* **sides** (*str*) : the characters to print at the beginning and at the end of the progress bar (must be at least two characters long)
* **full** (*str*) : the character to print for the done part of the bar (should be one character long)
* **empty** (*str*) : the character to print for the remaining part of the bar (should be one character long)
* **prefix** (*str*) : the prefix to print before the progress bar



## License

The project is a small one. The code is given to the GitHub Community  for free, only under the MIT License, that is not too restrictive.
