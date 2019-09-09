---
title: >-
    A final stroll through the complexity zoo in phonology
authors:
    - Thomas Graf
date: 2019-09-09
bibliography: references.bib
series: >-
    The subregular locality zoo
tags:
    - subregular
    - phonology
    - locality
    - strictly piecewise
    - strictly local
    - tier-based strictly local
    - typology
    - learnability
---

<!-- START_SUMMARY_BLOCK -->
After [a brief interlude]({filename}/Discussions/2019-09-05_graf_corpuslinguistics.md), let's get back to locality.
This post will largely act as a recap of what has come before and provide a segue from phonology to syntax.
That's also a good time to look at the bigger picture, which goes beyond putting various phenomena in various locality boxes just because we can.
<!-- END_SUMMARY_BLOCK -->

## What were all those locality classes again?

To recap: there are various degrees of locality, which are formalized in terms of the subregular classes
[SL]({filename}locality_sltsl.md#strictly-local-sl),
[TSL]({filename}locality_sltsl.md#tier-based-strictly-local-tsl),
[ITSL]({filename}locality_iotsl.md#adding-context-information-input-tier-based-strictly-local-itsl),
[OTSL]({filename}locality_iotsl.md#adding-projection-interdependencies-output-tier-based-strictly-local-otsl),
[IOTSL]({filename}locality_iotsl.md#mixing-input-and-tier-configurations-input-output-tier-based-strictly-local-iotsl),
and
[SP]({filename}locality_sp.md#complete-non-locality-strictly-piecewise-sp).
All of them have in common that they reduce well-formedness of a structure *S* to the question whether *S* contains at least one of finitely many forbidden substructures.
Their difference in power arises from what those relevant substructures are.

For SL, the forbidden substructures are substrings.
If a list contains *nb* and *np*, this means that no string may contain these particular consonant clusters.
SL captures strict locality, where phenomena take place within a domain of finitely bounded size (e.g. at most 5 adjacent segments).

SP occupies the very other end of the spectrum.
The forbidden substructures of SP are subsequences.
If the list of forbidden substructures contains *nb* and *np*, this means that a string must not contain any *n* that is followed by *b* or *p*, no matter how far apart the two are.
SP phenomena apply across arbitrary distances without any regard to locality, they are non-local.

The various types of TSL reflect notions of relativized locality.
Like SL, TSL and its extension operate with forbidden substrings.
The substrings aren't applied directly to the string, though.
Instead, one first projects a tier and then checks this tier for forbidden substrings.
The TSL variants differ in what information they may use to decide whether some segment *s* should go on the tier.
TSL may only look at *s* itself, ITSL may consider the local context of *s* in the string, OTSL may consider the local context of *s* on the tier, and IOTSL may do both.
They all share the intuition of relativized locality that there are elements that matter (i.e. what is on the tier) and elements that do not matter (i.e. what is not on the tier), and only the former matters for locality considerations.

It is commonly assumed by linguists that non-local phenomena are the most complex, but this is not true.
As we have seen, [every SP phenomenon is also OTSL]({filename}locality_sp.md#non-locality-does-not-subsume-locality), which means that the corresponding non-local constraints can be restated in terms of relativized locality.
The diagram below summarizes the subsumption relations between the various locality classes.

![Subsumption relations between various subregular classes]({static}/img/thomas/subreg_tutorials/sp_hierarchy.svg)

## Who cares?

Unless you're very OCD (guilty as charged), putting linguistic phenomena into various little boxes depending on some mathematical notion of locality may seem like a pointless exercise.
But these boxes are actually useful.

### Typology

First, complexity seems to be inversely related to typological frequency.
It is very easy to find phenomena that are SL or SP.
TSL is also pretty robust, but you're really moving into a territory where it wouldn't seem hopeless to write down a list of all phenomena that fit into this class and none of the weaker ones.
ITSL only has a handful of phenomena, including some blocking effects in Samala, Korean vowel harmony, and non-final RHOL.
OTSL has a whopping number of 0 attestations, and IOTSL has the Uyghur harmony pattern for suffix vowels and Sanskrit n-retroflexion (aka *nati*).
The empirical status of Sanskrit n-retroflexion is unclear, and Uyghur harmony might also turn out to be much simpler.

Phenomena reducing in complexity as we learn more about them isn't unusual.
Estonian has a case alternation that used to be described in terms of the number of syllables in the stem: if the stem has an even number of syllables, use allomorph X, if it has an odd number, use allomorph Y.
Even/odd distinctions are a case of *modulo* counting, and this cannot be done with our subregular classes.[^OTSL]
But as it turns out, the allomorphy isn't actually conditioned by the number of syllables, but by the position of the rightmost stress in the stem [@Kager96].
This actually makes the Estonian case allomorphy an SL phenomenon.

[^OTSL]: Actually, it is an open question whether OTSL or IOTSL can do modulo counting, but I'm 99.9% sure that the answer is No. Anybody looking for a topic for a short paper? This might be a good one. Or maybe it will result in you wasting years of your life with little progress because the proof is much harder than I think. If so, read this sentence many years from now to receive my belated apologies.

Anyways, the key point here is that as we move up in complexity, the phenomena that motivate these classes are increasingly rare.
The table below gives you a quick overview.
Phenomena are only listed for the weakest class(es) that can accommodate them.
I could have written down tons of things for SL, SP, and TSL.
With ITSL, the selection is almost an exhaustive list of what has been found so far.
For OTSL and IOTSL it is exhaustive.

| **Class** | **Segmental phenomenon**            | **Suprasegmental phenomenon** |
| --:       | :--                                 | :--                           |
| SL        | intervocalic voicing                | penultimate stress            |
| TSL       | Samala sibilant harmony             | culminativity                 |
| ITSL      | Korean vowel harmony                | unbounded tone plateauing     |
|           |                                     | non-final RHOL stress pattern |
| OTSL      |                                     |                               |
| IOTSL     | Uyghur backness harmony             |                               |
|           | Sanskrit *n*-retroflexion/nati      |                               |
| SP        | Samala sibilant harmony             | unbounded tone plateauing     |

The inverse correlation between complexity and typological attestation is curious.
Personally, I think of it in terms of an evolutionary metaphor: the higher the complexity, the more specific the parameters that your survival depends on.
Minor changes to the ecosystem will be more disruptive for an IOTSL phenomenon than an SL phenomenon, which can make do with pretty much anything.
So it's much less likely than an IOTSL phenomenon will survive long enough to be found by linguists.
One could hash this out in terms of Charles Yang's learning model [@Yang02] or Gerhard Jäger's game-theoric account of language evolution [@Jaeger10].
Quite generally, it would be very interesting to look at language change through the subregular lens.
Afaik nobody's done that yet, so for now we'll have to make do with a correlation and a metaphor.

### Learning

While the evolutionary metaphor hasn't been explored yet, learning certainly has.
There's learning algorithms for SL, SP, TSL, and soon ITSL (OTSL and IOTSL are still open, so those two really are the odd ones out in several respects).
Those learning algorithms adopt the Gold paradigm of learning, so they're not meant to be plausible models of language acquisition.
But they do provide some key insights.
First of all, you need a bit of UG.
Concretely, the learner must have an innate upper bound on the maximum size of substructures.
If you tell the learner "here's some data, learn the right SL constraint", then it's not gonna work.
But if you tell it "here's some data, learn the right SL constraint assuming that no forbidden substring is longer than 3", then the algorithm will succeed given enough data.
How much data?
Well, it depends on the complexity of the class, but overall a surprisingly small amount.
In the Gold paradigm, you sometimes get learning results that are underwhelming because they require tons of data.
SL, SP, and TSL are **efficiently learnable** [@KasprzikKotzing10; @Heinz.etal12; @JardineMcMullin17], which means that the amount of data they need stays below a pretty tight threshold.

It's nice to know that linguistic phenomena fall into classes that look very reasonable from a learning perspective.
This actually isn't trivial, in particular if you subscribe to the old-school view of a very rich UG.
The more information a learner is given in advance, the less data is needed to learn, and this can make a class efficiently learnable even if it allows for ludicrously complex phenomena.
To give a rather extreme example: if UG allowed for only one language, then this language would be learnable even if it requires the length of every well-formed sentence to be a prime number.
The less specific UG is, the more slack has to be picked up by the learning algorithm, turning the latter into an effective upper bound on the range of variation.
So the fact that we don't find particularly complex phenomena, and that efficient learnability can be achieved with very little prior information is linguistically insightful and sheds some light on the nature of UG.

### Cognitive parallelism

Alright, typology and learnability is all nice and dandy, but let's turn to what I consider the killer feature: cross-module notions of complexity.
While SL, SP, and the various TSL varieties were developed for phonology, they are not limited to just that.
Of course we can apply them to any domain with a string-based representation, from phonology to morphology and [even parts of semantics]({filename}/Discussions/2019-07-26_graf_kiss_semantics.md).
In one of the upcoming posts, we'll see that even some aspects of syntax can be studied from a string-based perspective.
But where this isn't enough, it is relatively easy to lift these notions of complexity from strings to trees, which allows us to directly compare the complexity of phonological dependencies to syntactic dependencies.
And what is truly striking about this is just how uniform the two turn out to be from this perspective.
Island constraints?
The counterpart to phonological blocking effects.
Idioms and suppletion?
Pretty much local assimilation.
Prosody?
Well that's just... um, okay, prosody will turn out to be a really tough nut, at least when we consider its interaction with focus.
So buckle up and strap in, it's finally time for syntax!

## References
