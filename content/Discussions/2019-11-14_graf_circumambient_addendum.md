---
title: >-
    More circumambience in syntax
authors:
    - Thomas Graf
date: 2019-11-14
bibliography: references.bib
series: >-
    Circumambience in syntax
tags:
    - subregular
    - syntax
    - movement
    - complementizer agreement
    - relative clauses
    - English
    - French
---

<!-- START_SUMMARY_BLOCK -->
This is a very short follow-up [to my previous post on circumambient patterns in syntax]({filename}2019-11-11_graf_circumambient_syntax.md).
I just realized that there's another, very robust example that makes all the cases look even more mundane: complementizer alternations in English relative clauses.
<!-- END_SUMMARY_BLOCK -->

## The data

This is short and sweet.
In English, object relative clauses (ORCs) can either have a pronounced complementizer (*that*) or an unpronounced one.
Subject relative clauses (SRCs), on the other hand, must have a pronounced complementizer.

(@) the man that I called was very rude **(ORC with pronounced C)**
(@) the man I called was very rude **(ORC with empty C)**
(@) the man that called me was very rude **(SRC with pronounced C)**
(@) \*the man called me was very rude **(SRC with empty C)**

## Promotion analysis of relative clauses

There's approximately 372 different analyses of RCs, but I'm particularly fond of the promotion analysis (actually, there's also tons of things I don't like about it, but, well, you gain some you lose some).
In the promotion analysis, the head noun of the RC starts out as an argument of the RC-verb and then moves to Spec,CP, triggered by some movement feature f^-^ on the head noun and a matching f^+^ on the complementizer of the RC.

(@) the [~CP~ man[f^-^] that[f^+^] I called *t*] was very rude **(ORC with pronounced C)**
(@) the [~CP~ man[f^-^] C[f^+^] I called *t*] was very rude **(ORC with empty C)**
(@) the [~CP~ man[f^-^] that[f^+^] [~TP~ *t* [~VP~ *t* called me] was very rude **(SRC with pronounced C)**
(@) \*the [~CP~ man[f^-^] C[f^+^] [~TP~ *t* [~VP~ *t* called me] was very rude **(SRC with empty C)**


## An OTSL grammar

The pattern above works just like the circumambient patterns in Irish, Kinande, and German, with mandatory *that* as an instance of movement-driven complementizer agreement.
But there's two minor differences.
First, it isn't just any mover that triggers the complementizer agreement, but only subjects.
Since we're working with MGs, we can recognize a subject based on its nom~-~ feature.
Second, the complementizer that we want to regulate also happens to be the right edge of the interval.
To accommodate that, we make some minor changes to the OTSL grammar.

1. Project every lexical item with an f^+^, and every lexical item with an f^-^ preceded by nom^-^.
1. Don't have f^-^ C[f^+^] on the tier.

Pretty simple, I'd say.
The same system can also be used to enforce the *qui*/*que* alternation in French.

Both phenomena then form a natural class with movement-driven complementizer agreement.
In all those cases, it's the same computational machinery doing the job.
If we're not surprised by something mundane like the SRC/ORC split for *that* in English or the *qui*/*que* alternation in French, then we shouldn't be surprised by movement-driven complementizer agreement in general.
