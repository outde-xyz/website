---
title: >-
    Vision on P vs. NP
authors:
    - Thomas Graf
date: 2019-07-03
bibliography: references.bib
tags:
    - fun allowed
    - complexity theory
---

<!-- START_SUMMARY_BLOCK -->
Come and listen to the Vision of the Avengers, who has saved this planet thirty-seven times.
Listen to his story of P vs. NP.
No, seriously, the following is an excerpt on complexity theory from Tom King's *Vision*.
<!-- END_SUMMARY_BLOCK -->

<a href="{static}/img/thomas/fun_allowed/pnp1.png">
    <img src="{static}/img/thomas/fun_allowed/pnp1_small.jpg">
</a>
<a href="{static}/img/thomas/fun_allowed/pnp2.png">
    <img src="{static}/img/thomas/fun_allowed/pnp2_small.jpg">
</a>
<a href="{static}/img/thomas/fun_allowed/pnp3.png">
    <img src="{static}/img/thomas/fun_allowed/pnp3_small.jpg">
</a>

Whoever said that comics can't be educational?
Well, tons of people, and they're largely right.
But this is a welcome exception.
I think this is a decent effort as far as newbie-friendly summaries of P vs. NP go.
It's certainly better than it has any right to be.
Heck, it's a pivotal moment in a story about a super-powered android pining for a 50s-style family life in a Virginia suburb --- it's certainly much more highbrow than anything I expected.
But!
Yeah, you knew there was a *but*, how could I possibly resist an opportunity to nitpick?

I really don't like how the explanation implies that the existence of efficient algorithms for NP would make all computational problems solvable.
That's a huge overstatement.
Many problems, like the Halting problem, are undecidable, so they cannot be solved algorithmically no matter what.
Even within the class of decidable problems, some are outside NP.
Practical examples are hard to come by because the usual suspects are in the class PSPACE, and we're just as far from proving P != NP as we are from proving NP != PSPACE.
But there is also the class NEXPTIME, and we know that NP != NEXPTIME.
So that would fit the bill.
NEXPTIME is to NP as EXPTIME is to P:

1. P is the class of problems that can be solved in **polynomial** time.
1. EXPTIME is the class of problems that can be solved in **exponential** time.
1. NP is the class of problems for which any purported solution can be verified in **polynomial** time.
1. NEXPTIME is the class of problems for which any purported solution can be verified in **exponential** time.

I have to admit though, I can't think of any problem that's NEXPTIME and doesn't look highly artificial.
Hold on, let me google this.

Ah, yes...

Hmm...

Right...

Okay, looks like this is the only example that makes some sense to my complexity-challenged mind:
Suppose you have two regular expressions that only use union, concatenation, and squaring.
Do they pick out the same stringset?
That's a NEXPTIME problem.

Alright, still not exactly riveting compared to the [travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem).
That's one of the reasons why P and NP are the poster children of complexity theory, the majority of interesting problems are in one of those two classes.
Perhaps a less complexity-challenged reader can graciously provide a more interest example for NEXPTIME in the comments section.

There's actually quite a bit to say about how these complexity classes relate to linguistic issues, in particular for parsing, but also binding theory.
But as you might have noticed, this is a *fun allowed* post, and I've already taken things into much too serious a direction.
So let's call it quits for today, and we'll return to complexity theory for linguistics in the near future.
As a bit of casual evening entertainment, I leave you with this complexity theory oldie-but-goodie:

![I hope none of you *knee*d any help to find the joke.]({static}/img/thomas/fun_allowed/pnp_futurama.jpg)
