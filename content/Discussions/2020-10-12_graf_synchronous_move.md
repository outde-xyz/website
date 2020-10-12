---
title: >-
    Synchronous movement: What could go wrong?
authors:
    - Thomas Graf
date: 2020-10-12
bibliography: references.bib
tags:
    - syntax
    - movement
    - Minimalist grammars
    - subregular
---

<!-- START_SUMMARY_BLOCK -->
I know I promised you guys a follow-up post on logical transductions and the status of representations, but I just have to get this out first because it's been gnawing at me for a few weeks now.
There's been some limitations of the subregular view of syntax in terms of movement tiers, and I think I've found a solution, one that somehow ends up looking a bit like the system in *Beyond Explanatory Adequacy*.
The thing is, my solution is so simple that I fear I'm missing something very basic, some clear-cut empirical phenomenon that completely undermines my purported solution.
So, syntacticians, this is your opportunity to sink my current love child in the comments section...
<!-- END_SUMMARY_BLOCK -->

## The problem with movement tiers

As you might remember, the basics of movement can be [modeled as local constraints on movement tiers]({filename}/Tutorials/locality_merge_move.md).
The idea is that we look at a syntactic derivation, represented as an MG dependency tree.
For each movement type, i.e. wh, topicalization, subject movement, and so on, we consider only those nodes that participate in this kind of movement as either the head of the moving phrase or the that provides the landing site.
This information is assumed to be encoded via features --- for instance, MGs use *licensee features* $\mathrm{f^-}$ for the mover and *licensor features* $\mathrm{f^+}$ for the landing site.
In such a system, it is very easy to find the relevant nodes for each tier.
On each $\mathrm{f}$-tier, we then require that 

1. every $\mathrm{f^-}$ has an $\mathrm{f^+}$ mother, and 
1. every $\mathrm{f^+}$ has exactly one $\mathrm{f^-}$ among its daughters.

This ensures a 1-to-1 match between movers and landing sites.

![Dependency tree and tiers for *Mary wonders which car Sue bought*]({static}/img/thomas/movement_synchronous/mtiers_basic.svg)

That's the general idea, and imho it's an intuitively pleasing one.
But this actually does not work in the general case, at least for MGs.
In MGs, a head can have multiple licensee features, and those features are linearly ordered.
For instance, if *which* is the head of a subject wh-phrase, its string of features would be something like $\mathrm{N^+}\ \mathrm{D^-}\ \mathrm{nom^-}\ \mathrm{wh^-}$.
This means that once *which* has merged with an NP and has been selected by some other head, checking its selector feature $\mathrm{N^+}$ and its category feature $\mathrm{D^-}$ in the process, it undergoes subject movement via $\mathrm{nom^-}$, and then wh-movement via $\mathrm{wh^-}$.

Crucially, the features of *which* are inactive until all the features before them have been checked.
You can think of this like a dot moving through the feature string from left to right, and the only feature that counts is whatever is immediately to the right of the dot.
The steps above would correspond to the following feature string configurations:

1. $\bullet \mathrm{N^+} \mathrm{D^-}\ \mathrm{nom^-}\ \mathrm{wh^-}$: the selector feature $\mathrm{N^+}$ is active and must be checked via Merge
1. $\mathrm{N^+} \bullet \mathrm{D^-}\ \mathrm{nom^-}\ \mathrm{wh^-}$: the category feature $\mathrm{D^-}$ is active and must be checked via Merge
1. $\mathrm{N^+}\ \mathrm{D^-} \bullet \mathrm{nom^-}\ \mathrm{wh^-}$: the licensee feature $\mathrm{nom^-}$ is active and must be checked via Move
1. $\mathrm{N^+}\ \mathrm{D^-}\ \mathrm{nom^-} \bullet \mathrm{wh^-}$: the licensee feature $\mathrm{wh^-}$ is active and must be checked via Move
1. $\mathrm{N^+}\ \mathrm{D^-}\ \mathrm{nom^-}\ \mathrm{wh^-} \bullet$: all features of *which* have been checked

Since features are inactive by default, there is nothing wrong with derivations like the one below, represented once again as an MG dependency tree.
The $\mathrm{wh}^-$ on *which* and *what* are never active at the same time, so there's no confusion about how these licensee features are matched up against $\mathrm{wh}^+$ on *saw* and the C-head.

![Dependency tree and tiers for *Which witness what saw*]({static}/img/thomas/movement_synchronous/mtiers_protected.svg)

But if you look at the wh-tier for this derivation, it does not obey the constraints above.
We have a $\mathrm{wh^+}$ without a $\mathrm{wh^-}$ daughter, whereas another $\mathrm{wh^+}$ has two.
The tier-based perspective misses the fact that the $\mathrm{wh^-}$ on *which* only becomes active after $\mathrm{nom^-}$ has been checked.
Basically, the position of *which* on the $\mathrm{wh^-}$ tier should be higher, corresponding to the point in the derivation where a $\mathrm{nom^+}$ checks the $\mathrm{nom^-}$ on *which*.

