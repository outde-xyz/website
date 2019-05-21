---
title: >-
    A song of middles and suffixes
authors:
    - Thomas Graf
date: 2019-05-21
tags:
    - phonology
    - subregular
    - strictly local
    - fun allowed
---

<!-- START_SUMMARY_BLOCK -->
Am I the only one who's worn out by the total lack of fun and playfulness in all public matters?
Everything is serious business, everything is one word away from a shit storm, everybody has to be proper and professional all the time, no fun allowed.
It's the decade of buzzkills, killjoys, and sourpusses.
Linguistics is very much in line with this unfortunate trend.
Gone are the days of Norbert Hornstein dressing up as Nim Chimpsky.
It is unthinkable to publish a paper under the pseudonym *Quang Phuc Dong* (that's at least a micro-aggression, if not worse).
Even a [tongue-in-cheek post on Faculty of Language](https://facultyoflanguage.blogspot.com/2019/05/gg-nn-thing-1-thing-2.html) is immediately under suspicion of being dismissive.
Should have added that `/s` tag to spell it out.

Compared to other fields, linguistics has never been all that playful, perhaps because we're already afraid of not being taken seriously by other fields.
But we've had one proud torch bearer in this respect: Geoff Pullum.
His *Topic... comment* column should be mandatory grad school reading.
[Formal Linguistics Meets the Boojum](https://www.jstor.org/stable/pdf/4047783.pdf) is a classic for the ages (and did, of course, get a very proper and professional response).
My personal favorite is his [poetic take on the Halting problem](http://www.lel.ed.ac.uk/~gpullum/loopsnoop.html).
So I figured instead of complaining I'd lead by example and inject some fun of my own.
To be honest, I'm probably better at complaining, but here we go...
<!-- END_SUMMARY_BLOCK -->

## Round 1

| We'll investigate a set of strings
| such is the passion of mathlings
| it could encode a lot of things
| DNA and words and sounds, methinks
|
| We want to test locality
| in the strict sense with formality
| we'll rely on math's regality
| to find the truth in totality
|
| We'll play a substitution game
| where distinct strings should be the same
| and if it fails we can proclaim
| it's not SL, oh what a shame
|
| Pick strings $s$, $t$ from this set
| and cut them up like a sextet
| prefix, suffix can[^1] differ, yet
| middle identity must be met
|
| Now switch the suffixes around
| and check if the result is sound
| you may ask why, I shall expound
| and so we start the second round:

## Round 2

| A recognizer for SL-$k$
| is just too easy to lead astray
| from left to right on its merry way
| it collects all substrings of size $k$
|
| If some $k$-grams are forbidden
| a $k$-gram scanner won't admit'em
| and the whole string plainly didn't
| follow the rules as they are written
|
| Now $s$ and $t$ are both just fine
| their $k$-grams all do toe the line
| the $k$-gram scanner should not whine
| if $s$ and $t$ do intertwine
|
| If the middle is long enough
| we've got the perfect SL-bluff
| suffix switching adds no stuff
| but is the outcome up to snuff?
|
| The $k$-grams are the same, you see,
| the $k$-gram scanner must decree:
| "Admit the string for its esprit!"
| and that's the trap! On to round 3:

## Round 3

| If the string is not permitted
| while SL-scanners do admit it
| then the proof has been submitted:
| the string set's not SL. You get it?
|
| If after all this neat exposure
| you still need the full disclosure:
| An SL language's composure
| requires...
| suffix substitution closure!


## Epilogue

This didn't actually take too long to write, I whipped it up in two hours while basking in the sun (in b4 someone says it shows).
The meter roughly matches parts of [this lovely Animaniacs song](https://www.youtube.com/watch?v=oc3xTj3g9QQ), so we can totally sing this at the next subregular workshop.

And if you have something linguistics- or academia-related that you did just for fun, perhaps even shits and giggles, I'd love to see it posted on the Outdex.
Jokes, songs, limericks, anecdotes, parodies, or a short proof that Klingon is not TSL, whatever.
Let's add a dash of light-hearted, tongue-in-check, silly, goofy **fun**.

[^1]: This was *should* originally. Thanks to Jeff for pointing out how misleading that choice of words would have been.
