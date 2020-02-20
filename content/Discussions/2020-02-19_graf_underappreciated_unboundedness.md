---
title: >-
    Unboundedness is a red herring
authors:
    - Thomas Graf
date: 2020-02-19
bibliography: references.bib
series: Underappreciated arguments
tags:
    - syntax
    - methodology
    - competence
    - performance
---

<!-- START_SUMMARY_BLOCK -->
Jon's [post on the overappreciated Marr argument]({filename}2020-01-12_rawski_marr.md) reminded me that it's been a while since the last entry in the *Underappreciated arguments* series.
And seeing how the competence-performance distinction showed up in the comments section of [my post about why semantics should be like parsing]({filename}2019-12-28_graf_semantics.md), this might be a good time to talk one of the central tenets of this distinction: unboundedness.
Unboundedness, and the corollary that natural languages are infinite, is one of the first things that we teach students in a linguistics intro, and it is one of the first things that psychologists and other non-linguists will object to.
But the dirty secret is that nothing really hinges on it.
<!-- END_SUMMARY_BLOCK -->

## The standard argument and the counterarguments

You all know the standard argument for unboundedness of certain syntactic constructions.
Native speakers of English know that all of the following are well-formed:

(@) John's favorite number is 1.
(@) John's favorite numbers are 1 and 2.
(@) John's favorite numbers are 1, 2, and 3.
(@) John's favorite numbers are 1, 2, 3, and 4.

We can continue this up to any natural number *n*, and the sentence will still be well-formed.
But that means there is no finite cut-off point, we can always construct a sentence that's even longer.
This unboundedness of the construction (in this case, coordination) implies that the set of well-formed sentences is infinite.
Of course in the real world there are outside factors that limit *n*.
For instance, you can only say a finitely bounded number of words before the heat death of the universe sets in and all existence ceases to be.
Or if you want something with less of a dash of cosmic horror, human memory and attention span can only handle so much before you slip up.
But that's orthogonal to the speaker's linguistic knowledge.
That's exactly why we want a competence-performance split, and hence we have unboundedness.

There's two counterarguments to the standard unboundedness argument.
The first one rejects the competence-performance distinction and says that linguistic knowledge is so deeply embedded in the performance systems that we cannot factor them out without losing the core of language.
Basically, this group of researchers doesn't want to study some lofty idealization of language, they want the real deal with all the behavioral quirks that come with it.
Let's call this the **plea for performance**.

The second argument is very different in nature as it fully acknowledges the importance of competence but takes umbrage with the inductive generalization step.
As far as I know @ScholzPullum02 were the first to make this argument in the literature, but it might have been floating around for a long time before that.
Their point is that the unboundedness argument relies on an empirically unsupported step of induction.
Thought experiments like the one above do not show us that there is no finite cut-off point past which competence breaks down.
At best one can show that there is no cut-off point that is so low that we can find it experimentally.
Except that there's actually plenty of such cut-off points, e.g. with center embedding, but they are deemed inadmissible due to the competence-performance distinction.
At this point the standard argument becomes circular: we assume a competence-performance split because the linguistic knowledge can generalize way beyond the limits of the performance systems, and all evidence to the contrary doesn't count because we assume a competence-performance split.
The standard argument implicitly assumes as an axiom that which it is supposed to derive, which means the unboundedness assumption is unfounded speculation.
Let's call this the **specter of speculation**.

We could now take deep plunge into the merits of the plea for performance or the specter of speculation, but in the spirit of the *Underappreciated arguments* series we'll simply avoid all of that by presenting an alternative argument for unboundedness that sidesteps the issues of the standard argument.
Spoilers: it's all about the rich combinatorics of syntax and how those are best described.


## Unboundedness is both red and a herring

### A bounded grammar fragment for syntax

Even the most ardent unboundedness skeptic will usually concede that the three English sentences below are well-formed.

<!-- (@) The man was surprised by the outcome. -->
<!-- (@) The woman was surprised by the rumor that the man was surprised by the outcome. -->
<!-- (@) The girl was surprised by the fact that the woman was surprised by the rumor that the man was surprised by the outcome. -->

