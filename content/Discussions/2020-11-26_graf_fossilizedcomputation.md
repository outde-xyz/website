---
title: >-
    Representations as fossilized computation
authors:
    - Thomas Graf
date: 2020-11-26
bibliography: references.bib
tags:
    - syntax
    - morphology
    - representations
    - features
    - category features
    - selection
    - subregular
    - logical transductions
---

<!-- START_SUMMARY_BLOCK -->
Okay, show of hands, who still remembers my [post on logical transductions from two weeks ago](fixme)?
Everyone?
Wonderful, then let's dive into an issue that I've been thinking about for a while now.
In the post on logical transductions, we saw that the process of rewriting one structure as another can itself be encoded as a structure.
Something that we intuitively think of in dynamic terms as a process has been converted into a static representation, like a piece of fossilized computation.
Once we look at representations as fossilized computations, the question becomes: what kind of computational fossils are linguistic representations?
<!-- END_SUMMARY_BLOCK -->


## The problem with category features

Let's start with a concrete example that I think I've got figured out.
The example will make it clearer why it is important to study representations as fossilized computations.

Some of you might be familiar with my Casandra-like theatrics when it comes to category features.
Category features allow you to trick c-selection into doing all kinds of linguistically unsavory things for you.
Suppose we have a language where the only category features are *O* and *E*.
Spoiler: those are short for *odd* and *even*, and that's the problem.
Now suppose that the language obeys the following rules:

1.  Every head has exactly one category feature.
1.  If a head takes no arguments, its category feature is *O*.
1.  If a head takes exactly one argument, then 
    1.  the head's category feature is *E* if the argument has category feature *O*;
    1.  the head's category feature is *O* if the argument has category feature *E*.
1.  If a head takes exactly two arguments, then
    1.  the head's category feature is *E* if the two arguments have distinct category features;
    1.  the head's category feature is *O* if the two arguments have the same category feature.
1.  All sentences are OPs.

These rules can be easily lexicalized in a manner that's fairly innocuous from a linguistic perspective.
Just like we may say that *show* is an N that selects nothing or a V that selects two D-heads or a D-head and a P-head, we may say that *show* is either an *O* or an *E* and that its subcategorization frame depends on the choice of category.
So *a priori* there isn't anything linguistically suspect about this.
Yet the resulting system is one that's highly unnatural: if all those rules are followed, then we can only build syntactic structures that contain an odd number of lexical items.

Here's two dependency trees to illustrate how this works.

figure: fixme

We're abusing category features as an information buffer that stores how many lexical item a subtree contains.
C-selection then carries out a simple even/odd calculus.
For instance, if a head *H* has two arguments, one of which is *O* and one is *E*, then the number of lexical items in the subtree rooted in *H* must be *O + E + H = odd + even + 1 = even = E*.
Everything here is local or lexicalized.
We're doing nothing special with the grammatical machinery, yet the result is very far from what we want.

This is just the tip of the iceberg.
A huge class of constraints can be made local in this manner, including even transderivational constraints.
In fact, all constraints in the syntactic literature can be pushed into the category system.
More troublingly, this also holds for insane variations of natural constraints, e.g. that island constraints are enforced iff 1) the size of the mover is less than 17 and either 2.1) there are at least 4 instances of movement in the tree, or 2.2) the number of violated island constraints is a multiple of 2 if the tree contains a deverbal noun, and a multiple of 5 otherwise.
Given this kind of insanity, it's no longer too shocking that we can also retool c-selection as a means for feature percolation, which in turn allows us to replace many instances of movement with a base merge mechanism that's no longer subject to island constrains.
It's overgeneration galore.

Most linguists I show this agree that this isn't desirable, but they also have an easy solution: the category system is only allowed to contain the familiar categories V, N, A, P, T, C, and so on.
I'm not a fan of this.
First of all, substantive universals aren't all that satisfying, in particular if they're just a list with no internal structure.
Second, I don't believe that this actually works.
Once you get down into the nitty-gritty, the number of categories you need really blows up.
Not all adjectives are alike, for instance:

(@) the ugly president
(@) the alleged president
(@) The president is ugly.
(@) \*The president is alleged.

There's many subtle differences of this kind, and since these differences can interact you end up with combinatorial explosion, which means the number of categories quickly gets very large.
Now you might say we can keep the standard category system and do everything else with constraints, but that's exactly the thing: constraints are computation, and categories are fossilized computation.