There's two ways to deal with this.
My position so far has been to assume that the grammar is in **single movement normal form**. 
This is a bulky term for the simple idea that no head can ever have more than one licensee feature.
It's simply impossible for *which* to carry both $\mathrm{nom^-}$ and $\mathrm{wh^-}$.
That's an innocent working assumption in the sense that it does not affect weak or strong generative capacity.
But it also pushes us farther away from the standard view of syntax, and that's the very opposite of what I'd like subregular syntax to accomplish.

The other option is to switch to a much more sophisticated tier projection mechanism.
It's not even that hard to define, but it's not particularly natural from a subregular perspective, and that's why it doesn't strike me as a very insightful route to take.
So recently I figured, the hell with it, what if the tier-based view of syntax is correct in its current form? 
What would syntax look like if we don't have the single movement normal form, but the tier constraints still apply in the same fashion?


## Synchronous movement

Remember that I said above that features in MGs get unlocked one after the other.
Features tend to spend most of their derivational life inactive, patiently waiting in line until $\bullet$ shows up to tell them its their turn.
The tier-based view of syntax cannot handle this orderly line, it thinks of each lexical item as a beehive where all features are active at the same time.
The $\mathrm{wh^-}$ on *which* doesn't give a damn that it isn't its turn yet, it's ready to rock right away and it won't have other $\mathrm{wh^-}$ barge into its territory.
In a system that works like this, the derivation above would no longer be allowed --- even though *which* can't even target the $\mathrm{wh^+}$ on *saw*, it still won't let any other phrase move there.

This may sound a little strange to you, but it gets even more bonkers once you look at it in terms of phrase structure trees.
Traditionally, we think of it as *which* moving to the subject position in Spec,TP, and then it undergoes wh-movement from Spec,TP to Spec,CP.

![Standard view: Movement is continuous sequence of steps]({static}/img/thomas/movement_synchronous/phrasestructure_normal.svg)

In tier-based syntax, *which* still undergoes subject movement as usual, but it simultaneously also undergoes wh-movement to Spec,CP.
Kinda like in Chomsky's *Beyond Explanatory Adequacy*.
And also a bit like in a multi-dominant syntax, where a mover never truly leaves its base position.
The fact that the feature string of is $\mathrm{N^+} \mathrm{D^-} \mathrm{nom^-} \mathrm{wh^-}$ no longer means that subject movement precedes wh-movement, it only tells us that wh-movement must target a position higher than the one targeted by nom-movement (and that requirement would have to be enforced by some additional mechanism besides movement tiers).

![Tier-based view: All movement steps start from the base position]({static}/img/thomas/movement_synchronous/phrasestructure_parallel.svg)

## Problems?

So the last few weeks I've been trying to come up with clear-cut empirical problems for this approach.
I can't find any.

The standard MG model predicts that it is bad for two wh-phrases to have overlapping wh-movement paths, unless the part where they overlap is actually part of a different movement step like subject movement.
That's not really how syntax seems to work.
You usually don't get overlapping wh-paths, but rather two wh-phrases competing as to which one gets to move at all, while the other has to stay behind (let's not get into multiple wh-movement here, all I'll say is that it is entirely unproblematic and perfectly natural from the tier-based perspective).

Then I thought the distinction between A-movement and A$'$-movement might produce a counterexample.
Perhaps a phrase must not undergo wh-movement from position X, but once it has undergone some other type of movement to a higher position it can move from there.
This also seems to happen a lot with scrambling.
But those cases can be reanalyzed as the difference between carrying just $\mathrm{wh^-}$ or $\mathrm{nom^-} \mathrm{wh^-}$ --- it's not the position itself that matters, but rather what kind of mover you are, a simple wh-mover VS a synchronous nom-wh-mover.

I'm mostly talking about wh-movement here, but I don't think things are much different for topicalization, raising, and so on.
I just can't find a good counterexample.
Part of that could be because of a category mismatch between what the movement literature cares about and what I'm looking for.
Subjacency and relativized minimality, for example, aren't directly about movement once you operate under the assumption that everything is encoded via features.
They are about how features must be distributed over heads: "no, you can't have a $\mathrm{wh^-}$, that has to go on this fellow over here because he's in a structurally more prominent position".
Tier-based syntax, on the other hand, is a model of how movement has to proceed once these features have been distributed over heads.
We're probing part of a larger system, which is difficult unless all parts of the system are precisely nailed down, which they aren't.

But as I said, maybe this is all just me being really dense.
Maybe there is an obvious problem that I'm missing.
Maybe there is a clear-cut argument why movement must be thought of as a road trip with several stops on the way, rather than a number of identical packages being sent from the same hub to different destinations.
