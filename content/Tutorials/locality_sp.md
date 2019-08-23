---
title: >-
    Full non-locality: Strictly piecewise
authors:
    - Thomas Graf
date: 2019-08-24
bibliography: references.bib
series: >-
    The subregular locality zoo
tags:
    - subregular
    - phonology
    - locality
    - strictly piecewise
---

<!-- START_SUMMARY_BLOCK -->
We're continuing our stroll through the subregular locality zoo, still in the service of ultimately being able to say something about syntax and its interface with PF and LF.
We started out with SL as the most restrictive kind of locality.
The step to the TSL region corresponds to a relativized notion of locality where it's not absolute locality that matters, but your position relative to other elements of a specific type.
TSL is actually a cluster of different classes, with standard TSL at the very bottom.
Depending on what context information the TSL tier projection may take into account, TSL expands to ITSL, OTSL, or IOTSL.
While IOTSL has a very liberal notion of locality that can even accommodate insane patterns like *nati*, it still involves some level of locality.
That's in stark contrast to the **strictly piecewise** (SP) dependencies of @Rogers.etal10, which throw locality out the window.
<!-- END_SUMMARY_BLOCK -->

## Complete non-locality: strictly piecewise (SP)

SP works just like SL in that it only provides a finite list of forbidden configurations.
But whereas SL specifies forbidden substrings, SP specifies forbidden subsequences.
Every substring is a subsequence, but the opposite does not hold.
For instance, the length 2 substrings of *abbccc* are *ab*, *bb*, *bc* and *cc*.
These are also length 2 subsequences, but *ac* is a length 2 subsequence that is not a length 2 substring.
So subsequences differ from substrings in that they may skip elements in the string.
They can pick out disconnected pieces of the string, hence the name strictly piecewise.

As SP is all about subsequences, it has absolutely no notion of locality beyond relative order.
An SP constraint against *ab* does not care whether *a* and *b* are right next to each other or separated by three trillion other segments.
Zero, three, three trillion, it's all the same for SP.
SP does not care how many instance of *a* and *b* there are, either.
SP does not care whether anything intervenes between *a* and *b*.
It's a blanket ban against any *a* being followed by any *b* at any distance.
Locality?
SP doesn't give a hoot.

Samala sibilant harmony and unbounded tone plateauing are examples of SP dependencies.
Yes, they were examples of TSL and ITSL, respectively, but a dependency can belong to multiple classes.
That's actually the case for most phenomena, and that's a welcome state of affairs because it deepens our formal understanding.
Anyways, let's look at those two phenomena as examples of SP.

For sibilant harmony, one forbids [+ anterior] sibilants to be preceded or followed by [- anterior] sibilants.
It's very similar to the TSL account, except that the tier is no longer needed because there is no notion of locality that the tier would have to relativize.
Unbounded tone plateauing is also very easy, just ban the subsequence HLH.
This subsequence occurs in all strings that violated tone plateauing, and only those.

## Non-locality does not subsume locality

Linguists usually work under the assumption that strict locality is weaker than relativized locality, which in turn is weaker than non-locality.
SP shows that this is not necessarily the case.
First of all, SL and SP are incomparable, which means that there are SL dependencies that are not SP, and there are SP dependencies that are not SL.
Samala sibilant harmony and unbounded tone plateauing are SP dependencies that are not SL, whereas intervocalic voicing is an SL dependency that is not SP.
If it were, it would work like unbounded tone plateauing in the sense that no voiceless sibilant may occur in an interval spanned by two voiced segments, no matter how far apart they are.

SP is also incomparable to TSL, for two reasons.
First, SP cannot require the presence of an element, as is the case with **culminativity** [@Heinz14].
Culminativity means that a phonological word has at most one primary stress and at least one primary stress.
Which is just a convoluted way of saying exactly one primary stress.
SP can block the presence of more than one primary stress, but it cannot enforce the presence of a primary stress.
If all you can do is say what may not occur anywhere in the word, you have a hard time requiring that something must occur.

