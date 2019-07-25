---
title: >-
    KISSing semantics: Subregular complexity of quantifiers
authors:
    - Thomas Graf
date: 2019-07-26
series: KISS theories
bibliography: references.bib
tags:
    - subregular
    - strictly local
    - tier-based strictly local
    - monotonicity
    - quantifiers
    - semantics
    - typology
---

<!-- START_SUMMARY_BLOCK -->
I [promised]({filename}2019-07-25_graf_kiss_followup.md), noone asked, but you shall receive: a KISS account of a particular aspect of semantics.
Remember, KISS means that the account covers a very narrowly circumscribed phenomenon, makes no attempt to integrate with other theories, and instead aims for being maximal simple and self-contained.
And now for the actual problem:

It has been noted before that not every logically conceivable quantifier can be realized by a single "word".
Those are very deliberate scare quotes around *word* as the real issue is much more intricate, but ignore that for now and just focus on the basic facts.
We have *every* for the universal quantifier $\forall$, *some* for the existential quantifier $\exists$, and *no*, which corresponds to $\neg \exists$.
English is not an outlier, these three quantifiers are very common across languages.
But there seems to be no language with a single word for *not all*, i.e. $\neg \forall$.
Now why the heck is that?
If language is fine with stuffing $\neg \exists$ into a single word, why not $\neg \forall$?
Would you be shocked if I told you the answer is [monotonicity]({filename}2019-05-31_graf_number-monotonicity.md)?
Actually, the full answer is monotonicity + subregularity, but one thing at a time.
<!-- END_SUMMARY_BLOCK -->


## Quantifiers as stringsets

As you probably know, *every*, *some*, and *no* are type $\langle 1,1 \rangle$ quantifiers.
This means that they establish a relation between two sets $A$ and $B$.
In *every bird flies*, the quantifier *every* establishes a relation between the set $A$ of birds and the set $B$ of things that fly.
With *every*, the established relation is one of **subset**.
Hence *every bird flies* is true iff $A \subseteq B$.
Since penguins are birds (members of $A$) but do not fly (not members of $B$), the sentence is false in our world.
So far so familiar.

The evaluation of a quantifier relative to some model, e.g. our world, can be represented as a binary string.
First, we put all elements of $A$ in some arbitrary order.
It really doesn't matter how we do that, we just need to establish some order to get a string.
If our set $A$ of birds consists of Tweetie (T), Daffy Duck (D), and the Roadrunner (R), we could for instance put them in alphabetical order to get the string DRT (how semantically appropriate).
Next we replace each individual by **1** if it is a member of our set $B$, and **0** otherwise.
So our example string DRT would become **001** because among those three cartoon birds, Tweetie is the only bird that actually flies once in a while.
Now we can ask ourselves whether this string is well-formed with respect to the quantifier *every*.
The answer is No, because the string contains some instances of **0**, i.e. things in $A$s that are not in $B$, and thus $A \subseteq B$ does not hold.
A string can be well-formed with respect to *every* iff it contains nothing but **1**s.
Did you notice what we just did there?
We turned the quantifier *every* into a set of strings over the alphabet of **1**s and **0**s.
We can do the very same thing with the other quantifiers:

| **Quantifier** | **Binary stringset** |
| --:            | :--                        |
| every          | $\{ s \in \{\mathbf{0, 1}\} \mid s \text{ contains only } \mathbf{1} \}$ |
| no             | $\{ s \in \{\mathbf{0, 1}\} \mid s \text{ contains only } \mathbf{0} \}$ |
| some           | $\{ s \in \{\mathbf{0, 1}\} \mid s \text{ contains at least one } \mathbf{1} \}$ |
| not all        | $\{ s \in \{\mathbf{0, 1}\} \mid s \text{ contains at least one } \mathbf{0} \}$ |

This idea of viewing quantifiers as strings is the foundation of semantic automata theory, which has been around for decades [@Benthem87].
But semantic automata theory relies on the coarse distinctions of the Chomsky hierarchy.
As we now know, subregular complexity is a better yardstick when it comes to language.
So let's look at those four quantifier languages from a subregular perspective.


## Strictly locality of *every* and *no*

One of the simplest subregular classes is the class of **strictly local** (SL) stringsets.
Intuitively, stricty locality means that one can decide the well-formedness of a string by inspecting all its substrings up to some fixed length $k$ and accepting the string unless one of those substrings is on a list of forbidden substrings.
The stringset for *every* is strictly 1-local (SL-1) because it suffices to look at all substrings of length 1 and check that none of them are **0**.
That way, we can rule out all strings that contain symbols besides **1**.
For the very same reason, the stringset for *no* is also SL-1, except that now we have to forbid **1** instead of **0**.

This leaves us with *some* and *not all*.
These quantifiers do not have SL stringsets.
We can prove this by picking an arbitrary bound $k$ and showing that the stringsets are not SL-$k$.
Suppose $k$ is 3, and consider the string **0001000**.
This string belongs to the stringset for *some* as it contains at least one **1**.
Since the whole string is well-formed, so must be each one of its substrings of length 3:

- **000**
- **001**
- **010**
- **100**

Out of these four substrings, **000** is the only one that matters for the next step.
Suppose we remove **1** from **0001000**, leaving us with **0000000**.
This string contains no instance of **1**, so it is not a member of the *some* stringset.
But now look at its list of length 3 substrings:

- **000**

