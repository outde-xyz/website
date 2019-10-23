---
title: >-
    Locality, suppletion, and cognitive parallelism
authors:
    - Thomas Graf
date: 2019-10-23
bibliography: references.bib
tags:
    - suppletion
    - locality
    - prosody
    - subregular
    - syntax
---

<!-- START_SUMMARY_BLOCK -->
Oh boy, this month is killing me.
I know I promised you one more detailed discussion of subregular complexity before we finally get back to the topic that started it all, [Omer Preminger's post on listedness](https://omer.lingsite.org/blogpost-listemes-and-morphemes-and-other-things/).
But in the interest of time I'll merge those two posts into one.
That means some points will be a bit more hazy than I'd like, but I think it will work just fine nevertheless (and for those of you sick of this series of posts, we'll get to something new sooner).
Alright, with that out of the way, here's the basic question: why aren't PF and LF more alike?
<!-- END_SUMMARY_BLOCK -->


## Recap: What's our machinery capable of?

Just as a reminder (I know, it's been a while), we have a few pieces of subregular machinery for syntax that model different kinds of locality.
One is the [tree tier approach]({filename}locality_merge_move.md).
This one starts out with a suitable tree structure, e.g. MG dependency trees, and then projects various tree tiers from that structure.
Each tier is subject to strictly local constraints, but since the tier is itself a condensed representation of the whole tree, this model gives us a particular kind of relativized locality.
The other approach looks at a node's [string of c-commanders]({filename}locality_constraints.md) and restricts that with constraints in the same way that phonotactic constraints may restrict the shape of words.
This string-based representation is blind to lots of structural aspects of the tree --- for any given node, it only looks at its c-commanders.
But it gets to reason about the well-formedness of these strings with more sophisticated machinery, e.g.~IOTSL, which is the upper bound of what seems to be needed in phonology.

This string-based model can actually be understood as a special case of a more general piece of machinery, which is the part we're **not** going to talk much about here because of time constraints.
If you want all the gory details, check out [this fairly technical MOL paper I wrote with Aniello De Santo](https://www.aclweb.org/anthology/W19-5702/).
We only need the very basic intuition for our LF/PF discussion, and that basic intuition is basically pretty basic in as basic a way as basically possible.

We know that parsing involves some kind of top-down component, so we can ask ourselves what syntactic constraints would have to look like in order to be easily verified during top-down parsing.
One particular formalization of that is what's called a **sensing tree automaton**.
This is a machine that has finitely many states, and its job is to assign each node a state, proceeding in a top-down fashion.
There are two central restrictions.
First, the machine has to be deterministic --- it cannot make an educated guess about what a subtree may look like and then backtrack if that guess turns out to be wrong.
Second, what state is assigned to a node *n* can only depend on the state of its mother, the labels of its sisters, and the label of *n* itself.

It's all a fair bit more abstract than the subregular notions we have encountered so far, but one central corolloary of these properties is that sensing tree automata cannot synchronize information between distinct subtrees.
If A and B are two subtrees such that neither one contains the other, then none of A's internals beyond its root can be used in the state-assignment of B.
And the same hold in the other direction: only the root of B can affect the assignment of A and any nodes below it.
If two nodes aren't related by dominance, siblinghood, or c-command, they are informationally insulated from each other.

It's as if the automaton has a large army of minions scouring the tree for ill-formedness.
At each branching node the automaton splits its minions into separate groups, one for each subtree. 
At this point, the groups can still see each other, and they can see the starting points of the individual subtrees (i.e. their roots).
But then each group start drilling into its respective subtree.
In doing so, it may learn a lot about its assigned subtree, but now it has also lost contact with the previous groups.
They don't have walkie talkies or telepathy or messenger pigeons to communicate.
So no group can tell the other what it has found out about its own subtree.

This kind of "subtree insulation" is a welcome property for syntax --- sensing tree automata seem to be about as complex as it gets.
In particular, we do not find constraints that hold between completely unrelated parts of the tree, which is exactly what sensing tree automata cannot do.
Whenever it looks like some node N deeply embedded in subtree A has some effect on a node N' deeply embedded in subtree B, it usually turns out that the structure is wrong.
For instance, there might be evidence for N moving to a position that c-commands N'.
If one assumes that sensing tree automata provide an upper bound on the complexity of syntactic dependencies, then the non-existence of such cross-subtree constraints follows for free.
And sensing tree automata are a reasonable upper bound because it looks like they can handle all the things a syntactician would want: subcategorization, agreement, adjunction, licensing conditions, island constraints, and so on.
For syntax proper, sensing tree automata are a good upper bound.
One we start looking at the interfaces of PF and LF, things get more complicated.
That would be fine, except they get complicated in a very lopsided manner.


## PF, LF, and suppletion (~ listedness)

So far we have only been talking about locality and subregular complexity for constraints, but we can extend this view to mappings between structures.
In particular, we can look at the mapping from syntax to PF and the mapping from syntax to LF.

The first question we may ask is whether there are aspects of these mappings that are strictly local in the sense of the subregular class SL.
That is to say, are there cases where the PF or LF realization of some node depends only on its surrounding context of finitely bounded size.
Why yes, and it's actually a notable point of parallelism between PF and LF:

1. PF inserts morphemes based on the structural context, and this insertion may be suppletic.
1. LF inserts meanings based on the structural context, and this insertion may be idiomatic.

Cool, both pipelines have some SL aspects, that's nifty.
Well, yeah, not quite.

When you look closer, there's a pronounced difference between PF suppletion and LF suppletion.
PF suppletion is a lot less idiosyncratic than LF suppletion, i.e. idioms.
For instance, there is no morphological counterpart to *kick the bucket* that requires the past tense of *kick* to be *kack* when it selects *bucket*, but in no other case.
Um, why?

Here's one conceivable yet faulty answer.
Perhaps LF suppletion is less local than PF suppletion?
Assume that we have the usual DP analysis where a determiner selects a noun, rather than the other way round.
Maybe LF gets to look past the determiner to also take the noun into account when determining the meaning of *kick*.
PF, on the other hand, is more local and can only see the determiner.
Okay, but then we should still get PF suppletion based on the determiner.
Are there any languages where a verb has a suppletive form based on the determiner of its argument?
I don't think so, although there are adjectives that inflect differently based on definiteness.
But that's exactly the thing: different inflection, no full suppletion.
PF can be sensitive to quite a bit of context and then instantiate that via various inflectional markers, it is just PF suppletion that doesn't get to do that.
Odd, very odd.

Now perhaps that's just due to what we count as PF suppletion.
If you believe *kill* is underlyingly *cause to die*, then PF suppletion works just like LF suppletion.
Just like *kick the bucket* LF-maps to *die* but *kick the can* doesn't, *cause to die* would PF-map to *kill* yet *cause to cry* would not.
I'm not the biggest fan of such decompositions.
Sure, I gladly jumped at it for *most* to [make my subregular semantics work]({filename}/Discussions/2019-07-26_graf_kiss_semantics.md), but let's not make a habit of it.
The cases still don't seem exactly analogous to me, because the PF-mapping is much more systematic.
There is a transparent connection between *cause to die* and *kill*, but mapping *kick the bucket* to *die* is completely arbitrary.
The basic point stands: even if the mapping from syntax to LF and from syntax to PF both have SL components, the PF side displays more systematicity.

So that might suggest that PF is more limited than LF.
But from a subregular perspective, the opposite seems to hold: PF gets to do quite a few things that are more complex than what we see in syntax, and also more complex than what we see at LF.


## The excessive complexity of PF

One job of PF is, presumably, to ensure prosodic well-formedness.
This is surprisingly hard, apparently harder than anything in syntax proper.
Now of course this depends a lot on one's assumptions about prosody.
For the sake of argument, let's take a particularly simplistic model because that's already plenty hard.

Suppose that all our trees are strictly binary branching and we have to annotate sisters with W (weak) or S (strong) depending on which subtree contains the carrier of primary stress.
In the linguistic literature W and S are usually treated as diacritics of unclear ontological status, but we may just as well think of them as automaton states for our purposes.
By default, stress goes in the direction of embedding, i.e. towards the complement.
So we always want to assign S to complements.
At the end, primary stress must be on the unique node that is reflexively dominated only by nodes that carry S.
In other words, primary stress falls on the very end of an uninterrupted S-path.

So far, so good.
A sensing tree automaton could handle that.
Even if you start at the root of the tree and move towards the leaves, it isn't very hard to figure out whether the complement of the current head is in the left or the right subtree.
If you know where the complement is, you know where S and W should go, so you can make sure that primary stress is exactly where it's supposed to be.
Default stress, then, stays within the reach of sensing tree automaton, and thus below the upper complexity bound we have identified for syntax.

But now consider a more complicated case, the interaction of prosody and focus.
If you focus an element, the default path for stress must be adjusted so that it passes through this element, yielding contrastive stress. 

(@) The old man likes the **girl**. (default stress)
(@) The old **man**~F~ likes the girl. (contrastive stress, focus on *man*)
(@) The [old **man**]~F~ likes the girl. (contrastive stress, focus on *old man*)

Suppose that ~F~ in the example above isn't just a descriptive device but an actual feature that can be attached to nodes in the tree (it could also be a functional head, but that's gonna make things slightly harder to work through).
Then we can rephrase primary stress assignment as follows:

1. If there is a node with a focus feature, it must appear along an uninterrupted S-path from the root to the carrier of primary stress.
1. Otherwise, primary stress must fall on the carrier of default stress.

A sensing tree automaton cannot do that.
Suppose you have two siblings X and Y and you have to decided which one gets W or S.
Even if you know that Y is the complement, this doesn't help you because you do not know whether X contains a focus feature.
If it does, then primary stress is illicit in Y.
But the only way to figure out if X contains a focus marker is to drill deep into it.
Once the automaton starts digging deeper into X, it cannot use its findings for processing Y because subtrees are informationally insulated for sensing tree automata.
The potential presence of a focus marker introduces an element of non-determinism that cannot be handled by sensing tree automata.
All of a sudden, PF goes beyond what we need for syntax.

And is if this wasn't bad enough, the description above is actually incomplete because it ignores Focus Economy: contrastive stress is only allowed if the constituent could not have been focused using default stress.
So, wow, PF really doesn't pull any punches.

I can't think of anything LF-related that requires this kind of coordination across different subtrees.
Maybe it's my underdeveloped semantics background, maybe it's because LF has been integrated much more tightly with syntax than PF has.
Either way, LF strikes me as pretty harmless by comparison.

## So what do we make of this?

We could quibble quite a bit about the specifics of the prosody example, but I think there's several take-home messages here.

1. The LF side seems to be much simpler than PF when we look at subregular complexity.
   At the same time, LF suppletion (i.e. idioms) is much more idiosyncratic than PF suppletion. 
   So perhaps LF is less complex, but more complicated?

1. We actually don't know enough about PF or LF to make any firm claims here.
   Maybe the [mapping from syntax to LF is a lot messier than semanticists have told us](https://omer.lingsite.org/blogpost-meaning-contrasts-generated-or-parasitic/).
   Maybe prosody is straight-forward once you have the right theory.
   I think subregular complexity is a very valuable perspective here.
   It tells us:
   "Look, this is the approximate ballpark of complexity for phonology, morphology, syntax.
    Ideally, we would like to stay within those bounds.
    If there's phenomena where we can't, that's really noteworthy and we should study those very carefully."

1. The extraordinary status of PF might give some belated validation to Omer Preminger.
   He has been claiming for a long time that the interfaces are in some sense more powerful than syntax.
   I've argued for the very opposite because of a specific formal property:
   every regular tree constraint over LF/PF structures can be reduced to a regular tree constraint over derivation trees or dependency trees, but the opposite is not true.
   Syntax can do things with regular constraints that cannot be done with regular constraints at the interfaces.

   The discussion here adds a new layer to this:
   The additional power of syntax relative to the interfaces only holds when you consider the full class of regular tree constraints, which is way too big.
   Once you move into subregular complexity, things get more complicated.
   Now, the interfaces may involve phenomena that would be regular in syntax, but do not fit into the subregular classes that we need for syntax proper.
   The interfaces are, perhaps, more complex after all.

Alright, this marks the end of our overly long journey into the land of subregular complexity.
It's good I got to cover some of the basics, in future posts I might just link back to the relevant parts.
But the next few posts will go in a very different direction, simply because I find myself craving some less technical fare.