(@ex1) The fact surprised me.
(@ex2) The fact that the fact surprised me surprised me.
(@ex3) The fact that the fact that the fact surprised me surprised me surprised me.

The last one is pushing things a bit, and with further levels of embedding things do break down for most speakers (if you don't like ((@ex1) and (@ex2) are strictly speaking sufficient for the underappreciated argument to work, so you can disregard (@ex3) if you don't like it for some reason).
Linguists usually treat the break down of center embedding as a performance artefact.
But who knows, maybe it's competence --- we won't make any commitments here.
All we need is the three examples above, with a maximum of two levels of embedding.

What kind of computational mechanism could produce (@ex1), (@ex2), and (@ex3)?
One of the simplest available options is a **finite-state automaton** (FSA).
Here is the FSA that generates the first sentence, and nothing else.

![An FSA for *the fact surprised me*]({static}/img/thomas/underappreciated_unboundedness/embedding0.svg)

This FSA has a unique starting point, the initial state 0 marked by *start*.
And it has a unique end point, the final state 4 marked by a double circle.
The FSA considers a string well-formed iff this string describes a path from an initial state to a final state.
In the example above, there is only one such path: *the fact surprised me*.
So this FSA considers (@ex1) well-formed, but nothing else.

Okay, then let's try to expand the automaton so that it also accepts (@ex2), which displays an instance of center embedding.
Note that we cannot simply add an edge labeled *that* from the final stack back to the initial state, as in the figure below.

![Looping back gives us right embedding, not center embedding]({static}/img/thomas/underappreciated_unboundedness/embedding0_loop.svg)

This automaton would produce right-embedding sentences like *the fact surprised me that the fact surprised me*, not center embedding as in (@ex2).
And since the FSA contains a cycle, right-embedding can be repeated over and over again, allowing for an unbounded number of embeddings.
We do not want that here because we're trying to construct an argument that has no commitment to unboundedness.

Back to the drawing board then.
In order to capture one level of center embedding, we have to add new structure to the automaton, yielding the FSA below.

![The FSA now can handle one level of center embedding]({static}/img/thomas/underappreciated_unboundedness/embedding1.svg)

Now there are two possible paths depending on whether we follow the *surprised*-edge or the *that*-edge after state 2.
Those two paths correspond to the strings in (@ex1) and (@ex2).
We can use the same strategy to add yet another "level" to the automaton and add (@ex3) to the set of well-formed strings.

![And finally two levels of center embedding]({static}/img/thomas/underappreciated_unboundedness/embedding2.svg)

Alright, so now we have a simple computational device that handles the three sentences above.
It doesn't even induce any tree structures, so if you're a fan of shallow parsing or similar ideas, this model does not directly contradict those assumptions either.
It really is a minimal base, you'd be hard-pressed to find something even simpler that can handle up to two levels of center-embedding.
Everybody on board?
Great, time for the mid-argument turn-around!

### Generalization is the key

Clearly the three sentences above aren't the only sentences of English.
At the very least, there's the following three variations.

(@var1) The fact shocked me.
(@var2) The fact that the fact shocked me shocked me.
(@var3) The fact that the fact that the fact shocked me shocked me shocked me.

We can of course extend the FSA to allow for those sentences, but note that we have to modify it in multiple places due to how the FSA handles embedding.

![Adding 1 verb requires 5 changes]({static}/img/thomas/underappreciated_unboundedness/embedding2_newverb.svg)

That's not nice, and it only gets worse from here.
The phrase *the fact* isn't exactly representative of the richness of English noun phrases.
All of the following are also well-formed:

(@np1) facts
(@np1) the facts
(@np2) the well-known facts
(@np3) three very well-known facts 
(@np4) these three very, very well-known facts
(@np5) these three very, very well-known, controversial, definitely irrefutable facts