This is not a forbidden substring!
It cannot be, because it shows up in well-formed strings like **0001000**.
So there is no length 3 substring that we can use to forbid the illicit **0000000** without also forbidding the licit **0001000**.
If the stringset for *some* were SL-3, then either both strings would be licit or both strings would be illicit.
As that is not the case, the stringset is not SL-3.
But of course we can use this argument for any $k$ by adding more **0**s to these two example strings.
Therefore the *some* string set isn't SL-$k$ for any $k \geq 0$, which means that it isn't strictly local at all (this is an instance of [suffix substitution closure]({filename}2019-05-21_graf_sl-poem.md)).

Just as with *no*, we can switch **0** and **1** in the argument above to show that *not all* isn't strictly local, either.
At this point, then, subregular complexity has given us a bifurcation between the SL quantifiers *every* and *no* on the one hand, and *some* and *not all* on the other.
But that's not the split we're looking for. 
We want a 3/4 split with *every*, *no*, and *some* on the one hand, and *not all* on the other.
For this, we have to take a step up in the subregular hierarchy, from strictly local to **tier-based strictly local** (TSL).


## Monotonic tier projection saves the day

TSL expands SL with a tier projection mechanism that allows us to ignore irrelevant material.
In the case of *some*, we first stipulate a tier alphabet that contains only **1**.
This basically amounts to saying that in order to check the well-formedness of a string with respect to *some*, we only need to pay attention to **1** and can ignore **0**.
Hence a string like **0001000** reduces to just **1**, whereas **00000000** reduces to the empty string.
This means that well-formedness for *some* reduces to a simple two-step check:

1. Once we remove all instances of **0**, is the result empty?
2. If so, reject the string.
   Otherwise accept it.

In order to check whether a string is empty, one needs an SL-2 grammar (this is largely a technical artifact, don't pay too much attention to the 2 here).
So the *some* stringset can be generated by an SL-2 grammar with tier alphabet **1**, making it a TSL-2 stringset.

As before, the very same strategy works for *not all*, except that the tier alphabet is $\{ \mathbf{0} \}$ instead of $\{ \mathbf{1} \}$.
Hmm, that still doesn't get us the desired 3/4 split.
Except it actually does once we look a little closer.
First, we can put *every* and *no* in the same group as *some* and *not all*.
That's because every SL string set is a TSL string set where the tier alphabet is identical to the full alphabet.

In other words, *every* and *no* are TSL-1 with tier alphabet $\{ \mathbf{0}, \mathbf{1} \}$.
Next, remember that every set is equivalent to its characteristic function, which maps members of the set to **1** and non-members to **0**.
This gives us four possible tier projections.

![Option 1: Nothing projects]({static}/img/thomas/kiss_theories/tierprojection_none.svg)

![Option 2: Everything projects (*every* and *no*)]({static}/img/thomas/kiss_theories/tierprojection_01.svg)

![Option 3: **1** projects (*some*)]({static}/img/thomas/kiss_theories/tierprojection_1.svg)

![Option 4: **0** projects (*not all*)]({static}/img/thomas/kiss_theories/tierprojection_0.svg)

Projecting nothing results in a pathological TSL grammar that cannot distinguish any strings, so we can ignore this case.
This leaves us with options 2--4, and those are not all the same.
The projections used by *every*, *no*, and *some* are **monotonic** (or to be more specific, isotonic): $x \leq y$ implies $f(x) \leq f(y)$.
The projection for *not all* is not monotonic in this sense as we have $\mathbf{0} < \mathbf{1}$ yet $f(\mathbf{0}) = 1 \not\leq 0 = f(\mathbf{1})$.
And [as I have pointed out before]({filename}/Discussions/2019-05-31_graf_number-monotonicity.md), monotonicity seems to be play a big role in morphology and its interface with syntax.
Well, here we are dealing with a problem at the interface of morphology and semantics: how complex a meaning can you stuff into a morphological atom?
It makes sense that monotonicity should once again be active here, giving us the observed 3/4 split.

This story generalizes beyond the four quantifiers discussed here.
For instance, *at least $n$* and *exactly $n$* are both TSL with monotonic tier projection, whereas *all but $n$* is not.
It's not surprising, then, that the former two can both be expressed just by a single numeral, whereas the latter always requires a multi-word construction in every language.
It would be interesting to see how far this approach can go, e.g. for adverbial quantifiers. 
Tim Fernando also has some work on string representations for temporal semantics, but I've never been able to figure out how this system is supposed to be applied to concrete data.
If one of you wants to join me in that enterprise, I'd appreciate a fellow traveler.


## Back to KISS

Let's not forget that this all started out as another example of a KISS theory.
My story clearly fits the main criteria:
It picks out a very small and limited empirical phenomenon, and gives a very simple story for it.
It has the added bonus, though, that it dovetails nicely with some other work.
Monotonicity might be *ad hoc* if it were limited to this phenomenon, but it crops up in so many places that this is just yet another instance of a more general principle.
SL and TSL are known to play a major role in phonology and morphology, and probably syntax, too --- finding these classes in the domain of quantifiers is a nice case of cognitive parallelism.

Finally, the one apparent counterexample to the generalization above would be *most*, which isn't TSL but looks like it is morphologically atomic.
Except that Martin Hackl has argued at length that *most* is the result of multiple interacting heads [@Hackl09].
From a semantic perspective, it is more like *not all* than *every* or *some*.

That's a nice demonstration that a KISS theory doesn't need to end up isolated from the rest of the field, it just starts out that way.
You do your own little thing, and when you're done you try to fit your findings into a bigger picture.
That's how KISS allows global understanding to evolve from local understanding, whereas monolithic approaches proceed in the other direction: we've fixed a framework of understanding, and now we have to squeeze everything in there.

## References
