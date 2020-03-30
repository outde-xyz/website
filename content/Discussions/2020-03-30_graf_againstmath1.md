---
title: >-
    Against math: Kuratowski's spectre
series: >-
    Against math
authors:
    - Thomas Graf
date: 2020-03-30
bibliography: references.bib
tags:
    - methodology
    - syntax
    - set theory
    - Merge
    - linearization
---

<!-- START_SUMMARY_BLOCK -->
As some of you might know, [my dissertation](https://thomasgraf.net/output/graf13thesis.html) starts with a quote from *My Little Pony*.
By Applejack, to be precise, the only pony that I could see myself have a beer with (and I don't even like beer).
[You can watch the full clip,](https://youtu.be/k3NkMTV9r5U) but here's the line that I quoted:

> Don't you use your fancy mathematics to muddy the issue.

Truer words have never been spoken.
In light of my obvious mathematical inclinations this might come as a surprise for some of you, but I don't like using math just for the sake of math.
Mathematical formalization is only worth it if it provides novel insights. 
<!-- END_SUMMARY_BLOCK -->

Some work falls short of this bar (your call whether mine does).
And some work is actively worse because of its use of math.
Both things have happened and are still happening in Minimalist syntax.
Ever since the publication of *Bare Phrase Structure* [@Chomsky95], there has been a line of Minimalist research that wants to formalize Merge in set-theoretic terms and derive linguistic properties from mathematical set theory.
This is, for lack of a better term, ass-backwards.

Today's post is the start of a two-part series.
It covers the general conceptual and mathematical problems with a lot of this work.
The next post will discuss a concrete example of how bringing in math can actively undermine a linguistic proposal rather than strengthening it.
So, without further ado, let's talk Kuratowski.


## Kuratowski and the confusion of sets and set theory

Quick show of hands, who has seen this before:
$$\{ \{a\}, \{a, b\}\} = \langle a, b \rangle$$
This is the **Kuratowski definition** of pairs in terms of sets [@Kuratowski21].
In contrast to sets, pairs have an intrinsic order, so that $\langle a, b \rangle \neq \langle b, a \rangle$ (unless $a = b$).
Instead of $\{ \{a\}, \{a, b\} \}$ one can also use $\{ a, \{a, b\} \}$, which is called the **short Kuratowski definition**.

I can't think of any other mathematical tidbit that has been invoked more often in syntax (although I have yet to find a paper that actually cites @Kuratowski21). 
Minimalists like this definition because it looks very similar to the set-theoretic objects @Chomsky95 uses to encode syntactic structure:
Merge takes two syntactic objects $a$ and $b$ and combines them into the syntactic object $\{ a, \{a, b\} \}$.
Even though the object is a set and thus unordered, we can use the (short) Kuratowski definition to establish a connection to pairs, which are ordered.
And from there we can develop all kinds of ideas about linear order in syntax.
Except that we actually can't because the (short) Kuratowski definition only holds in a specific version of set theory.
It's not a theorem about the connection between sets and linear order, it's a particular mathematical definition of pairs that works in a particular version of mathematical set theory.


## Why does the Kuratowski definition work?

Now before we go on any further, let's demystify the Kuratowski definition.
Why is this the set-theoretic definition of pairs?
First of all, it's not **the** set-theoretic definition of pairs, it's **one** set-theoretic definition.
As always in math, there's a million ways to set things up.
Wiener's definition represents the pair $\langle a, b \rangle$ as $\{ \{ \{a\}, \emptyset \}, \{\{b\}\} \}$.
Hausdorff uses the much more intuitive $\{ \{a, 1\}, \{b, 2\} \}$.
And there's many other alternatives.
So don't attach too much metaphysical importance to the Kuratowski definition, it's just a definition that happens to work because it captures a specific property of pairs.

Pairs are characterized by an essential equivalence:
$$\langle a, b \rangle = \langle c, d \rangle \text{ iff } a = b\ \&\ c = d$$
That's what separates pairs from sets, where the expression $\{ a, b \}$ is the same as $\{ b, a \}$ because of the lack of order.
With pairs, on the other hand, $\langle a, b \rangle \neq \langle b , a \rangle$ (unless $a = b$, in which case we would have $\langle a, a \rangle = \langle a, a \rangle$).

The Kuratowski definition works because sets of the form $\{ \{a\}, \{a, b\} \}$ satisfy the same equality condition:
$$\{ \{a\}, \{a,b\} \} = \{ \{c\}, \{c,d\} \} \text{ iff } a = b\ \&\ c = d$$
The right-to-left direction is easy to see.
That is to say, if $a = b$ and $c = d$, then it is pretty much inevitable that $\{ \{a\}, \{a,b\} \} = \{ \{c\}, \{c,d\} \}$.
It's the left-to-right direction of the *iff* that's tricky.
In order to show that $\{ \{a\}, \{a,b\} \} = \{ \{c\}, \{c,d\} \}$ entails $a = b$ and $c = d$, we have to consider several cases.

### Case 1: $a = b$

Suppose $a = b$.
Remember that sets are **idempotent**, which means that repetitions are ignored.
For instance, $\{ a, b, c, b, a, a \} = \{a, b, c\}$.
If $a = b$, then $\{ \{a\}, \{a,b\} \} = \{ \{a\}, \{a, a\} \} = \{ \{a\}, \{a\} \} = \{ \{a\} \}$.
But then $\{ \{a\}, \{a,b\} \} = \{ \{c\}, \{c,d\} \}$ is actually $\{ \{a\} \} = \{ \{c\}, \{c,d\} \}$.
This is possible only if $\{ c \} = \{c ,d\}$, which implies $c = d$.
So we actually have $\{ \{c\}, \{c,d\} \} = \{ \{c\}, \{c,c\} \} = \{ \{c\}, \{c,c\} \} = \{\{c\}\} = \{\{a\}\}$, and hence $a = c$.
Overall, then, we have $a = b = c = d$, which necessarily entails $a = c$ and $b = d$.

### Case 2: $a \neq b$

Now suppose $a \neq b$.
Then either $\{a\} = \{c,d\}$ or $\{a\} = \{c\}$.

1. Since two sets with distinct cardinality cannot be identical, the equality $\{a\} = \{c,d\}$ holds only if $c = d$.
   Then $\{ \{a\}, \{a,b\} \} = \{ \{c\}, \{c,d\} \} = \{ \{c\}, \{c\} \}$, but $\{c\} \neq \{a, b\}$ because $a \neq b$.
   This is a contradiction, so it must be the case that $\{a\} \neq \{c,d\}$.

1. Assume, then, that $\{a\} = \{c\} \neq \{c,d\}$.
   Then $c \neq d$, and $\{a, b\} = \{c, d\}$ iff $b = d$.
   Overall, then, we have $a = c$ and $b = d$, as required.


## When does the Kuratowski definition work?

Did you notice something in the proof above?
The proof is mathematically sound, but it relies on specific assumptions of set theory.
For instance, that it is impossible for both $c \neq d$ and $\{a\} = \{c,d\}$ to be true because a set with one member can never be identical to a set with two members.
Alright, that's intuitive enough, but things get worse.

For Minimalist syntax, we don't really care about the long Kuratowski definition with $\{ \{a\}, \{a,b\} \} = \langle a,b \rangle$, we want the short one with $\{ a, \{a, b\} \} = \langle a,b \rangle$ because that's the kind of set-theoretic object that's built by Merge.
The proof above, however, runs into a problem with the short definition.
Suppose $\{a, \{a, b\}\} = \{c, \{c,d\} \}$ and $a = \{c, d\}$.
Then either $\{a, b\} = c$ or $\{a, b\} = \{c, d\}$.
We have to rule out the case that $\{a, b\} = c$ --- otherwise, the connection to pairs will break down as we could have really weird sets that are equivalent even though they wouldn't be equivalent when viewed as pairs.

Intuitively, $\{a, b\} = c$ is easy to rule out.
If $\{a, b\} = c$ and $a = \{c, d\}$, then we get some kind of infinite loop by substituting $\{c, d\}$ for $a$ and $\{a, b\}$ for $c$:
$$a = \{c, d\} = \{ \{a, b\}, d \} = \{ \{ \{c,d\}, b \}, d \} = \{ \{ \{ \{a, b\}, d\}, b\}, d\} = \ldots$$
Clearly that's not okay, right?
Actually, it is.

Ruling out such cases of infinite recursion requires the **axiom of regularity**.
This axiom is part of the standard formalization of set-theory known as ZFC, **Zermelo-Fraenkel with the axiom of choice**.
That is actually a really weird axiomatization because it is a first-order definition, which means that sets and the objects contained by sets have the same type.
If you still think a set is a collection of objects, you're not thinking in ZFC terms where there is no distinction between objects and collections of objects.
ZFC is about as far away from our informal understanding of sets as one can get.

And to add insult to injury, the axiom of regularity does precious little work for ZFC.
All the important theorems for ZFC set theory hold irrespective of whether one enforces the axiom of regularity.
And there is a giant cottage industry of non-standard set theories that all eschew the axiom of regularity plus a truckload of other ZFC axioms.
There is no such thing as **the** definition of sets, there's many competing formalizations that support completely different theorems.
Many of them do not support the short Kuratowski definition.
The short Kuratowski definition simply does not work unless one makes very specific commitments about the nature of sets.


## The folly of mathing your syntax

I think what this shows is that this kind of set-theoretic work in syntax is trying to have its cake and eat it to.
On the one hand, nobody wants to say that syntax literally operates with a notion of set that corresponds to the ZFC axiomatization of set theory.
That would entail a commitment to the psychological reality of its highly abstract and counter-intuitive axioms, including the axiom of regularity.
And as far as cognitive commitments go, that's pretty far out there.
In general, the set-theoretic view of Merge is taken to be either a convenient metaphor or to be rooted in naive set theory.
I don't know of a single paper that uses the short Kuratowski definition and explicitly states that the sets built by merge are assumed to obey the laws of ZFC.
So that's one side of the cake: naive notions of set, rather than mathematical set theory.

But on the other hand this work then drags out mathematical properties such as idempotency and the short Kuratowski definition, without acknowledging that these do not work with the intuitive notion of sets.
Because, let's face it, sets simply aren't intuitive.
The closest thing we have to sets in the real world is bags, and those still aren't sets because they lack idempotency: a bag with two $a$-objects is not the same as a bag with one $a$-object.
There is no such thing as an intuitive notion of sets; sets are intrinsically unintuitive.

And this takes me to the broader point I want to make in this series.
All that mathematical quibbling about definitions, equivalences, and axiomatizations is completely pointless.
Why would you ever open yourself up to criticism of that kind?
None of the syntactic proposals that use the Kuratowski definition actually need it to make their point.
The ideas could be stated in very different terms, and they would be none the poorer for it.
Dressing up your linguistic idea in terms of sets doesn't magically make it better or derives some linguistic property without further stipulations.
Quite to the contrary: the moment you invoke the Kuratowski definition, you're implicitly stipulating the cognitive reality of half a dozen first-order axioms.
And in service of what?
If your idea works, we can define it in a million ways and it doesn't really matter what it looks like when it is hashed out in terms of sets.
If your idea doesn't work, then it doesn't work and is bunk no matter how elegantly you derived it from set theory.

## References
