---
title: >-
    Three types of generalizations
authors:
    - Thomas Graf
date: 2020-12-14
bibliography: references.bib
tags:
    - methodology
    - reduplication
---

<!-- START_SUMMARY_BLOCK -->
My [post on defossilization]({filename}2020-11-30_graf_fossilizedcomputation.md) clearly wasn't esoteric enough, so I'm upping the ante by turning to one of the most esoteric and ephemeral issues in linguistic theory.
Yes, we're gonna talk about generalizations and what their role ought to be in how we do linguistics.
Since it's a long post even for outdex standards, I'll give you a tldr: I think there's at least three types of generalization, and we shouldn't lump them together.
<!-- END_SUMMARY_BLOCK -->


## We want generalizations

Let's get to the obvious point right away: generalizations are essential for linguistics.
There's two reasons for that.
One is purely utilitarian: generalizations make broad empirical predictions and keep the theory simple, both of which support scientific inquiry.
The other reason is the empirical true-ism that language requires generalization.
The infant has to generalize from a finite data sample to an infinite one, native speakers have to generalize linguistic laws to nonce forms, and so on.
If the object of study necessarily involves generalizations, then our theory of the object shouldn't be missing them.
But where in our theory should the generalizations come from?


## Learner VS grammar

Traditionally, linguists encode generalizations directly in the grammar.
For instance, word-final devoicing isn't a collection of segment-based rewrite rules like
$$
\textit{z} \Rightarrow \textit{s} \mid \_ \$
$$
and
$$
\textit{v} \Rightarrow \textit{f} \mid \_ \$.
$$
Instead, we have a single feature-based rule
$$
[+ \textit{voice}] \Rightarrow [- \textit{voice}] \mid \_ \$
$$
or something along those lines.
That's easier to make sense of, and it explains why word-final devoicing tends to target a natural class of segments, rather than an arbitrary list of some voiced segments.

But this doesn't actually need to be in the grammar, it can be handled in the learning algorithm.
Suppose that the learner actually infers grammars that use segment-based rewrite rules, but in identifying the correct target grammar is relies on notions of natural classes that are similar to what we have in the feature-based rule.
Then the learner would be using a kind of meta-reasoning that is not directly encoded in the grammar.
In a very literal sense, you could think of this as the learner identifying a feature-based rule and then compiling it out to a bundle of segment-based rules, but that's probably too literal because learners can reason in much more abstract ways that consider the structure of the entire hypothesis space and aren't tied to a specific way of representing rules.
Either way the result is a system that still operates according to the relevant generalization, but the generalization is no longer encoded in the grammar.

Wug tests can be rethought along the same lines.
The grammar doesn't need to encode how to handle new forms.
Instead, the grammar could be a generalization-free bundle of rules that require specific diacritics to trigger.
For instance, nouns would be split into different subgroups *noun-z*, *noun-s*, *noun-zero*, *noun-ablaut* and so on, depending on what kind of plural they take.
When confronted with a nonce noun, the learning algorithm's job is to assign it the correct subtype (and perhaps add it to the lexicon for future use).
The way the learner would figure out the right subtype might look very similar to how linguists encode this in the grammar.
If so, then we'd still have our familiar generalization, but it would be in the learner, not the grammar.
Again, zero generalization in the grammar, but the whole system still obeys the relevant generalization.


## Grammars without generalization are simpler

Okay, at this point you're probably wondering what the freaking point is, we're just shifting around generalizations between two abstract entities --- learner and grammar --- that might not be cognitively distinct to begin with.
And you're essentially right.
But follow along for a bit more, this little thought experiment will teach us something important about generalizations: they're costly.

Let's look at total reduplication.
People usually claim that total reduplication cannot be handled by finite-state automata.
But that claim only holds with respect to a larger framework of assumptions.
For any given word, total reduplication can be made part of its representation.
Here's a lexical entry for *cat* that also allows for the total reduplicant *cat cat*:

![Reduplication in a finite-state automaton]({static}/img/thomas/generalization_types/reduplication.svg)

Do this with all words that can undergo total reduplication, and you have a grammar that generates all the correct surface forms, including reduplicated ones.
Hmm, so total reduplication can be handled with finite-state machines after all.

Now of course there's a huge array of arguments for why this is a dumb way to do it:

1. This doesn't work for nonce forms.
1. We could have just as well written down a representation that builds palindromes.
1. We could limit reduplication to words that contain a prime number of consonants.
1. ... and so on.

But these arguments are all about generalization, and, at the risk of repeating myself, that can be handled in the learner.
The learner could have a specific reduplication template for creating those representations.
Feed in a word, get out an FSA-representation that also allows for reduplication.
Then the concerns above disappear:

