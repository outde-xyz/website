---
title: >-
    Some observations on privative features 
authors:
    - Thomas Graf
date: 2019-06-11
bibliography: references.bib
tags:
    - features
    - privativity
    - phonology
    - syntax
---

<!-- START_SUMMARY_BLOCK -->
One topic that came up at the feature workshop is whether features are privative or binary (aka **equipollent**).
Among mathematical linguists it's part of the general folklore that there is no meaningful distinction between the two.
Translating from a privative feature specification to a binary one is trivial.
If we have three features $f$, $g$, and $h$, then the privative bundle $\{f, g\}$ is equivalent to $[+f, +g, -h]$.
In the other direction, we can make binary features privative by simply interpreting the $+$/$-$ as part of the feature name.
That is to say, $-f$ isn't a feature $f$ with value $-$, it's simply the privative feature $\text{minus} f$.
Some arguments add a bit of sophistication to this, e.g. the Boolean algebra perspective in Keenan & Moss's textbook *Mathematical Structures in Language*.
So far so ~~good~~ unsatisfactory.
<!-- END_SUMMARY_BLOCK -->

## Privativity is tricky

While the feature switch above is mathematically sound and creates a system of privative features, it's not playing by the intended rules.
Pretty much every linguist will confirm that.
The problem is that it isn't quite clear what the rules are.
Just like theoretical linguists can't directly ask native speakers about the rules of grammar, the mathematical linguist cannot ask the theoretical linguist about the rules of privative feature systems.
Neither group has concious access to the mechanisms that give rise to their judgments.
It's all fuzzy intuitions.
But the standard notion that a privative feature system is one where the features are written without $+$ or $-$ clearly doesn't cut it.
We just saw that, it fails to exclude all kinds of feature systems that are not deemed appropriately privative.

To be frank, I believe that getting a formal grip on the linguistic notion of privativity is not only hopeless, but pointless.
It's like asking a botanist to define *vegetable* --- that's a culinary term, it simply makes no sense from a botanist point of view.
But what we can do is devise formal concepts that are inspired by privativity.
They may not always map neatly onto what linguists consider a privative feature system, but they might be close enough to investigate some of the issues that linguists care about.

Make no mistake, though, this is quite a demanding enterprise.
The central problem is that it isn't enough to define a privative feature system, one also has to nail down how these features may interact with the rest of the grammar.
For instance, in propositional logic it does not matter whether features are privative because of negation.
Even if $f$ is privative, $\neg f$ is equivalent to referencing $[- f]$.
And obviously linguists vastly disagree on rule systems, feature representation, and so on.
This makes privativity a very fluid and ill-defined term.
As I said, vegetables.
So my goal is much less ambitious: in this post, I'll try to present a notion of privative **feature sets**, and then in the next post I'll integrate that with restrictions on finite-state transducers to arrive at a privative **feature system**.
I won't spoil the surprise whether this actually amounts to a meaningful restriction.


## Privative feature sets: Basics

The first thing we need is a definition of privative features that does not hinge on notation.
Notation is the devil, it never states its generalizations explicitly and is easily undermined by a creative mind.
Defining privativity as "features without values" does not capture what privativity is about.
Privativity starts with the idea that the $+$ and $-$ side of a binary feature aren't on equal footing.
Only one of the two can be invoked in the rules of the grammar.
As we'll see in the next post, this is a very tricky notion to capture.
But the starting point is simple enough: we don't want to be able to refer to the opposite of a feature.

First, let $E$ be some set of **exponents**.
This could be segments, morphemes, words, sentences, molecules, animals, all the people you had a crush on as a teenager, whatever.
Then a **feature set** $F$ is some finite collection of non-empty proper subsets of $E$ ($F \subseteq \wp(E) - \{E, \emptyset\}$ finite).
The sets in $F$ are called **$F$-features** or simply **features**.
A collection $X$ of $F$-features is a **feature bundle over $F$**, or simply $F$-bundle.
Its **denotation** consists of all the exponents in $\bigcap X$, and only those.

Intuitively, each subset of $F$ corresponds to a feature that holds of all the elements in this subset, and only those.
Since linguistic features are supposed to be non-trivial, the definition explicitly excludes features that hold of all exponents or none at all.
Feature bundles are sets of features, and the exponents they represent are determined via intersection.
So if $E := \{ a, b, c\}$ and $F$ contains $A := \{ a, c \}$ and $B := \{ b, c \}$, then $A \cap B$ yields $c$.

