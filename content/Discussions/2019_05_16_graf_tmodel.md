---
title: >-
    Underappreciated arguments: The inverted T-model
series: >-
    Underappreciated arguments
authors:
    - Thomas Graf
date: 2019-05-15
bibliography: references.bib
tags:
    - syntax
    - transductions
    - bimorphisms
    - T-model
---

<!-- START_SUMMARY_BLOCK -->
There's many conceptual pillars of linguistics that are, for one reason or another, considered contentious outside the field.
This includes the competence/performance split, the grammar/parser dichotomy, underlying representations, or the inverted T-model.
These topics have been discussed to death, but they keep coming up.
Since it's tiring to hear the same arguments over and over again, I figure it'd be interesting to discuss some little known ones that are rooted in computational linguistics.
This will be an ongoing series, and its inaugural entry is on the connection between the T-model and bimorphisms.
<!-- END_SUMMARY_BLOCK -->


## What's the T-model?

Ah yes, the *T-model*.
Also known as the *inverted T-model* or *(inverted) Y-model*.
If you've ever taken a syntax class or read a syntax textbook, you'll have come across the figure below:

![The standard T-model]({static}/img/thomas/underappreciated_tmodel/tmodel_modern.svg){ width=30% }

Cute little fella.
The T-model represents the idea that syntax is a structure-building process that assembles some kind of syntactic object and feeds it into two distinct "pipelines":

- PF (physical form), which ultimately leads to the pronounced sequence of sounds that make up the utterance, and
- LF (logical form), which produces the semantic interpretation.

But what exactly does that mean?
The description above mirrors the standard view in terms of an assembly line that has syntax as its starting point, but that is misleading.
The T-model is not a model of production, just like a derivation is not a literal description of how a syntactic object is actually assembled during production or processing.
When you want to say something, syntax doesn't just build a syntactic object willy-nilly without any attention to meaning, and then at the end you check if the meaning of that object actually matches what you wanted to express.
For the very same reason it is not a model of sentence processing either.
No, the T-model is a claim about cognitive architecture.

(@tmodel1)
**T-model (Paraphrase 1)**  
Syntax is the mediator between utterance and meaning, and the mediation is such that there is a single point of divergence.

Contrast that with the architecture of the Standard Theory as laid out in *Aspects* [@Chomsky65]:

![The Aspects model]({static}/img/thomas/underappreciated_tmodel/tmodel_aspects.svg){ width=30% }

Here syntax first builds up the Deep Structure, which is also the input for semantic interpretation. 
The Deep Structure is then turned into Surface Structure by a series of syntactic transformations, and S-structure is fed into the PF pipeline to add various non-syntactic.embellishments like prosody.
That's a very different picture, even though syntax is still the link between PF and LF.
So the single divergence point is really important for the T-model.
At the same time, the "mediator" part in (@tmodel1) is a little wishy washy.
I believe the following is a valid paraphrase that gets a bit more specific.

(@tmodel2)
**T-model (Paraphrase 2)**  
Syntax is the unique part of grammar that is shared equally by PF and LF.

To the syntacticians among you this might be too abstracted as it cuts out several concepts that are frequently associated with the T-model.
I'll return to that point later on.
But first let's put on our computational hats.


## Bimorphisms and the T-model

In computational linguistics we really care about mappings.
Mapping inputs to outputs, underlying representations to surface forms, trees to strings, grammars to other grammars, it's pretty much mappings all day long.
And of course linguists aren't all that different.
The core problem of language is one of mappings: how are utterances mapped to meanings, and meanings mapped to utterances?
The former we may call **analysis**, the latter **production**.
Analysis maps physical forms (utterances, signs, et.c) to meanings (however they might be encoded), and production proceeds in the other direction.

![The central problem of language]({static}/img/thomas/underappreciated_tmodel/directmapping_language.svg){ width=50% }

