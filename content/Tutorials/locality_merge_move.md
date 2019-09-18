---
title: >-
    The subregular complexity of Merge and Move
authors:
    - Thomas Graf
date: 2019-09-18
bibliography: references.bib
series: >-
    The subregular locality zoo
tags:
    - subregular
    - syntax
    - locality
    - strictly local
    - tier-based strictly local
    - Minimalist grammars
    - Merge
    - Move
---

<!-- START_SUMMARY_BLOCK -->
Alright, syntax.
Things are gonna get a bit more... convoluted?
Nah, interesting!
In principle we'll see a lot of the same things as in phonology, and that's kind of the point: phonology and syntax are actually very similar.
But syntax isn't quite as exhibitionist as phonology, it doesn't show off its subregular complexity in the open for the world to see.
So the first thing we'll need is a suitable representation.
Once we have that, it's pretty much phonology all over again, but now with trees.
<!-- END_SUMMARY_BLOCK -->

## Minimalist grammars

I'll boldly skip the part where we entertain the option of analyzing syntax in terms of strings --- in the future, I might come back to this and explain why even if syntax is viewed as a string generator rather than a tree generator, it has an intrinsic tree structure (the magic word is *computational trace*).
Let's go straight to trees, then.
This isn't all that trivial, though.
One consequence of syntax being so unwilling to reveal its naughty bits is that we cannot talk about syntax unless we first agree on a model of syntax.
A CCG analysis will look very different from a Minimalist analysis.
Any claim about syntax that goes beyond strings will inevitably be theory-laden to a large degree.
For now (and probably the next few years), we'll just have to deal with that, but the nice thing about mathematical approaches is that you can define translations between distinct theories, and this should allow us to eventually generalize the subregular view in a manner where it applies across many different formalisms.[^CCG]

[^CCG]: Except CCG, that one seems to be inherently incompatible with subregularity.

In the meantime, we'll use Stabler-style **Minimalist grammars** (MGs) as our model of syntax --- mostly because I like them and I'm calling the shots here.
And, okay, MGs also seem to be uniquely suited to the subregular view.
But we don't quite know enough yet to discuss this point in depth, so for now you'll just have to roll with MGs as the model of syntax.

MGs are very similar to old school Minimalist syntax, where all structures are built by Merge and Move.
We could add Agree, adjunction, Late Merge, phases, and the proverbial kitchen sink, but we won't because it's best to start with a simple model.
Merge and Move must be triggered by features:

1. Merge takes place whenever we have a **category feature** X^+^ and a matching **selector feature** X^-^.
1. Move takes place whenever we have a **licensor feature** f^+^ and a matching **licensee feature** f^-^.

Each lexical item is annotated with a string of features, and the features must be checked in the order they appear in on the lexical item.
For instance, the noun *car* only carries the category feature N^-^.
It may then be selected by say, *the*, yielding a DP.
This is expressed by assigning *the* the feature string N^+^ D^-^.
In other words, *the* selects a noun, and only after this selection step does its D^-^ feature become active.
Once that happens, the category feature could trigger Merge with say, the transitive verb *punch*, which has the feature string D^+^ D^+^ V^-^.
The example below shows how we can build the VP *somebody punched the man* this way.
Because I'm a nice guy, I've also added a moving bullet to each feature string so that it's readily apparent which features have already been checked.

(@) Introduce *the* and *man*  
![]({static}/img/thomas/subreg_tutorials/mgtree_01.svg)
(@) *the* selects *man*  
![]({static}/img/thomas/subreg_tutorials/mgtree_02.svg)
(@) Introduce *punched*  
![]({static}/img/thomas/subreg_tutorials/mgtree_03.svg)
(@) *punched* selects the object DP  
![]({static}/img/thomas/subreg_tutorials/mgtree_04.svg)
(@) Introduce *somebody*  
![]({static}/img/thomas/subreg_tutorials/mgtree_05.svg)
(@) *punched* selects the subject DP  
![]({static}/img/thomas/subreg_tutorials/mgtree_06.svg)

But as every Minimalist will tell you, *somebody punched the man* isn't just a VP, it's a CP where the subject *somebody* moves to Spec,TP.
So *somebody* doesn't have the feature string D^-^, it has D^-^ nom^-^.
This nom^-^ is a feature that allows it to move to the closest matching nom^+^, which we will put on the unpronounced head T.