This system is still very basic, but by the power of stipulation we can throw in a few additional properties.
The first one is coverage.

Coverage

: Every element of $E$ belongs to some $F$-feature.  
  $\bigcup F = E$

Coverage ensures that the feature set has some way of encoding each member of $E$.
However, it does not guarantee that every exponent has a unique encoding.
Consider once more the example with $E := \{ a, b, c\}$, $A := \{ a, c \}$ and $B := \{ b, c \}$.
Clearly $E = A \cup B$, but $a$ and $b$ cannot be uniquely identified.
The only available feature specifications are as follows:

| **Feature specification** | **Exponents** |
| :-:                       | :-:           |
| *A*                       | a, c          |
| *B*                       | b, c          |
| *A,C*                     | c             |
| *B,C*                     | c             |

We could of course strengthen coverage to ensure unique encodings.

Uniqueness

: For every exponent there is a feature bundle whose denotation includes only this exponent.  
  $\forall e \in E\ \exists X \subseteq F\ [ \bigcap X = \{e\} ]$

Uniqueness may be a desirable property for phonological feature sets, but it isn't for syntax where many lexical items may have exactly the same feature specification.
At the same time, coverage may not be quite right for phonology.
Government Phonology, for example, treats the mid-central schwa as being completely devoid of all features.
So we already have reached a point where it isn't quite clear what the fundamental axioms for a privative feature set should be.
In fact, it isn't even clear that either axiom constitutes a meaningful restriction.
I'll return to that in the next post.

## The essential property: Non-complementation

Let's put the Coverage vs Uniqueness issue aside for now and focus on what we're really interested in: 

Non-complementation

: No $F$-bundle denotes the complement of some other $F$-bundle.  
  $\forall X \subseteq F\ \neg \exists Y \subseteq F\ [\bigcap X = \overline{\bigcap Y}]]$

Non-complementation ensures that we cannot assign a feature-based representation to the negation of natural classes.
This is very similar to the linguistic notion of privativity: but there's a subtle difference.
Privativity only talks about negations of features.
We may formalize it as follows:

Privativity

: No $F$-bundle denotes the complement of some $F$-feature.  
  $\forall X \subseteq F\ \neg \exists Y \in F\ [\bigcap X = \overline{Y}]]$

Non-complementation extends privativity from features to feature bundles.
You might think they're effectively the same, but they're not!
There can be feature sets where the complement of any given feature cannot be defined, but the complement of some feature combinations can be.
A concrete example is shown in the table below:

| **Feature** |     |     |     |     |     |     |
| --:         | :-: | :-: | :-: | :-: | :-: | :-: |
| *A*         | a   |     |     | x   | y   | z   |
| *B*         |     | b   |     | x   | y   | z   |
| *C*         |     |     | c   | x   | y   | z   |
| *X*         | a   | b   | c   | x   |     |     |
| *Y*         | a   | b   | c   |     | y   |     |

It is impossible with this feature set to pick out the complement of any feature, so Privativity holds.
But the complement of $X \cap Y$ is $\{x, y, z\}$, which is the intersection of $A$, $B$, and $C$.
Despite Privativity, Non-complementation is not met.

## Patching some holes with compositionality

We are already pretty close to what a linguist might consider a privative feature set, but we still haven't enforced one crucial aspect.
Right now, we allow for systems where every feature is a singleton set, which means that there would be a separate feature for each exponent.
This misses the point of features to a ludicrous degree.
Sure, this would allow us to treat Social Security Numbers as features, but this isn't really what I had in mind.
Not too much SSN action in syntax or phonology.

Features are supposed to pick out larger subclasses that get whittled down through intersection.
Sounds simple, but formalizing this notion isn't trivial.
One could require every feature to contain at least $n$ exponents, but that doesn't really fix the problem --- one could still have non-combinatorial systems where feature sets do not overlap and no exponent ever has more than one feature.

More abstract conditions fail, too.
Consider the one below.

Linking

: Let $G$ be an undirected graph where nodes are $F$-bundles and two nodes $X$ and $Y$ are connected by an edge iff $X \cap Y \neq \emptyset$.
  Then $G$ must be connected.

