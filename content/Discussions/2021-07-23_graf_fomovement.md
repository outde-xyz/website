---
title: >-
    MGs do not struggle (as much as you think) with multiple wh-movement
authors:
    - Thomas Graf
date: 2021-07-23
bibliography: references.bib
tags:
    - Minimalist grammars
    - movement
    - multiple wh-movement
    - transductions
    - first-order logic
---

<!-- START_SUMMARY_BLOCK -->
In February I had a nice chat with [Bob Frank](https://bobfrank1.github.io/) and [Tim Hunter](https://timhunter.humspace.ucla.edu/) regarding [their SCiL paper on comparing tree-construction methods across mildly context-sensitive formalisms](https://timhunter.humspace.ucla.edu/papers/HunterFrank2021-SCiL.pdf).
Among other things, this paper reiterates the received view that MGs cannot handle unbounded multiple wh-movement.
That is certainly true for standard MGs as defined in @Stabler97, but my argument was that this is due to what may now be considered an idiosyncrasy of the definition.
We can relax that definition to allow for multiple wh-movement while preserving essential formal properties of MGs.
However, friendly chats aren't a good format for explaining this in detail, so I promised them an Outdex post with some math.
Well, 5 months later, I finally make good on my promise.
<!-- END_SUMMARY_BLOCK -->

## Why multiple wh-movement is considered problematic for MGs

In MGs, movement is feature-triggered: the landing site must have a licensor feature f^+^, the head of the mover carries an f^-^.
Consider a simple case of wh-movement:

(@simple) Which book did Mary give Kelly.

Let's ignore all the syntactic details like VP-internal subjects, what triggers do-support, and the positions of direct and indirect objects so that we can focus just on the wh-movement.
A fairly standard MG analysis would posit that *which* carries wh^-^ and *did* has wh^+^.
Those are movement features of the same name but opposite polarity, which triggers movement of the phrase headed by *which* (i.e. *which book*) to a specifier of *did*.
As part of this movement step, the wh-features that triggered it are also checked and deleted.
Overall pretty vanilla and close in spirit to @Chomsky95a or @Adger03, except that MGs use feature polarity instead of interpretability.

We can represent the whole derivation for (@simple) in the form of a tree, but again I'll only indicate the features that matter for wh-movement.

![]({static}/img/thomas/multiple_wh/der_simplewh.svg)

This isn't just a matter of notation, those trees will play a key role in generalizing MGs so that they can handle multiple wh-movement.

But first things first, we haven't even established yet why MGs have problems with multiple wh-movement.
The problem is actually two-fold.
One is what is know as the *Shortest Move Constraint* (SMC), the other is the 1-to-1 matching of MG feature checking.
Let's look at a concrete example.
In (@multiple) below, we now have a variant of (@simple) where all DPs undergo wh-movement.

(@multiple) Which book who whom did give.

What would the MG derivation for this have to look like?
Well, since each DP moved, each one has to have a wh^-^ on the respective head.
And since each wh^-^ must be checked against some wh^+^, which causes both features to be deleted, *did* must carry one wh^+^ for each moving DP, giving us a total of three wh^+^ on *did*.
The corresponding derivation is shown below, with arrows indicating what is supposed to move where.

![]({static}/img/thomas/multiple_wh/der_multiplewh_multifeatures.svg)

Alas, this is not a licit MG derivation because it violates the SMC.
The SMC could also be called the **Ghostbusters constraint**: do not cross the (feature) streams!
If we imagine each f^-^ sending a stream up through the tree until it finds a matching f^+^, then we may never have two f-streams travelling alongside each other.
But this is exactly what happens in the derivation above, where three distinct wh-streams end up entangled.

![]({static}/img/thomas/multiple_wh/der_multiplewh_ghostbusters.svg)

Now this issue we can actually work around because who's to say that we have to consider all those wh-features wh-features just because linguists treat them as wh-features.
Maybe those aren't wh^-^, wh^-^, and wh^-^ on *which*, *who*, and *whom*.
Maybe they're actually wh1^-^, wh2^-^, and wh3^-^, giving us the lovely derivation tree below.

![]({static}/img/thomas/multiple_wh/der_multiplewh_subscriptfeatures.svg)

From a formal (substance-free) perspective, wh1^-^ and wh2^-^ are just as distinct as, say, wh^-^ and top^-^.
They are completely different features, and as a result the SMC, which only cares about crossed streams of the same feature type, is no longer violated.
Yes, it is a very lame solution, but it is a solution.

Except, it's not really.
Because if there are languages with no upper bound on how many wh-phrases may move at the same time (and there might indeed be some depending on how one draws the line between competence and performance), then it's not enough to just have wh1^-^, wh2^-^, and wh3^-^.
We also need wh4^-^, wh5^-^, and so on, *ad infinitum*.
And this also means that we need infinitely many versions of *did*: one carrying only wh1^+^, one that carries wh1^+^ and wh2^+^, one with wh1^+^, wh2^+^, and wh3^+^, and so on.
But the most fundamental assumption of MGs is that the collection of lexical types must be finite, which means the lexicon cannot contain infinitely many variants of *did*.
We have finally hit a dead end: the combination of the SMC and one-to-one feature checking forces us to treat multiple wh-movement in a way that is incompatible with the very foundation of MGs.


## SMC, what art thou good for?

The argument above shows that MGs as defined in @Stabler97 cannot handle unbounded multiple wh-movement.
But it is important to keep in mind why MGs were defined this way, in particular with respect to the SMC.
The SMC has always been a bit of an ugly wart on MGs, the one thing that every syntactician immediately calls out as a major deviation from mainstream Minimalism.
Why then stick with the SMC?
Because it is a conceptually simple constraint that gives us three properties:

- **Move is deterministic:** there is no ambiguity as to what moves where (because the SMC rule out all configurations where such ambiguity could arise).
- **MG derivations are regular:** the set of well-formed derivation trees forms a regular tree language (which is something mathematical linguists care a lot about).
- **Movement is regular:** movement corresponds to a specific kind of regular tree transduction from derivation trees to derived structures (which, again, is something mathematical linguists care a lot about).

Instead of ensuring those three properties through independent means, one can just put in place the SMC and get them all as a corollary.
But the price we pay for this simplicity is that the SMC brings about its own set of problems, with multiple wh-movement being the most prominent exponent.
If we tackle the three properties independently of each other, then there is a fairly easy way to do multiple wh-movement in MGs.


## Regular derivations with a decomposed SMC

The standard MG feature calculus can be reinterpreted as a collection of constraints on derivation trees.
Side remark: That's quite generally a good perspective to take as it gets us to look beyond feature notation (where MGs and Minimalism differ quite a bit) to look at the behavior of the whole feature calculus (where MGs and Minimalism are very close in spirit).
Anyhoo, this tree-geometric view of feature checking is exactly what we need to get a grip on multiple wh-movement.

In tree-geometric terms, MG feature checking revolves all around what I decided to call **occurrences** many years ago, in my youthful exuberance.
Intuitively, a Merge node or a Move is an occurrence of a lexical item iff it checks one of the negative features on said lexical item.
More precisely:

1. The 0-occurrence of a lexical item *l* is the Merge step where *l* gets selected, checking its category feature (in MGs, category features are negative and selector features are positive, so the 0-occurrence still involves checking of a negative feature).
1. The $i$-th occurrence of *l* is the closest node that
    1. properly dominates the $(i-1)$-th occurrence of *l*, and
    1. can check the $i$-th licensee feature on *l* (i.e. the $i$-th negative movement feature).

This definition assumes that if a lexical item has multiple licensee features, they are linearly ordered to indicate in which order they must be checked.
There is an alternative definition for MGs with unordered licensee features, but for our discussion it won't matter either way because we can get away with assuming that no lexical item has more than one licensee feature.
So, feel free to stick with the intuitive notion, supplemented by whatever understanding you glean from the two examples below.

![]({static}/img/thomas/multiple_wh/der_simplewh_occurrences.svg)

![]({static}/img/thomas/multiple_wh/der_multiplewh_multifeatures_occurrences.svg)

The feature checking requirements of Merge and Move boil down to two simple constraints:

- **Full checking**: Every lexical item with exactly *n* negative features has exactly *n* occurrences.
- **SMC**: Every interior node is an occurrence for exactly one lexical item.

Yes, this looks different from how I described the SMC above, but it produces exactly the same tree language.
Consider the two derivations we saw earlier, one for simple wh-movement, the other for multiple wh-movement.
In the derivation with a single wh-movement step, both **Full checking** and **SMC** are satisfied:
each lexical item's number of occurrences matches the number of negative features it carries, and every interior node is an occurrence of exactly one lexical item.

In the illicit derivation with multiple wh-movement, however, only **Full checking** still holds whereas **SMC** is violated in multiple ways.
First, the lowest Move node is an occurrence for three separate lexical items because it is the closest Move node that properly dominates the 0-occurrences of those lexical items and can check wh~-~.
But because the lowest Move node sucks up all those extra occurrences, we also have the opposite problem: the two higher Move nodes aren't an occurrence for any lexical item at all, and as a result **SMC** is violated.
So **SMC** establishes a delicate balance where no node may have too many or too few occurrences.
The occurrence-based **SMC** looks very different from the Ghostbusters constraint, but the two are equivalent with respect to their derivational extension.

Alright, now that we can operate with the tree-geometric **SMC** constraint instead of the Ghostbusters constraint, we're only one modification away from handling multiple wh-movement.
The **SMC** condition is actually a shorthand for two separate constraints.

- **SMC (at least)**: Every interior node is an occurrence for at least one lexical item.
- **SMC (at most)**: Every interior node is an occurrence for at most one lexical item.

Suppose, then, that we drop **SMC (at most)**, leaving us only with the requirement that every Merge or Move node is an occurrence of at least one lexical item --- in other words, that it checks at least one negative feature.
In one important sense, this doesn't change much: the derivation tree language will still be regular, which is one of the three things the original SMC does for MGs.
The weakened version gets the job done just as well in this respect.
But with respect to multiple wh-movement, it completely changes things.

With the weakened SMC, we still can't have the multiple wh-movement derivation we had above because that one contains two Move nodes without any occurrences.
But what we can have is the configuration below:

![]({static}/img/thomas/multiple_wh/der_multiplewh_persistentfeature.svg)

This almost exactly the same except that *did* carries only one wh~+~ and hence there's only one Move node, which handles all three wh-movers at once.
The derivation is now well-formed because every interior node is an occurrence of at least one lexical item.
That a single node serves as multiple occurrences isn't a problem anymore because we dropped **SMC (at most)**.
Intuitively, you may think of this as the wh~+~ on *did* acting as a persistent licensor feature that can check any number of wh~-~ below it.
We could even parameterize it so that **SMC (at most)** is still active by default and only certain features on certain lexical items are exempt from it.
That way, we can allow for multiple wh-movement without allowing for, say, multiple subject movement --- although of course we would still need a theory of linguistic substance that explains to us why the latter never occurs even though it would be a simple parametric change.
But the goal here isn't to give an exhaustive analysis of multiple wh-movement, I merely want to show that multiple wh-movement isn't that big hurdle for MGs that it is commonly believed to be.


## A logical transduction for multiple wh-movement

We now have a variant of MGs that can strategically relax the SMC for some types of movement so that we can have derivations with multiple wh-movement, which we model as a persistent wh~+~ checking all wh~-~ below it --- or in tree-geometric terms, one Mode node serving as an occurrence for all wh-movers below it.
This takes care of the derivational challenges posed by multiple wh-movement, and in my not-so-humble opinion that is the key issue.
But of course it would be nice to know that this derivation can still be mapped to a derived structure.
The cool thing is, this doesn't even need any modifications on our part.

One particularly elegant view of movement is in terms of first-order transductions, which [you might remember from this post]({filename}/Tutorials/logicaltransductions_basics.md).
The idea here is that we define the relations that hold in the derived structure in terms of relations that hold in the derivation tree.
More concretely, we may treat movement as a first-order formula that reinterprets the derivation tree as a multi-dominance tree where the root of a phrase is connected to all the occurrences of its head.
Using $\triangleleft$ for immediate dominance in the derivation tree, we can define the immediate dominance relation $\blacktriangleleft$ in the output structure as follows:

$$
x \blacktriangleleft y \Leftrightarrow x \triangleleft y \vee \exists l [\text{occurrence}(x,l) \wedge \text{derivational-root}(y,l)]
$$

Or in plain English:

(@) Node *x* is a mother of node *y* in the derived multi-dominance tree iff one of the following holds:
    1. *x* is a mother of *y* in the derivation tree,
    2. *x* is an occurrence of some node *l*, and *y* is the root of the phrase projected by *l*.

This presupposes that we have first-order definitions of the predicates *occurrence* and *derivational-root*, which isn't too hard --- you can check @Graf11FG and @Graf12LACL for the precise formulas.

With the formula above, the derivation trees for simple and multiple wh-movement are mapped to the multi-dominance trees below.
You might notice that they look basically the same as the original derivation trees, except that movement arrows are now interpreted as immediate dominance arcs.

![]({static}/img/thomas/multiple_wh/der_simplewh_multidominance.svg)

![]({static}/img/thomas/multiple_wh/der_multiplewh_multidominance.svg)

The cool thing is that the first-order formula is independent of which version of the SMC is in place, it works equally well with both.
In fact, this is just the usual first-order transduction for standard MGs, with not a single thing changed about it.
Since the transduction hasn't changed at all, movement is still deterministic and regular: there is no ambiguity as to how we should connect movers to their landing sites, and doing so requires no new machinery.
The derivation tree languages are also still regular, as we saw above, so all three formal properties of MGs have been preserved while opening up the framework enough to handle multiple wh-movement.
Mission accomplished, multiple wh-movement handled (well, there's one more section coming, but let me gloat a bit for now).


## Linearization and c-command

The multi-dominance tree above probably looks weird to you because we have a node with more than two daughters.
That doesn't usually happen in Minimalism, and it does mean that multiple wh-movement still creates two problems for us: c-command and, by extension, linearization.
As is, all the movers c-command each other, which means that

1. they cannot be linearized according to the LCA, and
1. licensing between them should be unrestricted, e.g. for Principle A.

Now in an ideal world, it would turn out that multiple wh-movement affects c-command only with respect to phrases that are not part of the same cluster of multiple wh-movements.
In that case, we could basically patch our definition of c-command so that we ignore the mutual c-command relations (and only the mutual ones!) that are brought about by multiple wh-movement.
For our example derivation with multiple wh-movement, that would mean that we consider the wh-movement of *which book*, *who*, and *whom* with respect to other phrases so that they precede all the other lexical material, but then fall back to the base c-command linearizations between the three, giving us *who which book whom did give*.
If we instead wanted *which book who whom give*, then *which book* would first have to move to a position from where it c-commands the other wh-phrases, and only then does it partake in the multiple wh-movmeent.
From a mathematical perspective, this kind of "partially c-command transparent" movement would be an easy and maximally general addition to the definition of c-command that is well within the realms of first-order logic and works with any arbitrary number of wh-movers.

But that doesn't seem to be how things actually work.
[Omer Preminger mentioned that a while ago on this blog](https://outde.xyz/2021-03-30/handbook-chapter-on-minimalism-and-computational-linguistics.html#comment-1), citing work by Norvin Richards (if the link doesn't take you right to his comment: it's the one at the very top).
~~Multiple wh-movement seems to behave more like scrambling in that you can have any arbitrary order (modulo a few restrictions), and the c-command relations match that observed order.~~
{{{*Edit*: This characterization is overly simplified, and placing it right after the reference to Omer's comment suggests that it is his mischaracterization when it is in fact me that's being sloppy.
Here's the full quote:

> For Bulgarian: leftmost one must be the one whose highest-position-prior-to-wh-movement is highest. Order amongst the others is free.

I interpret this as a kind of two-class system, where we get to single out a finite number of wh-movers for the front positions, and the remaining wh-phrases, of which there can be an unbounded number, may show up in any arbitrary order.}}}
So we need to be able to get any random permutation of any arbitrary number of wh-movers, and we can't get that by starting with a fixed hierarchy and moving stuff around.
We could make the transduction non-deterministic, but that's a major step from a formal perspective, and more importantly, I think it's the less insightful route.

Keep in mind, with multiple wh-movement we're generalizing from a fairly small number of movers to an unbounded number, and whenever you do that, there is a risk that your generalization is off target.
Suppose, for instance, that multiple wh-movement works more like this: you get to single out three wh-phrases that go to the front, everything else is ordered by a complex metric that considers base c-command, morphological case, animacy, and prosody.
Does any of the available data rule out this option?
Probably not, because you'd need at least five movers to have a potential counterexample, and that's already more than you find in the wild.
If we assume that only one wh-phrase can be singled out, like in Bulgarian, then examples with two or three multiple wh-movers become more informative, and then we could test if something like this multi-variable metric fits the data.

To the best of my knowledge --- which is admittedly very limited in that empirical domain --- nobody has done that.
I don't blame them.
From a Minimalist perspective, it is the multi-variable metric that would be weird and convoluted, whereas a purely movement-based approach is enough for the observed data because there's no SMC to muck things up.
It is only from the computational perspective that you suddenly wonder whether there are any substance-based confounds in the data and how one could tease those out given the limits of performance.
It is a tricky issue, but I think it is one worth pursuing because it really changes what the key issues are about multiple wh-movement:

1. Multiple wh-movement is not special.
   In a formal sense, it is standard movement that is special because it requires us to rule out cases where a Move node is an occurrence for multiple lexical items.
   We don't need elaborate accounts to explain the existence of multiple wh-movement.
1. Multiple wh-movement is very special.
   In full generality, it constitutes an unrestricted system for creating c-command relations and linearizations.
   This makes it similar to scrambling, which has also proven a tough nut to crack.
   Just as with scrambling, there might be computationally meaningful restrictions that we've missed because we haven't looked at the data through this lens.

## The tl;dr for a very long post

In sum, the issue of multiple wh-movement is far from settled.
The received view that MGs can't handle multiple wh-movement only holds with respect to a very strong SMC, which isn't all that integral to the MG framework.
With a relaxed SMC, MGs can handle multiple wh-movement as long as there are additional restrictions on how c-command and linearization work for the wh-phrases.
The big empirical question is whether such restrictions can be found, and that would make for a wonderful joint project for theoretical and computational linguists.

## References
