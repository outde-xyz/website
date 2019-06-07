---
title: >-
    Surprising theorems
authors:
    - Thomas Graf
date: 2019-07-07
tags:
    - history
    - literature
    - formal language theory
---

<!-- START_SUMMARY_BLOCK -->
Time for a quick break from the feature saga.
A [recent post on the Computational Complexity blog](https://blog.computationalcomplexity.org/2019/06/what-happened-to-surprising-theorems.html) laments that theorems in complexity theory have become predictable.
Even when a hard problem is finally solved after decades of research, the answer usually goes in the expected direction.
Gone are the days of results that come completely out of left field.
This got me thinking if mathematical linguistics still has surprising theorems to offer.
<!-- END_SUMMARY_BLOCK -->

The field definitely had its share of results that can be considered surprising, although this is hard for me to judge decades later with little first hand experience.
Even limiting myself to the last 30 years I can think of at least half a dozen results that weren't obvious or contradicted expectations.
I imagine that the weak equivalence of TAG, CCG, Head Grammar and Linear Indexed Grammars [@Joshi.etal91] must have been a bombshell at the time.
The weak equivalence of MGs and MCFGs [@Harkema01;@Michaelis01] can't have been obvious or expected, either.
Or the excessive power of feature percolation and the Specifier Island Constraint [@KobeleMichaelis05].
On the empirical side, there were some interesting finds beyond the mild context-sensitivity boundary, e.g. Chinese number names [@Radzinski91], Old Georgian case stacking [@MichaelisKracht97], or the relativized predicate construction in Yoruba [@Kobele06].
Those aren't theorems, though, and as always with empirical data there was immediate debate about the robustness of the findings.
Still, that's indirect evidence that the findings were surprising, otherwise there wouldn't have been attempts to discuss them away.

However, nothing has ever surprised me more than [Sylvain Salvati's proof that the MIX language is a 2-MCFL](https://hal.inria.fr/inria-00564552/document) [@Salvati11a].
Perhaps that's just due to my limited understanding at the time, but I always thought of the MIX language as this crazy-complex thing.
The MIX language contains exactly those strings over *a*, *b*, and *c* where the number of *a*s, *b*s, and *c*s is the same.
In contrast to $a^n b^n c^n$, though, the symbols may occur in any order --- *aabbcc*, *abcabc*, *aacbbc*, *cbaabc*, all of them are fine.
The MIX language is like a farcical exaggeration of a free word order language.
No free word order language in the world allows you to shuffle the words in any arbitrary order.
You simply can't infer from the well-formedness of *That John thinks that Bill surprised Mary surprised Bill* that *Bill that that Mary surprised John Bill thinks surprised* is well-formed.
No language is that free.
Except the MIX language, so it was always a go-to example of something you don't want to generate.
Then Sylvain comes along and shows it's a 2-MCFL, so not that complex at all.
Easily done with an MG.
Yikes!
And it's not just the theorem that's surprising, the proof is highly unusual, too, as it translates the formal language problem into one of discrete geometry and tackles it through Jordan curves.
The whole paper was just a giant WTF to me, and it still blows my mind today.

In hindsight, I can kind of see that Sylvain's result isn't all that unexpected.
It's very easy to define a pushdown automaton for the MIX language over *a* and *b*, so the MIX language over *a*, *b* and *c* just requires a bit more counting power.
Since pushdown automata are equivalent to context-free grammars, which in turn generate 1-MCFLs, the minimal step up to 2-MCFLs is plausible.
But hindsight is 20-20, and it's a long road from a general idea to a sound proof.

In my own work, nothing strikes me as truly surprising.
The reduction of transderivational constraints to local ones was pretty much anticipated by earlier work on finite-state OT, and that syntax looks very similar to phonology from a subregular perspective just confirms what I always believed --- I was raised on Government Phonology, after all.
But as it says in the [original post](https://blog.computationalcomplexity.org/2019/06/what-happened-to-surprising-theorems.html), surprising theorems are rarely surprising to the researchers who established them.
So perhaps I've managed to surprise somebody once in a while.

Either way, it looks like our field still enjoys a high surprisal quotient.
And even if that may be due to a lack of maturity, I'm fine with mathematical linguistics still being stuck in the *Sturm und Drang* period of its teenage years.