1. This template can be applied to a nonce form just like a total reduplication rule would be in the grammar-based view of standard linguistics.
1. The template could be limited so that it cannot build palindromes.
1. The template might not be able to detect if the number of consonants is prime.
1. ... and so on.

And this leaves us with a system that contains the relevant generalizations yet uses finite-state machinery for total reduplication.

By the way, the same can be done in syntax.
Maybe the grammar is just a finite-state device that is built from a mildly context-sensitive system, with a fixed cut-off point on unbounded constructions.
Maybe the cut-off point is usually set to a low value like 3, but when you really hunker down and spend a lot of resources on understanding a more complex sentence, the learner produces a new finite-state grammar on the fly with a higher cutoff point.

In both cases, these compiled out grammars are less powerful than the template they're created from.
And that's because they do not have to carry the burden of generalization.
What this tells us is that generalization is costly.
And when something is costly, you shouldn't use it unless it is worth the cost.
So is generalization worth that cost?


## Three types of generalization

I think there's at least three types of generalization.

1. **M[eta]-generalizations**  
   Those are generalizations that researchers are aware of, but that aren't explicitly encoded in the cognitive machinery.
   For instance, tendencies about how context and memory load affects processing aren't explicitly encoded in the human parser, they're an emergent property of its behavior.
   The same goes for things like Zipf's law, which is a statement about the relation between word types and word token frequencies; that's an interesting generalization, but it's not a law of the grammar.

1. **F[rugal]-generalizations**  
   Frugal generalizations make the overall system less taxing on cognitive resources.
   For instance, the finite-state machinery you get from the learner's context-free template might be so large that it's easier to just use the original grammar for parsing.
   Similarly, a mildly context-sensitive formalism may provide a more succinct grammatical description than a CFG, and since parsing performance for sentences with less than ~50 words is largely dependent on grammar size, optimizing grammar size is preferable to optimizing grammar complexity.
   Or a specific phonological phenomenon may be actually SL-5 in a given language, but if you generalize to strings of unbounded length you get a much more succinct TSL-2 description.

1. **L[earner]-generalizations**  
   These are generalizations that pertain to the whole class of natural languages.
   Most linguistic generalizations are of this form.
   Going back to the example of word-final devoicing, the reason linguists prefer the feature-based rewrite rule is because of what it says about the space of possible devoicing processes.
   If you only consider a single fixed language, there is no difference between the feature-based rule and the segment-based one.

Side-note: Depending on your ontological commitments, everything may be a meta-generalization.
If you think language is a chaotic cacophony of neurons firing according to the laws of physics, then everything is an emergent property.
But even then it is methodologically useful to distinguish between M-generalizations, F-generalizations, and L-generalizations.

Now I haven't quite figured out how far it makes sense to push this, but it seems to me that these three types of generalizations should be approached in very different ways.
F-generalizations are prime candidates for generalizations that should be encoded directly in the grammar because they are useful for the stuff that builds on the grammar, i.e. parsing and production.
L-generalizations have the super-creative name they do because I think they can reasonably be outsourced to the learner.
And M-generalizations have no business being in either the grammar or the learner.


## L-generalizations and complexity

