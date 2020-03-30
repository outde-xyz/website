---
title: >-
    Some musings on corpora
authors:
    - Thomas Graf
date: 2019-09-05
bibliography: references.bib
tags:
    - syntax
    - corpus linguistics
    - Minimalist grammars
    - Combinatory categorial grammar
---

<!-- START_SUMMARY_BLOCK -->
Pro tip: Don't start a multi-part series of posts on locality right before the beginning of the semester and when you have a pile of papers to review.
On the upside, this will give you guys some extra time to digest all the concepts in the
[three]({filename}/Tutorials/locality_sltsl.md)
[previous]({filename}/Tutorials/locality_iotsl.md)
[posts]({filename}/Tutorials/locality_sp.md).
In the meantime, here's a quick and dirty post on corpus linguists and why it should be part of our syntax curriculum.
I didn't even proofread it, so beware.
<!-- END_SUMMARY_BLOCK -->

First, to be clear, by corpus linguistics I mean the science of designing and constructing corpora, not linguistics that happens to take data from corpora.
I have to admit, I consider corpus linguistics of this kind one of the dullest parts of computational linguistics.
Lots of annotation grind, tedious details like what tag set would be best, even how to structure the files and organize the whole corpus.
I don't envy anybody who has to spend a lot of time on such questions.
It's as if somebody decided that linguistics isn't enough like accounting and set out to fix that.

But you know what, accounting may be blander than a rice cracker in the shape of Benedict Cumberbatch's face (i.e., a brick), but that doesn't mean it's irrelevant.
Actually, everybody should know a bit about accounting, at least the very basics that run under the banner of personal finance.
And I think looking a bit at corpora would be a valuable addition to a grad-level syntax intro.
No, it's not because corpora are the bee's knees, it's because they highlight certain issues that are usually glossed over in syntax.

