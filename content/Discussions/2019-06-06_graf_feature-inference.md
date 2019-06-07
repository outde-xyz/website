---
title: >-
    Features and the power of representations
authors:
    - Thomas Graf
date: 2019-06-06
modified: 2019-06-07
bibliography: references.bib
tags:
    - features
    - constraints
    - representations
    - generative capacity
    - subregular
    - strictly local
    - transductions
---

<!-- START_SUMMARY_BLOCK -->
As you might have gleaned from my previous post, I'm not too fond of features, but I haven't really given you a reason for that.
It is actually straight-forward: features lower complexity.
By itself, that is actually a useful property.
Trees lower the complexity of syntax, and nobody (or barely anybody) uses that as an argument that we should use strings.
Distributing the workload between representations and operations/constraints over these representations is considered a good thing.
Rightfully so, because factorization is generally a good idea.

But there is a crucial difference between trees and features.
We actually have models of how trees are constructed from strings --- you might have heard of them, they're called parsers.
And we have some ways of measuring the complexity of this process, e.g. asymptotic worst-case complexity.
We lack a comparable theory for features.
We're using an enriched representation without paying attention to the computational cost of carrying out this enrichment.
That's no good, we're just cheating ourselves in this case.
Fortunately, listening to people talk about features for 48h at the workshop gave me an epiphany, and I'm here to share it with you.
<!-- END_SUMMARY_BLOCK -->


## Recap: Fear the Feature

Let's first make clear where my concern about features is coming from.
Gillian Ramchand has a [beautifully written recap of my workshop talk](https://gillianramchand.blog/2019/05/28/building-vs-renovation-features-workshop-blogpost-1/) that might make for a more accessible starter.
I can't resist including my favorite passage as a sample here:

> When you transform your landscape in Feature Land into Constraint Land, lakes turn into rain and volcanoes emerge from the mist, and vice versa. 

I'm afraid I can't offer a comparable level of prose, but I'll try to make up for it by bringing in equally beautiful math.

Like most linguists, I want our theories to be highly restrictive.
Some overgeneration is always unavoidable because of substantive universals, e.g. that we can't have the same phonetic exponent for each lexical root.
But on a formal level we don't want to see widely unnatural patterns like the following:

Absolute counting

: There must be at least three C-heads in the tree.

Modulo counting

: The number of lexical items must be a multiple of 3.

Symmetric opposites

: An NPI must c-command its licensor.

Boolean constraint conjunction

: Satisfy either NPI-licensing or V2 iff Principle B is satisfied.

No locality

: The last word of the first TP must be the same as the first word of the last TP.

Domain mixing

: If the first word is downward entailing, then the last word must not contain an onset cluster.

Constraint flutter

: If A is an adjunct containing an adjunct C, then A and C are both islands only if there is some adjunct B contained by A and containing C that is not an island.

I don't even...

: If the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) between *omniscience* and at least one lexical item in the tree is a prime number, then the tree is well-formed iff the number of instances of *God* in it exceeds the greatest Levenshtein distance between all lexical items in the tree.

All of this crazy stuff can be done with constraints that are definable in monadic second-order logic (MSO).
MSO is a relatively simple extension of first-order logic (FO) where we can also quantify over sets.
While MSO isn't nearly as well-studied as FO, it is quite popular in theoretical computer science because of its connections to automata theory.
An MSO formula over strings can be translated into an equivalent finite-state automaton, and the other way round.
Over trees, MSO corresponds to bottom-up tree automata, which are the natural tree counterpart of finite-state automata.
All of this has been known for a long time [@ThatcherWright68; @Doner70], making MSO the logic counterpart to computer scientists' favorite classes of automata.

Cute history lesson, but let's bring this back to linguistics before you close the tab in favor of some kitten pics.
Here's the rub: Every syntactic theory with a subcategorization mechanism can actually express any arbitrary MSO constraint.
The pipeline for this is fairly simple:

1. Express the constraint as an MSO formula over trees.
1. Translate the MSO formula into an equivalent bottom-up tree automaton.
   The automaton may be much larger than the constraint as every quantifier alternation in the MSO formula induces an exponential blow-up.
   In general, the resulting automaton will be a confusing mess, and once you combine multiple constraints into a single automaton you should forfeit all hope of ever making sense of the automaton.
   It's like translating Prolog into machine code.
1. Compile the automaton directly into the feature calculus by refining category and subcategorziation features [@Graf11LACL; @Kobele11].
   Intuitively, an automaton that enforces NPI licensing would split every category *XP* into *XP[+/- licensor, +/- needs licensing]* and then use subcategorization requirements to ensure that we never end up with [+ needs licensing] at the root.
   In practice, you get things like *XP357* selects *YP28* and *ZP39*, with no idea what the heck any of this does.

The details of the procedure aren't all the important actually.
If you're curious, check @Graf17Glossa for a relatively newbie-friendly discussion of this translation mechanism.
The bottom line is that features allow us to express arbitrary MSO constraints, and that's something we simply do not want.

And the problem actually goes much deeper than the translation suggests.
You might think that it's all a problem with subcategorization, but that's just one specific instantiation of a much more general principle: **every recognizable set is a projection of a local set**, or equivalently, **every local set is a cylindrification of a recognizable set**.
Yikes, that's two of the most jargony jargon sentences that ever jargoned.
Let's run them through the DeJargonator 2000:

1. A recognizable set is a set of structures that is definable in MSO.
   For instance a regular string language (recognized by finite state-automata), or a regular tree language (recognized by a bottom-up tree automaton).
   Remember, MSO is very powerful, so recognizable sets can be very complex.
1. A local set is a set of structures that can be described in terms of a finite list of licit, locally bounded contexts.
   The string language $(ab)^+$ --- *ab*, *abab*, *ababab*, and so on --- is a local string set because we can describe it in terms of finitely many forbidden substructures:
   1. Start with *a*: $a \mid \$ \_$
   1. Only have *b* after *a*: $b \mid a \_$
   1. You may also have *a* after *b*: $a \mid b \_$
   1. End with *b*: $b \mid \_ \$$

   Local sets are much simpler than recognizable sets.
   They're pretty much bottom-tier when it comes to complexity.
1. A projection is a relabeling that conflates distinctions, for instance mapping both *a* and *b* to *c*.
   A cylindrification is the opposite, it adds new distinctions, e.g. replacing *a* by either *c* or *d* depending on context (which may be arbitrarily complex).

In plain terms, we can take a very complex recognizable set and push it to the bottom-tier of local sets by choosing a smart relabeling.
The prototypical example for this is how modulo counting can be made strictly local.
Consider the set of all strings that only contain *a* and have an even length greater than 0.
That's *aa*, *aaaa*, *aaaaaa*, and so on.
This is a recognizable set, and it involves one of the most powerful mechanism of MSO, i.e. modulo counting.
But now suppose that we give each *a* an extra feature that tells us whether it is an odd or an even position.
Now we can describe the well-formed strings in terms of four forbidden substructures:

1. Start with *a[+odd]*.
1. Only have *a[-odd]* after *a[+odd]*.
1. You may also have *a[+odd]* after *a[-odd]*.
1. End with *a[-odd]*.

Yup, that's exactly the same constraints as for the *ab*-language above.
So this is clearly a local set.
Through the addition of a single feature, complexity has plummeted from recognizable to local.
And this isn't just a mathematical curiosity, this stuff actually happens in linguistics.
A concrete instance is GPSG, which takes the complex movement dependencies and reduces them to local dependencies by adding slash-features to the representation.
That's why every feature is by default suspicious --- even if it is linguistically motivated and seems innocuous, it might have accidentally reduced complexity.

