---
title: >-
    Representations as fossilized computation
authors:
    - Thomas Graf
date: 2020-11-30
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
Okay, show of hands, who still remembers my [post on logical transductions from over a month ago]({filename}/Tutorials/logicaltransductions_basics.md)?
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
Just like we may say that *show* is an N that selects nothing, or a V that selects two D-heads or a D-head and a P-head, we may say that *show* is either an *O* or an *E* and that its subcategorization frame depends on the choice of category.
So *a priori* there isn't anything linguistically suspect about this.
Yet the resulting system is one that's highly unnatural: if all those rules are followed, then we can only build syntactic structures that contain an odd number of lexical items.

Here's two simple dependency trees to illustrate how this works.
Each head's category is listed in parenthesis.
The left tree is an OP, whereas the right one is an EP and thus illicit.
That's not something we want our formalism to do because, well, languages don't do it.

![Only trees with an odd number of lexical items are OPs]({static}/img/thomas/representation_fossils/deptree_even_odd.svg)

We're abusing category features as an information buffer that stores how many lexical item a subtree contains.
C-selection then carries out a simple even/odd calculus.
For instance, if a head *H* has two arguments, one of which is *O* and one is *E*, then the number of lexical items in the subtree rooted in *H* must be *O + E + H = odd + even + 1 = even = E*.
Everything here is strictly local or lexicalized.
We're doing nothing special with the grammatical machinery, yet the result is unlike anything we find in language.

This is just the tip of the iceberg.
A huge class of constraints can be made local in this manner, including even transderivational constraints.
Virtually all constraints in the syntactic literature can be pushed into the category system.
More troublingly, this also holds for insane variations of natural constraints, e.g. a constraint that's exactly like the Adjunct Island constraints except that it is enforced iff 1) the size of the mover is less than 17 and either 2.1) there are at least 4 instances of movement in the whole tree, or 2.2) the number of violated island constraints is a multiple of 2 if the tree contains a deverbal noun, and a multiple of 5 otherwise.
Given this kind of insanity, it's no longer too shocking that we can also retool c-selection as a means for feature percolation, which in turn allows us to replace many instances of movement with a base merge mechanism that's no longer subject to island constraints.
It's overgeneration galore.

Most linguists I show this to agree that it isn't desirable, but they also have an easy solution: the category system is only allowed to contain the familiar categories V, N, A, P, T, C, and so on.
I am, to put it politely, not a fan.
First of all, substantive universals aren't all that satisfying, in particular if they're just a list with no internal structure or regularities.
Second, I don't believe that this actually works.
Once you get down to the nitty-gritty, the number of categories you need really blows up.
Not all adjectives are alike, for instance:

(@) the ugly president
(@) the alleged president
(@) The president is ugly.
(@) \*The president is alleged.

There's many subtle differences of this kind, and since these differences can interact you end up with combinatorial explosion, which means the number of categories quickly gets very large.
Now you might say we can keep the standard category system and do everything else with constraints, but that's exactly the thing: constraints are computation, and categories are fossilized computation.
You're not really changing what's going on, you're only changing what you bake into the representation.