Such back-and-forth mapping configurations aren't anything unusual.
They happen anywhere where one needs to be able to translate in both directions.
In more general terms, we may just consider a mapping $f: A \rightarrow B$ from $A$ to $B$ and a mapping $g: B \rightarrow A$ from $B$ to $A$.
It doesn't matter what $A$ and $B$ stand for as long as they are sets.

![Abstract form for back-and-forth mappings]({static}/img/thomas/underappreciated_tmodel/directmapping_abstract.svg){ width=30% }

This is a very general configuration that one finds in many domains.
Machine translation wants to map from string in one language to strings in another language, and back.
Compiler design is ultimately about relating strings of programming code to strings of machine code (although the other direction is much less important in this case).
Even converting between number systems or different currencies falls under this very broad picture.

Formalizing these systems can be difficult though.
First one has to define what $A$ and $B$ look like.
Depending on the domain, that might already be a Herculean.
In the case of language, this requires specifying exactly the set of licit physical forms for a given language, and the set of permissible meanings.
Yeah, that's pretty much impossible given our current understanding.
Then one has to define $f$ and $g$.
This too can be very, very hard.
As far as I know, there isn't a single linguistic theory of analysis and production in this technical sense --- that is to say, direct mappings between physical forms and meanings.
And the problem doesn't get much easier in other domains like machine translation.
Heck, even mapping a string of programming code to the corresponding machine code is far from trivial.

So what do people do instead?
Well, they don't do the mapping directly.
Instead, they work with intermediate steps that are easier to figure out.
One particular way of doing this is the **bimorphism** approach.
While the actual math is complex, the general idea is easy enough. 
One defines an **interpolant** $C$ and mappings $l: C \rightarrow A$ from $C$ to $A$ and $r: C \rightarrow B$ from $C$ to $B$.
Note how this changes the directionality of the problem.
There's no longer a direct link between $A$ and $B$, instead of starts with $C$ and goes from there to $A$ or $B$.

The definitions for $C$, $l$, and $r$ are carefully chosen to capture core aspects of $A$, $B$ as well as the mappings $f$ and $g$.
If done correctly, $f(a) = b$ iff there is a $c$ in $C$ such that $l(c) = a$ and $r(c) = b$.
In this case, it must also hold that $g(b) = a$.
In other words, $a \in A$ and $b \in B$ are treated as related because there is some interpolant $c$ from which $a$ can be obtained by $l$ and $b$ can be obtained by $r$.
Elements of $A$ and $B$ are related by $f$ and $G$ iff they share the same source in $C$.

![Abstract bimorphism configuration]({static}/img/thomas/underappreciated_tmodel/bimorphism_abstract.svg){ width=30% }

More formally, we can now define $f(a) = r(l^{-1}(a))$ and $g(b) = l(r^{-1}(b))$ ($^{-1}$ indicates the inverse).

As before, we can replace the general variables with the components of our linguistic example: physical forms, meanings, analysis, and production.
But what do $C$, $l$ and $r$ correspond to?
You guessed it: syntax, PF, and LF!

![The T-model is the language bimorphism!]({static}/img/thomas/underappreciated_tmodel/bimorphism_language.svg){ width=50% }

That is the very essence of the T-model.
An utterance can be mapped to a specific meaning, and the other way, because syntax furnishes an interpolant from which both can be obtained in a principled manner.
That interpolant could be a phrase marker, a derivation tree, a dependency graph, whatever.
It's some kind of syntactic object.
Analysis is the process of applying the PF-pipeline in reverse to obtain this syntactic object and feed it into the LF-pipeline, and production is pretty much the same except it starts with meanings and proceeds in the other direction.

So there you have it: anybody who subscribes to the idea that language involves mapping utterances to meanings and meanings to utterances also subscribes to the T-model.
There's no way around that, it's a mathematical inevitability.
Or is it?


## The baggage of the T-model

The T-model in the bare form of (@tmodel2) is indeed a mathematical inevitability.
But the fact of the matter is that syntacticians have attached many additional factors to the T-model that, in my opinion, are completely orthogonal to it.

