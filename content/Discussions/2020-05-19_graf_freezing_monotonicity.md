---
title: >-
    MR movement: Freezing effects & monotonicity
authors:
    - Thomas Graf
date: 2020-05-19
tags:
    - syntax
    - movement
    - freezing effects
    - monotonicity
---

<!-- START_SUMMARY_BLOCK -->
As you might know, one of my hobby-horses is reanalyzing linguistic phenomena in terms of monotonicity (see here, here, and then there's this lovely paper here).
<!-- fixme: links; add Sophie's stuff -->
I'm now in the middle of writing another paper on this topic, and it currently includes a chapter on freezing effects.
You see, freezing effects are obviously just bog-standard monotonicity, and I'm shocked that nobody else has pointed that out before.
But perhaps the reason nobody's pointed that out before is simple: my understanding of freezing effects does not match the facts.
In the middle of writing the paper, I realized that I don't know just how much freezing effects limit movement.
So I figured I'd reveal my ignorance to the world and hopefully crowd source some sorely needed insight.
<!-- END_SUMMARY_BLOCK -->


# Freezing effects primer

Freezing is the idea that once a phrase starts moving, it becomes opaque to extraction.
The sentence below presents a typical example --- to keep things readable, I'm using copies instead of traces, but that's just a descriptive device.

(@) ^*^[~CP~ [which car] did [~TP~ [the driver of ~~which car~~] T [~*v*P~ ~~the driver of which car~~ *v* cause a scandal]]]

Here the subject DP *the driver of which car* undergoes movement from the base subject position Spec,*v*P to the surface subject position in Spec,TP.
As a result, the DP effectively turns into an island, which makes it impossible to move the wh-phrase *which car* from within he subject into Spec,CP.
That's the essence of freezing, and it can be summarized in the form of a catchy slogan:

(@eng) **Freezing in a nutshell**  
    Once you've escaped, nothing escapes from you.

It's the Citizen Kane of movement: a free-spirited phrase that is eager to move finally achieves success but is corrupted by it and now uses its power to keep down all the other free-spirited phrases in its domain that would like to move.

Freezing has a well-known loophole: since a phrase P isn't opaque to extraction until it starts moving, other movers can escape from P as long as they do so before P moves.
This still allows for instances of remnant movement as in the German example below.

(@ger) [~CP~ [~VP~ ~~das Buch~~ gelesen] hat [~TP~ das Buch der Hans T [~*v*P~ ~~der Hans~~ *v* ~~[~VP~ das Buch gelesen]~~]]]  
    [~CP~ [~VP~ ~~the book~~ read] has [~TP~ the book the Hans T [~*v*P~ ~~the Hans~~ *v* ~~[~VP~ the book read]~~]]]  
    `Hans **read** the book.'

Yeah, that example is a lot harder to make sense of unless you're already familiar with the analysis.
Let's switch out the German for English glosses, just to make things a bit easier.
Then the sentence starts out with the structure [~*v*P~ the Hans *v* [~VP~ the book read]], where *the book* is the object of the finite verb *read* and *the Hans* is the subject.
At this point, *the Hans* undergoes the usual subject movement to Spec,TP.
Then, the object *the book* moves out of the VP into some part of what's called the *Mittelfeld*, which may be some kind of TP-adjunct position.
Notice that both movement steps are allowed because neither phrase was extracted from a moving phrase.
Now, finally, the whole VP moves to Spec,CP.
This, too, is a licit step --- freezing effects do not say that you cannot move once something has moved out of you, they say that nothing can move out of you once you start moving.
But that's not the case here.
So the whole VP gets to move to the left edge of the sentence, but since the object had already moved out of the VP before, only the head of the VP is visible at the left edge of the surface string.

If you're still confused, here's the bare phrase structure trees for (@eng) and (@ger).

fixme: trees here


# Connection to monotonicity

For the examples above, there is a straight-forward account in terms of monotonicity.
Remember that monotonicity is an order preservation principle ([check this earlier post](fixme)).
Given two structures $A$ and $B$ with orders $\leq_A$ and $\leq_B$, a function $f$ from $A$ to $B$ is monotonically increasing iff $x \leq_A y$ implies $f(x) \leq_B f(y)$.
For our purposes, it will be sufficient to think of monotonicity as a generalized ban against crossing branches.

We can apply the notion of monotonicity directly to the dependency tree representation provided by Minimalist grammars (MGs).
In this format, the phrase structure trees above are represented as the trees below, except that I have simplified things a bit by omitting all features and instead indicating movement dependencies via arrows.

fixme: figures here

Each dependency tree defines a partial order over the lexical items in the sentence.
Intuitively, this partial order encodes syntactic prominence in terms of head-argument relations, or, in Minimalist terms, (external) Merge.
That is to say, if X is the daughter of Y, then Y is more prominent than X, and so is the mother of Y, and the mother of the mother of Y, and so on.
Okay, so our first order for monotonicity comes straight from the MG dependency trees; I'll call this the **Merge order**.

For our second order, we construct a truncated version of the dependency trees that encodes prominence with respect to movement (internal Merge).
The construction is a bit more complicated, but putting aside some edge cases it's enough to take the dependency tree and remove all lexical items that don't provide the landing site for some mover.
This gives us the reduced structures below.

fixme: reduced figures here

Okay, order #2 is in place; I'll call this the **Move order**.

Now we define a mapping $f$ from the Move order to the Merge order such that each node M in the move order is mapped to the node N in the Merge order iff N moves to M.
Again it helps to look at this in terms of pictures.
As you can see, $f$ essentially encodes the reverse of the arrows I added to the original dependency trees.

Notice how the lines for $f$ cross in the illicit English sentence, but not in the well-formed German one.
So perhaps crossing branches aren't okay, and since monotonicity is essentially a ban against crossing branches, that would suggest that the problem with the English sentence is that it does not obey monotonicity.
Freezing effects, then, amount to the requirement that a sentence's Move order must preserve its Merge order.
The only permitted form of movement is **m**onotonicity **r**especting movement, or simply MR movement.


# Why this might not work

Alright, that's a nifty story, but it might not actually work.
MR movement is both more limited and more permissive than freezing effects.
And I'm not sure if that's a problem.

Let's first look at why MR movement is more restrictive.
Freezing effects tell us that once N has been extracted from M, it is free to move to wherever it pleases.
MR movement, on the other hand, can never move N to a position that's higher than the final landing site of M.
Does this ever happen?
I'm not sure.
German certainly furnishes cases that look like this.

(@ger) [~CP~ [~DP~ das Buch] hat [~TP~ [~VP~ ~~das Buch~~ gelesen] ~~[~DP~ das Buch]~~ der Hans T [~*v*P~ ~~der Hans~~ *v* ~~[~VP~ das Buch gelesen]~~]]]  
       [~CP~ [~DP~ the book] has [~TP~ [~VP~ ~~the book~~ read] ~~[~DP~ the book]~~ the Hans T [~*v*P~ ~~the Hans~~ *v* ~~[~VP~ the book read]~~]]]  
       `The book, Hans **read**.'

But to be frank, German is a bad example to begin with because scrambling can do all kinds of stuff that won't fly for standard movement.
I can't think of cases for other languages, but I'm pretty bad at remembering data points, so that's not saying much.
So, yes, MR movement might be too restrictive if it is stated with respect to the final landing site.

One way to fix that is to redefine the Move order so that it keeps track of the first landing sites instead of the final ones.
But for some reason I find that more ad-hoc.
It should it either be all landing sites, or the last one, there is no reason why the first one should enjoy some privileged status.
But that's neither here nor there, so I don't know, maybe?
Nah, I'd rather stick to my guns and reanalyze data that conflicts with MR movement.

But then there's also the fact that MR movement is less restrictive.
Once again it's because I chose to focus on the final landing site instead of the first one.
This means that MR movement can extract N from M after M has already started movement, provided that M eventually winds up in a higher position than N.
Again I'm not sure if that's a problem.
Whenever such a case arises, one could also make it fit with freezing movement by simply positing an additional movement step that extracts N at the very beginning before M starts to move.
Testing for the presence or absence of this initial movement step would be hard, so I'm not sure how things would pan out empirically.
Again I'm inclined to stick with MR movement simply because it provides a different perspective on freezing effects.
Maybe MR movement works, maybe it doesn't, but either result would provide useful insights into the nature of freezing effects.


# The punchline

Overall, freezing effects can be regarded as an instance of monotonicity, just not in the way I'd like to see.
I defined the move order in terms of the final landing site, but to get an exact match for the standard definition of freezing we have to use the initial landing site.
That's still interesting in that it allows us to reduce freezing to the more general principle of monotonicity, and I have argued many times that monotonicity really has a fundamental role to play in language.

But I'd really like to push for the MR movement perspective instead.
I just find it more pleasing, and I like that it differs from the standard view of freezing on some edge cases.
So what do you think?
Does MR movement have a shot, or is there robust evidence against it?
