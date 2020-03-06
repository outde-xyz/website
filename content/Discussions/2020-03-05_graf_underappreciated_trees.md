---
title: >-
    Trees for free with tree-free syntax
authors:
    - Thomas Graf
date: 2020-03-06
bibliography: references.bib
series: Underappreciated arguments
tags:
    - syntax
    - strings
    - derivation trees
    - phrase structure trees
---

<!-- START_SUMMARY_BLOCK -->
Here's another quick follow-up to the [unboundedness argument]({filename}2020-02-20_graf_underappreciated_unboundedness.md).
As you might recall, that post discussed a very simple model of syntax whose only task it was to adjudicate the well-formedness of a small number of strings.
Even for such a limited task, and with such a simple model, it quickly became clear that we need a more modular approach to succinctly capture the facts and state important generalizations.
But once we had this more modular perspective, it no longer mattered whether syntax is actually unbounded.
Assuming unboundedness, denying unboundedness, it doesn't matter because the overall nature of the approach does not hinge on whether we incorporate an upper bound on anything.
Well, something very similar also happens with another aspect of syntax that is beyond doubt in some communities and highly contentious in others: syntactic trees.
<!-- END_SUMMARY_BLOCK -->

## The first and only example

Remember that finite-state automata (FSAs) can be represented much more compactly via recursive transition networks (RTNs).
As long as we put an upper bound on the number of recursion steps, every RTN can be compiled out into an FSA, although the FSA might be much larger and contain numerous redundancies.
Here's the RTN I provided for a tiny fragment of English:

![An RTN with center-embedding]({static}/img/thomas/underappreciated_unboundedness/ftn_factored_embedding.svg)

And indubitably you also remember how this device would generate *the fact that the fact surprised me surprised me*, which I explained with such remarkable lucidity that it should be indelibly etched into your mind:

>We start at S0 and take the NP edge, which puts us at NP0.
>At the same time, we put S1 on the stack to indicate that this is where we will reemerge the next time we exit an FSA at one of its final states.
>In the NP automaton, we move from NP0 all the way to NP3, generating *the fact that*.
>From NP3 we want to move to NP4, but this requires completing the S-edge.
>So we go to S0 and put NP4 on top of the stack.
>Our stack is now [NP4, S1], which means that the next final state we reach will take us to NP4 rather than S1.
>Anyways, we're back in S0, and in order to go anywhere from here, we have to follow an NP-edge.
>Sigh.
>Back to NP0, and let's put S1 on top of the stack, which is now [S1, NP4, S1].
>We make our way from NP0 to NP2, outputting *the fact*.
>The total string generated so far is *the fact that the fact*.
>NP2 is a final state, and we exit the automaton here.
>We consult the stack and see that we have to reemerge at S1.
>So we go to S1 and truncate the stack to [NP4, S1].
>From S1 we have to take a VP-edge to get to S2.
>Alright, you know the spiel: go to VP0, put S2 on top of the stack, giving us [S2, NP4, S1].
>The VP-automaton is very simple, and we move straight from VP0 to VP2, outputting *surprised me* along the way.
>The string generated so far is *the fact that the fact surprised me*.
>VP2 is a final state, so we exit the VP-automaton.
>The stack tells us to reemerge at S2, so we do just that while popping S2 from the stack, leaving [NP4, S1].
>Now we're at S2, but that's a final state, too, which means that we can exit the S-automaton and go... let's query the stack... NP4!
>Alright, go to NP4, and remove that entry from the stack, which is now [S1].
>But you guessed it, NP4 is also a final state, so we go to S1, leaving us with an empty stack. 
>From S1 we have to do one more run through the VP-automaton to finally end up in a final state with an empty stack, at which point we can finally stop.
>The output of all that transitioning back and forth: *the fact that the fact surprised me surprised me*.

But believe it or not, this miracle of exposition can be represented more compactly in the form of a single diagram.

![A graph depicting how the subautomata call each other]({static}/img/thomas/underappreciated_unboundedness_trees/ftn_trace.svg)

Looks familiar?
There, let me rearrange it a bit and add an S at the top.

![OMG, it's a tree]({static}/img/thomas/underappreciated_unboundedness_trees/ftn_tree.svg)

Son of a gun!

## Trees = Computational traces

The graph that we have up there is called a **computational trace**.
It is a record of the steps of the computation that lead to the observed output.
Computational traces aren't anything fancy or language-specific, they arise naturally wherever computation takes place.

Computational traces don't necessarily exhibit tree-like structures.
They can just be strings, or they can be more complex objects, e.g. directed acyclic graphs (which a linguist would call multi-dominance trees that can have multiple roots).
The interesting thing is that models of syntax inevitably give rise to computational traces that are at least trees.
And the reason is once again that syntax pushes us in the direction of factorization, the direction of many small systems that invoke each other.
The computational nature of syntax is intrinsically tree-like.

## Closing thoughts

So there you have it.
Even if syntax may just generate strings, like an FSA or RTN, it nonetheless exhibits tree structure in the accompanying computations.
It doesn't hinge on unboundedness. 
It doesn't hinge on the self-embedding property or recursion, either --- even if the RTN were just a finite transition network, the process of moving between automata would induce tree structure.
And that's why this is an underappreciated argument: it depends on so little, it avoids all the usual hot-button issues like recursion, and yet it is used so rarely.

Btw, the connection between trees and computation isn't some fancy new insight.
Mark Steedman has long argued for this view of syntactic structure.
Heck, trees made their way into generative syntax as a compact way of representing the derivations of context-free grammars.
But they also got reified very quickly, changing from records of syntactic computation to the primary data structure.
This had the unintended consequence that the connection between trees and computation has slowly fallen into oblivion, and that makes trees look a lot more stipulative to outsiders.

I personally believe that the reification of trees has largely been a bad thing for the field.
The original insights got shortened to the dogma that a syntactic formalism that doesn't produce trees can't possibly be right, even though the structure of the generated object has no direct connection to the structure of the generation mechanism.
The reification of trees has erased that distinction, resulting in an overly narrow space of analytical options.
One of the most important developments in computational syntax in the last twenty years was to tease them apart again and study the computational traces independently of what output they produce.
This has been a very productive enterprise, and the insights obtained this way suggest that this is really what syntax is about.

It also fits naturally with the computational view of the inverted T-model.
The [bimorphism perspective]({filename}2019-10-15_graf_tmodel.md) puts syntax in the position of an interpolant, a means of succinctly describing a computational system of bidirectional mappings.
From this perspective, syntax simply is computation, and syntactic structure is computational structure.
And that's what makes syntactic structure inevitable.