The odd-even system above is just a fossilized computation of odd-even counting.
The insane constraint I mentioned above can be pushed into c-selection because there is a particular way of fossilizing its computation.
First we translate the constraint into a finite-state tree automaton, and then we record how this automaton can transition from one state configuration into another.
We then choose our categories and c-selection rules in such a way that they mimic these state transitions.
If you want all the details, [check out @Graf17Glossa](fixme), which is a more accessible version of @Graf11LACL and @Kobele11.

The bottom line is this: there is a principled way to fossilize computations into the category system.
That's why we can trick categories and c-selection into doing stuff nobody wants them to do, giving us overgeneration galore.
Short of stipulating a fixed set of categories, which is inflexible and unsatisfying, there isn't a good way of preventing this because we have no good way of telling a natural category system from an unnatural one.


## How to fix category features by fixing representations

For the longest time my solution to the issue above was to completely abandon the very notion of category features.
Everything should be done with constraints because with constraints we have well-defined notions of complexity that we can use to separate the natural from the unnatural.
But this was both too radical and, which I have realized only now, not radical enough.
It is too radical because categories are a fundamental component of all syntactic theories, ripping them out is gonna make things more complicated to work with.
And it is not radical enough because it doesn't plug the real loop hole: representations.

At the end of the day, language is about computation.
The computation is factored into two components, which are the representation and the constraints/operations that apply to this representation.
The dichotomy of category features and constraints shows that this is not a hard separation, we can take constraints and push them into the representation.
But representations are a black hole because there is no systematic way of measuring the complexity of a representation.
At least that's what I thought, until I started to think of representations as fossilized computations.
Once you make that shift in perspective, the issue is trivial: in order to measure the complexity of a representation, we can measure the complexity of the fossilization computation that converts computation into representation.

In the limited case of category features, this is easy enough to figure out.
Suppose we start out with a representation that lacks all features related to c-selection, so at the very least category features, and possibly selector features if that's how you encode c-selection.
In this scenario, how hard would it be to correctly annotate each lexical item with is category features (and selector features)?
This is sketched in the figure below (dependency trees are used merely for convenience, the basic idea applies to any kind of representation).

figure: fixme

The process isn't trivial because one lexical item could be annotated in various ways, as in the case of *show* that I mentioned earlier.
But natural languages seem to use category systems that minimize this indeterminacy.
As far as I can tell, the category of a lexical item can be reliable inferred from its local context in the tree.
I'm not quite sure how large the context is that needs to be considered --- that's an interesting empirical question, one that I hope to take a crack at soon.
But whatever the exact bound is, there is some finite upper bound on the size of the context, and in technical terms this means that natural languages use category systems that are strictly $k$-local.[^DM]
The [details can be found in @Graf20SCiL](fixme), the first half of which is actually meant to be accessible to a general audience and can be read in less than 20 minutes (just ignore the second half).
But details don't matter here.
Just remember that being strictly $k$-local means being computationally simple, so category systems that are natural are also computationally simple.

Now compare that to the *odd-even* system.
Here, there is no upper bound on the context.
In order to determine whether a head should get *O* or *E*, I have to know whether its subtree contains an odd or an even number of nodes.
But the only way to do that is to look at the entire subtree.
Since there is no upper bound on how large a subtree may be, this is not a strictly local problem.
In fact, even first-order logic can't assign the correct category features.
You need monadic second-order logic to get going, marking this as a very complex category system.

And this makes me happy; we no longer need to stipulate a fixed set of categories or rely on fuzzy criteria of why a given category system is or is not natural.
Instead, we have a rigorous procedure for measuring the complexity of category systems: we "defossilize" computation by ripping it out of the representation and asking how difficult it would be to put it back in.
And the procedure seems to be on the right track because what we find in natural language looks very reasonable from this perspective.


## Another example: Morphology

The "defossilization" strategy can be easily applied to other domains.
Here's an example from morphology.

There's many ways one may think about morphology.
In the item-and-arrangement tradition, we may posit an underlying representation with stems and abstract morphemes in the correct positions.
This underlying representation is then rewritten as a surface form.

figure: fixme

But where does this underlying representation come from?
How come all the morphemes are in the correct order?
Well, we can ask how hard it would be to construct this representation.
For the sake of argument, suppose that we start out with a derivation (don't worry, we'll also look at how we could get that representation):

figure: fixme

Rewriting the derivation as the underlying representation isn't all that hard as long as we know the general order of affixes in the language.

1. We do a first past of the derivation from left to right, checking if it contains a prefix that must always be initial.
   If we find this prefix, we add it as the first part of our underlying representation.
1. Once we reach the end of the derivation, no matter whether we found the affix, we go back to the beginning of the derivation and do another pass.
   This time we're looking for the next prefix, something that can occur in first or second position of the underlying representation.
   If we find it, we add it to the representation.
