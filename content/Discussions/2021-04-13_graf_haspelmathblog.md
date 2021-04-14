---
title: >-
    Discovering Martin Haspelmath's blog
authors:
    - Thomas Graf
date: 2021-04-13
bibliography: references.bib
tags:
    - publishing
    - methodology
    - universals
---

<!-- START_SUMMARY_BLOCK -->
Unbecoming at it may be for a blogging linguist, I am not particularly familiar with the overall blogosphere in linguistics.
As a dedicated Twitter & Facebook hermit, I am perpetually out of the loop, and I like it that way.
So it is only recently that I have become aware of [Martin Haspelmath's long-running blog](https://dlc.hypotheses.org/), thanks to [a post by David Adger](https://davidadger.org/2021/04/08/are-generative-grammarians-abandoning-innateness/).
There's tons of posts, but based on the limited sample I've read so far, it seems that most revolve around one of three issues: terminology, innateness, and peer-review.
The first two I didn't get much out of, but the latter is on to something.
For the sake of ~~completeness~~ self-indulgence, I'll quickly address the first two, but I mostly want to talk about the peer-review business.
If you're impatient, just skip to the end for an outdex-related announcement of medium importance.
<!-- END_SUMMARY_BLOCK -->


## Terminology

Haspelmath frequently talks about how X should actually be called Y or Z.
By [his own admission](https://dlc.hypotheses.org/989), he keeps "insisting on careful use of terminology in linguistics".
Examples include why [*typology* should be *comparative linguistics*](https://dlc.hypotheses.org/1915)
Many of the specific problems with his specific terminological proposals have already been pointed out in the comments there.
But imho the more fundamental issue has already been astutely pointed out by [xkcd](https://xkcd.com/927/) and [smbc](https://www.smbc-comics.com/comic/definition).

Since this is the outdex, where absolutely everything has to circle back to computation, let me point out one recent case of such terminological confusion.
Some of you might have heard of *sequential functions*, which are a subtype of finite-state transductions.
It doesn't matter here how they work or what they do.
The important thing is that a sequential function is a finite-state transduction that satisfies a number of conditions.
If we weaken one of those conditions, we get the more powerful class of *subsequential functions*.
They are **sub**sequential because the conditions they meet is a **sub**set of the conditions met by sequential functions.
But of course this means that the class of **sub**sequential functions is a **super**set of the class of sequential functions, rather than a **sub**set.
Can you see where this is going?
Some researchers felt that this is unintuitive and have started calling subsequential functions sequential, and sequential functions subsequential.
The end result of that well-intended change to terminology is that now I never know what type of function people are actually talking about.

Yes, yes, you could argue that it's just temporary growing pains and the end state will be better for everyone involved, like the shift from Python 2 to Python 3.
Except that if we go through all those growing pains, perhaps it should be for terminology that isn't just as broken:
If we ever define a class that lies properly between subsequential and sequential (in that new terminology where the latter are more powerful), we will have a class of functions that form a subset of the sequential functions but a superset of the subsequential functions.
Just wonderful!

Bottom line: terminology is messy, cannot be regulated in a top-down manner, and any meddling with it is unlikely to actually improve things.


## The grammar blueprint

Continuing the previous point, I am not a fan of the term *grammar blueprint* that Haspelmath uses for UG.
It's a change for the sake of change.
It's not an improvement because a blueprint is the very opposite of a large space of options with tremendous variation within.
But whatever, I know what he's referring to, and it's his blog, not mine, so fair enough.

Anyhoo, Haspelmath argues that the post-[@Chomsky05] idea of a minimal UG undermines the universalist methodology of Minimalism, where it is still assumed that languages are largely the same (e.g. same functional projections) and that insights can be meaningfully transferred between languages.
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

But I really shouldn't have brought up any of that, because the only thing that matters methodologically is that none of this matters.


## Peer-review

Okay, we've finally reached the topic that I found most interesting: peer review, be it for conferences, journals, or grants.
Haspelmath has [an](https://dlc.hypotheses.org/1138) [impressive](https://dlc.hypotheses.org/1070) [number](https://dlc.hypotheses.org/545) [of posts](https://dlc.hypotheses.org/2333#more-2333) on the topic.
The tldr is that reviews are a waste of time for reviewers, do not improve the final paper or proposal (e.g. because authors have to tack on extraneous stuff to please reviewers), and incentivize flashy presentation over substance.
There's a lot in there, enough for a whole series of posts on my own.

First, let me make it clear that I do not share Haspelmath's general stance on reviews as my own experience has been much more positive.
Perhaps that's because I'm in a subfield of linguistics where most of the issues he describes do not come up all that often:

1. Conferences are paper-reviewed, not abstract-reviewed.
1. With math-heavy papers, the criteria are pretty dry'n'cut: are the definitions internally consistent, are the proofs correct, is the writing clear enough that one can understand what the authors are doing and why it matters?
1. As a result, reviews are never nasty.
   In almost 15 years in the field now, I never got a nasty or overly imposing review when submitting to a computational conference.
   Errors and typos are politely pointed out, and the reviewers sometimes offer presentation tweaks or suggestions for related issues that might be discussed.
1. The authors are expected to revise the paper based on the reviews, but for conference proceedings there's no second round of reviewing.
   You made the cut, you're given an opportunity to make the paper as good as you can based on the feedback you got, and that's it.

When I submit to a linguistics journal, I tend to get formally minded reviewers who share that culture, so it's usually very laid back.
This leaves only the complaints about grant reviewing, and that's a lost cause --- if you're telling a giant bureaucratic machine like the NSF or the ERC that it should abandon its key mechanism of responsibility deferral, you might just as well tell the wind not to blow.

My personal experiences notwithstanding, I think Haspelmath is largely on point, and I would actually say he's not going far enough: the main issue isn't with peer review, it's with our outdated notion of journals.
Journals originally served a triple-role, which then grew into a quadruple-role:

1. They allow researchers to share their work within their community.
1. They direct the community towards work that they should be reading.
1. They take care of archiving, indexing, and so on.
1. They have an insane ROI for commercial publishers.

Except for the publishers and their shareholders, nobody should really care about the fourth point, so let's take that out of the equation.
What about the remaining three points?
I'd say that 1 and 3 are completely obsolete, and journals are doing a bad job with respect to 2 exactly because they still think of themselves primarily as distribution channels instead of aggregators.

Clearly journals are no longer needed to get your work out as there's tons of online platforms for just that purpose, e.g. lingbuzz.
The platforms have features that journals necessarily lack, for instance the ability to publish updated versions, public debate about problems with the paper, and typesetting the paper exactly the way the author wants to.
The latter should not be underestimated: journals like to pile on corporate branding crud like what capitalization and orthography to use, where to put commas, and what captions should look like.
I think everybody has a horror story about the hours they've wasted on copy-editing and/or fixing mistakes introduced by a well-meaning copy-editor.
And the publishers then double down on that with additional busywork like ORCIDs, stuff that makes their life easier but serves no purpose for authors.
Quite simply, journals as a means of distribution provide little added value, in particular if your tech skills go beyond using a word processor.[^unfair]
If it weren't for the fact that we have to publish in journals, most researchers probably would not do it nowadays.

[^unfair]: And this is where somebody will point out things like conversion to html and epub, but they're not exactly using magic there. If an author wants to go the multi-format route, they can use something like pandoc and convert their documents to pdf, html, epub and much more. There's a learning curve because there's no such thing as a free lunch, but the difference is that you master that learning curve once, whereas you have to deal with copy-editing with every paper you write.

Ah, but what about point 3, archiving and indexing and all that annoying stuff?
To be honest, I never understood what exactly it is journals are supposed to be doing there.
I still have to check my Google Scholar profile on a regular basis to make sure new papers have been added (spoilers: I'm lazy, so I don't do it on a regular basis).
Once it's in Google Scholar, any search engine can pick it up.
So whatever indexation is actually going on, it should be little more than a script that scrapes information from Google Scholar and similar services (he said in total ignorance of the complexities involved).
And with archiving, things are even more opaque.
True, journals currently keep paper copies of every published paper, and they have the PDF online with an associated DOI pointing to the correct URL.
But those are private servers of for-profit companies.
If Elsevier goes belly up, is there any guarantee that the servers won't just be shut down and all the papers are lost?
If Blackwell decides it no longer wants to be in the publishing business, is there anything we can do except appealing to their good will to keep those journal websites up and running?
Some universities are very aware of this issue, and that's why they now ask faculty to upload their papers into university repositories.
I think that's the wrong solution because it once again means extra work for researchers with few immediate advantages.
You know what we could do instead: every researcher who makes a decent salary buys a 12TB hard drive for \$200 (I'm looking forward to rereading this post in 2030 and laughing at the outrageous price).
Pro-tip: you can get even better deals on [March 31, which is world backup day](http://www.worldbackupday.com/en/).
And then each one of us mirrors the platform of their choice on a daily basis, be it arxiv, lingbuzz, or whatever, with incremental backups.
Boom, thousands of distributed, version-controlled backups, much better than what a single company could ever offer.
And you have a local copy that you can index with a desktop search engine, feed into a classifier so that it can automatically recommend papers to you, and much more.
Yes, there's a few wrinkles, and we could get bogged down in the technical details for hours.
But the crucial point is that all the necessary technology for archiving already exists, we just have to get off our butts and actually use it, rather than hoping that publishers will do it for us.

So that leaves us with point 2, highlighting important work.
In modern parlance, we would call this an aggregator, and this is exactly the role journals should fill.
They shouldn't be in the business of distributing papers, or copy-editing them, or archiving them, or entering them in various indexing services (why do those indexing services get to outsource their work to journals anyways?).
A journal's only job should be to point out high-quality papers.
It should be like a seal of quality that gets attached to a paper: "ooh, this got featured on LI's ticker, I should really check this out."
And do you notice something?
In this wonderful world of journals as aggregators, there is no reason why a paper should be connected to a single paper.
Maybe NLLT and Phonology also consider the paper top-notch work that they want to give a shout-out.
A paper could be featured in multiple journals.
In that case, it would also be fine for journals to contact an author with a note that their reviewers recommended featuring this paper, under the condition that X, Y, and Z are addressed.
Depending on what the requested changes are, an author may either incorporate them or just leave the paper as is because many other journals are happy to pick it up in its current form.
And maybe they don't care about journals at all because the paper already got thousands of downloads, multiple paper replies, and is all the rage on the social media platform *du jour*.

## An outdex announcement of medium importance

This is how the world ought to be according to Thomas the Cantankerous.
Obviously is not like this because science doesn't happen in an institutional vacuum and those institutions are, at best, resilient to change and, at worst, actively incentivized against such a system of distributed science.
But since I have recently outgrown my teenage attitude that complaining about the status quo is a equally valid alternative to fixing the status quo, I'm actually willing to put my money where my mouth is.
Well, not so much money as my time, but time is money, so, yeah, money.
More concretely:

1. I will start using the outdex as an aggregator of just that kind.
   Most of my outdex posts are more like my personal idea sketch board, or pretty straight-forward tutorials.
   What we don't have much of is paper recommendations, and I want to add that to the regular rotation.
   But I don't want it to be just a format of "Thomas recommends", my hope is that the prestigious outdex readership will also contribute in some manner that is yet to be determined.

1. I have plans for a series of lingbuzz-related posts: how to scrape it, create a personalized feed, and so on.
   This is stuff I've only started playing around with recently, and I don't know yet how well it will work out.

Yeah, I'm hedging like crazy because I don't know yet how well my current ambitions will translate into anything tangible.
But goddamn, I want to give it a try at least.


## References
