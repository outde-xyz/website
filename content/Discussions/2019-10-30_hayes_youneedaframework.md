---
title: >-
    We need a framework?
authors:
    - Thomas Graf
date: 2019-10-30
bibliography: references.bib
tags:
    - methodology
    - subregular
---

<!-- START_SUMMARY_BLOCK -->
As you might know, Stony Brook hosted AMP, the [American Meeting on Phonology](https://www.stonybrook.edu/commcms/amp2019/), ~~a week ago~~ quite a while ago (yikes, almost November again).
[Jane Chandlee](https://chandlee.sites.haverford.edu/) started off the conference with an invited talk on the subregular view of phonological mappings from underlying representations to surface forms.
It was well received, but during the question period [Bruce Hayes](https://linguistics.ucla.edu/people/hayes/) (no, [not that Bruce Hayes](https://www.brucehayes.com/?section=bio)) made a point that I found puzzling: "You need a framework!"
Unfortunately I didn't have time to ask Bruce afterwards what exactly he meant by that.
But every conceivable interpretation I've come up with I vehemently disagree with, and I think Bruce's demand for a framework stems from incorrectly applying the linguistic *modus operandi* to computational work.
<!-- END_SUMMARY_BLOCK -->


## Bruce's question

First, the relevant background.
Bruce started out with the question whether the use of (subclasses of) finite-state transductions marks a return to the SPE-days of yore.
This question was probably prompted by two points made in the talk:

1. [@KaplanKay94] showed that all of SPE can be recast in terms of finite-state transductions (not as defined, but as used by phonologists).
2. Jane mentioned that transductions can be daisy chained, similar to how SPE rewrite rules apply one after another.

Jane gave a very diplomatically phrased No to Bruce's question.
Still intoxicated by the new-car smell of my tenure, I would have been more blunt:

> No, Bruce, your question starts from a logical fallacy.
> The fact that SPE can be recast in terms of finite-state transductions does not imply that any approach that uses transductions marks a return to SPE.
> Lexical meanings can be modeled as vectors in a higher-dimensional space, that does not mean that everybody who uses vector spaces is doing lexical semantics.
> So, no, just no.

I then would have basked in the warm afterglow of my own awesomeness for having deflated Bruce's question.
The audience, in the meantime, would have emitted a collective 150db groan in reaction to me dismissing Bruce's methodological point on a technical matter.
So, kudos to Jane for not following my fictional example.
I have a hunch that if she were to write the rest of this post, it would also be more diplomatic.
By no means should she or anybody else in the subregular community be taken to endorse what I'm about to say.

Anyways, back to Bruce's question.
The real issue, as Bruce clarified next, is one of frameworks.
He thinks that subregular phonology must have an underlying framework, and he wants to know what it is.
But what does that mean, *framework*?
We could go full-blown Lakatos, but let's not get overly theoretical here.
Few things are less useful to science than philosophy of science.


## Option 1: Framework = linguistic theory

The strongest interpretation that I can come up with equates frameworks and linguistic theories.
In this case, Bruce's question could be rephrased as a demand for a pledge of allegiance:

- **Pledge of allegiance**  
  Look fella, we linguists have a range of options for you math folks to choose from: SPE, OT, Harmonic Grammar, Autosegmental phonology, Government Phonology, Strict CV, and much more.
  Pick your side, add those fancy formulas you guys love so much, but pick a side and run with it.

For the record, I don't think that's what Bruce had in mind.
But it is actually a common view.

For instance, I know some folks who are quite brilliant yet believe Minimalist grammars are a program of formalizing whatever Minimalist syntacticians come up with.
As [Shalom Lappin](https://clasp.gu.se/about/people/shalom-lappin) told me many years ago (paraphrasing from memory):

> The MG community is like medieval logicians: the formalist handmaiden that diligently cleans up the mess of the religious clergy.

And that's just not what it is about.
Ironically, many Minimalist syntacticians would say the very opposite --- MGs are very different from what they're doing and what they're interested in.
The MG community is not in the business of slavishly formalizing whatever Minimalist syntacticians think is interesting.
We treat Minimalist syntax as a valuable source of ideas and empirical generalizations, something that has a lot of merit and should not be dismissed just because it does not pass a mathematician's standard of rigor.
At the same time, we do not swallow it hook and sinker --- it's an inspiration, not an instruction booklet.

Similarly, subregular phonology is not in the business of resurrecting SPE or undermining OT or making a plea for underlying representations.
It is an attempt to understand phonology as a computational problem, and the community is opportunistically sampling from ideas in the linguistic literature.
If it looks useful, it's fair game.
Allegiance to one specific framework over another would directly undermine the subregular spirit of strength by diversity.

As I said, I do not think that Bruce had this kind of linguistic supremacy in mind.
It's way too strict a notion of framework.
And it certainly isn't the case that subregular phonology commits you to a specific formalism, be it SPE or OT or something else.
The whole point is not to be overly attached to specific means of description.
So let's look at the very other end, the loosest possible notion.


## Option 2: Framework = shared body of problems and potential answers

A framework can be construed more loosely as a shared body of issues, problems, and potential solutions.
For instance, what are the relevant issues that computational phonology should address?
How do we interpret the available data?
Do we factor out gradience in native speaker judgments or endorse it?
When we talk about underlying representation, what do we mean by that?
What is the ontological status of the machinery and representations we posit?
I think this is the weakest conceivable notion of framework, and nonetheless I do not think that the subregular approach has a framework in this sense, nor does it need one.

Let's make this a bit more concrete:

1. Subregular phonology is completely agnostic about whether well-formedess is categorical or gradient.
Right now we have results that tell us something about complexity in the case where we assume categorical well-formedness.
But somebody else can sit down, replace the Boolean semirings in the subregular recognizers by weighted ones, and get complexity results for the gradient case.
And then another person could prove linking theorems that tell us something about the connections between those classes, making it easier to transfer insights between the categorical and the gradient case.

1. When subregular phonology says that unbounded tone plateauing is not [TSL]({filename}/Tutorials/locality_sltsl.md), this statement is made with respect to a specific interpretation of the data --- for instance that HLLLLLH is not represented as HLH with a multiply linked L.
But one can also consider the latter case and ask how that affects complexity, and what the computational cost would be of using this representation instead.
That's when you're in Adam Jardine's subregular graph land.
And once again we would look for linking theorems that allow us to port insights from one perspective over to the other.
Neither perspective has some kind of privileged status compared to the other, both are valuable.

1. When Jane Chandlee talks about transductions from underlying representations to surface forms, the insights obtained this way are valuable irrespective of how one feels about underlying representations.
It is a way of studying the problem of connections between surface forms, and it provides a particular factorization that distributes the workload over the representations and the machinery manipulating them.
That's useful information irrespective of your theoretical priors.

Btw, none of these perspectives and research questions are in competition to each other, neither one is superior to the other.
In my experience, subregular linguists do not stomp their foot and say that X is the only right way of studying P and that anybody who deviates from X is confused.
Nor do we think that anybody who studies Q instead of P has nothing of value to add.
As long as there is a way to bring insights from Q to bear on P, working on Q is a good thing for P, too.


## There is no framework

Imagine if somebody told you your job were to measure objects, but you were only allowed to measure their volume, not their weight.
You'd say they're mad.
Sure, there can be some value in seeing how much you can do just with volume, but this doesn't mean that everybody has to join the volume-only club.

That's a caricature, but it isn't too far from what having a framework means in linguistic practice.
If you're a Minimalist, you can't just go and suddenly analyze syntax in terms of strings just because you think that's nicer.
That's not sticking with the program of Merge-driven structure building.
Linguistics needs this kind of framework to vaccinate itself against theoretical arbitrariness.
The only way to ensure a reliable flow of information between different researchers is to enforce a large shared base.

I don't think the subregular program has a framework in this sense, nor should it have one.
As long as you produce something that is useful, it's good work.
I doesn't even have to be on language.
If you want to take those subregular concepts and apply them to game theory or molecular biology or compiler design, good for you, that's nifty, that's a nice application.
Do whatever you think is interesting --- as long as it's worked out mathematically, we'll be able to cherrypick from that whatever is useful for our purposes.

That's the key issue here, the thing that's really nice about math: it allows you to see how much you can take from an argument that starts from completely different priors than your own.
In practice it's not always trivial, of course, and the linking can take years to figure out.
But we do get it eventually, and that's why frameworks aren't all that important.
For instance, we are very happy with weak generative capacity claims about syntax (i.e. strings) because we have various linking theorems that tell us what this implies about strong generative capacity (i.e. trees).
The discussion doesn't start and end with "well, you're making assumptions that don't fit my framework, so nothing you're about to say has any value to me".
I like it that way.
We don't need no framework.

## References
