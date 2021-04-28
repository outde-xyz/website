---
title: >-
    Discovering Martin Haspelmath's blog
authors:
    - Thomas Graf
date: 2021-04-28
bibliography: references.bib
tags:
    - methodology
    - universals
---

<!-- START_SUMMARY_BLOCK -->
Unbecoming at it may be for a blogging linguist, I am not particularly familiar with the overall blogosphere in linguistics.
As a dedicated Twitter & Facebook hermit, I am perpetually out of the loop, and I like it that way.
So it is only recently that I have become aware of [Martin Haspelmath's long-running blog](https://dlc.hypotheses.org/), thanks to [a post by David Adger](https://davidadger.org/2021/04/08/are-generative-grammarians-abandoning-innateness/).
There's tons of posts, but based on the limited sample I've read so far, it seems that most revolve around one of three issues: terminology, innateness, and peer-review.
I think the latter is actually the most interesting, but for the sake of ~~completeness~~ self-indulgence, I'll add my \$0.02 regarding the first two, leaving peer-review for a separate post.
<!-- END_SUMMARY_BLOCK -->


## Terminology

Haspelmath frequently talks about how X should actually be called Y or Z.
By [his own admission](https://dlc.hypotheses.org/989), he keeps "insisting on careful use of terminology in linguistics".
One terminological quibble that keeps coming up is why [*typology* should be called *comparative linguistics*](https://dlc.hypotheses.org/1915).
Many of the problems with his specific terminological proposals have already been pointed out in the comments there, and I don't have much to add on those.
I'll just take a moment to link to [xkcd](https://xkcd.com/927/) and [smbc](https://www.smbc-comics.com/comic/definition), which succinctly point out the real problem with such terminological musings.

But since this is the outdex, where absolutely everything has to circle back to computation, let's look at a recent case of such terminological confusion.
Some of you might have heard of *sequential functions*, which are a subtype of finite-state transductions.
It doesn't matter here how they work or what they do.
The important thing is that a sequential function is a finite-state transduction that satisfies a number of conditions.
If we weaken one of those conditions, we get the more powerful class of *subsequential functions*.
They are **sub**sequential because the conditions they meet form a **sub**set of the conditions met by sequential functions.
But of course this means that the class of **sub**sequential functions is a **super**set of the class of sequential functions, rather than a **sub**set.
Can you see where this is going?
Some researchers felt that this is unintuitive and have started calling subsequential functions sequential, and sequential functions subsequential.
The end result of that well-intended change in terminology is that now I never know what type of function people are actually talking about.

Yes, yes, you could argue that it's just temporary growing pains and the end state will be better for everyone involved, like the shift from Python 2 to Python 3.
Except that if we go through all those growing pains, perhaps it should be for terminology that isn't just as broken:
If we ever define a class that lies properly between subsequential and sequential (in that new terminology where the latter are more powerful), we will have a class that, although a subset of the sequential functions, contains some functions that are not subsequential.
Wonderful!

Bottom line: terminology is messy, cannot be regulated in a top-down manner, and meddling with it makes things worse.


## The grammar blueprint

Continuing the previous point, I am not a fan of the term *grammar blueprint* that Haspelmath uses for UG.
To me, a blueprint is the very opposite of a large space of options with tremendous variation within.
It makes me think of programming cookbooks like *Go Programming Blueprints*, which focus less on the programming language itself and more on prepackaged solutions to common problems.
But whatever, I know what he's referring to, it's his blog, not mine, and this isn't really what I find confusing about his take on UG.

Haspelmath argues that the post-[@Chomsky05] idea of a minimal UG undermines the universalist methodology of Minimalism, where it is still assumed that languages are largely the same (e.g. same functional projections) and that insights can be meaningfully transferred between languages.
This is what the debate with Adger is about, and Haspelmath also has earlier exchanges with other linguists that touch on this, e.g. [Gillian Ramchand](https://dlc.hypotheses.org/1811) and [Elena Anagnostopoulou](https://dlc.hypotheses.org/2205).
There's a few other posts that I think are informed by this view, e.g. [Haspelmath's evaluation of Laura Kalin's work on DOM](https://dlc.hypotheses.org/1496), which got an in-depth reply on [Philosophy of Linguistics](https://philosophyoflinguistics618680050.wordpress.com/2018/11/06/what-means-understanding-differential-object-marking-a-reply-to-haspelmath/) (another blog I was unaware of).
Overall, a lot of ink has been spilled, and it is not clear to me why:

Haspelmath says that current Minimalist work makes sense under a rich-UG view, but not under a small-UG view.
But with respect to the work being done, the two are interchangeable.
Here is the reasoning chain under a rich-UG view:

- **Assumption 1 (rich)**: Language is an innate ability.
- **Assumption 2 (rich)**: Innateness includes structural projections, categories, and so on.
- **Corollary (rich)**: Insights from one language can be transferred to other languages.

And here is what it looks like under a small-UG view:

- **Assumption 1 (small)**: Language is an innate ability.
- **Assumption 2 (small)**: Insights from one language can be transferred to other languages.

The only thing that has changed is that **Assumption 2 (rich)** is gone and **Corollary (rich)** has been upgraded to the status of an assumption.
But for anything downstream the reasoning chain, it doesn't matter whether transferability is an assumption or a corollary of an assumption.
As far as the methodology is concerned, it makes no difference.

Now if you want to get into the weeds of whether **Assumption 2 (rich)** is more plausible than **Assumption 2 (small)**, i.e. ontological commitments, knock yourself out.
I will point out, though, that

1. scientific assumptions have to be useful, not plausible, and
1. **Assumption 2 (small)** has more support than **Assumption 2 (rich)** in the sense that if we consider the space of axioms that have one of those assumptions as a corollary, the space for **Assumption 2 (small)** is larger than that for **Assumption 2 (rich)**.

But I really shouldn't have brought up those ancillary points, because the only thing that matters methodologically is that none of this matters.
The cognitive issues may be what motivates the program, but the analytical work is largely independent of that.
There's a reason why virtually all Minimalist textbooks include some spiel about the learning problem, syntax as a cognitive science, language as window into mental computation, yada yada yada, yet barely any of them contain a chapter on parsing, learnability, or computation (one notable exception being Sportiche, Koopman, and Stabler' *An Introduction to Syntactic Analysis*, and the list of authors should give you a clue how the computational chapter made it in).
I've [complained about that before]({filename}2020-01-31_graf_modern_syntax_textbooks.md), but that's the way things are.
And because that's the way things are, a Minimalist's analytical work does not hinge on any particular conception of UG.


## References
