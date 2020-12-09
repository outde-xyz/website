---
title: >-
    Three types of generalizations
authors:
    - Thomas Graf
date: 2020-12-10
bibliography: references.bib
tags:
    - methodology
    - reduplication
---

<!-- START_SUMMARY_BLOCK -->
My [post on defossilization]({filename}2020-11-30_graf_fossilizedcomputation.md) prompted an extended debate with Hossep Dolatian --- thx Hossep, it was a joy, and a welcome change from the daily rut.
One of the many points we disagreed on was the role of generalization in linguistic theory.
Yeah, pretty esoteric, but there are some real issues here.
I think there's at least three types of generalization, and we shouldn't lump them together.
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
In a very literal sense, you could think of this as the learner identifying a feature-based rule and then compiling it out to a bundle of segment-based rules.
The result is a system that still expresses the relevant generalization, but it is no longer encoded in the grammar.

Wug tests can be rethought along the same lines.
The grammar doesn't need to encode how to handle new forms.
Instead, the grammar is a generalization-free bundle of rules that require specific diacritics to trigger.
For instance, nouns would be split into different subgroups *noun-z*, *noun-s*, *noun-zero*, *noun-ablaut* and so on, depending on what kind of plural they take.
When confronted with a nonce noun, the learning algorithm's job is to assign it the correct subtype (and perhaps add it to the lexicon for future use).
The way the learner would figure out the right subtype might look very similar to how linguists encode this in the grammar.
So we still have our familiar generalization, but it is in the learner, not the grammar.
Again, zero generalization in the grammar, but the whole system still contains the relevant generalization.


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

But these arguments are all about generalization, and that can be handled in the learner.
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
Generalization is costly.
And when something is costly, you shouldn't use it unless it is worth the cost.
So is generalization worth that cost?


## Three types of generalization

I think there's at least three types of generalization.

1. **M[eta]-generalizations**  
   Those are generalizations that researchers are aware of, but that aren't explicitly encoded in the cognitive machinery.
   For instance, tendencies about how context affects processing aren't explicitly encoded in the human parser, they're an emergent property of its behavior.
   The same goes for things like Zipf's law with respect to word token frequency; that's not a law of the grammar.

1. **F[rugal]-generalizations**  
   Frugal generalizations make the overall system less taxing on cognitive resources.
   For instance, the finite-state machinery you get from the learner's context-free template might be so large that it's easier to just use the original grammar for parsing.
   Similarly, a mildly context-sensitive formalism may provide a more succinct grammatical description than a CFG, and since parsing performance for sentences with less than ~50 words is largely dependent on grammar size, optimizing grammar size is preferable to optimizing grammar complexity.

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


## Grammar VS grammar

As if this topic weren't already esoteric enough, it's further complicated by the ambiguity of the term *grammar*.
From a computational perspective, a grammar is a finite description of a possibly infinite set of objects, which could be strings, trees, graphs, input-output mappings (in the case of synchronous grammars), and so on.
It's what you feed into your parsing schema to get a parsing system, it's what you use to reason about the set of objects, and so on.

The learning algorithm interacts with this notion of grammar but is different.
For instance, strictly local grammars are useful for understanding how a learner could identify a strictly local string language in the limit from positive text, but at the end of the day the knowledge is in the learner, not the grammar.
If the grammars are segment-based instead of feature-based, that doesn't mean that the learner has to be segment-based, it can use higher order reasoning to maneuver the hypothesis space.
There is no direct coupling between the description format of the grammar and the reasoning of the learner.

Most linguists have a richer notion of grammar, something that is more of a general description language, or almost like an API to all aspects of language.
Syntacticians don't write out a learning algorithm or a parsing algorithm, they enrich the grammar with generalizations that are meant to aid learning, processing, and so on.
The grammar is the universal locus of generalization.
SPE is a prime example of that as its description language was also supposed to provide a learning/naturalness metric for phonology.
That's a-okay in my book, from a methodological perspective the kitchen-sink approach can sometimes be easier to work with than having things scattered across many different components, so it's good to have both options on the table.

But when we mathematical linguists engage in the process of analyzing the computational complexity of grammars and linguistic phenomena, we should take care to disentangle the different types of generalizations that theoretical linguists put in their grammars.
If putting an L-generalization into the grammar changes the complexity picture, that is not the same thing as an F-generalization increasing complexity.
One can be jettisoned for more efficient processing, the other can't.
And if your complexity claim hinges on an M-generalization, then it really tells us very little about language as a cognitive object.

That doesn't mean that only F-generalizations are fair game, or that we can ignore complexity in the learner --- heck, there might not be a cognitive difference between the grammar and the learner, just like there might be no difference between the grammar and the parser.
The complexity of building a grammar (the learner's job) is just as important as grammar complexity, but the two are not equally important for each task.
In the total reduplication example above, something has to build those finite-state automata, and the complexity of that process is what people have in mind when they say total reduplication is not finite-state.
But that is a one-time cost, so if you want an efficient processing system that can handle reduplication, you can pay that cost once in a precompilation step and after that you won't have to pay it again until a new entry needs to be added to the lexicon.
The cost of L-generalizations doesn't need to be paid all the time, you can take care of it once and then forget about it.


## A sloppy wrap-up

So that's where my thinking is at this point regarding generalizations.
As I said, I don't know how far I want to push this.
I'm pretty sure it can lead to some absurd results when applied indiscriminately.
My wishy-washy take-home message for now:
All I'm saying is that our current approach to how we treat generalizations is very free-wheeling and unstructured, and a few basic distinctions would provide us with a more nuanced picture.
