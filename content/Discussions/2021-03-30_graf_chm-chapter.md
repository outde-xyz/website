---
title: >-
    Handbook chapter on Minimalism & computation
authors:
    - Thomas Graf
date: 2021-03-30
bibliography: references.bib
tags:
    - Minimalist grammars
    - formal language theory
---

<!-- START_SUMMARY_BLOCK -->
Aah, the soothing sound of crickets.
In case you've been wondering about the recent radio silence at this prestigious online soapbox, my todo list finally caught up with me and I had to spend the last few weeks writing up/revising some papers that were way overdue.
It was a matter of life and death --- the editors were already contemplating Satanic blood sacrifices, and while I enjoy a good Black Mass as much as the next guy, I'd rather not be its subject matter.
In this post I'd like to talk a bit about one of those papers, [a chapter on Minimalist grammars in an upcoming handbook on Minimalism](https://manuscripts.thomasgraf.net/chm).
Though I have to admit that it's mostly a ruse to get some of you to give it a read and leave some feedback in the comments section.
<!-- END_SUMMARY_BLOCK -->


## Going short or going long?

The handbook is actually slated to contain two chapters on MGs.
The first one, written by [Greg Kobele](https://home.uni-leipzig.de/gkobele/index.html), presents MGs as a specific incarnation of the Minimalist framework, with an emphasis on the analysis of empirical phenomena.
My chapter, on the other hand, looks at the computational properties of MGs and how those relate to linguistic issues.
So, mostly big-picture stuff, no specific data.
In addition, my chapter was originally planned as a vignette, i.e. a short chapter of approximately 15 pages.
My thinking was that Greg's chapter would provide enough of a foundation that I could move at a brisker pace.
And since the average Minimalist probably does not want to slog through 30 pages of computational discussion, keeping it short and sweet would increase readership.

But that strategy did not quite work out: the paper isn't so short after all, and it might be too terse to qualify as "sweet".
This makes me wonder if the paper needs to be decompressed.
The question is, do I remove some topics and keep the length the same, or do I expand the presentation and accept that it will be a longer paper?
And if I extend it, do I want to add some other topics that wound up on the cutting floor?
It's a handbook chapter after all, and those should be comprehensive references.
Then again, it's a handbook on Minimalism, not MGs, so one could say it doesn't need to be **that** comprehensive.
So that's the first point I'm not sure about, short or long, and if the latter, just longer, or longer with extra content?


## Cut content

There's a few things that I decided to cut down or remove completely that I would love to put back in.
Foremost among them is multiple wh-movement because that is an area where computational considerations yield eminently empirical questions:

1. Is multiple wh-movement actually unbounded, or is there a principled finite bound on how many wh-phrases can be fronted (e.g., do the moved wh-phrases have to differ in morphological case)?
1. If there is no upper bound on how many wh-phrases are fronted, what is the evidence that those are individual wh-movement steps, rather than, say, a big cluster of wh-phrases undergoing a single instance of wh-movement?
1. What determines the order of the fronted wh-phrases?
   C-command modulo movement?
   Case?
   And how much variation is allowed?

The answers to those questions have a huge impact on what multiple wh-movement looks like from a computational perspective.

Also missing from the chapter is scrambling.
Syntacticians can't quite agree what to do with scrambling, and neither can computational linguists.
It's a challenging phenomenon from either perspective.
But again there are interesting takes on it.
@Joshi.etal00, for instance, argue that TAG puts a principled cut-off point on scrambling, so that rather than attributing the unacceptability of complex scrambling constructions to performance, we can simply treat it as a hard limit of syntax.
This makes concrete empirical predictions, which, to the best of my knowledge, have not been systematically tested so far.
Readers of a handbook on Minimalism probably should be aware of this, it's an excellent topic for a collaboration between theoretical and computational linguists.

And then there's learning, which I did not say anything about in this chapter, mostly because it's a huge can of worms with very little work that directly interacts with Minimalism.
Yes, [Alex Clark](https://alexc17.github.io/), [Ryo Yoshinaka](http://www.iip.ist.i.kyoto-u.ac.jp/member/ry/) and others have done amazing work on learning mildly context-sensitive languages, but learnability results are a subtle issue that is difficult to present in an accessible manner without grossly distorting the work.
And I honestly do not understand them well enough to contemplate their implications for the Minimalist mainstream.
There's also some early work on learning types of MGs that exhibit a very limited kind of lexical ambiguity.
But the result always struck me as a bit too artificial, and though I might well be wrong about that, talking about it still requires going into the whole learnability VS language acquisition thing, which I'd like to avoid.


## Literature

I really tried to be exhaustive when it comes to references.
Ideally, this and Greg's paper will jointly serve as a new, up-to-date entry point into the MG literature, so it's important to closely track what's out there and capture the full breadth of MG work.
I feel fairly confident that I've got that part covered --- almost one third of the paper is references,
But this also means that every accidental omission weighs heavy, and while I have already noticed a few, I'm sure there's more.


## Feedback?

If you're curious, [check out the manuscript](https://manuscripts.thomasgraf.net/chm).
All feedback is welcome.
Email is fine, but the comments section is also ready for your perusal.


## References
