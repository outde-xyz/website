---
title: >-
    The subregular locality zoo: SL and TSL
authors:
    - Thomas Graf
date: 2019-08-19
bibliography: references.bib
series: >-
    The subregular locality zoo
tags:
    - subregular
    - phonology
    - locality
    - strictly local
    - tier-based strictly local
---

<!-- START_SUMMARY_BLOCK -->
Omer has a [recent post on listedness](https://omer.lingsite.org/blogpost-listemes-and-morphemes-and-other-things/).
I have a post coming up that expands on my comments there, but it isn't really fit for consumption without prior knowledge of subregular complexity and how it intersects with the linguistic concept of locality.
So I figured I'd first lead in with a series of posts as a primer on some of the core concepts from subregular complexity.
I'll start with phonology --- for historical reasons, and because the ideas are much easier to grok there (sorry phonologists, but it's a playground compared to syntax).
That will be followed by some posts on how subregular complexity carries over from phonology to syntax, and then we'll finally be in a position to expand on Omer's post.
Getting through all of this will take quite a while, but I think it provides an interesting perspective on locality.
In particular, we'll see that the common idea of "strict locality < relativized locality < non-local" is too simplistic.

With all that said, let's put on our computational hats and get going, starting with phonology.
Or to be more specific: phonotactics.
<!-- END_SUMMARY_BLOCK -->


## The phonotactic lay of the land

Some of you might have already heard of subregular phonology.
It's a program of identifying formal mechanisms that have very limited expressivity, capture key aspects of phonology, and, ideally, are efficiently learnable.
Beyond that common goal, it's pretty freeform.
Many roads lead to Rome.
We may look at good-ol' strings (that's the corner of the program where I usually hang out because I'm old-school like that).
This subregular *string land* is where you get the classes SL and TSL that [figured prominently in an earlier post on morphosemantics](fixme).
But we could also look at *graph land* for autosegmental structures, or *mappings land* to get a better understanding of how underlying representations are converted to surface forms.
Pretty much anything is fair game as long as it is insightful.
Needless to say, that open mindset has resulted in many different perspectives on phonology.
I'll only cover string land in this post, i.e. phonotactics.
That's already a wide field.


### Strictly local (SL)

