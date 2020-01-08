---
title: >-
    Corrections to my semantics post
authors:
    - Thomas Graf
date: 2019-01-08
bibliography: references.bib
tags:
    - semantics
    - donkey sentences
    - parsing
---

<!-- START_SUMMARY_BLOCK -->
This is a follow-up to [my previous post on semantics]({filename}2019-12-28_graf_semantics.md).
It has been pointed out to me that this post contains several inaccuracies and grave omissions.
Some of them are in the summary of Lucas' talk, and that would probably have been noticed earlier if I had provided [a link to the slides](http://tr.im/dd74) or [the paper](http://doi.org/dd74).
Thanks to Lucas for sending me those by email and for walking me through the account again.
I'll briefly explain some of the misleading points later on in this post.

But the much bigger issue is that I failed to point out that Lucas wasn't just presenting his own work.
He made it very, very clear that this was joint work with
[Dylan Blumford (UCLA)](https://dylanbumford.com/)
and
[Robert Henderson (UArizona)](https://www.rhenderson.net/).
I'm really upset with myself about that one, in some sense giving partial credit is even worse than giving no credit at all, and the latter is already a dick move.
My sincerest apologies to Dylan and Robert.

If I had run the post past Lucas before publishing it, a lot of this could have been avoided, so I'll make that a priority for future posts that talk about work that I'm not well-acquainted with.
Alright, so let's talk a bit what I got wrong and how that affects the central message of the previous post.
<!-- END_SUMMARY_BLOCK -->


## World knowledge != QUD

This one was already pointed out by [Omer Preminger](https://omer.lingsite.org/) and [Amir Anvari](https://sites.google.com/site/amiraanvari/) in the comments:
world knowledge, context, and question under discussion are distinct things with specific definitions.
They should not be lumped together.
I don't think this affects the overall thrust of the original post, but it does show that I didn't grasp the finer points of the story.


## The account does what I want

The Champollion-Blumford-Henderson account (CBH from here on) is actually an instance of the kind of model that I want, with a very lean semantics that leaves a lot of work to other components.
The overall logic of the architecture is actually similar to Eric Reuland's Minimalist work on syntactic binding.
Reuland says that if a pronoun doesn't get bound in syntax, then it can try to establish binding relations in semantics, and if that doesn't work out, then pragmatics will figure out the antecedent.
CBH has a similar multi-layer machinery.
In cases that are clearly true or false, semantics does all the work.
But when context matters, semantics passes it on to pragmatics, which then fills in the gaps based on the current question under discussion.

That is indeed similar to what I said about how research on parsing is done (or ought to be done).
Consider the two sentences below:

(@single) I gave a movie to Arnold.
(@ambiguous) I watched a movie with Arnold.

Sentence (@single) has only one possible parse, so we don't need to go into the whole hullabaloo of context and world knowledge to pick the right parse.
There's only one choice, and that's the one you have to go with.
Whether Arnold is an actor is completely immaterial.
But (@ambiguous) is ambiguous, and that opens the floodgates of context-dependent choice.

The CBH case is still slightly different because the semantics doesn't fix a specific reading.
Instead, it just decides if the readings even need to be distinguished in order to determine the truth value of the sentence.
If that's not the case, it does all the work by itself.
Otherwise, it's time for pragmatics to do its things.
In parsing terms, CBH is more like a parser that ignores syntactic ambiguity when it cannot affect the semantics.


## So why no mic drop?

Lucas could have actually done the mic drop I expected and said "here's the part that semantics handles, and the rest isn't any of our business".
He didn't do that because the CBH story doesn't need a lot of extra work to also cover the pragmatics part.
A lot of it comes straight from Križ (2016), and that in turn allows CBH to link donkey sentences to the empirical phenomena covered in that work.
It also means that they can make much more specific predictions than if they had just dropped some sentences in the pragmatics trashcan like a used tissue.
This might sound familiar to you, Amir made a very similar point in the comments, but it didn't quite get through to me back then.

In light of these facts, I can now see that I was essentially complaining that Lucas went beyond the call of duty for a semanticist and also presented a worked-out pragmatics.
And that's not a reasonable complaint.
I still find that interesting from a sociological perspective, though.

Suppose I had a story about Heavy NP shift that also includes a specific theory of the syntax-external factors that make an NP heavy.
Perhaps that notion of heaviness builds on some existing theory that has been fruitfully applied to linear orderings of verbal particles.
I'm not so sure that it would be smart to include this part of the proposal in a submission to *Linguistic Inquiry* or *Syntax*.
I can imagine that some reviewers would ask for that to be removed on the grounds that 1) it makes the paper harder to follow, and 2) has nothing to do with syntax proper.
And I'd actually agree with them: that part should go into a separate paper, for a different journal.

Now it would be pretty ludicrous to ask CBH to remove the pragmatics part from their semantics paper considering that it appeared in --- drum roll --- *Semantics & Pragmatics*.
But I wonder if there is any semantics journal that would object to having a detailed pragmatics component in there.
Maybe, maybe not.
Maybe it's like asking a syntax journal to categorically rule out all papers that contain a significant portion of semantics, which isn't commonly done either (is there even one syntax journal that does that?).
Overall this is a point that I still find interesting, but it's neither here nor there.


## And then there's "pre-semantics"

The nice thing about blogging is that it allows me to throw out ideas that aren't fully baked and then see them take shape during the ensuing discussion.
In the case at hand, it should be apparent now that, contrary to my initial impression, the CBH work is actually a bad example of why I don't find semantics all that engaging.
But the discussion with Amir has led me to coin the term "pre-semantics".
It's not a well-defined term yet, but I envision it as the most minimal semantics possible, the very first step in the interpretative pipeline. 
That's something I'll have to think more about.
