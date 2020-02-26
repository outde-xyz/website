---
title: >-
    Unboundedness, learning, and POS
authors:
    - Thomas Graf
date: 2020-02-26
bibliography: references.bib
series: Underappreciated arguments
tags:
    - learnability
    - poverty of stimulus
    - lattices
---

<!-- START_SUMMARY_BLOCK -->
[Ignas Rudaitis left a comment under my unboundedness post]({filename}2020-02-20_graf_underappreciated_unboundedness.md) that touches on an important issue: the interaction of unboundedness and the poverty of the stimulus (POS).
My reply there had to be on the short side, so I figured I'd fill in the gaps with a short follow-up post.
<!-- END_SUMMARY_BLOCK -->

## Learnability : POS = Complexity theory : chess

Ignas worries that if we do not assume unboundedness, then a lot of POS arguments lose their bite because unboundedness is what makes the learning problem hard.
I do not agree with the latter, at least not in the literal sense.
I think the relation between learnability results and actual language acquisition is a lot more subtle, and it is comparable to the relation between complexity theory and algorithm design.

The most famous results in complexity theory are about asymptotic worst-case complexity.
That's a fancy way of saying: how hard is it to solve a problem if everything that can go wrong does go wrong and we do not get to put an *a priori* bound on the size of the problem?
To give a flowery analogy, complexity theorists don't study the complexity of chess, they study the complexity of chess on an arbitrarily large chess board.
But since we always play chess on an 8-by-8 board, results about arbitrary $n$-by-$n$ boards seem pretty pointless.
Except that, in practice, they're not.
The interesting thing is that many of the problems that complexity theory tells us are hard in the unbounded case aren't really any easier in the bounded case.
Hard problems tend to strike both hard and early.
Boundedness doesn't fix the issue.
What you have to do is pinpoint the true source of complexity, and unboundedness is a useful assumption in doing so.

Something similar is going on with learnability results.
Learnability is all about figuring out the structure of the hypothesis space and how that can be exploited to find the target language with as little input as possible.
Unboundedness can be useful in that enterprise.
But the insights that are gained this way are largely independent of unboundedness because the learning challenges strike hard and early.

## An example from learning SL-2

Let's see how this general point works out in a concrete case, the learning of strictly 2-local languages (SL-2).
As you [might remember from an earlier post]({filename}/Tutorials/locality_sltsl.md), a language is strictly local iff it can be described by a strictly local grammar, which is a finite set of forbidden substrings.
An SL language is SL-2 iff all forbidden substrings are of length 2.
Suppose that our alphabet only contains the symbol $a$, and that we use $\$$ to indicate the edge of a string.
Then there's 4 distinct forbidden substrings of length 2:

- $aa$: don't have $a$ next to $a$
- $\$a$: don't start with $a$
- $a\$$: don't end with $a$
- $\$\$$: don't have a string without any symbols (the **empty string**)

There are $2^4 = 16$ distinct grammars that we can build from those 4 forbidden bigrams.
For instance, $\setof{ \$\$ }$ permits all strings over $a$ except the empty string.
The larger grammar $\setof{ \$\$, aa }$, on the other hand, generates the string $a$ and nothing else ( $\$\$$ rules out the empty string, and $aa$ rules out all longer strings).
Since there's only finitely many distinct SL-2 grammars, we know that the space of of SL-2 languages is finite, which means that the class of SL-2 languages can be learned in the limit from positive text.
But the standard learning algorithm for finite language classes isn't all that efficient.
We can do better if we pay attention to the structure of the space.

To this end, we take all 16 SL-2 grammars and order them by the subset relation.

![Behold the space of SL-2 grammars]({static}/img/thomas/underappreciated_unboundedness_pos/sl2_lattice.tex})

Why that's a nice powerset lattice we've got there.
The learner can exploit this structure as follows:

1. Start with the grammar at the top of the lattice as the initial conjecture.
   That is to say, assume that everything is forbidden.
1. If you see an input *i*, extract all bigrams from *i* and remove them from the currently conjectured grammar.
   The intuition: bigrams we see in the input cannot be illicit and thus must not be in the set of forbidden bigrams.
1. Continue doing this until we converge onto a specific point in that lattice.

You might say this is a really obvious learning algorithm: just discard forbidden bigrams that you see in the input.
What's so great about that?
Well, nothing.
The interesting tidbit is the lattice structure that the learner operates over.
This structure tells us that the learner can converge on the target grammar really, really fast.
The number of steps the learner has to take is bounded by the number of "levels" in the lattice.
That's because removing a bigram will always move us down by at least one level in the lattice, and we can only go so far before we hit rock bottom.
Instead of 16 grammars, we have to test at most 4 grammars after the initial hypothesis that everything is forbidden.
This fact gets a lot more impressive as we move beyond bigrams.
The space of SL-$n$ grammars over the alphabet $a$ has $2^{2^n}$ grammars, but the learner has to test at most $2^n$.
With 5-grams, that's already a huge difference --- at most 32 grammars have to be tested in the space of 4,294,967,296 grammars.
Talk about exploiting the structure of the learning space!

Crucially, this insight is completely independent of unboundedness.
Suppose that we take all SL-2 languages and limit their strings to a length of 10.
This does not change anything about the structure of the hypothesis space.
To wit, here's two diagrams, one showing the mapping from SL-2 grammars to SL-2 string languages, the other one the mapping from SL-2 grammars to SL-2 string languages with string length less than 10.
To avoid clutter, I do not arrow for grammars that generate the empty language (which is deviant as a natural language anyways).

![The function $f$ maps SL-2 grammars to the corresponding SL-2 string languages]({static}/img/thomas/underappreciated_unboundedness_pos/sl2_unbounded.tex})

![The function $g$ maps SL-2 grammars to the corresponding SL-2 string languages, restricted to strings up to length 10]({static}/img/thomas/underappreciated_unboundedness_pos/sl2_bounded.tex})

Do you see a difference?
Because I certainly don't.
The boundedness has no impact on the hypothesis space, only in the relation between grammars and generated languages.

We could have gone with a different hypothesis space, of course.
For instance, we could have used the full space of SL-10 local languages, in which case the boundedness can be directly encoded in the grammar.
But then the space will be much larger, and we will miss crucial generalizations (e.g. that no language should allow *aa* while forbidding *aaa*).
And that's the POS argument right there.
Based on how those languages behave, the hypothesis space has to have a specific structure that is exploited in a specific way.
How that space is mapped to the output of generation is less important.
In fact, shifting aspects like boundedness into the hypothesis space just messes things up.
It's the FSAs all over again: our investigation is driven by the structure of the space, the need for compact descriptions and efficient generalizations.
Boundedness is immaterial for all that, it simply does not change the picture.
A red herring indeed.
