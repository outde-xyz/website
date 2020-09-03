---
title: >-
    A tribute to Joost Engelfriet
authors:
    - Thomas Graf
date: 2020-09-02
bibliography: references.bib
tags:
    - formal language theory
    - tree transductions
---

<!-- START_SUMMARY_BLOCK -->
Ed Stabler sent me a link to [the most recent paper](https://arxiv.org/pdf/2008.12151.pdf) by [Joost Engelfriet](http://liacs.leidenuniv.nl/~engelfrietj/), which concludes with the following message:

> **That's all folks!** This was my last paper. Thank you, dear reader, and farewell.

That's bitter-sweet.
On the one hand, I admire that he can draw a line in the sand like this.
On the other hand, I wish he'd erase that line and keep going for a few more years.
Even though Engelfriet isn't a mathematical linguist --- and might not even be aware of the more linguistic side of that field, the one that we serve here at the Outdex Café --- he has had a profound influence on the field, including a lot of my own work.
<!-- END_SUMMARY_BLOCK -->

I've never met Joost Engelfriet, I only know him through his papers.
But those are some impressive papers.
They have been my go-to source for anything related to tree transductions.
And if you're a regular reader of this blog, you know that this isn't just some mathematical curiosity, tree transductions are the lens that allows us to make sense of syntax.
Movement is a tree transduction.
The [bimorphism perspective of the inverted T-model]({filename}2019-05-15_graf_tmodel.md) involves tree transductions.
The derivation tree perspective of MGs wouldn't be possible without tree transductions, and that, in turn, means that we would have missed [the subregular nature of syntax]({filename}/Tutorials/locality_merge_move.md).
Engelfriet wasn't the first to work on tree transductions --- that honor goes to James Thatcher and William Rounds (who cites Transformational Grammar as a direct inspiration for tree transductions).
Engelfriet was about 5 years late to the party, yet he's shaped the field more than anybody else.
I think it's actually impossible to find a paper on tree transductions that doesn't cite Engelfriet.
He's that integral to the field; Engelfriet is the Chomsky of tree transductions.

Engelfriet has also worked hard on connecting the automata-theoretic view of tree transductions to mathematical logic, in particular monadic second-order logic (MSO).
And because tree transductions apparently aren't complicated enough for him, he also teamed up with [Bruno Courcelle](https://www.labri.fr/perso/courcell/ActSci.html) to produce [the definitive reference on MSO over graphs](http://www.labri.fr/perso/courcell/Book/TheBook.pdf).
And again this isn't just some pointless mathematical exercise, MSO has been an integral part of mathematical linguistics since the mid 90s, pioneered by [Jim Rogers](https://www.cs.earlham.edu/~jrogers/), Thomas Cornell, and [Uwe Mönnich](http://www.tcl-sfs.uni-tuebingen.de/~um/), among others.
It allowed us to study derivational formalisms as if they were representational formalisms, and that, too was an important stepping stone for me towards subregular syntax.

Almost every paper I have written incorporates work by Engelfriet in one way or another.
And it's not just that his research is essential to my work and the field at large, his papers are also **fun**.
I won't pretend that they're easy reads, at least they're not for me.
Tree transductions are much more complex than string transductions, and topics like tree transducer decompositions or the equivalence of MSO-definable tree transductions and macro tree transductions of linear size increase are not for the faint of heart.
But an Engelfriet paper never feels like it is any more complex than it has to be.
It's the same feeling of awe that I experience when watching somebody [speedrun Super Metroid](https://youtu.be/shNyq0TfHBs?t=230): I don't quite get everything they're doing, and I certainly can't do it myself, but I can recognize the beauty in it.

Engelfriet's work is also like Super Metroid speedruns in that many Outdex readers were probably unaware of its existence.
Well, now you're in the know. 
And if you now want to become a true Engelfriet aficionado, here's a list of papers (and one book) that were essential reading for me:

- @Engelfriet75:
  Back in the days when tree transductions were the wild west, this paper established the key differences between bottom-up and top-down tree transductions that all modern work builds on.

- @Engelfriet77:
  Another classic, this one introduced the notion of regular look-ahead for top-down tree transductions; look-ahead is now a fundamental parameter of tree transducers.
  I've been thinking about look-ahead a lot recently in an attempt to expand sensing tree automata into transducers for movement.
  Don't get your hopes up, though, it's not ready for a post yet.

- @EngelfrietVogler85:
  The arrival of **macro tree transducers**.
  Every kind of tree transduction that you'll come across in computational syntax is equivalent to some constrained macro tree transducer.
  Once you understand macro tree transducers, everything else is just a special case of a very general top-down device.

- @EngelfrietHoogeboom01:
  Engelfriet isn't just all about trees and graphs, he also did some work on string transductions.
  This paper shows how two-way finite state transducers over strings are related to MSO string transductions, and this result is now spreading in the subregular phonology community.

- @EngelfrietManeth03:
  The paper that establishes the lovely result I mentioned above: MSO tree-to-tree transductions are equivalent to macro tree transductions of linear size increase.
  This is an important bridge that allows to connect the logical view to the automata-theoretic one.
  Both are used in mathematical linguistics, e.g. in work on MGs, so it's good to have some way of translating between them, even if we still need to learn a lot more about how the weaker subclasses relate to each other.

- @EngelfrietEtAl09:
  While this paper is focused on a particular type of tree transductions (**extended multi bottom-up tree transducers**), it gives a good idea of what the modern tree transducer landscape looks like and what the advantages and shortcomings of various transduction types are.
  I don't know how many times I've looked up Table 1 and Figure 5 in this paper.

- @MalettiEngelfriet12:
  Another paper that's not directly about tree transductions, but is more closely aligned with the interests of computational linguists.
  This is a follow-up to a paper by Marco Kuhlmann and Giorgio Satta where they show that TAGs are not closed under (strong) lexicalization.
  Kuhlmann & Satta left open what kind of grammar formalism would be needed to strong lexicalize TAG, and this paper provides the answer: simple context-free tree grammars.
  This one stings a bit every time I see it because I was working on a reply to Kuhlmann & Satta, but Maletti & Engelfriet were faster and had a much better result.

- @CourcelleEngelfriet12:
  The massive tome on MSO graph transductions that I mentioned earlier.
  No, I haven't read the whole thing.
  Yes, I do keep coming back to it.

- @EngelfrietEtAl15:
  Tree transducers break down into two macro-classes, the top-down transducers and the bottom-up transducers.
  Standard bottom-up transducers don't cut it for many tasks, including handling movement, so nowadays a lot of the attention goes to **multi bottom-up transducers**.
  Top-down transducers are also very limited, prompting the introduction of **extended top-down tree transducers**.
  But extended top-down tree transducers aren't closed under composition, which means that a cascade of these transductions can do things a single extended top-down tree transducer cannot do.
  This raises the question how powerful these cascades are, and this paper provides the answer.

- @EngelfrietEtAl18:
  This paper studies multiple context-free tree grammars, which are closely related to (set-local) multi-component TAG and multiple context-free string grammars.
  As you might know, the latter two are weakly equivalent to MGs.
  I haven't fully absorbed this paper yet, but I have long wondered if [my translation from standard TAG to MGs with lowering](https://thomasgraf.net/doc/papers/Graf12TAG.pdf) could be extended to multi-component TAG.
  With a bit more time, I might find the answer in this paper.

There's many other papers I could've listed here.
Feel free to link to your favorite in the comments.
Happy reading everyone!

## References (The Engelfriet Paperpalooza)
