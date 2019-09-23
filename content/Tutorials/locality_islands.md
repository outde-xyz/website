---
title: >-
    Islands are unexpectedly expected
authors:
    - Thomas Graf
date: 2019-09-23
bibliography: references.bib
series: >-
    The subregular locality zoo
tags:
    - subregular
    - syntax
    - locality
    - Move
    - islands
---

<!-- START_SUMMARY_BLOCK -->
In the [previous post]({filename}locality_merge_move.md) we saw Merge is SL-2 over dependency trees, and Move is TSL-2. 
For every movement feature f we project a separate tier that contains only lexical items that have a licensor feature f^+^ or a licensee feature f^-^.
A tier is well-formed iff every lexical item with a licensee feature has a mother with a licensor feature, and every lexical item with a licensor feature has exactly one lexical item among its daughters that carries a licensee feature.
It's a pretty simple system.
Despite that simplicity, it predicts a fundamental aspect of movement: island effects!
<!-- END_SUMMARY_BLOCK -->

## The unexpected nature of islands

There is a lot of debate as to whether island effects are due to the grammar or the parser.
Personally, I think that's an ill-defined question because it presupposes a distinction between grammar and parser that doesn't make a lot of sense if you probe it very deeply.
But no matter which side of that debate you come down on, we can all agree that if your view of syntax furnishes an explanation or island constraints for free, that's a good thing.
It ultimately might not be the correct explanation, but more is better in this case.

But the striking thing about islands is how unexpected they are in most syntactic theories.
They do not arise naturally from the basic machinery.
Consider two simple examples of islands below:

(@) \*Who did John complain [~CP~ because Bill yelled at \_]?
(@) \*Who did you hear the [~N~ rumor [~CP~ that Mary punched \_]]?

Why should we find Complex NP islands and adjunct islands?
I don't mean in the specific sense of "why is X an island, but not construction Y".
No, I mean why should we find any islands at all?
Why should movement ever be forbidden?
If syntax is just Merge and Move, how do islands arise?

Some proposals tell at least a partial story.
CCG and TAG can derive quite a few island effects once you commit yourself to only positing structures that follow certain principles.
@Stepanov01 derives adjunct islands from the assumption that all adjuncts are merged at a later stage of the derivation where the material they contain can no longer interact with movement.
I have [my own story](https://thomasgraf.net/output/graf13cls.html) for deriving adjunct islands and the coordinate structure constraint while still allowing for parasitic gaps and across the board movement.
The downside to all these stories is that deriving islands from first principles makes it damn hard to accommodate exceptions like the ones in @Truswell07Lingua:

(@) What did John drive Mary crazy while trying to fix \_?

That's why islands always have a certain unexpected nature from the perspective of grammar.
If you don't derive them from your basic machinery, then it is the existence of islands that is unexpected.
If you do derive them from your basic machinery, then it is the existence of exceptional non-islands that is unexpected.
I think that's the allure of parsing-based explanations to many linguists: they derive island effects from independently motivated processing assumptions,[^debatable] but since parsing measures are gradient they also allow for exceptions.
But as I said, a grammar-based explanation would be a welcome addition --- and the TSL view of Move provides just that.

[^debatable]: It's actually debatable whether processing accounts derive islands for free. They tend to invoke ancillary assumptions, e.g. that adjuncts are somehow more costly than arguments. At that point, you're just restating the facts through several layers of obfuscation. Then again, my student Aniello De Santo has some promising results that use an MG processing model and don't need these assumptions. He'll have a poster at SCiL, colocated with the LSA, so if this sounds interesting to you you should drop by.

## The unexpected nature of islands is expected...

Let's take a closer look at the Complex NP island.

(@) \*Who did you hear the [~N~ rumor [~CP~ that Mary punched \_]]?

It's dependency tree is pretty simple.

![Dependency tree with Complex NP island ]({static}/img/thomas/subreg_tutorials/complexnp_dependency.svg)

If we look at the two respective movement tiers of the tree (nom and wh), there doesn't seem to be much wrong either.
On both tiers, every licensee has exactly one licensor mother, and every licensor has exactly one licensee among its daughters.

![Corresponding movement tiers]({static}/img/thomas/subreg_tutorials/complexnp_tiers_noisland.svg)

But who's to say that these are the right tiers?
From a computational perspective, there's nothing special about the lexical items that go on the respective tiers.
Yes, we said we're gonna project only lexical items that carry the relevant features, but that's a linguistic stipulation.
The computational machinery can put anything on the tier, including, say, anything with the feature string C^+^ N^-^.
Hmm, now those tiers look quite different.

![Corresponding movement tiers, with Complex NP head on both tiers]({static}/img/thomas/subreg_tutorials/complexnp_tiers_island.svg)

While the nom-tier is still well-formed, the wh-tier has become ill-formed because *who* now has *rumor* as its mother, which does not have a matching licensor feature.
The local licensing relation has been destroyed by the island-inducing material intervening on the tier.

The nifty thing about this perspective is that islands are perfectly natural.
Without any additional assumptions about what may or may not go on a tier, one necessarily allows for systems where some lexical items induce island effects.
At the same time, exceptions are also expected to exist.
Just because most adjuncts project on the tier does not mean that every adjunct has to.
If you start out with the assumption that any grammar is fine as long as movement stays TSL-2, both islands and island exceptions are expected.

## ...mostly

As all the other island stories on the market, the TSL story is not perfect.
It's main problem is that it underestimates the systematicity of islands:

1. In the current system, anything could be an island, e.g. ditransitive verbs.
   That's false.
1. In the current system, there should be languages where adjuncts are never islands.
   That's false.
1. In the current system, islands could be sensitive to the type of movement --- some islands could block wh-movement but allow for topicalization.
   That's (largely) false.
1. Not all island constraints can be handled this way.
   Freezing effects, for instance, do not fit this view.

On the upside, it does explain why we can't have configurational islands that depend on non-local information, e.g. "X is an island iff it is c-commanded by Y".
The tier projection for TSL does not take context into account, so whether something projects can only depend on the lexical item itself and its feature annotation.

But yes, I can't deny that the TSL account of islands is far from the final word.
At the very least, it still needs a more fully articulated theory of tier projection to explain why islands are much more systematic than they could be.
We also need some other subregular perspectives on islands to handle some cases that can't be captured by the TSL account at all.
Together with my student Nazila Shafiei I've been exploring several subregular options for that.
The interesting thing is that cross-linguistically robust island effects like, say, adjunct islands, fall out naturally from all those different perspectives.
Less common constraints on movement like freezing effects or the *that*-trace effect often work with only one of those models.
This suggests that there might actually be multiple factors at work, and what we call islands and movement constraints is an emergent property of these distinct systems.

This is a very fast moving research program at this point, pretty much every month we figure out something new that adds a yet another subregular facet to islands specifically and syntax in general.
The TSL perspective I described here came first, and it certainly has its shortcomings.
But I still like how it provides a very natural place for islands in the grammar without tying your hands so much that exceptions become impossible to accommodate.
If you assume that grammars have free rein over what projects as long as it stays within the preordained computational boundaries, then islands are expected, and so are exceptional non-islands.
What's missing is the additional element of divine order that explains why the lay of the land for islands isn't nearly as chaotic as it could be.

## References
