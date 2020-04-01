---
title: >-
    Against math: When sets are a bad setup
series: >-
    Against math
authors:
    - Thomas Graf
date: 2020-04-06
bibliography: references.bib
tags:
    - methodology
    - syntax
    - set theory
    - Merge
    - linearization
---

<!-- START_SUMMARY_BLOCK -->
Last time I gave you a piece of my mind when it comes to [the Kuratowski definition of pairs and ordered sets]({filename}2020-03-30_graf_againstmath1.md), and why we should stay away from it in linguistics.
The thing is, that was a conceptual argument, and those tend to fall flat with most researchers.
Just like most mathematicians weren't particularly fazed by Gödel's incompleteness results because it didn't impact their daily work, the average researcher doesn't care about some impurities in their approach as long as it gets the job done.
So this post will discuss a concrete case where a good linguistic insight got buried under mathematical rubble.
<!-- END_SUMMARY_BLOCK -->

Our case study is a [2018 paper](https://doi.org/10.1353/lan.2018.0037) by [Jordi Fortuny](https://doi.org/10.1353/lan.2018.0037), which refines the ideas first presented in @Fortuny08 and @FortunyCorominasMurtra09.
The paper wrestles with one of the foundational issues of syntax: the interplay of structure and linear order, and why the latter seems to play second fiddle at best in syntax.
Let's first reflect a bit on the nature of this problem before we look at Fortuny's proposed answer.


## Structure VS linear order

The primacy of structure is pretty much old hat to linguists.
You've all seen the standard auxiliary fronting example before:

(@) The man who is talking is tall.
(@) Is the man who is talking \_ tall?
(@) \*Is the man who \_ talking is tall.

Why is there no language that defines auxiliary fronting in terms of linear precedence such that the leftmost --- or alternatively the rightmost --- auxiliary in the sentence is fronted?
Quite generally, why doesn't syntax allow constraints that are based entirely on linear order, such as:

1. **Sentence-final decasing**  
   Don't display case if you are the last word in the sentence.
1. **RHOL subject placement**  
   The subject of a clause *C* is the rightmost DP with at least two lexical items.
   If no such DP exists in *C*, the subject is the leftmost DP instead.
1. **Linear movement blocking**
   No adjunct may linearly intervene between a mover and its trace.
1. **Modulo binding**  
   Every reflexive must be an even number of words away from the left edge of the sentence.

That's exactly the kind of question that keeps me up at night.
As you know, I like the idea that syntax and phonology are actually very similar at a computational level, so the non-existence of the constraints above is problematic because they are all modeled after phenomena from the phonological literature.
How can we explain the absence of those constraints?

There's two answers here, and neither one is satisfying.
We might reject the initial assumption that linear order doesn't matter in syntax.
That's basically [Benjamin Bruening's story for binding](https://www.linguisticsociety.org/sites/default/files/342-388_0.pdf) [@Bruening14].
I have a weak spot for contrarian takes, but the Bruening stance doesn't answer why we still can't get constraints like the ones listed above.
Perhaps linear order matters to some extent, but if so the extent seems to be much more limited than one could imagine.

This leaves us with option 2, which is the standard story: syntactic representations have no linear order, hence syntax can't make reference to linear order.
The idea goes back to @Kayne94 and is also a major reason for the use of sets in Bare Phrase Structure [@Chomsky95].
But it simply doesn't work because syntax is inherently asymmetric.
And this is where @Fortuny18 enters the picture.


## Order from computation

I take Fortuny's basic point to be one that I'm very sympathetic to: linear order emerges naturally from the asymmetry that is implicit in syntactic computation.
Hence it is hopeless to stipulate linear order out of syntax, the best one can do is to systematically bound the role of linear order in syntax.

Here's my take on this, which I think is close in spirit to what Fortuny is driving at, but without any reliance on sets.
A (strict) linear order arises when you have a relation that is transitive, irreflexive, asymmetric, and trichotomous:

- **transitive**: whatever can be reached in $n$ steps can be reached in one step  
  ($x \mathrel{R} y$ and $y \mathrel{R} z$ implies $x \mathrel{R} z$)
- **irreflexive**: nothing is related to itself  
  ($x \not\mathrel{R} x$ for all $x$)
- **asymmetric**: no two elements are mutually related  
  ($x \mathrel{R} y \rightarrow y \not\mathrel{R} x$)
- **trichotomous**: no two elements are unrelated
  ($x \mathrel{R} y \vee y \mathrel{R} x \vee x = y$)

If you look at syntax in terms of binary Merge (or something
[slightly]({filename}2019-05-15_graf_tmodel.md)
[more]({filename}/Tutorials/locality_merge_move.md)
[abstract]({filename}2020-03-05_graf_underappreciated_trees.md)), you already have an order that satisfies three of those properties: transitivity, irreflexivity, and asymmetry.
That's the (strict) partial order we usually call **proper dominance**, but you can also think of it as **derivational prominence** or some other, more abstract concept.
Not really the point here.
Either way you are already dealing with something that's inherently asymmetric and ordered, and this asymmetry can be inherited by any relation that piggybacks on this.
This recourse to proper dominance ($\triangleleft^+$) is exactly how linear order ($\prec$) is usually defined in formal terms:
$$
x \prec y \Leftrightarrow
    x \mathrel{S} y
    \vee
    \exists z_x, z_y [
        z_x \triangleleft^+ x
        \wedge
        z_y \triangleleft^+ y
        \wedge
        z_x \mathrel{S} z_y
        ]
$$
This says that precedence is inherited via dominance.
If $x$ and $y$ are properly dominated by $z_x$ and $z_y$, respectively, and $z_x$ precedes $z_y$, then $x$ precedes $y$.
But hold on a second, that's circular, we're defining precedence in terms of precedence.
And if you look at the formula, there's actually a completely different symbol there, $S$, which isn't the precedence symbol $\prec$.
So what's $S$?
It's the successor relation, and in contrast to precedence it's only defined for siblings.
So $x \mathrel{S} y$ is true iff $x$ is the left sibling of $y$.
Aha, so this is where it all breaks down, syntax doesn't actually have such a successor relation because there is no linear order in syntax!

Nope, sorry, this particular hook you can't get off that easily.
You see, $S$ doesn't actually need to tell us anything about linear order.
The term successor applies to any asymmetric order.
So $S$ just needs to be some relation that establishes an asymmetry between $x$ and $y$.
And there is a relation in syntax that does this for us, it's the head-argument relation.
Merge tends to be presented as a symmetric operation, but it's not.
One of the guys is more important because it has a bigger influence on the behavior of the newly formed constituent.
That's the head.
Instead of successor, you may interpret $S$ as some kind of **superior** relation, and the formula above will still work fine.

What this shows us is that linear order cannot be simply stipulated away.
Syntax furnishes all the asymmetries that make up linear order, and thus a computation device that can keep track of these asymmetries is perfectly aware of linear order.
The problem, then, has to be with the computational complexity of determining linear order from those asymmetries.
That is to say, the formula for $\prec$ above is too hard to compute.
Something about inheritance via proper dominance is beyond the computational means of syntax.
If so, this would dovetail quite nicely with my pet idea that syntax overall has very low subregular complexity.
For instance, I've argued together with [Aniello De Santo](https://aniellodesanto.github.io/) that [sensing tree automata furnish an upper bound for syntax](https://www.aclweb.org/anthology/W19-5702.pdf), and these automata are indeed incapable of fully tracking linear order.
So, yes, sign me up for the idea that linear order constraints don't show up in syntax because linear order is too hard to compute from the combination of proper dominance and head-argument asymmetries.
But that's very different from the standard story that syntax lacks linear order because its representations don't directly encode linear order.

Fortuny provides a technically different answer, but the core idea is very similar in nature to the story I just sketched.
He first shows that syntax naturally produces linear orders, and then tries to explain why the impact of that is so limited.
But he does it with sets, and that opens up a whole can of worms. 


## Fortuny's approach in detail

Fortuny starts out with a generalization of the Kuratowski definition from pairs to tuples (btw, when rereading his paper I noticed that he actually cites @Kuratowski21; kudos!).
With this generalized definition, an $n$-tuple $\langle a_1, \ldots, a_n$ is encoded as the **nest**
$$
\{ \{a_1\}, \{a_1, a_2\}, \{a_1, a_2, a_3\}, \ldots, \{a_1, a_2, a_3, \ldots, a_n\} \}
$$
Based on earlier work [@Fortuny08; @FortunyCorominasMurtra09], he then postulates that syntactic derivations produce sets of this form, rather than the standard bare phrase structure sets.
Think of it as follows: suppose that the syntactic workspace currently contains only $a$, which by itself forms the constituent $\{ a \}$.
Now if we Merge some $b$ into this constituent, we get $\{ a, b \}$ as the output.
Fortuny then says that the actual constituent is the set of the sets built by Merge, i.e. $\{ \{a\}, \{a,b\}$.
Personally, I think it makes more sense to think of this as a derivation rather than a constituent, but my infatuation with derivation trees should be well-known by now.
I won't quibble over terminology and just follow Fortuny in calling these complex sets constituents.
So we have an **output** $\{a,b\}$, but a **constituent** $\{ \{a\}, \{a,b\} \}$.
If we merge a $c$ into the current output, we get $\{ a, b, c\}$, and the constituent grows to $\{ \{a\}, \{a,b\}, \{a,b,c\} \}$.
In a nutshell, Merge just inserts a lexical item into a set, and the nested structure arises if we collect all the outputs into a single set, which Fortuny calls a constituent.

But that's also where we run into the first problem.
Well, two problems.
Three, actually.
First, [and as I said before]({filename}2020-03-30_graf_againstmath1.md), this kind of definition only works for specific axiomatizations of sets, and that's a lot of baggage to attach to your linguistic proposal.
Second, redefining Merge in that way means that large parts of the audience will immediately check out.
A major deviation from established machinery is always a tough sell, so you should avoid that if you can.
And then there's still problem three, which in a sense is the worst because it brings with it a rats tail of other problems.

You see, the set-theoretic representation of tuples used by Fortuny doesn't work in full generality.
Consider the following tuples and their set-theoretic representation as nests:

1. $\langle a, b \rangle = \{ \{a\}, \{a,b\} \}$
1. $\langle a, b, a \rangle = \{ \{a\}, \{a,b\}, \{a,b,a\} \} = \{ \{a\}, \{a,b\}, \{a,b\} \} = \{ \{a\}, \{a,b\} \}$
1. $\langle a, b, b \rangle = \{ \{a\}, \{a,b\}, \{a,b,b\} \} = \{ \{a\}, \{a,b\}, \{a,b\} \} = \{ \{a\}, \{a,b\} \}$

As you can see, three distinct triples all end up with same set-theoretic encoding.
That's not good.
This means that if your syntax outputs $\{ \{a\}, \{a,b\} \}$, you don't actually know if it gave you the tuple 
$\langle a, b \rangle$,
$\langle a, b, a \rangle$,
or
$\langle a, b, b \rangle$.
If your encoding can't keep things distinct that should be distinct, it's not a great encoding.

Fortuny is aware of that, and he has a workaround.
Since the problem only arises for tuples that contain identical elements, one has to ensure that there are no identical elements.
To this end, he subscripts each entry with the derivational step at which it was introduced.
Here's what this would look like for our previous counterexample:

1. $\{ \{a_1\}, \{a_1,b_2\} \} = \langle a_1, b_2 \rangle$
1. $\{ \{a_1\}, \{a_1,b_2\}, \{a_1,b_2,a_3\} \} = \langle a_1, b_2, a_3 \rangle$
1. $\{ \{a_1\}, \{a_1,b_2\}, \{a_1,b_2,b_3\} \} = \langle a_1, b_2, b_3 \rangle$

Alright, that fixes the math problem, but it creates even bigger problems --- I told you its a rat tail.
Now that Fortunay has added subscripts, and he has to allow for arbitrary many of them.
From a computational perspective, that's not that great.
At best it's clunky, at worst it creates serious issues with computational power.
And from a linguistic perspective, it violates the Inclusiveness condition [@Chomsky95a], according to which syntax does not enrich lexical items with any mark-up, diacritics, or other encodings of non-lexical information.
I certainly am not gonna lose any sleep over somebody's proposal violating the Inclusiveness condition, but I'd wager that this attitude isn't shared by the main audience for a pure theory paper on Merge and linearization.
The set-theoretic formalism has forced Fortuny into a stance that makes his argument, which ultimately doesn't hinge on sets, less attractive to his target audience.

If you're willing to accept all those modifications, you now have a system where linear order is baked directly into syntax.
But Fortuny still has to tell us why linear order doesn't seem to matter all that much, then.
He relates this to a crucial limitation of Merge.
As you might have noticed, the nesting system doesn't work as intended when you try to merge a complex specifier.
Suppose you have already built the complex specifier $\{d, e\}$, ignoring subscripts because the notation is cluttered enough as is.
Suppose furthermore that $\{d, e\}$ belongs to the constituent $\{ \{d\}, \{d, e\} \}$.
Let's try to merge $\{d, e\}$ into $\{ a, b, c \}$, which is part of the constituent $\{ \{a\}, \{a,b\}, \{a,b,c\} \}$.
What should be the output?
Fortuny says that the whole constituent $\{ \{d\}, \{d, e\} \}$ is merged in, yielding the output $\{ a,b,c, \{ \{d\}, \{d,e\}\}\}$.
Adding this to the previous constituent $\{ \{a\}, \{a,b\}, \{a,b,c\} \}$, we get the new constituent
$$
\{ \{a\}, \{a,b\}, \{a,b,c\}, \{ a,b,c \{\{d\}, \{d,e\}\} \} \}
$$
Not the most readable, but internally consistent.

Fortuny then observes that in general we do not want to allow movement from such subconstituents --- the Specifier Island Constraint and the Adjunct Island Constraint strikes again.
Under the assumption that Move is just a variant of Merge, he defines a single application domain for Merge that does not allow this operation to target any proper part of the subconstituent $\{\{d\}, \{d,e\}\}$.
But if you take that as a general constraint on syntax, it also means that syntax cannot directly relate $d$ and $e$ to $a$, $b$, or $c$.
Consequently, syntax cannot define a linear order over all of $a$, $b$, $c$, $d$, and $e$.
And that's why linear order in syntax has very limited role, even though linear order is directly baked into syntax.


# Did the sets help?

Alright, time to take stock.
If we compare Fortuny's set-theoretic operations to the more high-level story I presented above, do the sets actually illuminate anything?
I don't think so.

You don't need nests to establish that the syntactic computation naturally furnishes all the asymmetries that are needed to establish linear order.
Actually, nests muddle this point because they force you into dealing with occurrences, subscripts, the Inclusiveness condition, and all that other stuff that's completely orthogonal to the core issue.
Nor do sets really help us understand why the role of linear order is limited.
Fortuny stipulates a specific notion of domain based on empirical observations about Move, but that's completely independent of sets as it's a generalized version of the Specifier and Adjunct Island constraints.
And those are all just more specific instances of the assumption that sensing tree automata are a computational upper bound on syntactic expressivity.
I'd also say that Fortuny's set-based definition of domain is much harder to make sense of than sensing tree automata.
Overall, the set-based presentation is a detriment to the paper, not a boon.

It's unfortunate, because Fortuny's big picture points are right on the money imho.
But they're buried under the mathematical clutter of sets, sets, and more sets.

## References