The odd-even system above is just a fossilized computation of odd-even counting.
The insane island constraint above can be pushed into c-selection because there is a particular way of fossilizing its computation.
First we translate the constraint into a finite-state tree automaton, and then we record how this automaton can transition from one state configuration into another.
We then choose our categories and c-selection rules in such a way that they mimic these state transitions.
If you want all the details, [check out @Graf17Glossa](https://www.glossa-journal.org/articles/abstract/10.5334/gjgl.212/), which is a more accessible version of @Graf11LACL and @Kobele11.

The bottom line is this: there is a principled way to fossilize computations into the category system.
That's why we can trick categories and c-selection into doing stuff nobody wants them to do, giving us overgeneration galore.
Short of stipulating a fixed set of categories, which is inflexible and unsatisfying, there isn't a good way of preventing this because we have no good way of telling a natural category system from an unnatural one.


## Wanna fix category features? Fix your representations!

For the longest time my solution to the issue above was to completely abandon the very notion of category features.
Everything should be done with constraints because constraints give us well-defined notions of complexity that we can use to separate the natural from the unnatural.
But this was both too radical and --- which I have realized only now --- not radical enough.
It is too radical because categories are a fundamental component of all syntactic theories, ripping them out is gonna make things more complicated to work with.
And it is not radical enough because it doesn't plug the real loop hole: representations.

At the end of the day, language is about computation.
The computation is factored into two components, which are the representation and the constraints/operations that apply to this representation.
The dichotomy of category features and constraints shows that this is not a hard separation, we can take constraints and push them into the representation.
But representations are a black hole: there is no systematic way of measuring the complexity of a representation.
At least that's what I thought, until I started to think of representations as fossilized computations.
Once you make that shift in perspective, the issue is trivial.
In order to measure the complexity of a representation, we can measure the complexity of the fossilization computation that converts computation into representation.

In the limited case of category features, this is easy enough to figure out.
Suppose we start out with a representation that lacks all features related to c-selection, so at the very least category features, and possibly selector features if that's how you encode c-selection.
In this scenario, how hard would it be to correctly annotate each lexical item with is category features (and selector features)?
This is sketched in the figure below (dependency trees are used merely for convenience, the basic idea applies to any kind of representation).

![Measuring the complexity of category systems via defossilization]({static}/img/thomas/representation_fossils/defossilization.svg)

The process isn't trivial because one lexical item could be annotated in various ways, as in the case of *show* that I mentioned earlier.
But natural languages seem to use category systems that minimize this indeterminacy.
As far as I can tell, the category of a lexical item can be reliable inferred from its local context in the tree.
I'm not quite sure how large the context is that needs to be considered --- that's an interesting empirical question, one that I hope to take a crack at soon.
But whatever the exact bound is, there is some finite upper bound on the size of the context, and in technical terms this means that natural languages use category systems that are strictly $k$-local.[^DM]
More precisely, their category systems are **input strictly local** because we only need to consider the context in the input representation that we are adding category features to.
The details can be found in @Graf20SCiL ([pdf here](https://scholarworks.umass.edu/scil/vol3/iss1/35/)), the first half of which is actually meant to be accessible to a general audience and can be read in less than 20 minutes (just ignore the second half).
But details don't matter here.
Just remember: category systems of natural languages are input strictly local.

Now compare that to the *odd-even* system.
Here, there is no upper bound on the context.
In order to determine whether a head should get *O* or *E*, I have to know whether its subtree contains an odd or an even number of nodes.
There's two ways to do that.

1. We can look at the entire subtree.
   Since there is no upper bound on how large a subtree may be, this is not strictly local.
   In fact, even first-order logic can't assign the correct category features.
   You need monadic second-order logic to get going, marking this as a very complex category system.
1. Alternatively, we can process the tree bottom-up, adding category features as we go.
   In this case, determining the category of a head only requires us to look at the category features of its arguments.
   This is strictly local because we only need to consider a context of bounded size.
   But the context is different: now we have to look at the output we are producing, rather than the input tree without category features.
   This is **output strictly local**.

Whichever route we take, the odd/even system is now formally distinct from the category systems we find in natural languages.
And this makes me happy; we no longer need to stipulate a fixed set of categories or rely on fuzzy criteria of why a given category system is or is not natural.
Instead, we have a rigorous procedure for measuring the complexity of category systems: we "defossilize" computation by ripping it out of the representation, and then we check how difficult it would be to put it back in.
While the procedure may seem odd at first, I find it very encouraging that what we find in natural language looks very reasonable from this perspective.


## Another example: Morphology

The "defossilization" strategy can be easily applied to other domains.
Here's an example from morphology.

There's many ways one may think about morphology.
In the item-and-arrangement tradition, we may posit an underlying representation with stems and abstract morphemes in the correct positions.
This underlying representation is then rewritten as a surface form.
Here is an example from Krongo (Kadugli; Sudan) [that I took from WALS](https://wals.info/chapter/51).

(@) **Underlying representation**: Instr-baton  
    **Surface form**: á-kÙUfi  

But where does this underlying representation come from?
How come that the case affix appears correctly before the stem?
Looks like our representation already contains some fossilized computation.
Let's see, then, how hard it would be to construct this representation.

First we might ask how hard it is to get the underlying representation from the derivational history, where case is added to the stem later on.
This is basically an item-and-process view of morphology.

(@) **Derivation**: baton-Instr

Switching the order of these two guys is input strictly local.
But this is a pretty simple case.
Let's consider a more complicated scenario.

Suppose our language allows for recursive prefixation and suffixation, and that the two can depend on each other.
For example, a prefix *foo-* turns verbs into nouns, and a suffix *-bar* turns nouns into verbs.
So you could have something like

(@) **Underlying representation**: foo-[[foo-[[foo-go]-bar]]-bar]*

Yet the derivation for this would be as follows:

(@) **Derivation**: go-foo-bar-foo-bar-foo

How hard is it to compute the underlying representation from this derivation?
Not too difficult, actually.
I won't go into details here, but this can be done with a transduction definable in first-order logic (go ahead, give it a try, it's not too difficult).
This entails that it can be computed by a **2-way finite-state transducer**, and Hossep Dolatian and Jeffrey Heinz have argued recently that [these transducers provide a good fit for morphology](http://jeffreyheinz.net/papers/DolatianHeinz-2020-CCR2FT.pdf).
As always, their argument is a bit more nuanced and defines several restricted subtypes of these transducers, but I'll completely gloss over this because the post is already plenty long.
The interesting point is that the difference between an item-and-arrangement view with underlying representations and an item-and-process view with derivations is just a single transduction of a complexity class that we might need anyways for morphology.

Ah, but now you wonder where the derivation is from.
We don't have to take that as a representational primitive either.
We can just start with a stem as the input, and have that non-deterministically rewritten as a derivation.
In our example above, *go* could be mapped to an infinite number of derivations:

1. go
1. go-foo
1. go-foo-bar
1. go-foo-bar-foo
1. and so on

This can be done by a non-deterministic finite-state transducer with epsilon-transitions (holy jargon, Batman).

![Non-deterministic 1-way FST for morphological derivations]({static}/img/thomas/representation_fossils/derivation_builder.svg)

The non-determinism is only needed to choose between the many different derivations that are available for any given stem.
Given a fixed choice, the transducer would be deterministic.
I haven't completely worked through this, but it seems to me that this is a very generous upper bound.
The pattern above would actually be input strictly local if those transductions could do $\varepsilon$-transitions.
So we might be able to make do with very little power, getting us into the range of transductions that Hossep and Jeff identify.

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
   Extend the example above to a derivation with multiple stems that each carry their own affixes, and you're in trouble.
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
   Even though graphs might seem more complex than trees, I think autosegmental structures are actually easier because they're still pretty "stringy".
   The simplest case of autosegmental structures is TSL, where it is obvious that the tier is the result of a strictly 1-local transduction.
   Making this transduction more complex yields more powerful extensions of TSL.
   The autosegmental structures I have seen so far also seem local in a specific way, all we need at this point is a formal model of strictly local string-to-graph transduction.
   Once we have that, I think it will fit the bill just fine.

As you can see, plenty of work for the interested researcher.
I think this is a very useful perspective, and one that really gets us closer to issues linguists care about.
There's many linguistic debates that seems pointless from a formal perspective because the representations provide too many loopholes.
Defossilization gives us a firm grip on representations, and that's what we really need at this point.
Subregular complexity has allowed us to tighten the constraint space, now we have to rein in representations.


## References

[^DM]: Things work slightly different if you think in terms of Distributed Morphology.
       In that case, we start out with a reduced tree that only contains the roots, and we have to figure out what functional material to insert above those roots.
       I believe that this does not change the strictly local nature of category systems in natural languages, but it might affect how much context you need to take into account.
       For instance, if you're an old school Minimalist and your syntactic structure includes fully inflected lexical items, then you don't need any context to figure out that *waters* is a verb, not a noun.
       If all you have is an uninflected root, you need to dig a bit deeper.
