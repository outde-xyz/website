---
title: >-
    Semantics should be like parsing
authors:
    - Thomas Graf
date: 2019-12-28
bibliography: references.bib
tags:
    - semantics
    - donkey sentences
    - parsing
---

<!-- START_SUMMARY_BLOCK -->
I spent a few days before Christmas at the [Amsterdam colloquium](http://events.illc.uva.nl/AC/AC2019/), which exposed me to a much heavier dose of semantics than I'm used to.
I've always had a difficult relation with semantics.
On the one hand I like that it has its fair share of [KISS theories]({filename}2019-07-12_graf_kiss.md), and generalized quantifier theory is aesthetically very pleasing to me.
On the other hand most of semantics is pretty dull, and I think that's because semanticists put way too much stuff in their theories that has nothing to do with natural language semantics.
I've previously had a hard time putting this into concrete terms, but Lucas Champollion's invited talk on donkey sentences finally presented me with a specific example.
<!-- END_SUMMARY_BLOCK -->


## Donkey sentences: More interesting than I thought

Lucas's talk was really a marvel, the rare kind of talk where you feel like a veil has finally been lifted and you can see an obscure subject matter much more clearly now.
Before, I never quite got why everybody made such a fuzz about donkey sentences.
We've all seen them before:

(@beat) Every farmer who owns a donkey beats it.

Okay, you get a universal reading here instead of an existential, so what?
It's not that hard to design an interpretative system that assigns a universal reading to an existential embedded inside a universal.
It doesn't look nice in the lambda calculus, but that's because the lambda calculus is awful at capturing structure-sensitivity.

The first thing I learned is that this shift from existential to universal in specific environments is only part of the puzzle.
In some cases, the existential stays an existential.

(@hat) Every farmer who owns a hat wears it at church.

No reasonable person interprets this as a claim that each farmer wears every hat they own at church.
It only means that if a farmer has at least one hat, then he wears a hat at church.
And this kind of minimal reading is actually available for (@beat) if we set up the context in a way where the relevant piece of information is whether at least one donkey of each farmer is being beaten.
That's in contrast to the (@taxes), where this reading is very hard to get:

(@taxes) Every farmer who owns a donkey pays taxes on it.

Obviously no government body would be satisfied with taxing only one donkey per farmer, no, every taxable donkey will be taxed.
So we have at least three kinds of donkey sentences:

1. Existential reading strongly preferred
2. Universal reading strongly preferred
3. Mixed cases that can go either way

Alright, now that looks a lot more interesting.
I guess I could have known that for years already if I had paid more attention in my semantics intro, but somehow I never made it past the familiar (@beat) case.


## How much of donkey sentences is semantics?

With the problem clearly laid out, Lucas then explained how the differences between the three types of donkey questions hinge on the concept of question under discussion (QUD).
In my limited understanding, that's just another guise of world knowledge.
Whether a donkey pronoun gets an existential reading or a universal one is ultimately a matter of world knowledge.
In the cases of taxes, we know that there is a major difference between paying taxes on one donkey or on all of them --- the latter is what you're supposed to do, and doing the former will get you into trouble with the IRS.
In the case of wearing hats, the salient point is just that the farmer doesn't show up to church without a hat, so the existential reading is chosen instead.
At this point, I was really hyped and expected Lucas to drop the hammer on donkey sentences: the semantic problem is much simpler than previously believed, we just have underspecification with respect to existential/universal, and the rest is world knowledge.

But that's not what happened.
Instead, Lucas gave a very precise formalization that integrates the world knowledge into the semantics.
It's good work, but it's exactly what I think semantics shouldn't do.
Instead of a simple factorization, we now have a complex piece of machinery.
And the machinery doesn't allow us to do something that would be impossible otherwise.
For instance, you can't implement the proposal on a computer and run it because the analysis still builds on world knowledge, which is very hard to get into computers.
So it looks like we would have been better off factoring out world knowledge right away to focus only on the mechanical parts of the interpretative system that can be easily captured algorithmically.


## An analogy from parsing

In many ways, the problem of donkey sentences reminds me of structural ambiguity in parsing.
Consider the following sentence:

(@arnold) I watched a movie with Arnold.

This sentence is ambiguous.

(@watch) I [[watched a movie] with Arnold].
(@actor) I watched [[a movie] with Arnold].

Perhaps me and my friend Arnold watched a movie together, as in (@watch).
Or I watched a movie featuring Arnold Schwarzenegger, as in (@actor).
The latter reading is available only because Arnold Schwarzenegger is the only actor that is regularly referred to by his first name.
The actor-reading is really hard to get if we pick a different name instead.

(@sylvester) I watched a movie with Sylvester.

Even though Sylvester Stallone is the only well-known actor whose first name is Sylvester, it is very unlikely that anybody would assign the actor-interpretation to this sentence.
So far, so familiar.

The important thing is that it would be ludicrous to expect a theory of parsing to account for the contrast between (@arnold) and (@sylvester).
That's not the job of a parsing algorithm.
All we require is that the parser allows for the structural ambiguity that gives rise to these different interpretations.
On top of that, we may then build a mechanism that ranks different parses, and this mechanism would be allowed to interface with some kind of oracle that encodes aspects of world knowledge such as the *Arnold*/*Sylvester* contrast above.
A simple core on top of which we can put various extensions in order to get a better fit for actual human behavior.

Going back to donkey sentences, it seems to me that semantics (by which I mean both the interpretative system and the subfield of linguistics) has only one job: correctly identifying donkey pronouns and providing both an existential and a universal interpretation in those cases.
Choosing between those two goes far beyond what semantics should be about.
It hinges on so many subtle aspects of human cognition and how humans carve up he world that I think the problem is hopeless from a scientific perspective.
Engineers may of course try to design various probabilistic heuristics to approximate human behavior, that's a worthy goal.
But that's not what semanticists are doing, which puts their work in this odd spot that is neither here nor there.
They're taking on way more than just defining a parser for meaning, but the payoff of this extra work remains dubious to me.
