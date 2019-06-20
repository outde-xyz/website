---
title: >-
    The anti anti missile missile argument argument
authors:
    - Thomas Graf
date: 2019-06-21
bibliography: references.bib
tags:
    - formal language theory
    - generative capacity
    - morphology
    - semantics
---

<!-- START_SUMMARY_BLOCK -->
Computational linguists overall agree that morphology, with the exception of reduplication, is regular.
Here regular is meant in the sense of formal language theory.
For any given natural language, the set of well-formed surface forms is a regular string set, which means that it is recognized by a finite-state automaton, definable in monadic second-order logic, a projection of a strictly 2-local string set, has a right congruence relation of finite index, yada yada yada.
There's a million ways to characterize regularity, but the bottom line is that morphology defines string sets of fairly limited complexity.
The mapping from underlying representations to surface forms is also very limited as everything (again modulo reduplication) can be handled by non-deterministic finite-state transducers.
It's a pretty nifty picture, though somewhat loose in my subregular eyes that immediately pick up on all the regular things you don't find in morphology.
Still, it's a valuable result that provides a rough approximation of what morphology is capable of; a decent starting point for further inquiry.
However, there is one empirical argument that is inevitably brought up whenever I talk about the regularity of morphology.
It's like an undead abomination that keeps rising from the grave, and today I'm here to hose it down with holy water.
<!-- END_SUMMARY_BLOCK -->

## The *anti missile missile* argument

The argument goes back to a discussion in @Halle73 and centers around the *anti-X-missile* construction in English.
A missile that shoots down a missile is an *anti-missile-missile*.
A missile that shoots down such an anti-missile-missile is an *anti-anti-missile-missile-missile*.
But then there could of course also be an *anti-anti-anti-missile-missile-missile-missile*.
You see where this is going.
The overall pattern is $\text{anti}^n \text{missile}^{n+1}$ for $n \geq 0$.
Such counting patterns are (barely[^cfl]) context-free, but not regular. Consequently, morphology cannot be regular.

[^cfl]:
String sets of the form $a^n b^n$ are usually presented as the prototypical case of context-freeness.
But that is very misleading.
It's like saying that $(ab)^*$ is regular.
That's true, but $(ab)^*$ is also strictly 2-local, making it one of the least complex regular languages one can imagine.
Similarly, $a^n b^n$ is a **counter language** --- first you count up with each symbol, and as soon as you see your first $b$ you switch over to counting down with each symbol, hoping to reach 0 at the end.
The class of counter languages includes all regular languages but is a proper subclass of the deterministic context-free languages, which are already a much more restricted fragment of the context-free languages (they can be parsed in linear time, whereas arbitrary CFLs are cubic time).
So $a^n b^n$ is a pretty bad example of what a context-free language can look like.
A better choice would be $ww^R$ (the language of palindromes) or $a^n b^n \cup a^n b^{2n}$.
Both crucially involve non-deterministic guesses that could only be offset by perfect lookahead.

This argument is undermined by two major flaws.
The first one is already enough to shoot it down, but for the sake of completeness I'll discuss both here.

## Fault 1: Subset fallacy