An undirected graph is connected iff every pair of nodes has a path connecting the two.
A tree is a simple example of a connected graph if one is allowed to move both up and down along branches --- clearly, every node can be reached from every other node by moving up and down within the tree.
Hence linking guarantees that every feature must have some overlap with at least one other feature.
The feature set below violates this condition as there is no feature that connects the ABC-group to the XY-group.

| **Feature** |     |     |     |     |     |     |
| --:         | :-: | :-: | :-: | :-: | :-: | :-: |
| *A*         | a   | b   |     |     |     |     |
| *B*         |     | b   |     |     |     |     |
| *C*         |     | b   | c   |     |     |     |
| *X*         |     |     |     | x   | y   |     |
| *Y*         |     |     |     |     | y   | z   |

But this still allows for very shallow system with tiny feature denotations.
For instance, we could still have one feature for each exponent as long as we also have bigger feature classes that have sufficient overlap to guarantee connectedness.
Sometimes the addition of a single, ultimately meaningless feature to a single element can be enough.
This is shown below, where the addition of feature *C* to exponent *x* creates a connected graph even though *C* is redundant for differentiating *x* from the other exponents.

| **Feature** |     |     |     |     |     |     |
| --:         | :-: | :-: | :-: | :-: | :-: | :-: |
| *A*         | a   | b   |     |     |     |     |
| *B*         |     | b   |     |     |     |     |
| *C*         |     | b   | c   | x   |     |     |
| *X*         |     |     |     | x   | y   |     |
| *Y*         |     |     |     |     | y   | z   |

Linking doesn't help at all, then, it's way too weak.
Let's try something more extreme.

Compositionality

: It holds for all distinct $F$-bundles $X$ and $Y$ that $\bigcap X \cap \bigcap Y$ is a non-empty proper subset of $\bigcap X$.

This is strong, incredibly strong.
It mandates that a feature bundle may never have an empty denotation, and that every feature must always have a meaningful contribution to make.
Features cannot be incompatible, and the feature set must be completely redundancy free.
There is no room for features that make a meaningful contribution in only some special cases.
I don't think any feature set on the market satisfies this requirement, except perhaps the highly abstracted one of [Bobaljik and Sauerland](http://doi.org/10.5334/gjgl.345).
It might be workable if each language is assigned its own set of features rather than fixing a universal base for all languages.
Even then I have my doubts.
In morphosyntax, we want tense features for verbs and case features for nouns.
They have no overlap at all (although I vaguely remember some proposal along those lines).

That said, let's run with it for now.
I see no mathematically natural middle ground between compositionality and linking, and I'd rather explore an overly restricted system than one that's too loose.
It will already be messy enough as it is.


## Summary

While the notion of privativity is too malleable to be put into rigorous terms, we can define a formal model that follows the general spirit. 

Given a set $E$ of exponents, a **privative feature** is some non-empty proper subset of $E$. 
A **feature bundle** is a finite set of features.
A **privative feature set** $F$ is a finite collection of features that satisfies two conditions:

Non-complementation

: No $F$-bundle denotes the complement of some other $F$-bundle.  
  $\forall X \subseteq F\ \neg \exists Y \subseteq F\ [\bigcap X = \overline{\bigcap Y}]]$

Compositionality

: It holds for all distinct $F$-bundles $X$ and $Y$ that $\bigcap X \cap \bigcap Y$ is a non-empty proper subset of $\bigcap X$.

In addition, coverage and/or uniqueness may hold.

Coverage

: Every element of $E$ belongs to some $F$-feature.  
  $\bigcup F = E$

Uniqueness

: For every exponent there is a feature bundle whose denotation includes only this exponent.  
  $\forall e \in E\ \exists X \subseteq F\ [ \bigcap X = \{e\} ]$

This definitely puts some restrictions on what kinds of sets of exponents can be defined in comparison to a binary feature set.
But I don't consider that particularly noteworthy in itself.
Nobody cares about natural classes in isolation, what matter is how they interact with the rules of the grammar.
This is the step from a feature set --- a tool for picking out sets of exponents --- to a **feature system**, which controls how grammar rules are applied to exponents.
That's the real crux, and it's sufficiently complicated that it requires its own follow-up point.
