---
title: >-
    More observations on privative features 
authors:
    - Thomas Graf
date: 2019-06-17
bibliography: references.bib
series: Privative feature
tags:
    - features
    - privativity
    - phonology
    - syntax
    - transductions
---

<!-- START_SUMMARY_BLOCK -->
In an [earlier post]({filename}2019-06-11_graf_privativity.md) I looked at privativity in the domain of feature sets: given a collection of features, what conditions must be met by their extensions in order for these features to qualify as privative.
But that post concluded with the observation that looking at the features in isolation might be a case of the dog barking up the wrong tree.
Features are rarely of interest on their own, what matters is how they interact with the rest of the grammatical machinery.
This is the step from a **feature set** to a **feature system**.
Naively, one might expect that a privative feature set gives rise to a privative feature system.
But that's not at all the case.
The reason for that is easy to explain yet difficult to fix.
<!-- END_SUMMARY_BLOCK -->

## Feature set recap

Let's quickly recap the essential properties of a feature set.
Each feature is a set of exponents, and a feature bundle is a finite collection of features.
A feature bundle picks out the exponents that carry all the features of the bundle --- mathematically, the intersection of the exponent sets that correspond to the features in the bundle.
A **feature set** is a finite collection of features from which feature bundles may be built.
Without further restrictions, pretty much anything goes, but I argued that (a very strong notion of) privativity arises from two additional conditions: 

Non-complementation

: No $F$-bundle denotes the complement of some other $F$-bundle.  
  $\forall X \subseteq F\ \neg \exists Y \subseteq F\ [\bigcap X = \overline{\bigcap Y}]]$

Compositionality

: It holds for all distinct $F$-bundles $X$ and $Y$ that $\bigcap X \cap \bigcap Y$ is a non-empty proper subset of $\bigcap X$.