The first problem is the **subset fallacy**: just because some subset of string set *L* has complexity *C* does not entail that *L* is at least of complexity *C*.
That's really damn obvious.
The set $\Sigma^*$ of all strings over alphabet $\Sigma$ is strictly 1-local, which is about as weak as it gets for formal languages (depending on your definitions, it's even strictly 0-local, which really is rock bottom for complexity).
So $\Sigma^*$ is really, really simple.
Yet if we look at all subsets of $\Sigma^*$ we'll find some that are context-free, context-sensitive, or not even computable.
Or the other way round, $\text{anti}^n \text{missile}^{n+1}$ is context-free, but this does not imply that its superset $\Sigma^*$ is not regular.
That's because the well-formedness distinctions that need to be made for the subset do not necessarily have to be made for the superset, and well-formedness distinctions are what complexity is all about in formal language theory.

The subset fallacy is a well-known problem with empirical arguments.
It's not enough to show that a language contains a construction of a specific complexity, you have to measure the complexity of the language as a whole.
Just because a string is not part of the construction does not entail that it isn't part of the language.
@PullumGazdar82 use this line of reasoning in their defense of GSPG to dismantle tons of purported counterexamples to the context-freeness of syntax.
@MohriSproat06 deemed the subset fallacy a sufficiently widespread problem to write an entire paper about it.
Identifying a subset of a specific complexity simply doesn't equate to a robust claim about the complexity of the whole language, and that's why we have to rely on more indirect inference steps like the intersection approach that @Shieber85 used to show that syntax is not context-free after all.

In the specific case of *anti-X-missile*, this would work as follows:

1. Start with the regular string set $L := \text{anti}^* \text{missile}^+$, i.e. 0 or more instances of *anti* followed by 1 or more instances of *missile*.
1. View English morphology as a string set $E$ and intersect it with $L$.
1. Since regular languages are closed under intersection, $E$ cannot be regular if $E \cap L$ is not regular.

And here's where the argument comes tumbling down.
The intersection of $E$ and $L$ is actually regular.
There is nothing wrong with a word like *anti anti anti anti missile*.
Nor is there a problem with *anti missile missile missile missile*.
How often one occurs does not affect how man instances the other might have.

Sure, you might have a hard time assigning a concrete meaning to these strings, but that's just the freestyle nature of compounding.
I could imagine that a *missile missile* is a missile that shoots out smaller missiles.
So of course I can have a *missile missile missile* which shoots out *missile missiles*.
And then I could have an *anti missile missile missile missile* whose job it is to shoot down missile missile missiles.
Heck, we can take this further and talk about *missile anti missiles* in opposition to *laser anti missiles* --- one uses tiny missiles to take down missiles, the other one lasers.
Or perhaps *missile anti missiles* is just another way of saying *anti missile missiles*, with additional emphasis that what's being shot down is missiles, not zombie dragons.
I also have no problem assigning *anti anti missile* exactly the same meaning as *anti anti missile missile missile*.
Perhaps your readings differ, but that's not the point.
The crucial fact is that none of these strings are ill-formed, they just lack a fully conventionalized meaning, which is typical for nonce compounds.

## Fault 2: Well-formed != readily interpretable

At this point the second problem with the argument kicks in.
One could argue that there is something like an *anti-X-missile* construction that comes with a very specific, grammaticalized meaning attached to it.
So $\text{anti}^n \text{missile}^{n+1}$ is a natural class of some kind that must be distinguished from $\text{anti}^* \text{missile}^+$ that just uses arbitrary compounding.
That may well be so, but that's semantics.
The claims about morphological complexity are --- spoilers! --- about morphology.
In both cases we combine morphological material.
It just so happens that some of these steps may have a conventionalized semantics, just like merging *kick* with *the bucket* can give rise to a more specialized meaning.
That doesn't mean that syntax contains a privileged *kick the bucket* operation.

Also keep in mind that semantics can do all kinds of things that are crazy complex.
If Principle C does indeed work according to its common description in terms of assigning indexed guises, then it isn't computable in full generality [@Rogers98].
Rule I as formulated by Tanya Reinhart and later on Irene Heim requires identity of meaning, a notion that isn't even computable for first-order logic, let alone the higher-order logics used by semanticists.
Perhaps those analyses just vastly overstate the true complexity of the problem, but quite generally semantics seems a lot more powerful than it's structure-building brethren.
That's exactly why we don't want semantics to invade all aspects of grammar, it hides their structural simplicity under the rubble of complex meanings.

But even if we do bring in semantics and grant it a privileged role in morphology, the *anti missile missile* argument only tells us that word interpretation can be much more complex than word formation.
Frankly, I think it even fails at that, but for now I'll refrain from picking this fight because it's completely immaterial for the issue at hand.
The bottom line is that morphological complexity is completely different from semantic complexity, and the fact of the matter is that English morphology is perfectly fine with stuff like *anti anti anti missile* or *anti missile missile missile*.
That's why the *anti missile missile* argument has no bearing on the complexity of morphology.
And thus concludes the anti *anti missile missile* argument argument.

## References
