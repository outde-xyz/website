---
title: >-
    Omnivorous number and Kaiowa inverse marking: Monotonicity trumps features?
authors:
    - Thomas Graf
date: 2019-05-31
tags:
    - features
    - monotonicity
    - morphosyntax
    - hierarchies
    - omnivorous number
    - inverse marking
    - Kaiowa
---

<!-- START_SUMMARY_BLOCK -->
I just came back from [a workshop in Tromsø on syntactic features](http://site.uit.no/castl/workshop-on-thirty-million-theories-of-syntactic-features/), organized by 
[Peter Svenonius](https://blogg.uit.no/psv000/)
and
[Craig Sailor](http://www.craigsailor.net/)
--- thanks for the invitation, folks!
Besides yours truly, the invited speakers were
[Susana Béjar](https://www.linguistics.utoronto.ca/people/directories/all-faculty/susana-b%C3%A9jar),
[Daniel Harbour](http://webspace.qmul.ac.uk/dharbour/),
[Michelle Sheehan](https://sites.google.com/site/michellesheehan54/home),
and
[Omer Preminger](https://omer.lingsite.org/).
I think it was a very interesting and productive meeting with plenty of fun.
We got along really well, like a Justice League of feature research (but who's Aquaman?).

In the next few weeks I'll post on various topics that came up during the workshop, in particular privative features.
But for now, I'd like to comment on one particular issue that regards the feature representation of number and how it matters for omnivorous number and Kaiowa inverse marking.
Peter has [an excellent write-up on his blog](https://blogg.uit.no/psv000/2019/05/31/on-the-privativity-of-number-and-the-possibility-of-negative-feature-specifications/), and I suggest that the main discussion about features should be kept there.
This post will present a very different point of view that basically says "suck it, features!" and instead uses hierarchies and monotonicity.
<!-- END_SUMMARY_BLOCK -->

## The empirical facts

For your convenience, I'll quickly summarize the relevant empirical facts as they're presented in Peter's blog post.
Omnivorous number is the phenomenon whereby a transitive verb displays plural agreement unless both the subject and the object are singular.
This gives us the agreement table below, where the columns represent the number of the subject and the rows the number of the object.

|        | **sg** | **pl** |
| :-:    | :-:    | :-:    |
| **sg** | sg     | pl     |
| **pl** | pl     | pl     |

Note that we never get the opposite, i.e. singular trumping plural: 

|        | **sg** | **pl** |
| :-:    | :-:    | :-:    |
| **sg** | sg     | sg     |
| **pl** | sg     | pl     |

Omer Preminger has used this to argue for a specific representation of number in terms of privative features, i.e. a system where features have no +/- values.

In Kaiowa inverse marking, we get inverse marking if the number feature on a Num-head disagrees with the "inherent number" of the noun.[^number]
The Num-head can be either singular, dual, or plural.
According to Daniel Harbour, these are specified via binary feature matrices as follows:

[^number]: This characterization is slightly misleading. Check Peter's blog for a full discussion of Daniel Harbour's analysis and where the "inherent number" part comes from.

1. [+sg, -pl] for singular
1. [-sg, +pl] for plural
1. [-sg, -pl] for dual

The missing [+sg, +pl] is not instantiated.
The inherent number specification is similar, but allows for different feature matrices:

1. [+sg]
1. [-pl]
1. [-sg, -pl]
1. [-sg]

Two feature matrices are compatible iff they can be unified.
Whenever the inherent number is feature-incompatible with the number on the Num-head, one gets inverse marking.
Otherwise, the number of the Num-head is realized.
It's again nice to put that in a table for easy reference. 

|            | [+sg] | [-pl] | [-sg, -pl] | [-sg] | 
| --:        | :-:   | :-:   | :-:        | :-:   | 
| [+sg, -pl] | sg    | sg    | inv        | inv   | 
| [-sg, +pl] | inv   | inv   | inv        | pl    | 
| [-sg, -pl] | inv   | dual  | dual       | dual  | 

As you can imagine, this is a bit trickier to account for with a privative feature system.
How, then, can one reconcile these two representations for number?
That's the issue on Peter's blog, but I'd like to pursue a completely different route: forget about features, and find the generalization at a more abstract level.

## Enter monotonicity

As some of you might know, I've been working on an algebraic approach to morphosyntax for quite a while now.
If that's the first time you hear about this, you should check out [this 50-page paper](https://thomasgraf.net/output/graf18jlm.html), I'm sure you have plenty of time to read it all.
What, you don't?
Alright, here's the gist: Phenomena in morphosyntax can be analyzed in algebraic terms by combining a specific base hierachy (e.g. for person, case, or number) with a mapping to the set of surface realizations.
The surface realizations can be inflected forms, morphological stems, grammaticality judgments, whatever.
The important thing is the shape of the base hierarchy, and that the mapping from the hierarchy to the surface realizations must be monotonic.

Monotonicity

: Let $\langle A, \leq_A \rangle$ and $\langle B, \leq_B \rangle$ be two partially ordered sets.
  Then a function $f$ from $A$ to $B$ is monotonic iff $x \leq_A y$ implies $f(x) \leq_B f(y)$.[^monotonic]

[^monotonic]: Yes, I know, that's the definition of isotonicity. But it doesn't matter for this approach whether functions are isotonic or antitonic, so I just subsume it all under monotonicity.

Monotonicity requires that ordering statements be preserved.
In entails that whenever we have $x < y < z$ in some hierarchy, $x$ and $z$ cannot be mapped to the same value while $y$ is mapped to something else.
So we get a contiguity requirement over hierarchies.

This readily explains Bobaljik's *ABA generalization.
No natural language has paradigms like *good*-*better*-*goodest*.
If we start out with a semantically natural hierarchy of positive < comparative < superlative, this follows from monotonicity.
As both the positive and the superlative are mapped to a stem *good*, monotonicity requires the comparative to be mapped to the very same stem.
Quite generally, monotonicity predicts that the following patterns are possible over this linear order with 3 cells:

1. ABC (all distinct stems)
1. ABB (comparative and superlative the same)
1. AAB (positive and comparative the same)
1. AAA (all the same)

Except for AAB, all these patterns are attested, and Bobaljik argues that AAB is illicit for independent reasons.
If we look a pronoun paradigms instead, we do find all combinations at least in the singular.
This is expected if we assume an underlying hierarchy of 1 < 2 < 3.

Monotonicity makes good typological predictions for various other morphosyntactic phenomena, including case syncretism, noun stem allomorphy, and the Person Case Constraint.
Many linguistic constraints can also be reanalyzed as instances of monotonicity, e.g. the Williams-cycle or the Ban Against Improper Movement.

Alright, so now let's see how monotonicity cracks the empirical nut of fitting omnivorous number and Kaiowa agreement under the same umbrella.

## Monotonicity with omnivorous number

Number is an area I haven't look at through the monotonicity lens before, so the following will necessarily be a bit handwavy.
But a reasonable assumption is to start out with a hierarchy $\text{sg} \leq \text{pl}$.
Yes, Uli Sauerland has argued at length that plural is more basic than singular, but that's about semantic number which doesn't line up perfectly with morphosyntactic number (*the group* is singular even though it denotes a plurality).
Still, if you're unhappy, feel free to switch the order, just make sure to also switch every other hierarchy in this post. 
For everybody else, $\text{sg} \leq \text{pl}$ it is.

Now consider omnivorous number.
We can model this as a sequence of value determinations.
So the verb gets two arguments and then the end result is determined.

| **Argument 1** | **Argument 2** | **Final marking** |
| :-:            | :-:            | :-:               |
| sg             | sg             | sg                |
| sg             | pl             | pl                |
| pl             | sg             | pl                |
| pl             | pl             | pl                |

The evaluation order of the arguments does not matter, so instead of a table one may use the hierarchy below.

![This hierarchy captures that the final value is determined from the two arguments]({static}/img/thomas/monotonicity/omnivorous_base.svg){ width=35% }

Notice something?
Imagine that we want to map values from this hierarchy to $\text{sg} \leq \text{pl}$.
Then, by monotonicity, the result must be plural as soon as at least one of the arguments is plural.
There simply is no way around this.

Alright, this might have been a bit too fast, so let's do it step by step.
Remember, monotonicity requires that the order of output values must not contradict the order of input values.
In linguistic terms, we may have no crossing branches between elements that are ordered with respect to each other.
One option is to simply map everything to singular.

![All singular agreement]({static}/img/thomas/monotonicity/omnivorous_allsg.svg){ width=55% }

This is the default case without any omnivorous shenanigans.
In principle, we could also have both arguments being singular and the final marking being plural.
This is a kind of resolved agreement.
I'm not sure if this happens with subject and object, but it certainly happens in cases of coordinated singular subjects.

!["Resolved" agreement]({static}/img/thomas/monotonicity/omnivorous_resolved.svg){ width=55% }

And of course everything can go to plural.

![Uniform plural agreement]({static}/img/thomas/monotonicity/omnivorous_allpl.svg){ width=55% }

These are the basic cases.
Notice how none of the branches ever cross.
This is also the case for omnivorous agreement.

![Omnivorous plural agreement via the second argument]({static}/img/thomas/monotonicity/omnivorous_good.svg){ width=55% }

But now suppose that omnivorous agreement could produce singular if just one argument is singular.

![Illicit singular agreement via the first argument]({static}/img/thomas/monotonicity/omnivorous_bad.svg){ width=55% }

The arcs of the second argument and the final marking cross, violating monotonicity.
So we cannot get omnivorous singular agreement this way.
But this exhausts the set of possible configurations.
We've tried everything, and omnivorous singular agreement simply cannot arise under monotonicity.

So there you have it, omnivorous number is just an instance of monotonicity.
Or rather, omnivorous plural agreement is compatible with monotonicity, and the counterpart where one singular is sufficient to trigger singular is not.
Intuitively, the derivational sequence of operations is tied into the number hierarchy, and together with monotonicity this gives us effects like omnivorous number.
The Williams Cycle and the Ban Against Improper Movement work exactly the same, by the way, so this is nothing *ad hoc* that I designed just for this small problem set.
No, omnivorous number is a bog-standard instance of the general monotonicity requirements that seem to be active in syntax.


## Kaiowa number

Alright, one down, leaving only Kaiowa number.
This one looks quite a bit different, but is still monotonic.
First, we extend the number hierarchy to $\text{sg} \leq \text{pl} \leq \text{dual}$.
I believe this is fairly natural.
Yes, it does not jive with semantics, but this hasn't stopped me before, now has it?
And the hierarchy is in line with the generalization that dual is more marked than plural and that no language has a dual without also having a plural.

Next, I will also define a hierarchy of Kaiowa noun classes:

$$\lbrack-\text{sg}\rbrack \leq \lbrack-\text{sg},-\text{pl}\rbrack \leq \lbrack-\text{pl}\rbrack \leq \lbrack+\text{sg}\rbrack$$

I use the feature terminology from Peter's blog post here, but I could just as well have called them 1, 2, 3, 4.
The names of nodes are meaningless, what matters is their place in the hierarchy.
That said, this is still a fairly natural hierarchy as it moves from $[-\text{sg}]$ to its polar opposite $[+\text{sg}]$.
Intutively, it is a hierarchy of the form *plural* - *dual* - *not plural* - *singular*.

As the last piece of the puzzle, assume that we have a hierarchy $\text{no inverse} \leq \text{inverse}$.
This is just a mathematical device to allow us to talk about the monotonicity of inverse marking.
As usual, it doesn't matter which order you put the two elements in.

With all these pieces, we can finally show a very peculiar kind of monotonicity.
First, we can look at all the conceivable monotonic maps from the noun classes to the inverse hierarchy.
There's a lot of those.
Basically, any way to draw a circle around a continuous region of the noun class hierarchy is fine as long as it includes the start or the end of the hierarchy:

1. none
1. $[-\text{sg}]$
1. $[-\text{sg}], [-\text{sg},-\text{pl}]$
1. $[-\text{sg}], [-\text{sg},-\text{pl}], [-\text{pl}]$
1. $[-\text{sg}], [-\text{sg},-\text{pl}], [-\text{pl}], [+\text{sg}]$
1. $[-\text{sg},-\text{pl}], [-\text{pl}], [+\text{sg}]$
1. $[-\text{pl}], [+\text{sg}]$
1. $[+\text{sg}]$

That's 8 patterns.
Now we can ask ourselves if some of those correspond to the behavior we find for singular, dual, and plural in Kaiowa.
That is to say, can we identify monotonic maps that correspond with patterns we get with number features on the Num-head?
So singular, dual, and plural on the Num-head are not features or part of any hierarchy here, instead they are analyzed as mappings from the noun class hierarchy to the inverse hierarchy.
This might seem like a conceptual leap, but once we take it we can find patterns for all three numbers.
These are drawn below, with boxes to indicate that a node is mapped to "inverse".

![Kaiowa singular on Num triggers inverse with the first two noun classes]({static}/img/thomas/monotonicity/kaiowa_sg.svg){ width=55% }

![Kaiowa plural on Num triggers inverse almost everywhere]({static}/img/thomas/monotonicity/kaiowa_pl.svg){ width=55% }

![Kaiowa dual on Num triggers inverse only with the last noun class]({static}/img/thomas/monotonicity/kaiowa_dual.svg){ width=55% }

We already know that these mappings are all monotonic.
So for any given number and noun class combination in Kaiowa, the mapping to an inverse or non-inverse form is monotonic.
That's our first insight, but things get a lot more interesting from here.

The three mappings above aren't just a random sample from the 8 available monotonic maps.
No, they instantiate a monotonic system of their own!
If we rank these mappings according to where they start mapping noun classes to the inverse marker, we get $\text{sg} \leq \text{pl} \leq \text{dual}$, which reflects our original number hierarchy.
If you ask me, this is damn nifty.

So what does this mean?
It means that Kaiowa obeys a kind of double monotonicity: picking a specific part of the hierarchy for inverse marking must obey monotonicity, and the mapping from inverse marking functions to the number system must also be monotonic.
I don't know about you, but my mind is blown.

## Implications for features

One point I want to emphasize is that this account is completely feature-free.
Terms like singular and plural don't refer to features, they're but a shorthand for collections of objects that go into a specific place in a hierarchy.
All the work is done by establishing high-level relations between such classes of objects that restrict how grammar is allowed to operate on them.
This is a very high-level perspective.
It tells us precious little about how these things are implemented in syntax.
But that's a boon.
As you can see in Peter's post, getting features to work well across domains is tricky.
Instead of worrying about the nitty-gritty, we can just focus on the high-level behavior and identify abstract properties that tie these domains together.
