---
title: >-
    The 2021 Outdex bingo
authors:
    - Thomas Graf
date: 2021-01-05
bibliography: references.bib
tags:
    - fun allowed
    - LaTeX
    - Python
---

<!-- START_SUMMARY_BLOCK -->
2020 hasn't been particularly kind to most folks, although it did work out really well for my department here at Stony Brook (more on that in some other post, perhaps).
2021 still has that "new car" smell, but it might need some help to stay fresh for the full 52 weeks.
This is why I present you with my revolutionary invention: **Outdex bingo**.

![Reduplication in a finite-state automaton]({static}/img/thomas/outdex_bingo/output/from_py/bingo1.svg)

<!-- END_SUMMARY_BLOCK -->

It works pretty much like regular bingo:

1. Get yourself an Outdex bingo card (if everybody uses the one above, it'll be pretty boring).
1. Whenever you read an Outdex post in 2021, make sure to mark off all terms on your bingo card that appear in the post.
1. Keep doing that until you have filled in a row, column, or diagonal.
   The BINGO! field in the middle is treated as a wildcard.
1. Peruse the prestigious Outdex comments system to announce your bingo victory.
   Your reward will be determined by a D20 roll on a secret table.

But where, I hear you ask, can you get yourself an Outdex bingo card?
Why, you can compile it yourself, or ask a slightly tech-savvy friend to do it for you.


## How to compile

You will need Python 3.6 or newer, as well as a working LaTeX installation with a recent version of tikz.

1. All the files you need are in a separate folder in the Outdex repository: <https://github.com/outde-xyz/website/tree/master/content/img/thomas/outdex_bingo/>
1. Download three files from this folder:
    - `taglist`
    - `outdex_bingo.py`
    - `bingo_template.tex`
1. In a shell, run `python3 outdex_bingo.py`.
1. In the same folder, there is now a file `bingo.tex`, which you can compile to a PDF in the usual fashion.

If that sounds like a pain, I'm sure there's some newbie-friendly way to set this up in Overleaf, but I won't look into it because I don't even have an Overleaf account.
If somebody wants to do that, though, I'll be happy to help any way I can.


## How it works

First I wrote `word_counts.py` as a small script to get an idea for what tags and terms commonly show up in Outdex posts.
I then put 50 of those in the text file `taglist`.
The Python script `outdex_bingo.py` randomly picks terms from this list and converts the selection into a tikz matrix.
The matrix code is then combined with `bingo_template.tex` to produce `bingo.tex` for a specific bingo card.

So if you want to mix things up a bit, there's three places where you can make modifications:

1. You can add or remove entries in `taglist` to change what terms can appear on your bingo cards.
1. You can run `outdex_bingo.py` with different parameters to get smaller or larger bingo cards, or bingo cards without a wildcard in the middle.
1. You can change the tikz styles in `bingo_template.tex` to get a different layout for your bingo cards.


## The code

If there's interest, I can write a follow-up post that explains little bit what's going on in the Python script and the tex-template.
Neither one does anything fancy, but if you're just starting out with Python and/or LaTeX you might find some useful techniques in there.

Oh, and if you check the linked folder in the github repo, you'll also see a file `outdex_bingo.tex`.
That was my first attempt, for which I tried to skip Python do everything directly in LaTeX, based on code from some stackexchange posts.
However, I couldn't quite get it to work as it sometimes produces only a partial bingo card with empty cells.
No idea what the problem is, maybe somebody with better LaTeX skills could take a look.
