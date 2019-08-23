---
title: >-
    Extensions of TSL
authors:
    - Thomas Graf
date: 2019-08-22
bibliography: references.bib
series: >-
    The subregular locality zoo
tags:
    - subregular
    - phonology
    - locality
    - tier-based strictly local
---

<!-- START_SUMMARY_BLOCK -->
The [previous post]({filename}locality_sltsl.md) covered the essentials of strictly local (SL) and tier-based strictly local (TSL) dependencies over strings.
We saw that even though TSL generalizes SL to a relativized notion of locality, it is still a restrictive model in the sense that not every non-local dependency is TSL.
In principle that's a nice thing, but among those non-local dependencies beyond the purview of TSL we also find some robustly attested phenomena like unbounded tone plateauing.
Fair enough, but that does not mean that unbounded tone plateauing is entirely non-local.
<!-- END_SUMMARY_BLOCK -->

### Adding context information: input tier-based strictly local (ITSL)

Remember that standard TSL relies on tier projection to mask out irrelevant material, creating a kind of relativized locality.
Crucially, the tier projection mechanism only looks at a segment in isolation and never takes its structural context into account.
For instance, we cannot choose to only project *n* whenever it is part of a consonant cluster --- either all instances of *n* project, or none of them do.
That's a major limitation of TSL (and it is interesting that so many phonotactic dependencies are TSL despite this restriction).

We get an even more relaxed notion of locality if the tier projection mechanism of TSL is sensitive to strictly local context information.
That is to say, we may now project only some instances of a given segment, provided we can make the decision based only on a surrounding context up to some finitely bounded size.

Here's what this looks like for unbounded tone plateauing.
We first project every high tone H, no matter what it's context.
A low tone L, on the other hand, projects iff it appears immediately after an H.
That's SL information because we only need to look one segment to the left of each L.
In fact, it is SL-2 because we only need to consider two adjacent segments: the segment to be projected, and one piece of the surrounding context.
Context-information can't get any more local than that without reducing to standard TSL.

![Unbounded tone plateauing is TSL if the tier projection is sensitive to SL-2 contexts.]({static}/img/thomas/subreg_tutorials/itsl_toneplateauing.svg)

With this projection mechanism, \*LHLLLHL receives the tier HLH.
And that's also the tier of \*LHLLLLLLHL, and \*HLLHLLLL.
Some strings will also have longer tiers, e.g. \*LHLLLHHHHLLLH gets HLHHHHLH.
But an illicit string will always have a tier that contains HLH.
And in the other direction, if HLH appear anywhere on the tier, the whole string must contain a violation of unbounded tone plateauing.
So now we have reduced unbounded tone plateauing to an SL dependency: no tier may contain HLH.
This extension of TSL is called **input tier-based strictly local**, or simply **ITSL**.

## ITSL still is not enough

Alright, so we've gone from SL to TSL and now to the even more relaxed notion of ITSL.
Surely that will cover all linguistically relevant notions of locality, right?
Obviously not, otherwise I wouldn't have asked.
@MayerMajor18 point out that Uyghur backness harmony is not TSL, and I'll show you guys here that it's not ITSL either.

At first glance, Uyghur backness harmony seems simple enough.
Some stems show up with a single suffix.
The vowel in this suffix must match the backness of the final harmonizing vowel in the stem.
Alright, that's easy peasy, project all harmonizing vowels, project the suffix vowel, do not project any other vowels or consonants, and do not allow the last two vowels on the tier to differ in backness.

![A simple version of Uyghur backness harmony is ITSL.]({static}/img/thomas/subreg_tutorials/itsl_uyghur_simple.svg)

Boom, there's your backness harmony, and it's all TSL.
Except things aren't that simple.

You see, some words may not contain any harmonizing vowels at all.
In this case, the suffix vowel must match the backness of the last harmonizing dorsal consonant.
Careful: the last harmonizing consonant isn't necessarily the last consonant of the stem.
It could even be the first one as long as it the last consonant that can participate in harmonies.
Now we have a problem (we actually have two, but one thing at a time).
We not only want to project harmonizing vowels, but also harmonizing consonants.
If we do that, though, we may loose track of the harmonizing vowel in cases where it is actually present.
At full generality, there may be arbitrarily many harmonizing consonants between the harmonizing vowel and the suffix.
If we project all those consonants, the harmonizing vowel and the suffix vowel will no longer be in a strictly local configuration on the tier, and consequently we cannot use (I)TSL to enforce harmony between them.

![Harmonizing consonants on the tier may accidentally push a harmonizing vowel out of the "constraint window".]({static}/img/thomas/subreg_tutorials/itsl_uyghur_consonants.svg)

But hold on a second, we don't need all harmonizing dorsal consonants, only the last one.
If we project only that guy, we're back to an SL configuration on the tier: the tier will start with a string of 0 or more harmonizing vowels, followed by at most one harmonizing consonant, and the suffix vowel.
We only need to pay attention to the last three symbols on the tier to guarantee harmony.
Alright, that works --- assuming we can limit projection of consonants to just the last one.
Unfortunately, we cannot.