(@) Introduce *somebody* with nom^-^ feature  
![]({static}/img/thomas/subreg_tutorials/mgtree_07.svg)
(@) *punched* selects the subject DP  
![]({static}/img/thomas/subreg_tutorials/mgtree_08.svg)
(@) Introduce the T-head  
![]({static}/img/thomas/subreg_tutorials/mgtree_09.svg)
(@) T-head selects the VP  
![]({static}/img/thomas/subreg_tutorials/mgtree_10.svg)
(@) Subject moves to Spec,TP  
![]({static}/img/thomas/subreg_tutorials/mgtree_11.svg)
(@) Introduce the C-head  
![]({static}/img/thomas/subreg_tutorials/mgtree_12.svg)
(@) C-head selects TP  
![]({static}/img/thomas/subreg_tutorials/mgtree_13.svg)

Now suppose that the sentence is actually *the man, somebody punched*.
In this case, we also want the C-head to carry a licensor feature top^+^ that will attract the topicalized phrase. 
And the head of the topicalized phrase has to carry the matching licensee feature top^-^.
Note that the features are ordered in such a way that the topicalized element can only move once its head has selected all its arguments and it has been selected by the next higher head.
The licensor feature on the C-head, on the other hand, occurs before the category feature so that topicalization must happen before we have a completed CP.

(@) C-head with top^+^ selects TP; *the* carries top^-^  
![]({static}/img/thomas/subreg_tutorials/mgtree_14.svg)
(@) Object undergoes topicalization to Spec,CP  
![]({static}/img/thomas/subreg_tutorials/mgtree_15.svg)

Move is subject to only two constraints.
First, a mover always has to target the closest possible landing site.
You do not get to jump over an f^+^ that you could have checked with your f^-^.
Second, a derivation is automatically ill-formed if two movers can target the same landing site.
This is actually a corollary of the first constraint:
If two movers target the same landing site, only one gets to check the corresponding f^+^ feature.
The other one has to move to a higher position even though it could have checked f^+^.
This is basically a maximally self-centered version of Chomsky's Shortest Move Constraint (SMC) --- "I had to do all that extra work because this other guy suddenly barged in and snatched up the f^+^ I wanted, so I'm gonna file a complaint with the grammar supervisor".
There have been approximately 2,713 discussions as to whether this version of the SMC is compatible with standard Minimalist analyses, and I don't want this to turn into discussion 2,714.
So I'll just say that, yes, there are ways to have this strong SMC and still do what linguists want to do.

Overall, this may seem like a very restricted model of syntax, but it can actually do an astounding amount of stuff.
Rather than immediately bolting on three thousand and seven extensions, let's keep things simple and ask ourselves how complex this basic machinery is.

## Derivation trees and dependency trees

Our question now is the following: can the correct application of Merge and Move be described by subregular means, and if so, how complex are those means?
This is not as simple a question as one might think.
In the example above, we were looking a phrase structure trees.
Phrase structures are actually a dead end for this enterprise, they cannot provide a subregular view of syntax.
It is well-known that syntax goes beyond context-free at the string level, which through a chain of theorems also entails that it goes beyond regular at the level of phrase structure trees.
So if a language's set of phrase structure trees isn't even regular, then that's not a great place to look for subregularity.

But if you think about it, phrase structure trees are supposed to do several things for syntax:

1. encode linear order,
1. encode head-argument relations,
1. encode constituency,
1. encode scope,
1. encode locality.

Phrase structure trees are not the only way to encode all this information.
One could also look at **derivation trees**.
A derivation tree records how a given phrase structure tree is to be assembled.
For instance, the phrase structure tree for *the man, somebody likes* is assembled by following the instructions of the derivation tree below.

![Derivation tree for *the man, somebody likes*]({static}/img/thomas/subreg_tutorials/mgtree_16.svg)

Each derivation tree provides all the information of the phrase structure tree that can be built from it.
But the derivation tree chooses an alternative encoding, and this greatly reduces complexity.
For any given MG, its set of well-formed derivation trees is regular.
Ah, good ol' regularity, now we have a chance to look at subregularity.

But we can actually provide an even more compact representation in terms of **dependency trees**.
If you think about it, the Merge and Move nodes in the derivation tree don't really provide any information that we can't already get from the feature annotation.
Of course *the* and *man* are combined via Merge, that's what has to happen since *the* starts with a selector feature and *man* with a category feature.
And of course the phrase headed by *the* has to move to Spec,CP once the C-head has been merged, that's the only option at that point given the assignment of top^+^ and top^-^.
We can just remove all the interior nodes and instead follow a format where a head is the mother of the arguments its selects.

![Dependency tree for *the man, somebody likes*]({static}/img/thomas/subreg_tutorials/mgtree_17.svg)