One thing that makes the subregular perspective so useful for linguistics is that it provides a plethora of distinct notions of locality.
**SL** and **TSL** are both local, but SL is more local (it's the pigs).
SL is the class of **strictly local** dependencies, which can be expressed by a finite list of forbidden substrings.
Think intervocalic voicing, which can be expressed as "don't have VsV", "don't have VfV", and so on.

SL can also handle unbounded phenomena as long as they proceed in strictly local steps.
Many types of vowel harmony work like this.
They are unbounded in the sense that there is no maximum number of harmony steps after which it stops.
Even if your word has 100 vowels, they all need to be harmonic.
But vowel harmony is still SL because the harmony moves from one vowel to the next, and each vowel can only be so far away from the next one.

As a concrete example, consider a language with

- CV and CVC as the only licit syllable templates, and
- a 5-vowel system *a*, *e*, *i*, *o*, *u*, and
- *b* and *m* as the only consonants.

Now suppose that this language requires all vowels to agree in backness (and that there are no neutral vowels).
This vowel harmony system is SL-4, which means that the longest forbidden substrings consists of at most 4 segments.
Because I'm such a nice chap I've written down the full list for you (with *a*, *o*, *u* as back vowels and *e* and *i* as front vowels):

1. abe
1. abi
1. ame
1. ami
1. obe
1. obi
1. ome
1. omi
1. ube
1. ubi
1. ume
1. umi
1. eba
1. ebo
1. ebu
1. ema
1. emo
1. emu
1. iba
1. ibo
1. ibu
1. ima
1. imo
1. imu
1. abbe
1. abme
1. abbi
1. abmi
1. ambe
1. amme
1. ambi
1. ammi
1. obbe
1. obme
1. obbi
1. obmi
1. ombe
1. omme
1. ombi
1. ommi
1. ubbe
1. ubme
1. ubbi
1. ubmi
1. umbe
1. umme
1. umbi
1. ummi
1. ebba
1. ebma
1. ebbo
1. ebmo
1. ebbu
1. ebmu
1. emba
1. emba
1. embo
1. emmo
1. embu
1. emmu
1. ibba
1. ibma
1. ibbo
1. ibmo
1. ibbu
1. ibmu
1. imba
1. imma
1. imbo
1. immo
1. imbu
1. immu

Well that's a pretty long list (thanks to a vim macro, it was actually faster to write than it is to read).
We can of course specify this more succinctly as $\mathrm{V[\alpha \text{ back}] C_1 C_2 V[-\alpha \text{ back}]}$, but it is instructive to see the long list that this expression compiles out to.

SL is agnostic about whether the list is specified as a single expression like $\mathrm{V[\alpha \text{ back}] C_1 C_2 V[-\alpha \text{ back}]}$ or can just be written down one entry after the other.
If we removed a random number of entries from the list above, the result would still be SL. 
For instance, we may remove *embo* and *ubi* to create a vowel harmony system where for some reason *e* does not need to be harmonic with *o* across *mb*, and *u* does not need to harmonize with *i* across *b*.
This is why I have avoided the standard terminology of calling such a list an **SL grammar**.
To a linguist, the term grammar conveys a lot more, in particular when it comes to issues of specification. 

From a typological perspective, the removal of *embo* and *ubi* from the list above would result in a freakish system with very unusual exceptions.
As linguists, we might not like the idea that SL can define such unusual vowel harmony systems.
I agree, but this isn't really about SL. 
The solution to this problem arguably lies in the choice of representation.
If we use features instead of segments, then we can rule out such unnatural cases by putting restrictions on how features may be used in the specification of forbidden substrings.

Matters of representation are largely orthogonal to what SL is about, though.
SL is a specific assumption about how parts of a representation may interact to determine well-formedness.
SL is the class of dependencies where the well-formedness of any given node *n* in the representation depends only on its surrounding context up to some fixed finite bound *k*.
Parts that are more than *k* steps away simply cannot affect the status of *n*.
Why linguistic substance rules out some conceivable SL interactions is a completely different issue.
What matter is that SL takes the space of all logically possible dependencies given a specific representation format and draws a clear demarcation line between what strict locality can do and what is beyond its purview.
This is good to know because SL dependencies are fairly easy to learn --- a dependency that's not SL poses a very different acquisition challenge from one that is.
As it turns out, tons of linguistics dependencies are SL, so this is a useful division with a reasonable match to the empirical landscape.
But as always with language, things aren't quite that simple and there are also some well-attested dependencies that go beyond the SL boundary.


### Tier-based strictly local (TSL)

The space beyond SL can be carved up in many different ways depending on one's mathematical inclinations and what kind of dependencies one wishes to understand better.
But for linguistics, TSL has proven particularly useful.
TSL is the class of **tier-based strictly local** dependencies [@Heinz.etal11], and as its name so kindly suggests, this class is largely inspired by linguistic ideas about locality.

TSL dependencies are no longer local in the strict sense as they can hold across arbitrary distances.
But they still have to obey a **relativized** notion of locality: if we mask out all material that is irrelevant for the dependency, the resulting dependency is SL.
This masking out corresponds loosely to the notion of phonological tiers, which allow parts of the representation to be adjacent even though other segments intervene between them.

The poster child for TSL is long-distance sibilant harmony in Samala.
It requires that the sibilants in a word must not differ in anteriority, no matter how far apart they are.
Since there is no principled upper bound on the distance between sibilants, this is not an SL dependency.
But if we ignore all segments that are not sibilants, we are left with a string that only consists of sibilants.
Long-distance sibilant harmony then reduces to the SL constraint that an anterior sibilant cannot be adjacent to a non-anterior sibilant.
And that's why the whole phenomenon is TSL.

![Even though sibilant harmony is unbounded, it is strictly local over tiers.]({static}/img/thomas/subreg_tutorials/tsl_sibilantharmony.svg)

TSL can also provide a more elegant perspective of some phenomena that are SL.
Since it was so much fun, let's go back to the SL example for vowel harmony.
It required a ludicrously long list of forbidden trigrams and 4-grams (and it would have been much longer if the example language had more than two consonants).
With TSL, we can give a more succinct description.
We can project a vowel tier which contains all string segments except the consonants.
Over that vowel tier, a handful of bigrams get the harmony job done just fine:

1. ae
1. ai
1. oe
1. oi
1. ue
1. ui
1. ea
1. eo
1. eu
1. ia
1. io
1. iu

So even though TSL isn't necessary to get the phonotactics right, the added power of tiers allows for a more pleasing description.
In particular, the TSL account completely factors out the syllable template.
It no longer matters whether syllables can only be CV and CVC, the account would work just as well for a string like CVCCCCCCCCCCCV.
TSL also allows us to handle harmony systems with neutral vowels --- those vowels simply aren't projected to the tier.
A string like CVCNCNCNCNCNCV (where each N is a neutral vowel) would still be subject to vowel harmony.
Overall, then, the TSL perspective seems to generalize in the right way for vowel harmony.
Both SL and TSL can get the job done, but TSL does it better.

It is also very important that moving from SL to TSL has allowed us to reduce the size of the forbidden substrings for vowel harmony.
We have gone from SL-4 (forbidden 4-grams over strings) to TSL-2 (forbidden bigrams over tiers).
This is insightful.
As stated as the beginning, TSL is an extension of SL, so every SL-*k* dependency is also TSL-*k*.
But it is not the case that every SL-*k* depenency is TSL-$(k-1)$.
SL-4 and TSL-2 carve out incomparable classes of dependencies.
This in and off itself is already insightful.
It tells us that this vowel harmony system is in the intersection of SL-4 and TSL-2, which is a more narrowly circumscribed region.
We have pinpointed its complexity more accurately.
But more importantly, we can then look beyond that and ask if vowel harmony as a whole is more insightfully analyzed as SL or TSL.
For all the reasons mentioned so far, TSL seems to be a better fit.


### Not everything is TSL

Now you might think TSL is a vacuous class --- of course anything can be made local if we mask out the parts that make it non-local.
First of all, don't use the term *local*!
That's too vague.
We're talking about SL and TSL here, which are very specific, rigorously defined notions of locality.
And given those specific definitions, you're dead wrong: it is not the case that every long-distance dependency is TSL.
But you're not really to blame for thinking otherwise, I glossed over a crucial aspect of TSL.
When deciding whether a segment goes on the tier, you may only consider the segment itself, not its surroundings.
That's a huge handicap.

Again we have a nice empirical example for this.
In unbounded tone plateauing, a low tone may not occur between two high tones, no matter how far apart they are.
For the sake of simplicity, let's assume a representation where L represents a syllable with low tone and H a syllable with hight tone.
So we might have strings like LHLLLL or LLLLHL, or LHHHHL, but not \*LHLLHL.
Unbounded tone plateauing is not TSL, and the reason is the lack of context-information for tier projection.
If the dependency were TSL, then it must be possible to write down a finite list of types of segments that should be masked out.
But we clearly can't mask out low tones because then we might miss an illicit L between two Hs.
And we clearly cannot mask out H for the very same reason.
Both H and L matter to unbounded tone plateauing, so neither can be masked out.
Tiers just became a big whopping pile of useless.
The tier for something like \*LHLLHL is just \*LHLLHL, which literally doesn't help things one bit.

Remember, unbounded tone plateauing can be TSL only if it is SL over tiers, and that's simply not the case over these useless tiers.
In order to decide if a low tone L is licit in its current position, we may have to look arbitrarily far to the left or right to check that there are no high tones in the same word.
Looking arbitrarily far in at least one direction is impossible with SL, so unbounded tone plateauing isn't SL over the only kind of tier we can construct.
But then it can't be TSL.
Et voilà, we have identified a long-distance dependency that is not TSL.


## Lesson(s) of the day

SL-*k* is the class of all dependencies where the well-formedness of a given node depends only on the surrounding context up to size *k*.
This includes many dependencies that are not natural from a linguistic perspective.
But this is not the point of SL.
Every formal class requires assumptions about linguistic substance to prune overgeneration.
The important insight is how dependencies of this type differ from others, what they can and cannot do.

TSL-*k* is the class of all dependencies where the well-formedness of a given node depends only on the surrounding tier context up to size *k*.
Formally, a TSL-*k* grammar is an SL-*k* grammar with a tier projection mechanism.
Whether a node is projected onto the tier depends just on the shape/label of the node itself, not its structural context.
TSL is an instance of what linguists call relativized locality: the dependency is local once one ignores material that is irrelevant for the dependency.
Some, but not all, non-local dependencies are TSL.

## References