One is the problem of translating between theories.
For instance, CCGbank was automatically created from the Penn Treebank to serve as a large scale corpus for Combinatory Categorial Grammar.
[This paper by Hockenmayer & Steedman](https://www.mitpressjournals.org/doi/pdf/10.1162/coli.2007.33.3.355) covers in detail how it was done, and it's not straight-forward.
There's multiple reasons for that.
One is that CCG doesn't have movement/traces and instead relies on flexible constituency to get things to combine in the right manner.
That's a major difference to other formalisms, and while a lot of it is fairly easy to translate, there are some tough nuts.
Those also tend to be nuts that linguists care about.
There are some syntacticians who subscribe to the idea that all syntactic formalisms are essentially different encodings of the GB insights.
The problem of translating corpora shows that even if this is true, the encodings are sufficiently different that humans can't figure out how to automatically translate between them while preserving all linguistic commitments.

But that's just the first reason why creating CCGbank was hard.
Another one is that the Penn Treebank isn't based on fully formalized grammar of English, so there can be idiosyncratic differences between trees due to annotator preferences or hunches.
That's a nice argument why you want to have a grammar rather than just winging it, right?

Actually, hold your horses.
If the Penn Treebank hadn't gone with just winging it, it probably would not exist at all.
There are tons of cases that are devilishly hard to figure out yet haven't attracted a lot of attention from linguists.
Now you could stipulate a specific solution only to realize 2000 sentences later that your solution doesn't always work, or you just accept that you won't be able to come up with something good and decide to just wing it.
This is very interesting because it points out phenomena that we do not have a solid handle of yet.
Syntacticians tend to emphasize the opposite side of the coin, i.e. that many interesting phenomena won't be present in a corpus at all.
For instance, the Penn Treebank is an annotated sample of WSJ articles, so you're not gonna find any negative concord in there, and questions and imperatives are also rare.
But we should not fall prey to the fallacy of implicational perfection and infer that corpora contain nothing of interest at all.

A year or two ago, John Torr told me about the challenges he encountered in creating a large-scale corpus for Minimalist grammars.
One thing that really struck me is that there was a large residue of sentences that involved constructions for which there was no widely agreed upon, off-the-shelf solution in the Minimalist literature.
I think John said it was something like 7% of the whole corpus, but I might have that completely wrong.
If it is, that's a lot of sentences!
[The paper on neural A* parsing](https://stanojevic.github.io/papers/2019_ACL_MG_Wide_Coverage.pdf) that [Aniello discussed a while ago]({filename}/Discussions/2019-06-23_desanto_torracl-mgpaper.md) actually lists a few examples, including discontinuous quotes and definiteness effects with expletives:

(@) "Funny thing," says the kicker "both these candidates are named Rudolph Giuliani".
(@) There seem to be some/several/\*the/\*those problems.

Discontinuous quotes are different from parentheticals, and parentheticals are already very hard to fit into Minimalist syntax.
The ban against definites with expletives is well-known, but I don't think there's a widely agreed upon solution beyond "how about we say it's semantics?".
Adding my own examples, I can't resist opening Pandora's box: idioms.
Just how do you handle something like *sleep x's way to the top* so that it is open to modification but closed to other operations?

(@) John slept his way to the top.
(@) John slept his way right to the fucking top.
(@) \*His way was slept to the top by John.
(@) \*Where did John sleep his way to?
(@) \*To the top, John boldly slept his way.
(@) \*It is to the top that John slept his way.
(@) \*John slept to the top his freaking abusive way.
(@) It is the biggest company in the world that John boldly slept his way to the top of.

Yes, it's an idiom, and this is pretty much how idioms works.
Just saying so isn't enough, though, the question is how you get that into the grammar.
And then of course there's amalgams like *John went to I believe it was Chicago*, which nobody except Henk van Riemsdijk seems to care all that much about.
Considering how common all of these constructions in the wild, it's surprising how little attention they actually receive compared to split probes, the direction of agree and things like that.
I know, I know, frequency is no indicator of scientific relevance or merit, otherwise all physicists would have to spend their time on models of falling leaves.
Still, if there's problematic phenomena that are frequent enough that they make corpus creation hard, that's a great playground for syntax newbies.
Heck, there should be a platform where our syntax students can look at those 7%, pick a few, and try to figure out what's going on.
They might not come up with a solution, but it will show them that there's more than ECM, raising, island constraints, binding, and probe-goal relations.

Another thing you realize when doing corpus work is just how much lexical ambiguity you need to make things work.
Here's some stats for CCGbank, from p. 388 of the [Hockenmaier & Steedman paper](https://www.mitpressjournals.org/doi/pdf/10.1162/coli.2007.33.3.355):

| **Word** | **Lexical entries** |
| :--      | --:                 |
| as       | 130                 |
| is       | 109                 |
| to       |  98                 |
| than     |  90                 |
| in       |  79                 |
| 's       |  67                 |
| for      |  66                 |
| at       |  63                 |
| was      |  61                 |
| of       |  59                 |
| that     |  55                 |
| not      |  50                 |
| are      |  48                 |
| with     |  47                 |
| so       |  47                 |
| if       |  47                 |
| on       |  46                 |
| from     |  46                 |

That's a lot of lexical ambiguity.
You might say that's due to misanalysis or putting too much stuff into the lexicon.
Fair enough, but can you do better?
If you haven't tried, the point is moot.
Creating a fully rigorous grammar for a corpus is essentially writing a giant grammar fragment.
And if there's one thing that all grammar fragments have in common, it's that they quickly have to add all kinds of bells and whistles to make everything work.
It really dissuades you of the idea that all syntactic categories are variations of $[\pm N, \pm V]$.
I think this is something that students should be made aware of in a syntax intro: our theories are small, compact, and elegant because we gloss over a lot of details that actually take a lot of effort to get right.

This is actually part of a much broader point: glossing over the details is okay when you're trying to figure out a more fundamental issue, but as a field we can't do that indefinitely --- sooner or later, somebody has to sit down and work this out.
Minimalists complain that their ideas haven't gained much traction outside theoretical syntax.
Well, that didn't happen because those outsiders are too dumb or narrow-minded to appreciate Minimalism (some might be, but I've learned through first-hand experience that it's more productive to think about why somebody might not appreciate your work rather than just dismissing them as confused, misinformed, or too freaking dumb).
Minimalism didn't get much traction because what other fields want to do with language requires work that Minimalists consider low priority.
Look at CCG, which has made major inroads into NLP in the last two decades.
This is largely thanks to the creation of CCGbank and the work it enabled.
With CCGbank, you can train a robust, broad coverage CCG parser.
Once you have a parser, you can do tons of things, from question answering to analyzing tweets to semantic parsing.
Maybe your CCG parser includes a neural supertagger, and boom, now you're interacting with the neural machine learning crowd and present them with problems to solve and they'll cite your work as motivation for whatever they're trying to get published.
Thanks to John Torr's MGbank there now is an opportunity for similar work on MGs, but we're at least a decade behind the curve.
And the fact of the matter is John shouldn't have had to build it himself.
A large, high-quality corpus for Minimalist syntax should have been a high priority for Minimalists from the get go.

Speaking of the lack of corpora, let's talk machine learning.
Linguists remain skeptical of domain-general machine learning techniques.
Rightfully so, those models are trained and tested on corpora that are horrible for probing linguistic knowledge.
But bickering is pointless, the situation will only improve if linguists get more involved.
In bioinformatics, there's annual competitions for the best protein folding models.
Each year this involves a new test set that's carefully designed by an interdisciplinary team of computer scientists, biologists, and chemists.
This is a model linguists should strive to emulate.
If you do not trust the ability of current corpora to tell us much about language, you should build better corpora.
Corpora that are carefully controlled to test structure independently of linear order, include long-distance dependencies, garden paths, less common phenomena that are systematically undersampled in current corpora, typologically rare phenomena such as the Person Case Constraint or omnivorous number, or use the interaction of bounded constructions to yield unbounded dependencies (think multiple levels of raising + ECM + passive in one sentence).
Tal Linzen is doing some of this, but he's one guy, and he's not even a syntactician (at least I think Tal doesn't identify as one).
Why aren't linguists seizing the low hanging fruit?
This would be such a great opportunity to get students involved, to have them see first-hand how well --- or not so well --- domain-general machine learning fares on the complex stuff they study in their syntax class.

I can already see some of you brush aside the challenges of corpus linguistics with the old Chomsky adage that those who build bridges need additional assumptions beyond what physics furnishes --- in the real world, you need hacks to make things work.
That's a convenient position for old-school theoreticians because it maintains the status quo.
But it incorrectly couches the issue as a one-way street, with theoreticians, left to their own devices, producing knowledge that slowly trickles down to the world of applications.
Just like trickle-down economics, trickle-down knowledge is a sham.
Science not only informs applications, it is also informed by them. 
The applied side is both a knowledge consumer and a question generator.
And let's be perfectly blunt here for a second: nowadays, the fate of scientific programs is decided in the court of resource allocation.
In general, it's easier to get those resources when your field is well-connected with other fields, but this means you sometimes have to do things that aren't all that interesting but are nonetheless valuable.
Old dogs don't learn new tricks, but if our students have at least some exposure to corpora as part of a standard curriculum, the next generation might fare better in this respect.