One is the separation of syntax and the interfaces.
That is to say, syntax has no insight into what happens in the PF and LF pipelines, and consequently syntax pays no attention to extra-syntactic factors.
This is the exact opposite of the bimorphism perspective.
There, syntax is just a means to an end for linking utterances and meanings, and hence it necessarily knows about all factors that are crucial to this linking.
If the separation of syntax and the interfaces is important to you, the bimorphism view won't ring true to you.

That said, I don't understand why anybody would want to endorse this strict separation.
Even hardcore Minimalists assume that syntax is sensitive to interface requirements, that's what the whole feature interpretability/valuation spiel was about.
It's also very clear that many processes (e.g. scrambling) are at least partially controlled by extra-syntactic factors like prosody and information structure.
A lot of interesting approaches like Contiguity Theory [@Richards16] would be impossible under this strict view.
And at the end of the day, the restriction is formally vacuous anyways because interface constraints can be "backported" to syntactic constraints for pretty much any formalism we have right now.
So, no, this is not a strike against the bimorphism approach, if anything it's a boon that it highlights how shaky the ground is that the separation of syntax and interfaces rests on.

But the bimorphism perspective also has some much more radical implications.
One is that syntax might not exist at all.
For the bimorphism approach, syntax is but an interpolant that we have constructed to simplify the mapping between physical forms and meanings.
It is a useful abstraction, but that does not mean that syntax is a separate component of linguistic cognition.
Anything we can a syntactic constraint would just be a reflex of the rules that govern physical forms, or meanings, or both of them.

If that still sounds off to you, consider the following toy example.
Suppose we have a function $h$ and we know that $h$ gives us the same result as $g(f(x))$, where $f(x) = 2x + 1$ and $g(x) = x - 1$.
Clearly $g(f(x)) = 2x$ for any number $x$.
Does calculating the value of $h(x)$ require us to first calculate $2x - 1$ and then subtract $1$?
No, we can go straight from $x$ to $2x$.
The interpolant $2x + 1$ is never part of the actual calculation, it was just a specific decomposition of $h$ that we had come up with.
The very same could be true for syntax.
In that case, humans map directly between utterances and meanings without ever constructing an intermediate representation that corresponds to what we call syntax.
Syntax is just a useful abstraction for us to make the actual processes easier to specify.

Again, though, I see this is as a boon of the bimorphism perspective.
It completely undermines those imho pointless debates about the role of syntax, whether there's tree structures, and so on.
It's like arguing about whether $2x - 1$ is part of calculating $h(x)$.
Who cares?
We're trying to figure out how $h(x)$ works, and decomposing it to $g(f(x))$ is just the best solution we currently have to offer.
Yes, I know, there's evidence from lesion studies that language enjoys some degree of modularity, but just like any other neural evidence I consider this inconclusive because the linking problem between abstract specification and neural implementation is just so damn hard (if not insurmountable).
And keep in mind that the bimorphism approach is compatible with modularity.
It does not commit you either way.
The two sets we're trying to define mappings for may well be produced by a modular machinery, that does not mean that the interpolant lines up with any of those modules.
Quite generally, I've always believed that ontological commitments only make sense if they come with a significant payoff.
And I don't see how the issue of whether syntax is ontologically real or just a useful abstraction has any bearing on the questions linguists care about.


## Back to the beginning

The last few paragraphs might have rustled some feathers since they're advocating a view that's pretty far from the linguistic mainstream.
The bimorphism approach itself, however, should not be contentious.
It has been proven very useful in formal language theory [@ArnoldDauchet82], and at the end of the day it supports the T-model rather than undermining it.
I always find it neat when two very different lines of thinking converge on the same end result.
And the T-model is a beautiful case where decades of linguistic theorizing have converged with purely mathematical considerations.
At the same time, the mathematical perspective also highlights that the T-model comes bundled with ancillary assumptions that are strictly speaking independent of its core idea.
If you're a fan of the T-model, you may consider those additions indispensable. 
I disagree, but either way the bottom line is that the mathematical view firmly establishes the conceptual core of the T-model as an inevitable baseline.
And that is a point that should be made more often in the literature.


## References