Both derivation trees and dependency trees can be useful for various things, and both play a role for subregular complexity.
But for now let's focus on dependency trees because they make some things easier to understand.

## Merge is SL-2 over dependency trees

Merge corresponds to the creation of mother-daughter configurations in a dependency tree.
For every lexical item, we have to make sure that it has a sufficient number of daughters, not too many daughters, and that the daughters have the right category features.
Since the first argument corresponds to the rightmost daughter in a dependency (and the last argument to the leftmost one), all these conditions reduce to a single constraint.

Merge constraint

: The category feature of the *i*th daughter *d* from the right must match the *i*th selector feature of the mother of *d*.

The next few figures show how this constraint works in practice.

![Well-formed dependency tree for *the book, somebody gave to Bill*]({static}/img/thomas/subreg_tutorials/mgtree_18.svg)

(@) Check C-T configuration  
![]({static}/img/thomas/subreg_tutorials/mgtree_19.svg)
(@) Check T-V configuration  
![]({static}/img/thomas/subreg_tutorials/mgtree_20.svg)
(@) Check verb and all its arguments  
![]({static}/img/thomas/subreg_tutorials/mgtree_21.svg)
(@) Check *the* and its argument  
![]({static}/img/thomas/subreg_tutorials/mgtree_22.svg)
(@) Check *to* and its argument  
![]({static}/img/thomas/subreg_tutorials/mgtree_23.svg)

The Merge constraint requires us to only look at a node and its string of daughters.
Intuitively, this means that only two "levels" of tree structure are involved at any given time.
Hence Merge is SL-2.
This is about as simple as it gets.
Remember, in phonology SL-2 handles really simple phenomena like assimilation of *n* to *m* after a bilabial plosive.
It's baby stuff.
SL-2 is the simplest, maximally local class you can pick if you want to have at least some dependence on the surrounding context.
In phonology, SL-2 means looking at two parts of structure related by immediate precedence, and in syntax SL-2 means looking at two parts of structure related by immediate dominance.


## Move is TSL-2 over dependency trees

Now SL-2 obviously won't cut it for Move.
In fact, SL won't work at all because Move is not strictly local.
There is no fixed upper bound on how far a mover may travel to reach its landing site.
But movement does display relativized locality, and as you hopefully remember from our phonology discussion, we can get that by moving from SL to TSL.
For each kind of movement feature (wh, top, nom, and so on), we'll construct a separate tree tier.
The wh-tier, for instance, contains all lexical items that carry wh^+^ or wh^-^.
Just like precedence in the string determine precedence in the tier for phonology, dominance in the dependency tree determines dominance in the tier.

![Dependency tree for *the book, somebody gave to Bill*, and its two movement tiers]({static}/img/thomas/subreg_tutorials/mgtree_24.svg)

Now what do these tiers have to look like?
Well, every carrier of an f^-^ must have a matching f^+^ mother, otherwise there's nowhere for it to move to.
Every f^+^ must have an f^-^ daughter, otherwise there's nothing moving to it.
And it also cannot have more than one f^-^ daughter, otherwise those daughters would be competing, which isn't allowed by the SMC.
This leaves us with a very simple constraint.

Move constraint

: For every movement feature f, the following two conditions must hold of every node on the f-tier.
  1. If the node carries an f^-^ feature, it must have a mother carrying an f^+^ feature.
  1. If the node carries an f^+^ feature, it must have exactly one node with an f^-^ feature among its daughters.

This works as intended even in more complex cases.

![Dependency tree for *John thinks that Bill complains that Mary left*, and its nom-tier]({static}/img/thomas/subreg_tutorials/mgtree_25.svg)

And that's all there is to it.
Just like Merge, Move only involves mother-daughter configurations, but here we're looking at mother-daughter configurations over tree tiers instead of the actual dependency tree.
Merge is SL-2, Move is TSL-2.


## Lesson(s) of the day

There's quite a few mathematical complications that I've glossed over here to focus on the --- imho very appealing --- big picture.
Merge is the simplest kind of mechanism that involves awareness of the local context, and Move is the simplest kind of mechanism that involves relativized locality.
While syntax looks very different from phonology, its two most basic operations aren't all that different from what we find in phonology.
SL-2 and TSL-2 are very common classes for phenomena.
The difference is that syntax relies on more complex representations than phonology (dependency trees or derivation trees).

Admittedly, though, syntax is more than just Merge and Move.
What about islands, NPI licensing, binding, idioms, prosody?
Patience, patience, one thing at a time.
