title: >-
    News from the MG frontier
series: >-
    Writing for the Outdex
authors:
    - Aniello De Santo
date: 2019-06-23
bibliography: TorrACL_MGpaper.bib
tags:
    - MGs
    - parsing
    - NLP
---



True to my academic lineage, I’m a big fan of Minimalist grammars (MGs): they are a pretty malleable formalism, their core mechanisms are very easy to grasp on an intuitive level, and they are close enough to current minimalist syntax to allow for interesting computational insights into mainstream syntax.
However, I often find that MGs’charms are a bit wasted on my more NLP-oriented colleagues, compared to those of very close cousins like, say, TAGs or CCGs.
They are very practical reasons for this, of course, but two things in particular come to mind right away: the lack of any large MG corpus (and/or  automatic ways to generate such corpora) and, relatedly, the lack of  efficient, state-of-the-art, probabilistic parsers.

This is why I’m very excited about [this upcoming paper](https://stanojevic.github.io/papers/2019_ACL_MG_Wide_Coverage.pdf) by John Torr  and co-authors (henceforth TSSC), on a (the first ever?) wide-coverage MG parser.
The parser is implemented by smartly adapting the $A^*$ search strategy developed by @LewisSteedman14ccg for CCG (basically, a CKY chart + a priority queue) to MGs, and coupling it with a  complex neural network supertagger trained on an MG treebank.

Truth to be told, John Torr has been working towards this result for a while, by building his wide coverage MG treebank, and providing some already [interesting parsing results](https://www.aclweb.org/anthology/P18-1055).
However, it is the $A^*$ algorithm that does the trick here, hopefully putting this parser (and thus MGs) on the NLP map.

The paper does, imho, a very good job at clarifying the importance of the result.
So I’ll spare you a super technical summary post (**just go read it!**). Just a few thoughts:

1) **How does the parser perform?** The worst case time complexity is $O(n^28 log n)$, in the length of the sentence.
*“What?! You told us this was an interesting result! We already knew MG parsing was slow”*.
As people have mentioned on twitter: Yes, that is insanely high (CKY is $O(n^3)$, and recent RNN-based constituency parsers are linear).
However, the cool thing about the $A^*$ component is that the parser performs way better ($O(n^3)$) in practice.
This might not be an astonishing performance (I personally find the high variance still a bit concerning) but is definitely encouraging.

Note also that Milos Stanojevic (who has been producing [so.](https://stanojevic.github.io/papers/2019_NAACL_CCG_Incremental_Rotation.pdf) [many.](https://linguistics.ucla.edu/people/hunter/parsing/move-eager-mg-lc.pdf) parsers!) has [recently shown](http://fg.phil.hhu.de/2019/papers/FG2019-Stanojevic.pdf) that the worst case time complexity for parsing MGs with head movement can be dropped to $O(n^13)$ (so I’m assuming $O(n^13 log n)$ for their CKY+$A^*$ implementation).
My guess is that this might also reduce the expected time complexity, but of course one would have to try and see.

2) Although cross-formalism comparisons are tough (as the authors mention: are we comparing the quality of the parser or the quality of the grammar?), having lifted the CKY+$A^\*$ strategy directly from CCGs allows this paper to do a few interesting comparisons (cf. @Rimell2009).
So, in terms of accuracy , results are not exactly comparable to those of the CCG algorithm on comparable dependencies.
However, the authors point out that this might be due to the MG parser requiring more training than the CCG one (due to the increased complexity of the supertags?).
Thus, lower performance might depend on the early development stage the MG treebank is at the moment. So, *go and contribute*!

2) There are a lot of interesting syntactic considerations one could make based on the test cases the authors report. 
I’ll just point out that the MGbank makes very specific syntactic choices. 
While it’s possibly a bit too early for this, it would be interesting to look into how different theoretical choices could impact the quality of the grammar with respect to parsing performance.

3) A side note. MG researchers have long known that Move is a powerful operation, which needs to be restricted quite a bit.
The MGbank does this by following the usual suggestions in the literature (SMC, SpIC, etc). 
SMC (or equivalents) aside,  the appeal to syntactically motivated constraints is interesting (although not new), and reopens questions about the relation between syntactic constraints and parsing performance.


## References