I don't think many readers of this prestigious blog would complain about keeping M-generalizations out of the grammar, nor would there be an uproar against keeping F-generalizations in the grammar.
The tricky one is L-generalizations, in particular if we put on our generative capacity hat (if you don't own one, you may borrow mine for a few minutes).

When mathematical linguists make claims of the form "phenomenon X is at least in complexity class C", those claims often build on hidden L-generalizations.
A good example of that is the claim in @Jardine15 that unbounded tone plateauing is not weakly deterministic (what exactly this means is completely irrelevant for my point, so don't worry about the fancy terminology).
As a blanket claim about how unbounded tone plateauing works, the statement is correct.
But once you look at the individual languages that exhibit unbounded tone plateauing, each one displays a confound that makes the phenomenon weakly deterministic in this language.
The confounds differ across languages, but each one invariably displays such a confound.
Maybe that's a coincidence.
Or maybe it's something fundamental: maybe L-generalizations are allowed to exhibit a certain level of complexity, but in the end it must all compile out to a system whose complexity does not exceed some much lower complexity threshold.
Basically this: "Hey learner, grammar here! If you want to get all fancy-schmancy with your high-brow pie in the sky stuff, that's cool, different strokes for different folks. But in the end please break it down to simple principles I can actually enforce."

I've been idly toying with the idea that something along those lines may be going on with reduplication.
Reduplication tends to be subject to additional constraints and restrictions, it's rarely a straight-forward affair.
There's restrictions on what kind of stems can get reduplicated, what can be targeted by partial or total reduplication, and so on.
I won't pretend to have a good command of the empirical landscape on reduplication, but the impression I got from several discussions with Hossep Dolatian is that it's all pretty convoluted.
That's in stark contrast to the current models of reduplication, which are very elegant.
Too elegant, perhaps.
It makes me wonder why reduplication isn't a much more free-wheeling operation, something every language throws around left and right in a very principled manner without many exceptions or additional restrictions.
Well, the culprit could be a hidden L-generalization.
If you look at all the cross-linguistic reduplication data as a single, natural phenomenon that requires a single, unified model, then you're dealing with something fairly complex.
But maybe things are different if we consider each language in isolation.
Maybe each language has enough confounds that allow us to come up with something less complex, albeit more convoluted.

I have no idea if that's a plausible scenario.
But it's a scenario that I find highly fascinating, largely because it would put a new spin on overgeneration.
Once you have a computational model an attested phenomenon, you invariably also have the power to handle other phenomena that are not attested.
Why, then, don't those occur?
It could be that the attested phenomenon differs from those unattested phenomena in that it can be reduced to something much simpler once we cut out the L-generalization and look only at the language in isolation.
Mathematical linguistics isn't well-equipped to pursue this idea at this point.
This perspective requires keeping track of all idiosyncratic properties of the language, which means a lot of moving pieces (some of which we may be unaware of because of missing data).
The more moving pieces, the harder it is to construct a proof --- you quickly reach a point where you're better off running simulations, and that has its own giant bundle of drawbacks.


## Grammar VS grammar

As if this topic weren't already esoteric enough, it's further complicated by the ambiguity of the term **grammar**.
From a computational perspective, a grammar is a finite description of a possibly infinite set of objects, which could be strings, trees, graphs, input-output mappings (in the case of synchronous grammars), and so on.
It's what you feed into your parsing schema to get a parsing system, it's what you use to reason about the set of objects, and so on.
This is how I've been using the term **grammar** in this post so far.

The learning algorithm interacts with this notion of grammar but is different.
For instance, strictly local grammars are useful for understanding how a learner could identify a strictly local string language in the limit from positive text, but at the end of the day the knowledge is in the learner, not the grammar.
If the grammars are segment-based instead of feature-based, that doesn't mean that the learner has to be segment-based, it can use higher order reasoning to maneuver the hypothesis space.
There is no direct coupling between the description format of the grammar and the reasoning of the learner.

Most theoretical linguists have a richer notion of grammar, something that is more of a general description language, or almost like an API to all aspects of language.
Syntacticians don't write out a learning algorithm or a parsing algorithm, they enrich the grammar with generalizations that are meant to aid learning, processing, and so on.
The grammar is the universal locus of generalization.
SPE is a prime example of that as its description language was also supposed to provide a learning/naturalness metric for phonology.
That's a-okay in my book, from a methodological perspective the kitchen-sink approach can sometimes be easier to work with than having things scattered across many different components, so it's good to have both options on the table.

But when we mathematical linguists engage in the process of analyzing the computational complexity of grammars and linguistic phenomena, we should take care to disentangle the different types of generalizations that theoretical linguists put in their grammars.
If putting an L-generalization into the grammar changes the complexity picture, that is not the same thing as an F-generalization increasing complexity.
One can be jettisoned for more efficient processing, the other can't.
If you're making a claim about the complexity of a cross-linguistic phenomenon, that does not mean that there is a single language where the phenomenon is actually that complex.
And if your complexity claim hinges on an M-generalization, then it really tells us very little about language as a cognitive object.

## A sloppy wrap-up

Let me wrap up with a point of clarification: I'm not saying that only F-generalizations are fair game and L-generalizations should be excised from mathematical linguistics.
Nor that we can ignore complexity in the learner --- heck, there might not be a cognitive difference between the grammar and the learner, just like there might be no difference between the grammar and the parser.
The complexity of building a grammar (the learner's job) is just as important as grammar complexity, but the two are not equally important for each task.
In the total reduplication example above, something has to build those finite-state automata, and the complexity of that process is what people have in mind when they say total reduplication is not finite-state.
But that is a one-time cost, so if you want an efficient processing system that can handle reduplication, you can pay that cost once in a precompilation step and after that you won't have to pay it again until a new entry needs to be added to the lexicon.
The cost of L-generalizations doesn't need to be paid all the time, you can take care of it once and then forget about it.

Similarly, we should not mistake L-generalizations with claims about specific processes in specific languages.
Language is a biological system.
Biology tends to be messy, and it tends to implement the same idea in many different ways.
Suppose a linguist from the future were to show up on your door step and tell you that there actually is no such thing as reduplication, and in fact it's a cluster of language-specific processes that are all distinct yet look the same at a sufficient level of abstraction.
Would you be shocked?
I wouldn't.
It's a useful piece of information that does not undercut the idea of reduplication as something worth studying at various levels of generalization.
We just have to make sure we know which level our theorems operate at.

## References
