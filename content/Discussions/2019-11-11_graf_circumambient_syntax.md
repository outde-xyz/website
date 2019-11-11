---
title: >-
    Circumambient patterns in syntax
authors:
    - Thomas Graf
date: 2019-11-11
bibliography: references.bib
tags:
    - subregular
    - syntax
    - phonology
    - tone plateauing
    - movement
    - complementizer agreement
---

<!-- START_SUMMARY_BLOCK -->
Last week I gave an invited talk at UMass on the subregular program and the computational parallels it reveals between syntax and phonology.
If you're curious, [the slides are on my website](https://thomasgraf.net/output/graf19umasstalk.html).
The talk went over a lot better than I expected, and there were lots of great questions.
UMass has a tradition of letting students ask questions first before the faculty get to chime in, and the students were relentless in a good way.
I think there was only 5 minutes left for faculty questions at the end.
It was a great experience, and probably the best question period I've ever been on the receiving end of.

Anyways, after the colloquium [Brian Dillon](https://people.umass.edu/bwdillon/) asked a few questions about more complex movement cases, and those are very interesting because they're yet another instance of computational parallelism between phonology and syntax: tone plateauing = movement-driven complementizer agreement.
<!-- END_SUMMARY_BLOCK -->

## A dash of data

Let's start with some empirical data, simply because my usual posts don't have a lot of data and it's nice to mix things up once in a while.

It has been known for a long time that complementizers can be sensitive to elements that move across them.
I'll call this **movement-driven complementizer agreement**, or simply **MCA**.
The simplest form of MCA is exemplified by Irish complementizer agreement [@McCloskey79; @McCloskey01].

(@C) Deir said **gu**-r ghoid na síogaí í  
     say they C-Pst stole the fairies her  
     "They say that the fairies stole her away."

(@Cagr) [cén t-úrscéal] **a** mheas mé **a** dúirt sé **a** thuig sé *t*  
          which novel C[agr] thought I C[agr] said he C[agr] understood he  
          "Which novel did I think that he said the he understood?"

In (@C), the complementizer surfaces in its standard form *gu*.
But in (@Cagr), the complementizer is crossed by a wh-mover and thus is spelled out as *a* instead, glossed here as C[agr] instead of default C.
The surface form of the complementizer thus is contingent on whether it is crossed by a mover.

But there are also languages where complementizers aren't just sensitive to whether a mover crosses them, but also to what this mover looks like.
One example is Kinande, where the complementizer agrees in noun class with the mover.

(@) ekihi **kyo** Kambale asi nga **kyo** Yosefu akalengekanaya **kyo** Maty akahuka *t*  
    7.what 7.wh 1.Kambale 1.know if 7.wh 1.Yosefu 1.thinks 7.wh 1.Marya 1.cooks  
    "What did Kambale know that Yosefu thinks that Mary is cooking (for dinner)?"

Notice how both the wh-phrase *what* and the wh-complementizer *kyo* belong to noun class 7.

If you want to know more about the empirical landscape, take a gander at [[@Georgi19]](https://publishup.uni-potsdam.de/files/42654/of_trees_and_birds.pdf), which discusses the known data and its implications for TAG (kudos to Doreen for taking a close and very insightful look at TAG).

I'll add one more piece of data from German here, which is usually considered a different phenomenon.

(@) Wen glaubst du **wen** die Maria gesagt hat **wen** der Hans mag *t*?  
    Who.Acc think.2sg you who.Acc the.Nom Maria said has who.Acc the.Nom Hans likes  
    "Who do you think that Mary said that Hans likes?"

It is commonly believed that the second and third instance of *wen* are pronounced versions of the copies left behind by successive cyclic wh-movement of the DP *wen*.
I've never been a fan of this analysis because this only works with bare wh-words, not d-linked wh-phrases.

(@) \*Welchen Film glaubst du **welchen Film** die Maria gesagt hat **welchen Film** der Hans mag *t*?  
    which.Acc movie think.2sg you which.Acc movie the.Nom Maria said has which.Acc movie the.Nom Hans likes  
    "Which movie do you think that Mary said that Hans likes?"

So to me, this has always looked like a case of the lower complementizers agreeing with the wh-mover and thus coming out as *wen*.
If the wh-mover does not move up all the way, the complementizers that aren't crossed by the wh-movement come out as *was* instead.

(@) [~DP~ Wen] glaubst du **wen** die Maria gesagt hat **wen** der Hans mag *t*?  
(@) Was glaubst du [~DP~ wen] die Maria gesagt hat **wen** der Hans mag *t*?
(@) Was glaubst du was die Maria gesagt hat [~DP~ wen] der Hans mag *t*?

Alright, so that's the rough lay of the land.
It's an interesting cluster of phenomena, and it's something that Minimalism handles better that many of its competitors.
As @Georgi19 points out, TAG has a hard time capturing these facts nicely, and I'm not at all sure how they fit into CCG.
But the Minimalist account still treats these phenomena as something uniquely syntactic, something that hinges on assumptions like successive cyclicity.
With the subregular perspective, we can take the Minimalist analysis as a starting point and desyntactify it until these phenomena just look like tone plateauing.

## Tone plateauing and circumambience

[I've talked about tone plateauing before]({filename}/Tutorials/locality_sltsl.md), but a refresher never hurts.
When viewed as a phonotactic constraint, tone plateauing states no low tone L may occur between two high tones H, no matter how far apart the two H are.
As long as both high tones are part of the same word, no L can appear in the interval spanned by them.
So we get the following patterns:

(@) good: HLLL
(@) good: LLLH
(@bad) bad: HLLLH

The form in (@bad) should have been realized as HHHHH instead.

Adam Jardine calls such processes **circumambient** [@Jardine15] because it isn't enough to look at one H in isolation.
There is nothing wrong with an L appearing to the right or to the left of an H.
Only if L is surrounded by H do we get a problem.

Tone plateauing is not [TSL with the usual tier projection]({filename}/Tutorials/locality_sltsl.md#not-everything-is-tsl), i.e. a tier projection that does not consider any structural information beyond the segment itself.
As a reminder, here's why.
First, the tier needs to contain H and L since we want to regulate the distribution of L but cannot do so unless we are also aware of every H.
So the tier of something like HLLLH is, well, HLLLH.
The tier doesn't actually help in this case, so TSL reduces to SL.
And as you might remember, SL dependencies have to satisfy [suffix substitution closure]({filename}2019-05-21_graf_sl-poem.md).
Basically, if HL^n^ with *n* instances of L is well-formed, and so is L^n^H, then an SL grammar will incorrectly treat HL^n^H as well-formed.
So the pattern isn't SL, and since we looking at a (useless) tier, tone plateauing is not TSL.

However, tone plateauing is TSL with more powerful tier projections.
For instance, we can construct a tier that contains every H but only those L that are immediately preceded by an H.
This allows us to ignore some instances of L, and as a result tiers suddenly do some work for us:

| **String** | **Tier** |
| :--        | :--      |
| HLLL       | HL       |
| LLLH       | H        |
| HLLLH      | HLH      |

With tiers like that, tone plateauing is enforced by forbidding the trigram HLH from ever appearing on the tier.
This is an [ITSL grammar]({filename}/Tutorials/locality_iotsl.md#adding-context-information-input-tier-based-strictly-local-itsl) of tone plateauing.

Alternatively, we could use an [OTSL grammar]({filename}/Tutorials/locality_iotsl.md#adding-projection-interdependencies-output-tier-based-strictly-local-otsl).
In this case, the tier projection is sensitive to what is already on the tier.
Again we project all H, and we project L only if the tier built so far ends in H.

| **String** | **Tier** |
| :--        | :--      |
| HLLL       | HL       |
| LLLH       | H        |
| HLLLH      | HLH      |

Well, that's exactly the same tiers as before, so the same constraint will do: No HLH on the tier.

While I originally thought of tone plateauing as an ITSL process, I think OTSL is the better choice if one really wants to go with a TSL-style analysis.
The reason is that the OTSL grammar is more robust.
Suppose that your language also has mid tone M, which is transparent for tone plateauing.
In this language, HMLM and MLMH are well-formed, whereas HMLMH is illicit.
In that case, ITSL stumbles whereas OTSL marches on as if nothing had happened.

| **String** | **ITSL Tier** | **OTSL Tier** |
| :--        | :--           | :--           |
| HMLM       | H             | HL            |
| MLMH       | H             | H             |
| HMLH       | H             | HLH           |

Anyways, the bottom line is the tone plateauing has a relatively well-defined spot in the subregular hierarchy.
It's not TSL, but it is ITSL or OTSL.
Abstracting away from the phonological content, tone plateauing emerges as a concrete instance of a computational mechanism that limits the shape of elements when they happen to be sandwiched between some other elements.
And MCA happens to be just that: a restriction on the shape of complementizers that are sandwiched between a mover and its landing site.


## Movement paths as strings

For the sake of simplicity, let's recast the data from Irish, Kinande and German in terms of English.
Suppose that we have a language E that works just like English except that we have a default complementizer C and a complementizer C[agr]. 
When a mover crosses a complementizer, that complementizer must be C[agr] rather than C.
That's illustrated in the [MG dependency trees]({filename}/Tutorials/locality_merge_move.md#derivation-trees-and-dependency-trees) below.

1. The tree for *John said Mary punched somebody* has the default, non-agreeing complementizer since no movement takes place.
1. The second tree for *Who John said Mary punched* shows that in our fictitious language E, wh-movement triggers the switch from default C to C[agr] in all complementizers that are crossed by the mover.
1. The third tree for *Bill wonders who John said Mary punched* illustrates that complementizers that are not crossed by the mover keep their default form.
1. The fourth tree is an illicit version of three where none of the complementizers display agreement.

![ Tree 1: Without movement, each complementizer keeps its default form]({filename}/img/thomas/movement_toneplateauing/dep_default.svg)

![ Tree 2: Complementizers crossed by a mover surface with special agreement]({filename}/img/thomas/movement_toneplateauing/dep_agree.svg)

![ Tree 3: Complementizer agreement does not extend beyond the landing sight]({filename}/img/thomas/movement_toneplateauing/dep_partial.svg)

![ Tree 4: A tree with non-agreeing complementizers along a movement path is illicit]({filename}/img/thomas/movement_toneplateauing/dep_noagree.svg)

As you might remember, it is sometimes convenient to truncate the tree representation to a string.
We've done that before with [c-strings]({filename}/Tutorials/locality_constraints.md#the-role-of-command-strings).
That doesn't mean that syntax literally operates over strings, but rather that large parts of the tree representation do not matter for the phenomenon at hand and can be safely discarded to simplify the model.
In our case, the only thing that matters is whether a complementizer occurs along a movement path.
A movement path is just a special case of an **ancestor chain**.
The ancestor chain consists of a lexical item L and all nodes that dominate L in the dependency tree.
A movement path is the special case of an ancestor chain where L has some f^-^ feature.
Movement paths, by virtue of being ancestor chains, are strings.

As a concrete example, the table below lists the wh-movement path for each one of the three trees above.
Or rather, what those movement paths look like after we strip out all irrelevant features in a valiant effort to reduce clutter.

| **Tree** | **wh-path** |
| --:      | :--         |
| 1        | none        |
| 2        | who[wh^-^] punched T C[agr] said T C[agr,wh^+^] |
| 3        | who[wh^-^] punched T C[agr] said T C[agr,wh^+^] wonders T C |            
| 4        | who[wh^-^] punched T C said T C[wh^+^] wonders T C |            

Yep, those are strings, alright.
The first three are from well-formed trees.
The fourth string is from an ill-formed tree, and it is the reason the tree is ill-formed.
We can separate the three well-formed ones from the illicit one with a simple constraint: don't have C between matching f^-^ and f^+^.
Only C[agr] can occur there, C is out.
Just like we can't have L between H.
It's basically syntactic tone plateauing --- circumambience in syntax.

True, in tone plateauing we are comparing like objects (i.e. tones), whereas here there seems to be no natural connection between C and the elements that carry the movement features.
But that's a matter of substance, not computation.
In terms of what computational machinery is involved, there's no difference.

If you still don't believe me, here's the OTSL grammar over these movement paths:

1. Project every f^-^ and every f^+^ (just like we project every H in tone plateauing).
1. Project C if the previous symbol on the tier is f^-^ (just like we project L only if the tier ends in H).
1. Don't have f^-^ C f^+^ on the tier (just like we don't allow HLH on the tone tier).

There you have it, tone plateauing in syntax!
Convinced?

...

...

...

Alright, you got me, there's one thing we have to add.
Right now, we only say that C cannot occur along a movement path.
But that's not enough: we also have to say that C[agr] cannot occur anywhere except along a movement path.
We didn't have to worry about that in tone plateauing because there is no counterpart to C[agr].
That would be a tone that can only occur in an interval spanned by two high tones.
Limiting C[agr] to movement paths is a very different problem formally and would lead us down a very different rabbit hole.
So if it's okay with you, I'll put that part aside here.
If you're curious, we can hash it out in the comments section.


## A technical objection

Since we're on the topic of technical wrinkles, let's add another one.
Strictly speaking, the constraints on movement paths aren't really circumambient patterns because of how the MG feature calculus is set up.
If you see an f^-^ on a mover, you can immediately assume that there will be a matching f^+^ later on.
Otherwise, the structure would be ill-formed, and there's no point in checking well-formedness constraints for a structure that is already ill-formed.
The strict matching between f^-^ and f^+^ in MGs allows us to infer the presence of the latter from the former, like some kind of syntactic quantum entanglement or simply **feature entanglement**.

Things are different with tone plateauing.
Tone plateauing only applies within an "H ... H" interval.
A single H on its own does not accomplish anything, you need the other one to have a proper interval.
That's why HLLL and LLLH are perfectly fine, whereas HLLLH is ill-formed and should be HHHHH.
Crucially you cannot tell from the presence of one H that there will be another H later on.
Maybe it's there, maybe not.
Feature entanglement does not extend to high tones, and that's why tone plateauing is a harder problem than MCA.

That's a fair point, but I think it's mostly a technical detail that makes us miss the forest for the trees.
First, suppose we actually accept this technical divide.
Then I misspoke when I said that MCA is like tone plateauing.
Instead, it is like tone spreading.

Suppose you have progressive spreading of high tone with B as a blocker.
Then a single H is enough to immediately rule out any instance of HL in a string because H failed to spread to the right.
At the same time, HBL is fine thanks to the blocker B.
MCA works just like that.
We cannot have a wh^-^ with a non-agreeing complementizer to the right because that would mean having a non-agreeing complementizer along the wh-movement path.
But we can have a non-agreeing complementizer to the right of wh^+^.
So if MCA isn't like tone plateauing, at least it is like spreading, which is still a surprising parallel between phonology and syntax.

But the more fundamental issue is that feature entanglement strikes me as an accident of the MG formalism rather than a substantive property of syntax.
If an f^-^ without a matching f^+^ would simply be treated as a mover that does not get to move, rather than something that always, without exception, causes ungrammaticality, then feature entanglement disappears.
In addition, entanglement only helps you when your model of syntax only makes a categorical distinction between well-formed and ill-formed.
In that case, you can freely assume the presence of f^+^ because that is the only way to violate the constraint you're testing for, and if there is no such f^+^ then the sentence is ill-formed anyways and there's no point in testing the constraint.
But if you want to use a weighted formalism where well-formedness is gradient, that argument no longer holds.
Yes, if there is no f^+^ then the sentence might be pretty bad, but if you incorrectly pile on MCA violations because you assumed an f^+^ that doesn't exist, you may end up saying that the sentence is much worse than it actually is.

## Take-home message

In sum: it is technically true that tone plateauing is more complex than movement-driven complementizer agreement.
But that hinges on MG's feature entanglement, which I would say obscures the picture more than it illuminates it.
And at the end of the day, it doesn't matter so much whether the appropriate analogue for MCA is tone plateauing or tone spreading.
The mere fact that the subregular perspective allows us to hash out this analogy in rigorous terms is why I find it so fascinating.
And it allows us to reduce something that may look odd from a syntactic perspective and reduce it to the utterly mundane in phonology.

I only have one more, teeny-weeny, totally innocent little question: as discussed in @Jardine15, Copperbelt Bemba has a circumambient spreading process that only affects the four closest targets.
This means that HLLLLLH would become HHHHHLH, not HHHHHHH.
Do we find anything like that in syntax?
I doubt it, but 1) Copperbelt Bemba spreading looks pretty weird, and 2) syntax tends to be a lot weirder than I think.


## References
