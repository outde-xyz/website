---
title: >-
    Syntax as phonology: Syntactic constraints as string constraints
authors:
    - Thomas Graf
date: 2019-09-29
bibliography: references.bib
series: >-
    The subregular locality zoo
tags:
    - subregular
    - syntax
    - locality
    - c-command
    - constraints
    - islands
---

<!-- START_SUMMARY_BLOCK -->
The [previous post in this series]({filename}locality_islands.md) discussed the lay of the (is)land from the perspective of TSL (I'm so disappointed in myself for not making this pun last time; better late than never).
I mentioned that the TSL view cannot handle all island constraints.
Sometimes, we need an alternative approach.
But this alternative approach doesn't come out of nowhere.
It is also what we need for all kinds of licensing constraints, and it also handles restrictions on movement that are not island constraints.
<!-- END_SUMMARY_BLOCK -->

## The *that*-trace effect

No syntax introduction is complete without discussion of the *that*-trace effect.
While unpronounced complementizers do not block movement, a pronounced *that* does, but only for subjects, not for objects.

(@) Who did you say \_ likes John?
(@) Who did you say John likes \_?
(@) \*Who did you say that \_ likes John?
(@) Who did you say that John likes \_?

The *that*-trace effect isn't all that different from say, Complex NP islands or adjunct islands, yet it does not work well with TSL.
Let's see what the problem is.
We may try to capture the constraint in TSL by projecting *that* onto every movement tier.
Of course we only want to project *that* when it is the complementizer of a sentential argument, not the head of a relative clause or a demonstrative.
That's not a problem.
Those different instances of *that* all have different feature strings in MGs, so we can indeed pick out just the right kind of *that* without too much trouble.
No, the real problem runs a bit deeper than that (i.e, *that*).

It is the conditioning on subjects vs objects that screws things up.
If we project *that* onto the wh-tier, then the wh-mover won't have a wh^+^ mother, irrespective of whether it is a subject or an object.
So all kinds of wh-extraction will be forbidden.
If we don't project *that* onto the wh-tier, then all kinds of wh-extraction will be allowed.
The TSL view predicts that islands are mover-agnostic.

(@) **TSL's mover-agnosticism**  
    If X blocks some instance of f-movement, then it blocks every instance of f-movement.

That clearly doesn't cut it for the *that*-trace effect, and it won't work for any islands that allow extraction of arguments but not of adjuncts --- i.e. weak islands.
Naturally this can be fixed in various ways.
Instead of limiting ourselves to mother-daughter configurations on the tier, we could look at bigger chunks so that we can still see the mover and its landing site even if *that* intervenes.
Then it might be possible to make the effect of the blocker, in this case *that*, contingent on the nature of the mover.
Or we could have a more powerful tier projection that only projects *that* in cases where it matters.
That is to say, we could have separate tiers for wh-movement of subjects, wh-movement of objects, and wh-movement of adjuncts, and *that* would only end up on the subject wh-movement tier, heads of weak islands only on the adjunct movement tiers, and so on.

But that's actually easier said than done because we can't easily tell which one of those wh-tiers a wh-licensor feature should be projected to.
And even if we could make it work, it exacerbates the problem of TSL arbitrariness.
Oh, and there'll still be at least one aspect of the *that*-trace constraint that we can't handle this way (more on that below).
It's an interesting idea, but it would need some additional, currently unknown tweak to get it ready for prime time.
Perhaps, though, this is all just a case of squeezing a square peg into a round hole.
If some constraints can't be handled with the simple TSL mechanism that is sufficient for movement itself, then maybe that simply isn't the right perspective for those constraints and we should switch to an alternative.


## The role of command strings

The appeal of TSL (or rather, TSL-2) for movement is that it arose fairly naturally from considerations that had nothing to do with movement: the role of TSL in phonology, the connection between TSL and relativized locality, and TSL-2 as a minimal extension of SL.
So rather than custom-tailoring a solution for the *that*-trace effect and weak islands, let's see if there's some general considerations that would yield something useful.

A core property of MGs is that everything is handled in terms of features.
Merge expresses a linkage between category and selector features, Move a link between licensor and licensee features.
This link is commonly called checking --- but this often implies a notion of deletion or valuation that's more specific than mere linking, so I'll use the latter term for now.
A constituent is a chunk of lexical items that are connected through such links.
The head of the constituent is the lexical item in that chunk whose positive features (selector features X^+^, licensor features f^+^) entered such a link most recently.
So we may regard structural prominence as a reflection of the derivational sequence of feature linking steps.
Base on this idea, we can formulate a notion of **derivational command**, or simply **d-command**.
I won't bore you with the math here, the intuition is very easy:

1. If X and Y are linked, then X is more prominent than Y iff X contributes the positive feature to the linking.
1. If X and Y are both linked to some Z, then X is more prominent than Y iff X was linked to Z more recently than Y.

If we restrict our attention to Merge features, this translates into a very simple system for computing d-command over dependency trees:

1. Every node d-commands every node that it properly dominates.
1. Every node d-commands all its right siblings.

Or in the other direction: every node is d-commanded by its left siblings, its mother, and everything that d-commands its mother.
The table below lists a few examples over the dependency tree for *who did the destruction of Kandor prove that Brainiac hates*.
For the sake of readability I omit all features in the table and denote empty heads by their category.

![A moderately complex dependency tree]({static}/img/thomas/subreg_tutorials/cstring_exampletree.svg)

| **Lexical item** | **d-commanders** (from least to most prominent) |
| :--              | :-- |
| the              | prove, T, did |
| that             | the, prove, T, did |
| Brainiac         | hates, T, that, the, prove, T, did |
| who              | Brainiac, hates, T, that, the, prove, T, did |

As you can see, this version of d-command is very similar to base c-command, i.e. c-command between base positions when all movement is factored out.
The only difference is that the direction is reversed between heads and specifiers.
Heads d-command their specifiers but not the other way round, whereas the opposite is true for c-command.
This makes d-command more similar to the long abandoned notion of m-command in @AounSportiche83.
I honestly don't know whether there is any reason to prefer m-command over c-command, empirically they seem to do pretty much the same work.

Okay, so why are we doing all of this?
Well, let's assume that d-command is actually an important aspect of syntax.
That's not an outlandish hypothesis given that d-command is similar to c-command and c-command shows up a lot.
@FrankVijayShanker01 even argued that c-command should be the primitive, most basic relation of syntax, not mother-of, dominance, precedence, or whatever else you might be able to imagine.
Suppose, then, that a dependency tree need not only pass the SL and TSL constraints for Merge and Move, but a d-command check for every node.
To do this, we look a given node's list of d-commanders, ordered from least prominent to most prominent.
This will be a string, just like in the example above.
This is called a **command string**, or simply **c-string**.
Each c-string must meet certain well-formedness criteria based on which node it is a c-string of.

## Example 1: NPI licensing

NPIs must be c-commanded by a lexical item of a specific kind.
This could be a head that induces a downward entailing context, an interrogative C-head, or something else.
There's many theories as to how the set of licensors should be characterized.
But that's orthogonal to my basic point, so for this example it only matters that the set of licensing heads is finite (afaik it is).
Once that is the case, NPI licensing is exceedingly simple.

(@) **NPI licensing**  
    If X is an NPI, then c-string(X) must contain an NPI licensor.

Let's look at some concrete examples.

(@) Nobody thinks that Mary has ever been to Mars.
(@) Does John think that Mary has ever been to Mars?
(@) \*John thinks that Mary has ever been to Mars.

Here are the corresponding c-strings, with empty heads represented by their category:

(@) has that nobody thinks T C
(@) has that John thinks T does[interrogative]
(@) has that John thinks T C

Since *nobody* and interrogative C-heads are NPI licensors, the first two examples are fine.
The c-string of the third example lacks any NPI licensor, so the sentence is ill-formed.
One ill-formed c-string is enough to doom the whole derivation.

So far this is all fairly trivial, just a restatement of familiar ideas in new terms.
Allow me to make it a bit more interesting.
Here's the c-strings above, keeping only the elements that can license NPIs.

(@) nobody
(@) does[interrogative]
(@)

Yes, the last guy is empty.
That's exactly what separates an ill-formed from a well-formed c-string for NPI licensing.
The former contains no NPI licensors, the latter at least one.
And this distinction between c-strings is TSL.

(@) **NPI licensing is TSL-2**  
    If X is an NPI, then c-string(X) must have a non-empty Lic-tier, where Lic is the set of NPI licensors.

Keep in mind, we're working with strings here, so this is the TSL-2 we saw for things like long-distance harmony in phonology.
It doesn't involve any tree tiers.
Even though we're regulating trees, we're back in string land.
For each node in the tree, we look at its c-string, and that c-string might have to obey a string constraint.
In the case of NPI licensing, that is a TSL-2 constraint, making it very simple and natural.


## Example 2: Locally bound reflexives

The same idea also works for handling the distribution of reflexives.
**Caution:** this only means determining whether some possible antecedent exists within the right locality domain, not picking out a specific reading.
I'm well aware that many syntacticians think that's too reductionist, but I'd say it's the only notion of binding that has any place in syntax.

Under this narrow construal, Principle A says that every reflexive must be c-commanded by a $\phi$-compatible DP within its binding domain (usually a TP containing an abstract subject).
This, too, is TSL-2.

(@) **Local binding of reflexives is TSL-2**  
    Suppose that the binding domain for reflexives is delineated by some head H (possibly subject to cross-linguistic variation).
    If X is a reflexive, then c-string(X) must have a tier that
    1. contains all instances of H, and
    1. all D-heads that are phi-compatible with X, and
    1. does not start with H.

The key bit here is projecting all potential licensors and all binding domain edges, represented by the head H.
Remember that a head d-commands its specifier, so if Spec,HP furnishes a suitable antecedent, it will appear before H in the c-string.


## Example 3: Non-locally bound reflexives

Some languages have pronominals that must be syntactically bound but cannot be locally bound.
One example is **aapan** in Marathi [@Kiparsky02].
For those, the constraint is no longer TSL, but it is OTSL-2.
Remember, OTSL is TSL where the projection is contingent on what's already on the tier.

(@) **Non-local binding of reflexives is OTSL**  
    Suppose that the binding domain for reflexives is delineated by some head H (possibly subject to cross-linguistic variation).
    If X is a reflexive that must be non-locally bound by some antecedent A, then c-string(X) must have a tier of the form HA.
    The tier is constructed as follows:
    1. If the tier is empty, project H.
    1. If the last symbol on the tier is H, project Y if Y is a possible antecedent.
    1. Never project in any other case.

These are of course simplified examples.
But based on all the constraints that have been studied via c-strings so far, it seems that IOTSL is a safe upper bound on the complexity of c-string constraints.
As you might remember, IOTSL is also an upper bound on phonotactic constraints.
Once again it looks like phonology and syntax are actually very similar.
Believe me, I never planned for things to fall out this way, it just happens naturally when you're looking for elegant solutions to syntactic phenomena.


## Back to the *that*-trace effect

Alright, so can we handle the *that*-trace effect with c-strings?
Yes, and we can even account for a well-known exception.

(@) **The *that*-trace effect over c-strings**  
    Suppose that subjects are introduced as the last argument of some functional head H.
    If X is an f-mover, then c-string(X) must not be of the form H...*that*...f^+^.

This is a pretty sneaky solution.
It looks at the first symbol in the c-string in order to determine whether X is a subject.
If the first symbol is the head of some other argument, e.g. a DP or a PP, then X has some left siblings in the dependency tree, and consequently it cannot be the subject.
If, on the other hand, the c-string immediately starts with the functional head H that introduces subjects, then X is the leftmost daughter of H and hence the subject.
From here on out, it is just a matter of verifying that no *that* occurs between X and the landing site.
All of this can be done with IOTSL.

(@) **The *that*-trace effect is IOTSL**  
    Suppose that subjects are introduced as the last argument of some functional head H.
    If X is an f-mover, then c-string(X) must not have a tier of the form H *that*.
    The tier is constructed as follows:
    1. Always project the first symbol.
    1. If the last symbol on the tier is H, project f^+^.
    1. If the last symbol on the tier is H, project *that*.

Note how f^+^ here effectively blocks projection of *that*.
The complementizer projects only if the last symbol on the tier is H, so if anything else is projected first that effectively stops the tier projection.
This way, we don't care about *that* if the f-movement never actually crosses it.

Now suppose that f^+^ weren't the only thing that gets to project this way.
Suppose that, say, the heads of certain TP-adjuncts also could go on the tier.
Then that would prevent *that* from being present on the tier, making it transparent for movement.
Hmm, I feel like that is exactly what happens in some exceptional cases.

(@) \*Who did you say that \_ likes John?
(@)  Who did you say that without a doubt likes John?

That's nice.
The exceptions to the *that*-trace effect are once again expressible with the same machinery that we're already using to express the non-exceptional cases.
And this machinery isn't all that remarkable because it's roughly in the same ballpark as what we find in phonology.
Just as with the TSL-view of islands, the surprising thing is not that these constraints exist, or that there are exceptions to those constraints, but that things tend to be more systematic than they could be.
That's okay.
It just means that we're missing a theory of linguistic substance to further narrow down the class carved out by the formal restrictions.


## The big picture, once more

Alright, the subregular syntax picture just got a bit more complicated.
Merge and Move we analyze as SL and TSL over dependency trees (or, with minor changes, over derivation trees).
Licensing conditions that are mediated by c-command are instead viewed as constraints over c-strings, with the intriguing result that these string constraints seem to have the same upper bound on complexity as constraints in phonology.
Island constraints seem to be scattered across both, with some fitting into the TSL view, some into the c-string approach, and some into both.
And I haven't even talked about how we handle cases of movement feeding or bleeding licensing.
Even seemingly simple phenomena need a lot more in-depth investigation to make sure that there isn't some minor detail that trips up a putative subregular analysis.
We're basically talking Ph.D. thesis and research monograph territory (let me know if you're interested, there's some low-hanging fruit here; for instance, freezing effects).

There is a real risk, though, of ending up with a fractured system of many different levels of complexity, which would undermine the whole idea of subregular complexity as a unified, cross-domain window into locality in natural language.
But the problem isn't actually all that severe.
The next post will describe how these two perspectives can be regarded as special instances of a more general mechanism that operates over dependency trees.
So it's not like tree tiers and c-strings are completely irreconcilable.
But they do provide us with very good tools for analyzing specific subdomains of syntax.
Tree tiers represent a notion of relativized locality directly over tree structures.
It still presents a holistic view of the whole structure, just with immaterial stuff filtered out.
C-strings individualize well-formedness in that they present a limited view of the tree from the perspective of a given node.
This is intrinsically limited in that it only provides information about derivationally more prominent material, but on the flip side these constraints get to use more powerful notions of relativized locality.

In a nutshell: tree tiers and c-string are distant points in a two-dimensional space, where one axis encodes how much of the tree structure is visible to the constraint, and the other expresses degrees of locality over the visible pieces of structure.
We haven't gotten this balance quite right yet.
But I don't think we're all that far away from a very good approximation.

## References
