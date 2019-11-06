---
title: >-
    Shellshock
authors:
    - Thomas Graf
date: 2019-11-06
bibliography: references.bib
tags:
    - syntax
    - Larsonian shells
    - constituency
    - CCG
    - Minimalist grammars
---

<!-- START_SUMMARY_BLOCK -->
This semester I am teaching a seminar on computational syntax.
It's mostly on subregular syntax, but I started out with a discussion of CCG.
CCG is noteworthy because it is a theory-rich approach that has managed to make major inroads into NLP.
It would be cool if we could replicate this with MGs, but in order to do that you need a killer app.
Subregular complexity might just be that because CCG doesn't have a regular backbone, so it can't have a subregular one either (more on that in a future post).
CCG's killer app was flexible constituency and a one-to-one mapping from syntax to semantics.
You combine that with a corpus ([CCGbank](http://groups.inf.ed.ac.uk/ccg/ccgbank.html)) and an efficient parsing algorithm (e.g. [supertagging with A* parsing](https://www.aclweb.org/anthology/D14-1107/)), and you have something that is both linguistically sophisticated and sufficiently fast and robust for practical applications.
Anyways, this post collects some of my thoughts on flexible constituency and how it could be emulated in MGs.
Spoiler: shells, lots and lots of shells.
<!-- END_SUMMARY_BLOCK -->


## Adjuncts in CCG

Here's a bunch of fairly unremarkable sentences.

(@) John definitely showed Bill a gift and allegedly gave Peter a briefcase.
(@) John definitely showed Paul and allegedly gave Peter a briefcase.
(@) John definitely showed and allegedly gave Peter a briefcase.

The standard MG analysis for this follows the Minimalist literature closely.
In all three sentences, \emph{definitely} and \emph{allegedly} are adjuncts that adjoin to a VP.
Whenever it looks like the adjuncts modify something smaller than a full VP, this is a result of across-the-board movement to the right.

(@) John [~VP~ definitely [~VP~ showed Bill a gift]] and [~VP~ allegedly [~VP~ gave Peter a briefcase]].
(@) John [~VP~ definitely [~VP~ showed Bill ~~a briefcase~~]] and [~VP~ allegedly [~VP~ gave Peter ~~a briefcase~~]] a briefcase.
(@) John [~VP~ definitely [~VP~ showed ~~Peter~~ ~~a briefcase~~]] and [~VP~ allegedly [~VP~ gave ~~Peter~~ ~~a briefcase~~]] Peter a briefcase.

In CCG, on the other hand, there is no movement or other kinds of displacement.
The adjuncts can directly combine with a verb or a V'.
Similarly, coordination is not limited to XPs and can combine heads or X'.
You just combine adjacent constituents according to their syntactic types.

(@) John [~VP~ [~VP~ definitely [~VP~ showed Bill a gift]] and [~VP~ allegedly [~VP~ gave Peter  a briefcase]]]].
(@) John [~VP~ [~V'~ [~V'~ definitely [~V'~ showed Paul]] and [~V'~ allegedly [~V'~ gave Peter]]] a briefcase].
(@Vcoord) John [~VP~ [~V'~ [~V~ [~V~ definitely [~V~showed]] and [~V~ allegedly [~V~ gave]]] Peter] a briefcase].

Intuitively, CCG can do things like construct a complex ditransitive verb *definitely showed and allegedly gave*.
This is particularly clear once we look at the CCG derivations and the types of constituents.
In CCG, verbs can have the following types.

| **Verb**     | **Syntactic type** |
| :--          | :--                |
| intransitive | S\NP               |
| transitive   | (S\NP)/NP          |
| ditransitive | ((S\NP)/NP)/NP     |

And in the derivations below, those types appear on heads as well as constituents.
That's flexible constituency at work.

![VP adjunction in CCG]{%filename%/img/thomas/shells/ccg_vpadjunction.svg}
![V' adjunction in CCG]{%filename%/img/thomas/shells/ccg_vbaradjunction.svg}
![V adjunction in CCG]{%filename%/img/thomas/shells/ccg_vadjunction.svg}


## Emulating sub-XP adjunction

The flexible constituency analysis can be added to MGs by allowing adjunction to and coordination of lower levels than just XP.
But it would actually be quite ugly, in particular the coordination part. 
In MGs, each ditransitive verb selects for two object DPs, so if we have two ditransitive verbs we need four DPs to meet the selection requirements.
But (@Vcoord) only contains one direct object and one indirect object, which is definitely less than four.
That's not a problem in CCG because coordination can combine two ditransitives that need four DPs into a single ditransitive that only needs two.
MG coordination has no obvious way of doing that, and it would have to be hacked in.
It's doable, and to some extent that's what across-the-board movement does, but it's not exactly nice.

There is an alternative, though.
Rather than making every level below X' accessible for adjunction and coordination, we can make every level below XP an XP (or rather, an X'P).
Every argument is introduced in its own shell, and the lowest shell consists just of the head itself.
Crazy, perhaps, but it's just the natural evolution of Larsonian shells [@Larson88].
Rather than having an object level and a subject level for verbs, we would then have a verb level, an indirect object level, a direct object level, and a subject level.
The figure below shows the intuition for an arbitrary XP.

![Splitting an XP with n arguments into n+1 shells]{%filename%/img/thomas/shells/shells.svg}

To some extent we're already there for verbs thanks to an ever more fine-grained hierarchy of verb-related heads, e.g. applicative.
But for some reason nobody has co-opted this approach to generalize coordination and get rid of across-the-board movement --- at least I'm not aware of any work along those lines.


## Idle exploration of some predictions

One prediction of the *maximum shelling* approach is that each verb layer can move independently.
We see that in German, where we can topicalize VPs of varying size.
Let's look at the default word order first.

(@) [~Subj~ Der Peter] hat [~IO~ dem Hans] [~DO~ ein Geschenk] gegeben.  
    the.Nom Peter has the.Dat Hans a.Acc present given

And here's a sample of the many possible topicalization variants.

(@) Dem Hans ein Geschenk gegeben hat der Peter.
(@) Ein Geschenk gegeben hat der Peter dem Hans.
(@) Gegeben hat der Peter dem Hans ein Geschenk.

Or if you prefer a more abstract representation:

(@) IO DO V has Subj
(@) DO V has Subj IO
(@) V has Subj IO DO

Usually this would be handled in terms of scrambling or remnant movement, but that's no longer needed for the patterns above.
In each case, we just move a different VP-layer.

(@) [~V2~ IO DO V] has Subj
(@) [~V1~ DO V] has Subj IO
(@) [~V0~ V] has Subj IO DO

That's not all possible options, though.
We could also have the following, among others.

(@) Dem Hans gegeben hat der Peter ein Geschenk.
(@) DO V has Subj IO
(@) Ein Geschenk dem Hans gegeben hat der Peter.
(@) DO IO V has Subj

And you can have all kinds of orders after *hat*.
It seems, then, that the *shells all the way down* analysis in its current form does not fully do away with scrambling or remnant movement.
However, what if the order of shells could be permuted?


## Shell permutation: even more flexible constituency.

For the sake of simplicity, let's consider a transitive verb.
Under the *so many shells, I can't even* analysis, this would look as follows:

![Transitive verb with a separate shell for each argument]{%filename%/img/thomas/shells/transv.svg}

Now suppose that the order of the higher shells could be switched, yielding the tree below.

![The same shell structure, but with permuted argument positions]{%filename%/img/thomas/shells/transv_permuted.svg}

This actually allows us to emulate yet another instance of flexible constituency in CCG.

(@) Harvey loves and Rose despises mud wrestling.

The Minimalist analysis once again involves XP-level coordination and across-the-board movement to the right.

(@) [[Harvey loves ~~mud wrestling~~] and [Rose despises ~~mud wrestling~~]] mud wrestling.

The CCG analysis, on the other hand, uses type raising and functional composition to directly combine each verb with its subject, yielding a complex verb *Harvey loves and Rose despises* that is still looking for an object.

(@) [[Harvey loves] and [Rose despises]] mud wrestling.

![CCG analysis of VP-coordination to the exclusion of the object]%filename%/img/thomas/shells/ccg_subjcoordination.svg}

We can do the very same thing with the *shelling out shells* analysis if we assume that shell order may be altered in some cases.
In contrast to the CCG approach, this solution does not require the subject to select the verb.
However, it does require that the subject does not move to Spec,TP (which doesn't serve much purpose anyways once you can adjoin below VP and can permute shell order).

![Shell explosion counterpart to CCG analysis]{%filename%/img/thomas/shells/subjVP_coordination.svg}

And the same approach can also be used to topicalize [IO V] to the exclusion of DO in German.
Topicalization of [Subject V] to the exclusion of DO and IO would still be impossible because the subject has to move to Spec,TP.

Shellification + shell-permutation certainly can do a lot.
It is not enough to emulate all cases of flexible constituency in CCG --- unbounded cross-serial dependencies still need to be handled differently, and I think the MG solution is much better in this case.
CCG can also form complex modifiers via type composition.

(@) The [old ugly] man died.
(@) Peter is [without a doubt heavily] indebted.

I have no idea how to make that work in MGs, but it's also much less clear that those cases of constituency are all that useful.
Shell explosion and shell permutation still don't allow for the full flexibility of CCG constituency, but they grant plenty.


## One more possible application

One more thing before I wrap up.
I also wonder if the *what the shell* analysis could be used for some other constructions that are usually taken to involve ellipsis.

(@nicht) Gegeben hat der Peter dem Hans ein Geschenk, nicht weggenommen.  
    given   has the.Nom the.Dat Hans a.Acc present, not taken-away  
    'Peter gave Hans a present, he didn't take it away.'

Suppose we analyze *nicht* as a coordination head whose semantics is $\lambda f \lambda g. f \wedge \neg g$ instead of $\lambda f \lambda g. f \wedge g$ for *and*.
Then the structure above could be derived as follows.

(@) Gegeben hat der Peter dem Hans ein Geschenk [V0P [V0P ~~gegeben~~] [V0' nicht [V0P weggenommen]]].

Since we now allow for adjunction, (@nicht) can actually be quite a bit more complex.

(@nicht2) Gegeben hat der Peter dem Hans ein Geschenk, und später wieder weggenommen.  
          given has the.Nom Peter the.Dat Hans a.Acc present, and later again taken-away  
          'Peter gave Hans a prsent, and later on he took it from him.'

And we can have a very complex topicalized VP here.

(@nicht3) Gegeben und später wieder weggenommen hat der Peter dem Hans ein Geschenk.
(@nicht4) Gegeben, nicht weggenommen, hat der Peter dem Hans ein Geschenk.

I have no idea how CCG would handle those cases.


## Cause for shellebration?

This post was mostly about whether we can emulate flexible constituency in MGs, not whether that is a smart thing to do.
I think it opened up some new perspectives on well-known phenomena, but it clearly would require throwing out fundamental assumptions of Minimalist syntax.
I'm sure there's also tons of empirical problems that I missed.
The specter of overgeneration looms large with flexible constituency.
Add shell permutation on top of that, and you have a lot of undesirable constructions to stipulate away.

Nonetheless, I hope this was an insightful thought experiment for you.
For me, there are several take-home messages:

1. MGs and CCGs are very different views of syntax.
   One cannot easily port a CCG analysis to MGs without revamping fundamental assumptions about phrase structure.

1. Coordination is a sore spot in MGs, and it's where CCG truly shines.
   Across-the-board movement, deletion, those are all fixes to deal with the fact that coordination is much more flexible than Minimalism can easily accommodate.

1. Quite generally, a lot of movement steps exist largely to work around the rigidity of the fixed constituency assumption in Minimalist syntax.
   It would be insightful to try a more constituency focused route.
   For instance, deriving Universal 20 from variable headedness rather than the LCA proved very insightful imho [@AbelsNeeleman06].
   Doing so might also help us identify cases where CCGs struggle.

I'll have another post in the near future about fundamental computational differences between MGs and CCG.
For some reason, there is this widely held belief that the two are very similar.
I hope you're much more skeptical about that now ---- you've seen how hard it is to get flexible constituency.


## References