TSL is a non-starter because we don't get to use context information, and clearly you need at least a teeny bit of context to distinguish the **last** harmonizing dorsal consonant from those that come before it.
But ITSL doesn't work either because finding the last harmonizing dorsal consonant isn't strictly local over the input.
If the last harmonizing consonant were always, say, at most 3 segments away from the stem boundary \#, then we would have a strictly local context that clearly identifies this consonant.
But there doesn't seem to be such a principled bound.
There's a few other things one could try, but at the end of the day there isn't a satisfying ITSL solution that doesn't hinge on specific properties of Uyghur such as the syllable template and the maximum length of existing words.
Like TSL, ITSL just won't cut it for Uyghur's backness harmony.
At the same time, though, it isn't exactly non-local either...


### Adding projection interdependencies: output tier-based strictly local (OTSL)

About two years ago there was a horribly uncreative sod that I will refer to as TG.
TG figured if there's an input-based extension of TSL, we might just as well define an output-based extension and see if it's useful for anything.
And thus the class of **output tier-based strictly local (OTSL)** dependencies was born.
Or rather, stillborn, because TG couldn't find any phenomenon that worked this way.
But then TG happened to be a reviewer for @MayerMajor18 and suggested OTSL as a solution for Uyghur backness harmony.

Like ITSL, OTSL gets to take strictly local context information into account.
However, an OTSL dependency considers configurations on the tier instead of the input string.
In OTSL, one can say things like "project X unless the tier constructed so far ends in a Y".
That makes Uyghur's backness harmony a piece of cake:

1. Always project a harmonizing vowel.
1. Project a harmonizing consonant unless the tier built so far ends in a vowel.
1. Project the suffix vowel.
1. The last two symbols on the tier must agree in backness.


By preventing consonants from projecting if there's already a vowel on the tier, we capture the fact that consonants only matter in the absence of harmonizing vowels.
This is the main perk of OTSL: it allows us to capture certain conditionals of the form "if X, do Y, otherwise Z".
Another advantage is that we can flatten multiple instances of the same symbol into one.
For instance, unbounded tone plateauing is not just ITSL but also OTSL: always project H, and only project L if the previous symbol on the tier is H.
This kind of flattening and conditional projection is actually very useful for syntax, but that's a topic for one of the follow-up posts.


### Mixing input and tier configurations: input output tier-based strictly local (IOTSL)

We're not quite done with Uyghur backness harmony yet.
We've only handled problem #1, the interaction between harmonizing vowels and consonants.
The OTSL account above presumes that we can easily identify the suffix vowel without any context information.
But that's not the case at all, giving us problem #2.
Yes, if the suffix vowel is a harmonizing vowel, then it will be projected because we always project harmonizing vowels.
It could also be a non-harmonizing vowel, though, and that too needs to project.
So we always have to project the last vowel in the word, no matter what.
That's a strictly local configuration, but it's SL over the input, not the tier.
This means that Uyghur actually requires a tier projection mechanisms that uses both input information and tier information.
This makes it **input output tier-based strictly local** (IOTSL).

Uyghur actually corresponds to a specific subclass of IOTSL where the input and output information do not mix.
That is to say, we have no projection rule of the form "project X iff both of the following hold: X is followed by Y in the input and the current tier ends in Z".
We might call this **autonomous IOTSL**, a term I just made up.
Autonomous IOTSL differs from **blended IOTSL**, which allows such mixing.
Yes, that's another term I just made up.
And I'll also unleash the corresponding acronyms aIOTSL and bIOTSL on the world because we mathematical linguists love a good symbol salad.

Before you ask, there is actually one phenomenon that is bIOTSL but not aIOTSL: Sanksrit *n*-retroflxion, also known as *nati*.
But I won't talk about it here.
Connor and me showed that *nati* is IOTSL [@GrafMayer18Sigmorphon], and that's it, I've had my share.
This phenomenon is such a Lovecraftian descent into phonological madness that I've come to the conclusion that all the data was planted by a time-traveling linguist as some kind of 4-dimensional prank.
Still, it's blended IOTSL and hence local... in a bloody demented way.


## Lesson(s) of the day

TSL is not the end of the line when it comes to relativized locality.
We can make tier projection dependent on the local context.
But there are two choices for the context: the context in the string, or the context in the tier.
Depending on these choices, we get ITSL or OTSL.
And we can combine the two to get IOTSL.

ITSL has all kinds of applications, from unbounded tone plateauing to the non-final RHOL stress pattern or Korean vowel harmony.
OTSL is a bit of an oddball in that it doesn't seem to do much on its own, but makes for a viable addition to ITSL.
IOTSL seems to cover pretty much anything in natural language phonotactics (primary stress in Creek and Cairene Arabic might be an exception, but the data is contested).
One might say, then, that relativized locality reins supreme when it comes to phonotactics.
But there are many shades of relativized locality (TSL, ITSL, IOTSL), and the higher up one moves in that hierarchy, the harder it is to find robust phenomena.
For whatever reason, the typological frequency of dependencies seems to be inversely correlated with their complexity.

## References