You might wonder now:
Isn't reducing complexity a good thing?
Isn't this why we factor problems into subproblems and always look for the simplest explanation?
Those are valid points, but the feature coding above has very little to do with that.
It doesn't furnish new insights or bring to light important parallels.
All it does is artificially lower the complexity of the problem through feature coding.
It obscures the problem rather than illuminating it.
Once we allow ourselves this kind of feature coding, every MSO-definable constraint can be expressed this way.
Even if we limit ourselves to linguistically natural feature uses, that might open the flood gates just enough to let in all kinds of ludicrous overgeneration.
We simply do not want feature coding.

Unfortunately, it is very difficult to distinguish feature coding from innocent uses of features.
I've tried many different routes and didn't find anything that works.
So that's why I've taken a very strict methodological stance: **fear the feature**.
During the workshop, though, a question by Gillian prompted me to think about the problem in a new way, and now I might have a solution so that linguists can have their cake and eat it, too.


## Feature use without feature abuse

From a complexity perspective, the central problem of features is that they hide complexity.
Throw in some features, and a complex computation becomes much simpler.
We're shifting the workload from the computation into the representation.
As I said at the beginning of this post, this can be a very fruitful route.
Syntax is the prime example where things become much more manageable once one moves from strings to trees.
The problem isn't so much with having features in the representation, it is that we have no good handle of how specific features affect the complexity of representations.

At least that's what I thought, until I realized we do have a way of measuring this: transductions!
Transductions are the computational counterpart to rewrite rules.
We can have string-to-string transductions, tree-to-tree transductions, tree-to-string transductions, tree-to-graph transductions, whatever.
Transductions are simply a way of manipulating structures.
One of the first papers on tree-to-tree transductions, @Rounds70, even cites transformational grammar as an inspiration.
As with string languages and tree languages, there's a veritable zoo of complexity classes for transductions.
And that's exactly the leverage we need to measure the complexity of features.
Basically, how hard is it to add the features to the representation?
That's the computational work hidden by making features explicit in the representation!

Let's dive right into an example.
Remember the recognizable set of even-length strings over *a* and how we made it local by adding a feature [+/- odd]?
How hard is it to add this feature?
Arguably the simplest kind of string-to-string transductions are the input strictly local (ISL) functions that Jane Chandlee has been doing lots of work on [@Chandlee14; @ChandleeHeinz18].
ISL functions are basically SPE rewrite rules where the context is finitely bounded and there's no optionality.
In addition, all the rewrite rules apply simultaneously, so there's no feeding or bleeding either.
Whether a rewrite rule applies to some segment depends only on the segments itself and its local context in the underlying representation.
So can an ISL function add the [+/- odd] features?
No.
The starting point is easy enough.
The first *a* should get [+odd], which is captured by the rule
$$
a \Rightarrow a[+\text{odd}] \mid \$ \_
$$
Crucially, though, we cannot use the fact that the first *a* is [+odd] in any other context specifications.
So the only way to make sure that the second *a* gets [-odd] is to look at a larger chunk of the input:
$$
a \Rightarrow a[-\text{odd}] \mid \$ a \_
$$
We can continue like this for a while.
$$
\begin{align*}
a \Rightarrow a[+\text{odd}] \mid & \$ aa \_\\
a \Rightarrow a[-\text{odd}] \mid & \$ aaa \_\\
a \Rightarrow a[+\text{odd}] \mid & \$ aaaa \_\\
a \Rightarrow a[-\text{odd}] \mid & \$ aaaaa \_\\
a \Rightarrow a[+\text{odd}] \mid & \$ aaaaaa \_\\
a \Rightarrow a[-\text{odd}] \mid & \$ aaaaaaa \_\\
\end{align*}
$$
But as we can only have a finite number of contexts, we cannot keep counting from the left edge.
At some point, we have to say something like
"Okay, this *a* is preceded by at least 17 other instances of *a*, but I don't know how many. 
Should it get [+odd] or [-odd]?"
And there's no safe answer given the available information.
Therefore, an ISL function cannot correctly assign [+/- odd].