Second, SP cannot handle blocking effects.
Suppose that *a* must never be followed by *c* unless a *b* occurs between them.
That's very easy in TSL, but it's impossible for SP.
Go ahead, try it yourself, or even better, pose it as a challenge to your class when you need a breather of 5 to infinity minutes.
It can't be done.
SP ain't got no clue about blocking.

Even more surprising from a linguistic perspective is that SP is properly subsumed by OTSL (and hence also by aIOTSL and bIOTSL).
Yes, non-locality can be reduced to relativized locality, at least when you're SP and don't get to do much with your non-local prowess.
The reduction is a bit odd, though.
It uses output-sensitive projection to reduce every string to a tier of at most length *l* so that every dependency is trivially strictly local by virtue of involving at most *l* symbols on the tier.
In detail:

1. Since every SP dependency can be described by a finite list $F$ of forbidden subsequences, there are only finitely many configurations to consider.
   Let this number be *n*.
1. Since the number of forbidden subsequences is finite, there is a longest forbidden subsequence of length *k*.
1. All *n* configurations can be instantiated as subsequences of a string whose length is at most $l := k \cdot n$.
1. Now suppose furthermore that we prepend a diacritic $\diamond$ to each forbidden subsequence in $F$.
   The diacritic keeps track of how much of a subsequence is instantiated in a string.
   For instance, we may have $a b \diamond c d$ in a string $cdaacb$.
   When the string is expanded to $cdaacbc$, $\diamond$ shifts one to the right to give us $a b c \diamond d$.
1. Suppose we have an OTSL projection that can look at the preceding *l* symbols on the tier.
   We project a symbol iff doing so would cause at least one $\diamond$ in $F$ to shift one step to the right.
1. It follows that every tier has at most length $l$.
   We forbid every string of length $l$ that contains an illicit subsequence according to $F$.
   This is an SL description on the tier.
1. Consequently, we have reduced a non-local (SP) dependency to a local (OTSL) dependency.

The reduction isn't cheap, and we might find a huge mismatch in the number of involved segments.
In the first post we discussed that an SL-7 dependency might also be, say, a TSL-3 dependency --- relativized locality gives us a more succinct description.
The connection between SP and OTSL is the opposite: an SP-2 dependency could end up being an OTSL-12 dependency.
In fact, the blow-up can be much worse than that.
But then again, OTSL can do things SP cannot.
So we have a general trade-off between strict locality, relativized locality, and non-locality on the one hand and the size of forbidden configurations on the other.

As a result, locality is a multi-faceted issue.
One the one hand, we have clear subsumption relations between the full classes.

![Subsumption relations between various subregular classes]({static}/img/thomas/subreg_tutorials/sp_hierarchy.svg)

But on the other hand, we get incomparability once we consider the size of forbidden configurations.
SL-5, SP-3, and IOTSL-2 are all incomparable, so there are no principled grounds for choosing between them.
If a phenomenon fits into multiple classes, it's more insightful to study it from the perspective of each one of these classes, rather than picking one on *a priori* grounds.
We can't say "TSL is more local than ITSL, so if something can be TSL, we'll analyze it as TSL and only TSL".
Locality simply ain't that simple.

## Lesson(s) of the day

SP-*k* is the class of all dependencies where the well-formedness of a give node depends on at most *k* nodes somewhere to its left and/or right.
Whereas SL picks out forbidden substrings, SP picks out forbidden subsequences.
SL and SP actually cover the large majority of phonotactic dependencies, so SP is an empirically robust class.
But many things that can be done by SP can also be done by TSL.
In fact, everything done by SP can be done by OTSL, at the expense of a much more convoluted description.

This means that locality isn't a nice linear hierarchy of the form *strict locality < relativized locality < non-local*.
There's at least two dimensions to it, one being the complexity of the underlying mechanism (substrings, subsequences, various tiers), the other one the size of the structural descriptions that are used by those mechanisms (bigrams, trigrams, etc).
That's a much more refined picture.
We should be careful when we talk about X being more or less local than Y, because that can be a very misleading statement.

## References