And at the same time there's some combinations that do not work, e.g. using the indefinite with a mass noun (*a furniture*) or combining a sentential complement with a noun that cannot take such an argument (*the car that you annoyed me*).
Let's put those aside and try to give an FSA that handles only the very basic facts in (@np1)--(@np5).
To save space, I don't number the states, I use parts of speech instead of lexical items in this FSA, and I allow loops, which strictly speaking allows for unboundedness.
But look guys, this is already a chunky FSA as is, I really don't want to explode it even further to enforce a limit on how many adverbs or adjectives we may have:

![An FSA for (a fragment of) English noun phrases]({static}/img/thomas/underappreciated_unboundedness/np.svg)

And now we have to --- you guessed it --- insert that into the previous automaton in three distinct subject positions.

![We can't make it smaller than this, and this is a mess]({static}/img/thomas/underappreciated_unboundedness/embedding2_npsubjects.svg)

Yikes!
Pleasant to look at this is not.
And this is already a simplification because we only expanded the options for the subject position, while objects are still limited to just *me*.
And remember that we didn't worry about things such as the mass/count distinction or the selectional restrictions of nouns.
Nor did we consider that noun phrases can be embedded inside other noun phrases:

(@np6) this fact about language in your talk
(@np7) the destruction of the city

Assuming again at cut-off point of 3 levels of embedding for noun phrases, we should actually have the FSA below.

![I mean, seriously]({static}/img/thomas/underappreciated_unboundedness/insane.svg)

At this point, we should really start looking for a different way of describing those FSAs because nobody can make sense of those giant graphs, and we're still just talking about a tiny fragment of English.

And while we're at it, this description mechanism should also enforce a certain degree of uniformity across the levels of embedding.
In principle, we could modify the FSA above such that adjectives are only allowed at the lowest level of embedding, or such that odd levels of embedding have the linear order Det-Num-Adj-N and even levels instead have Num-N-Adj-Det.
No natural language works like this.
But the FSA can make this distinction because it is always aware of which level of embedding it is at.
We can exploit the fact that the rules of grammar are (largely) uniform across levels of embedding to give a more compact, factorized description of FSAs.

### Factoring FSAs into transition networks

Suppose that instead of a single, all-encompassing FSA, we have a collection of FSAs that we can switch between as we see fit.
For instance, the very first FSA we saw, which only generates *The fact surprised me*, could instead be described as a collection of three interacting FSAs.

![A network of interacting FSAs]({static}/img/thomas/underappreciated_unboundedness/ftn_factored.svg)

We start with the S-automaton.
In order to move from state S0 to state S1, we have to make our way through the NP-automaton.
In this automaton, we follow the path *the fact* to make our way from NP0 to NP1 and then NP2, which is a final state.
At this point we are done with the NP-automaton and reemerge in position S1.
From there we want to get to S2, the final state of the S-automaton, but doing so requires us to make our way through the VP-automaton.
Alright, so we start at VP0 and trace a path to VP2, giving us *surpised me*.
Once VP2 is reached, we reemerge at S2, and since that is a final state of the FSA we started with, we can finally stop.
The path we took through these automata corresponds to the string *the fact surprised me*.
So the factored description in terms of multiple automata generates the same output as the original FSA.

This kind of factored representation is called a **finite transition network** (FTN).
For each FTN, we can construct an equivalent FSA by replacing edges with the automata they refer to.
For the FTN above, we take the S-automaton and replace the NP-edge with the NP-automaton and the VP with the VP-automaton.

![The FSA network can be compiled out into a single FSA]({static}/img/thomas/underappreciated_unboundedness/ftn_compiled.svg)

Structurally, that is exactly the same automaton as the one we originally gave for *the fact surprised me*.

Factoring automata via FTNs can definitely be overkill, but it pays off for large automata because we can avoid duplication.
To give just one example, it's very easy to allow more complex objects than just *me*:

![Complex objects come at a minimal cost]({static}/img/thomas/underappreciated_unboundedness/ftn_factored_object.svg)

All we did is add an NP-edge from VP1 to VP2, and now our objects can be just as complex as our subjects.

The FTN above does not handle any levels of center embedding yet.
The easiest way to do this is to add an S-edge to the NP automaton.

![And center embedding is also easy to add]({static}/img/thomas/underappreciated_unboundedness/ftn_factored_embedding.svg)

Our FTN is now a **recursive transition network** (RTN).
The RTN uses a stack to keep track of how we move between the FSAs.
Here's how this works for *the fact that the fact surprised me surprised me*.
Warning, this will take a bit:

We start at S0 and take the NP edge, which puts us at NP0.
At the same time, we put S1 on the stack to indicate that this is where we will reemerge the next time we exit an FSA at one of its final states.
In the NP automaton, we move from NP0 all the way to NP3, generating *the fact that*.
From NP3 we want to move to NP4, but this requires completing the S-edge.
So we go to S0 and put NP4 on top of the stack.
Our stack is now [NP4, S1], which means that the next final state we reach will take us to NP4 rather than S1.
Anyways, we're back in S0, and in order to go anywhere from here, we have to follow an NP-edge.
Sigh.
Back to NP0, and let's put S1 on top of the stack, which is now [S1, NP4, S1].
We make our way from NP0 to NP2, outputting *the fact*.
The total string generated so far is *the fact that the fact*.
NP2 is a final state, and we exit the automaton here.
We consult the stack and see that we have to reemerge at S1.
So we go to S1 and truncate the stack to [NP4, S1].
From S1 we have to take a VP-edge to get to S2.
Alright, you know the spiel: go to VP0, put S2 on top of the stack, giving us [S2, NP4, S1].
The VP-automaton is very simple, and we move straight from VP0 to VP2, outputting *surprised me* along the way.
The string generated so far is *the fact that the fact surprised me*.
VP2 is a final state, so we exit the VP-automaton.
The stack tells us to reemerge at S2, so we do just that while popping S2 from the stack, leaving [NP4, S1].
Now we're at S2, but that's a final state, too, which means that we can exit the S-automaton and go... let's query the stack... NP4!
Alright, go to NP4, and remove that entry from the stack, which is now [S1].
But you guessed it, NP4 is also a final state, so we go to S1, leaving us with an empty stack. 
From S1 we have to do one more run through the VP-automaton to finally end up in a final state with an empty stack, at which point we can finally stop.
The output of all that transitioning back and forth: *the fact that the fact surprised me surprised me*.

### Hey, that's not bounded!

I mentioned earlier that every FTN can be compiled out into an equivalent FSA.
The same is not true for RTNs, and that's because there is no limit on how deeply the automata can be nested.
Generating *the fact that the fact that the fact that the fact surprised me surprised me surprised me surprised me* would have been exactly the same, mechanically.
However, RTNs can still be converted to FSAs if we put an upper bound on the depth of the stack.

But I think you'll agree that it doesn't really matter for the RTN whether the stack depth is bounded.
Yes, for some applications it may be convenient to convert the RTN to an FSA.
But that has no impact on the shape of the RTN and dependencies between automata that it describes.
It is immaterial for the generalizations.
And that's why it doesn't matter whether language is truly unbounded or not.
Maybe what we have in our heads is just a giant FSA.
It simply does not matter.
The combinatorics of syntax are such that the quest for a compact description will inevitably drive you towards machinery that is largely agnostic about whether unboundedness holds.


## The underappreciated argument in a nutshell

Alright, this has been a long read (and those pesky automata made it an even longer write).
But the bottom line is that there's no need to commit to unboundedness as an empirical truth.
It's not gonna fly for psychologists, and it runs into all the philosophical problems of arguments by induction.
We can sidestep all of that.

Even if we stick only with those utterances that are easily processed, the combinatorial space displays an extraordinary degree of systematicity.
Succinctly capturing these combinatorics requires factorization very much along the lines of what linguists have been doing.
Linguistic analysis is not undermined by the issue of whether language is truly unbounded because this is completely independent of the factors that push us in the direction of factorization and succinctness.
The same considerations that favor transformations over CFGs in @Chomsky57 also favor not committing to boundedness.
Bounded, unbounded, it simply does not matter, so don't get hung up about it.

## References