Now if the transduction were output strictly local (OSL), then things would be easy.
An OSL function gets to look at the segment and the context in the output.
It's comparable to an SPE-rule that applies left-to-right or right-to-left.
This makes it fairly easy to enforce the alternation between [+odd] and [-odd].
$$
\begin{align*}
a \Rightarrow a[+\text{odd}] \mid & \$ \_\\
a \Rightarrow a[-\text{odd}] \mid & a[+\text{odd}] \_\\
a \Rightarrow a[+\text{odd}] \mid & a[-\text{odd}] \_\\
\end{align*}
$$
It seems, then, that OSL would be a bad model of feature inference because it allows us to do all kinds of undesirable things via feature coding.
ISL, on the other hand, is a reasonable baseline, as long as we don't allow ridiculously large contexts.

I gave a string-based example here for simplicity, but rest assured that we can do the very same thing for trees.
For instance, we can require category and subcategorization features to be inferable by an ISL function.
This greatly reduces what subcategorization is allowed to do, effectively shutting down the translation pipeline of @Graf11LACL and @Kobele11.
I think this also makes interesting empirical predictions about subcategorization, but this would lead us too far here.
ISL functions won't be able to correctly infer movement features, for two reasons.
The more obvious problem is that movement is not locally bounded in the sense that ISL requires.
But movement also has the property of being partially non-deterministic.
The only difference between the derivation trees for *this book, John gave to his daughter* and *to his daughter, John gave his book* lies in which D-head carries a topicalization feature.
ISL functions, by virtue of being functions, struggle with such non-determinism.
Neither challenge seems insurmountable, though, so I might have something workable in the near future.
It sure would be nice to finally be able to distinguish feature use from feature abuse.


## A dessert of conceptual remarks

Let's take a step back to take a broader view of what this post is about.
The primary issue is that features in the technical sense of generative grammar aren't just properties or building blocks, they are reified units of computation.
This computation could be inferring class membership --- the feature *pl* conveys that we have determined that the carrier of the feature belongs to a class of elements that we call *plural*.
But it could also represent more complex computations, e.g. modulo counting in the case of [+/- odd].
Putting features into the computation is a loose analog of dynamic programming: we have already carried out a specific computation, and now we're storing the result of this computation in the form of a feature.

In and of itself, there's nothing wrong with that.
But the way features are used, we completely skip the actual computation step and go immediately to storing the result.
Without a principled linking theory between features and computation, features can hide incredibly complex computations.
I think this is a point that's not sufficiently appreciated by linguists.
In a comment on my previous post, Peter Svenonius says

> If features are real, then it follows that they are "an explicit part of the representation".

I hope that this post has shown that things aren't as clear-cut.
Features represent computations that may well be real, yet this does not entail that features are an explicit part of the representation.
They may be, but methodologically we cannot take this as carte blanche to freely put features into our representations, no matter how plausible or natural they may seem.
Two weeks ago, my stance would have been "Sorry, you can't do that without opening Pandora's box".
I think I can now offer a more palatable compromise: Sorry, features aren't as innocent as you think, but by measuring the transduction complexity of feature assignment we might soon be able to separate appropriate feature use from inappropriate feature abuse.

In hindsight, it's actually baffling to me that I didn't think of this any sooner.
The trade-off between representations and operations/constraints is basically folklore in mathematical linguistics.
Jeff has been insisting on the importance of complexity classes for representations for ages now and has had some ideas for getting at this through transductions.
And together with my student Aniello De Santo I have recently argued that TSL, a very basic approximation of autosegmental phonology, should be studied in terms of constraints on the representation and a transduction for inferring the representation [@DeSantoGraf19FG].
It was all there in plain sight, but it took a nudge from Gillian for the pieces to assemble in the right way.
So, thank you Gillian!
You guys can expect a paper on feature inference within the next few months, with some nifty applications to subcategorization.

## References