As Peter Svenonius [points out in the comments section of the previous post](https://outde.xyz/2019-06-11/some-observations-on-privative-features.html#comment-1), this might be so strong that it rules out many feature sets that linguists would still consider privative.
But let's run with it for now, being too strong a restriction isn't much of a problem for the purposes of this post.


## Feature systems and privativity

Alright, so now we have a notion of feature set, but we have no model of how the feature set is integrated into the grammar.
That's a serious omission, but it's also hard to fill in because grammars are a moving target.
According to recent census counts, there are currently 3,289,777 registered grammar formalisms, but officials estimate that the number of unregistered grammar formalisms is much larger.
However, I think there's a general point to be made that's largely independent of the specific grammar formalism: as soon as you have disjunction, features become immaterial.

Suppose you have a privative feature set and you have a process or constraint that should target any exponent that lacks some feature *f*.
Due to Non-complementation there can be no feature bundle that picks out the complement of *f*, so we have no feature bundle description of the exponents targeted by the process.
The linguistic intuition behind privativity is that this means the process cannot take place --- you cannot make reference to the absence of features, you cannot use feature negation.
If only things were this easy.
There's a major loop hole here: each individual exponent lacking *f* has a description in the form of a feature bundle, so we can use a disjunction of feature bundles to describe the domain of the process.

Suppose that the set of exponents consists of *u*, *v*, *w*, *x*, *y*, *z* and that *f* picks out *u*, *v*, and *w*.
The exponents lacking *f* are *x*, *y*, and *z*.
A process that can target *x* or *y* or *z* is one that targets the complement of *f*, violating privativity.
This strategy works for any feature system, privative or not, as long as the set of exponents is finite.
In that case, the complement of any feature is a finite set, so one can simply enumerate all the members of the complement with a disjunction.
Privativity of feature systems, then, has to limit both negation of features and disjunction of feature bundles.
If we can rein in negation and disjunction, then privativity of feature sets would have some formal bite.

Unfortunately, both negation and disjunction can be hidden inside other mechanisms.
Rule ordering, for instance, can take on the role of disjunction.
Instead of a single process *p* that targets *x* or *y* or *z*, we have *p~x~* targeting *x*, *p~y~* targeting *y*, and *p~z~* targeting *z*.
All three processes produces the same output, they only differ in their target.
Run them in a cascade *p~x~ - p~y~ - p~z~*, and you've got the same output that *p* produces in one fell swoop.

There's some potential complications here as breaking up *p* into a cascade of processes might cause (counter)feeding or (counter)bleeding so that the cascade does not always produce the same output as *p* itself.
Depending on one's formalisms, these problems be coded around in very unintuitive ways like the following: if *p* maps its targets to some *a*, then *p~x~* *p~y~* and *p~z~* map targets to some *b* instead that is an exponent that cannot occur in such contexts, and then some process *p'* at the end maps illicit instances of *b* to *a*.
Admittedly crazy, and there are some kinds of mathematical models that do not allow for these shenanigans.
But this just shows that privativity cannot be easily reduced to a single piece of the grammar.
It is an emergent property of the whole formalism.


## Abstract privativity

In the characterization of privative feature sets, I had to completely abstract away from the usual nitty-gritty of linguistic features.
I didn't say a word about notation.
A multi-valued feature apparatus can actually meat Non-complementation and Compositionality, making it privative according to my criteria.
What matters is the high-level behavior of how the set of exponents is carved up into subclasses and how these subclasses are related to each other.
There's infinitely many ways to encode this behavior, so stating Non-complementation and Compositionality at the level of encodings would have been a hopeless task.

The same holds for privativity of feature systems.
There's simply too many parameters, too much machinery to state privativity at this level.
How could one possible define privativity for SPE rewrite rules in a way that naturally generalizes to autosegmental spreading?
How does one ensure that the grammar doesn't provide hidden means for negation and disjunction that the current definition fails to take into account?
The answer is that one simply doesn't.
Grammars are not the right level of description.
Perhaps we should go in the other direction, as high-level as possible: transductions.

A transduction is any kind of input-output mapping between representations of some kind.
An SPE rewrite rule is a string transduction that maps an input string to an output string.
Autosegmental spreading is a transduction that maps an input graph to an output graph.
Movement is a transduction that maps a phrase structure tree to another phrase structure tree.
And a constraint is a transduction that maps a well-formed structure to itself and an ill-formed structure to nothing at all, thereby removing it from the set of licit structures.
We can even view each grammar as one big transduction that maps inputs to outputs in one fell swoop without any intermediate steps.

So transductions are a pretty all-encompassing notion.
If we could find a formal approximation of privativity at this level, that would be huge.
Alas, I'm not quite sure how to do it.
Here's one simple idea: if a grammar contains a transduction targeting some set *S* of exponents, no other transduction in the grammar may target the complement of *S*.
But that doesn't work because the domain of a transduction can always be extended to the full universe.
For instance, suppose we have a universe consisting of *a*, *b*, and *c*.
If we have one transduction that maps both *a* and *b* to *d*, then we should not have another transduction that maps *c* to *e*.
But we can just take the union of the two to have a single transduction that maps *a* and *b* to *d* and *c* to *e*.
Or alternatively, we extend the first transduction so that it maps *a* and *b* to *d* and *c* to *c*, whereas the second one maps *a* to *a*, *b* to *b*, and *c* to *e*.
Either way the requirement of non-complementary domains has been rendered null and void.

Looks like we went too far in the other direction, from overly specific grammar formalisms to overly general transductions.
Somewhere in between there might be a suitable level of description for privativity.
For phonology, one could pick a subclass of the finite-state string transductions, and for syntax perhaps a subclass the transductions definable in first-order logic.
These are sufficiently general to encompass almost everything that matters for their respective domain.
At the same time, they are concrete enough that privativity can be stated in a specific form.
I have no clue what that will look like, though.
For first-order logic, the obvious candidate is banning negation and disjunction, but that won't work in its most radical form because negation is indispensable, and disjunction is redundant if one has unlimited access to negation.

I feel like there's a very simple trick to make all of this work beyond the level of features, and I just haven't found it yet.
It's an important issue, though, one that bridges formal and substantive universals, so I'll keep thinking about it.
Feel free to add your suggestions in the comments below --- if it works, your name will be immortalized in a tiny footnote of my groundbreaking paper ;-)
