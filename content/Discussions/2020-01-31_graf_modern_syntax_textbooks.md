---
title: >-
    Hey syntax, where's my carrot?
authors:
    - Thomas Graf
date: 2020-01-31
bibliography: references.bib
tags:
    - syntax
    - textbooks
    - teaching
---

<!-- START_SUMMARY_BLOCK -->
Last week I [blogged a bit about syntax textbooks]({filename}2020-01-22_graf_syntax-textbooks.md).
One question I didn't ask there, for fear of completely derailing the post, is what should actually be in a syntax textbook.
There's a common complaint I hear from students about syntax classes, and it's that syntax courses are one giant bait-and-switch.
They're right, and it's also true for syntax textbooks.
<!-- END_SUMMARY_BLOCK -->


## The bait-and-switch

Be it a class or a textbook, a student's first encounter with syntax usually starts with all that interesting big-picture stuff like UG, the puzzle of language acquisition, the poverty of the stimulus, the surprising complexity of sentences given how easy it is for us to process and interpret them, and so on.
And then, after week 2, when they can no longer drop the class without major paperwork, or when they've bought the book after finding the first chapter really interesting, we bring out constituency tests, c-command, raising VS control, all that technical nitty-gritty.
At the end of the semester, the students can (hopefully) analyze a bunch of English constructions and draw a bunch of tree structures.
But they don't have an inkling of understanding how any of those sentences may be parsed and how that maps to actual human sentence processing;
they have no idea how the grammars they wrote down could be learned;
they don't know if UG has anything concrete to say about language acquisition;
they have no opinion on basic issues like the pros and cons of corpus methods;
and they certainly didn't get to experiment with corpora on their own to see if they can answer the questions they're interested in.
From their perspective, it's a giant scam.
We keep dangling the cognitive-computational carrot in front of them, but all they ever get is the syntactic analysis stick.

What's puzzling is that things no longer need to be this way.
Yes, in the 80s we didn't have robust parsing algorithms for GB, there wasn't a lot of work on learning these grammars, and psycholinguistics was still a niche affair compared to nowadays.
It was all aspiration with little concrete to show for it.
This has changed, and there's now plenty of work that could be included in a syntax introduction.


## What could be discussed in a modern syntax class

Let's start with learnability and language acquisition.
One obvious choice for a syntax course that operates in the framework of Principles-and-Parameters is @Yang02 and the work that followed from that.
It builds directly on the idea of UG and parameters, it allows you to model actual phenomena in language acquisition, and the math is fairly simple.
It would also be instructive to contrast that approach against the Trigger algorithm and all the problems it faces [@NiyogiBerwick93; @BerwickNiyogi96].
And then there's all the work coming out of the grammatical inference and machine learning world.

Mind you, I'm not saying that syntacticians have to endorse any of that work, but an intro course should engage with it.
If acquisition is the initial hook for talking about syntax, that theme should be explored in depth, even if the conclusion is that these models fall short in some respects.
For instance, one could point out the frequent mismatch between the assumed learning paradigm and language learning in the real world.
And there's a lot of nice work right now on how neural networks fail to generalize in a human-like fashion.
There's enough to fill multiple chapters without even getting all that deep into the math and computation.

The same is true for parsing.
Any class on Minimalism will inevitably run into the question how those trees can be built up if processing and production proceeds left-to-right and hence top-down.
That prompts the usual discussion of the competence-performance distinction, and that is certainly a good thing to get into students' heads: syntactic derivations  are not a literal description of the production/comprehension assembly line.
But it's also a good time to point out that

1. left-to-right processing does not imply top-down parsing (because bottom-up can proceed left-to-right, too), and
1. there are top-down parsing algorithms for Minimalism, and they're actually fairly simple.

Heck, just discussing what is and isn't a parsing algorithm would be tremendously valuable.
And then there's the whole mine field of islands and whether they are grammatical constraints or processing effects.

Corpus linguistics is a touchy subject, but again one that I think shouldn't be swept under the rug.
It's only natural for students to ask if syntax has anything to say about preferences rather than just well-formedness.
The honest answer to that is that some people are trying to do that with probabilities they get from corpora, at which point students would probably be eager to try for themselves how well that works.
That's a great moment to bring out the Penn treebank and let them hack away.
And then there's an extensive discussion to be had about why the structures in the Penn treebank look so different from what's covered in the class and how that affects the validity of corpus-based claims.


## Syntax is syntax is syntax

I could go on, but I think you catch my drift.
There's plenty of work nowadays that hashes out the ambitious claims that syntax courses and textbooks start with.
Yet there's no syntax textbook that makes this work an **integral** part of its design.
The focus is purely on syntactic analysis and the technical machinery of `$current_year`.
The basic formula hasn't changed in decades.
It imprints the next generation of researchers with a very narrow view of what it means to do syntax:
A syntactician who combines their analysis with a learning model like Charles Yang's is not a syntactician but a computational linguist.
A syntactician who tests the predictions of their analysis with data from sentence processing is not a syntactician but a psycholinguist.
Most peculiar, and imho a disservice to the field of syntax.