1. We continue this doing left-to-right pass after left-to-right pass, until we're done with prefixes.
   Then we do a pass looking for the stem.
   After that, we start doing passes looking for suffixes.

There's some hiccups to take care of when we don't have a fixed linear order of affixes.
For instance, a derivational suffix that converts verbs to nouns and another one that converts nouns to verbs could alternate in the string.
But in that case they'd also alternate in the derivation, so I think this can still be made to work.
If so, that's interesting because it would mean that underlying representations can be obtained from derivations by a **2-way finite-state transduction**.
And @DolatianHeinz20 have argued recently that [2-way finite-state transducers provide a good fit for morphology](fixme).
So the difference between an item-and-arrangement view with underlying representations and an item-and-process view with derivations is just a single transduction  of a complexity class that we might need anyways for morphology.

Ah, but now you wonder where the derivation is from.
We don't have to take that as a primitive either.
We can just start with a stem as the input, and have that non-deterministically rewritten as a derivation.
As far as I can tell, this can be done by a non-deterministic 1-way finite-state transducer with epsilon-transitions (holy jargon, Batman).
The non-determinism is only needed to choose between the many different derivations that are available for any given stem.
Given a fixed choice, the transducer would be deterministic.
Again, I haven't completely worked through this, but it seems to me that this is a very generous upper bound and we could actually make do with way less power, getting us into the range of transductions that @DolatianHeinz20 identify.

If all of that is on the right track, we can bootstrap morphological representations from nothing but the stem.
And doing so doesn't really change the complexity picture because we're staying within classes we would need anyway.
Morphological representations can be completely defossilized, turning them into pure, pristine computation.


## So much work left to be done

At this point I'm sure you're all very eager to do some defossilization of your own, so here's a list of hot button issues that still need to be solved:

1. **Movement features**  
   That's the big one.
   In Minimalist grammars, half of movement is actually figuring out what movement features to put where.
   Should this wh-phrase get to move, or this one?
   Movement features fossilize a lot of computation that syntacticians deeply care about, e.g. relativized minimality.
   We want to have a good idea of how these computations work.
   This might also provide us with new explanations as to why these conditions on movement should hold in the first place.

1. **Compounds**  
   I gave you such a nice picture of morphology, but unfortunately it only works if we ignore compounds.
   Follow the procedure above for a derivation with multiple stems that each carry their own affixes, and you're in trouble.
   And with compounds, there seems to be no way around tree structures, which takes me to the next point.

1. **Defossilizing trees**  
   Morphological representations can be summoned out of thin air with nothing but the stem as input.
   But with trees, things are tricky.
   What should be the input?
   A numeration with all lexical items?
   There's tons of ways to combine those, yielding vastly different trees.
   And do those lexical items get to carry features?
   Perhaps an LF-string would be a better input, and then we have to reverse engineer that into a tree.
   But that's basically parsing, and the reason parsing is studied with parsers rather than transducers is because we have no model of string-to-tree transductions that fits the automata-theoretic view.
   Yeah, trees are tricky, and I'm not sure what to do with them.

1. **Autosegmental structure**  
   There has been lots of work recently on the subregular complexity of autosegmental phonology, driven mostly by Adam Jardine and his group at Rutgers.
   Here, too, we would like to know what kind of computational fossils these additional structures are.
   Even though graphs might seem more complex than trees, I think this problem is actually easier.
   The simplest case of autosegmental structures is TSL, where it is obvious that the tier is the result of a strictly 1-local transduction.
   Making this transduction more complex yields more powerful extensions of TSL.
   The autosegmental structures I have seen so far also seem local in a specific way, all we need at this point is a formal model of strictly local string-to-graph transduction.
   Once we have that, I think it will fit the bill just fine.

As you can see, plenty of work for the interested researcher.
I think this is a very useful perspective, and one that really gets us closer to issues linguists care about.
There's been many linguistic issues that I couldn't address in a satisfying manner because the representations provided too many loopholes.
Defossilization gives us a firm grip on representations, and that's what we really need at this point.
Subregular complexity has allowed us to tighten the constraint space, now we have to rein in representations.


## References

[^DM]: Things work slightly different if you think in terms of Distributed Morphology.
       In that case, we start out with a reduced tree that only contains the roots, and we have to figure out what functional material to insert above those roots.
       I believe that this does not change the strictly local nature of category systems in natural languages, but it might affect how much context you need to take into account.
       For instance, if you're an old school Minimalist and your syntactic structure includes fully inflected lexical items, then you don't need any context to figure out that *waters* is a verb, not a noun.
       If all you have is an uninflected root, you need to dig a bit deeper.
