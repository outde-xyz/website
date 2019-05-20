---
title: >-
    Two dimensions of talking past one another
authors:
    - Thomas Graf
date: 2019-05-20
tags:
    - theory
    - methodology
    - Minimalism
---

<!-- START_SUMMARY_BLOCK -->
This post will be a bit of a mess since it's mostly me trying to systematize some issues I've been grappling with for a while now.
I have discussed my research with people who come from very different backgrounds: theoretical linguists, computer scientists, molecular biologists, physicists, and so on.
Many of these discussions have involved a fair amount of talking past one another.
To some extent that's unavoidable without a large shared common ground.
But ironically, most of the *talking past one another* actually didn't occur with, say, biologists, but with theoretical linguists, in particular Minimalists.
The rest of this post presents my personal explanation for what might be going on there.
I believe there are two factors at play.
Both concern the horribly fuzzy notion of a *linguistic theory*. 
<!-- END_SUMMARY_BLOCK -->


## The two dimensions

Let me start with a disclaimer: everything that follows is obviously simplified.
This isn't meant as an exhaustive categorization, just a quick-and-dirty approximation of the different sides individual researchers come down on.
It isn't terribly original, either.
These distinctions have been drawn before, but in my opinion they don't get enough attention.

First, there is what we might call the **formalist-analyst** axis.
Formalists equate linguistic theory with, well, the formalism.
It is the properties of the formalism that provide the key insights into language as a cognitive ability.
Linguistic analysis is only of interest to the extent that it allows us to improve the formalism.
This perspective is the dominant view among folks like me who care deeply about expressivity, learnability, and parsing.
On the other end of the spectrum you have the **analyst**, for whom the formalism is just a description mechanism.
The actual linguistic theory is the collection of analyses that have been developed for various phenomena.
This is the received view in HPSG.
Which one of the two is preferable --- formalist or analyst --- is not the point here.
It only matters that this distinction exists.

Orthogonal to the formalist-analyst axis lies the **atomist-holist** axis.
Both involve a significant amount of cognitive commitment.
So if you believe that a linguistic theory (whatever that may be) need not express any aspects of linguistic cognition, you have no place on this axis at all.
In Chomskyan terms, everybody on this axis subscribes to some notion of I-language.
Where they differ is in how that commitment is expressed through linguistic theory.

Atomist

: If you have more than one viable description, you do not fully understand the object you're describing.

Holist

: If you have only one viable description, you do not fully understand the object you're describing.

The atomist believes that each individual component, each *atom* of the theory comes with a cognitive commitment.
An underlying representation isn't just a convenient abstraction of how surface forms are related, it literally exists in the human mind.
Syntactic features exist, and a cognitively committed theory must determine which of them are privative, binary, or multi-valued.
The Chomskyan view of syntax is largely atomist, although it is more a matter of ambition than a genuine conviction that the atoms of our current theories are all cognitively real.

The holist, on the other hand, grants cognitive reality only to the theory as a whole.
For the holist, it does not matter whether underlying representations are real or a useful abstraction because either way one captures the fact that a native speaker knows how surface forms cluster into groups of related forms.
Nor does it matter to the holist if features are cognitively real or just convenient mark-up for encoding something much more abstract and tacit.
That is not a meaningful distinction by itself.
Only if it is embedded in a broader network of assumptions can one possibly derive any specific cognitive claims from it.
The holist is always mindful of the fact that there's many ways to skin a cat, and whether one is preferable to the others depends on circumstances.
The holist strives for a cognitively real theory but recognizes that a theory can enjoy cognitive reality even if there isn't a single part of it that's cognitively real.
The holist thus sees encodings largely as a utilitarian matter rather than a deep window into the mind.

Again, I'm not judging here, and I don't particularly care if one position is more or less sound than the other.
I'm just trying to make sense of how different commitments play into linguistic discussions.


## The coordinate system of linguistic theorizing

We now have a coordinate system with four quadrants, each one of which we can associate with specific linguistic communities.

|              | formalist | analysist |
| --:          | :-:       | :-:       |
| **holist**   | CompLing  | HPSG, LFG |
| **atomist**  | Minimalist (Hornstein-style) | Minimalist (Legate-style) |

I place myself in the formalist-holist quadrant, and I suspect that my holisticity (totally a word) is unusually high even for a computational linguist.
I think that many syntacticians working with HPSG and LFG comfortably fit in the analyst-holist category, assuming that they don't completely shy away from cognitive commitments.
Despite that, the majority of syntacticians would probably fit best in the atomist half of the coordinate system; in particular Minimalists.
To them, interfaces exist, so do features, and there is one right way to invoke them and many, many wrong ways.

Within the atomist camp, the split between formalists and analysts is slightly hazy.
The prototypical cases are straight-forward if we only consider Minimalist syntacticians:
A formalist Minimalist will focus a lot on Merge, Move, the basic laws and operations that drive syntax, third factor explanations, that kind of stuff.
The analyst Minimalist treats those as a mere tools for carrying out analyses.
To some extent the formalist-analyst divide among atomists mirrors what Norbert Hornstein calls the *linguist*-*languist* divide.

If I had to give names (gun to my head), I'd say that Norbert Hornstein is an example of a formalist-atomist, whereas Julie Legate and Jessica Coon are examples of analyst-atomists.
But putting people into boxes rarely works well, and in this case it's particularly fraught with difficulties.
In my experience, barely any Minimalist is firmly in only one of the two camps.
There's two reasons for this: 

1.  Both camps share an implicit agreement that the formalism itself matters less than it's intended usage.
    If there's a serious loop hole, that doesn't matter if nobody's using that loop hole or doing so would be unintuitive.
    The idea is that the loop hole is a formal curiosity that can somehow be patched out, rather than a serious issue that warrants deep probing.
    This is an analyst attitude, yet it's also held by formalist Minimalists.

1.  At the same time, very few Minimalists are true analysts that don't care about the formalism at all.
    There is a shared believe that at the end of the day, the formalism is not just a description language but a broad-strokes theory of what's going on in the human mind, with the analyses filling in the details.
    You won't find many Minimalists who are willing to bend the formalism to their will just to fit the data.
    A true analyst wouldn't have any gripes with that.

And this is why talking to a Minimalist is a more subtle affair than talking to somebody who does HPSG or LFG.
With the latter, I have a pretty solid idea where they're coming from.
Minimalists are more of a moving target because they don't neatly cluster into just one of the four quadrants.
On average, I can be sure that I'm talking to an atomist rather than a holist, but the formalist-analyst split does not work well for them.


## Why it matters

Here's an example why this matters.
One result I consider very important is the intimate connection between features and constraints.
Constraints can be reduced to features, and features can be abstracted into constraints.
More precisely: In any syntactic formalism with subcategorization (i.e., every syntactic formalism), every constraint definable in monadic second-order logic (MSO) can be compiled directly into the feature calculus to be enforced via subcategorization.
Similarly, the feature calculus can be abstracted into a collection of MSO-definable constraints.

As mentioned before, I'm a formalist-holist (hardcore formalist-holist, to be precise), so I have a specific view of what this result entails.
First, there is nothing unnatural or undesirable about switching between features and constraints, that's just a matter of changing encodings and does not affect the overall system.
That's the holist in me speaking.
At the same time, my inner formalist tells me that this result is a serious problem.
We don't want grammars that can express arbitrary MSO-constraints.
But subcategorization allows for that.
So we have to dig deeper to fix this.
And years of digging haven't really resulted in any good ways of limiting the power of subcategorization or the feature calculus.
Hence my current stance is that we should shy away from both as much as possible and focus firmly on constrains, where it is a lot easier to limit expressivity.

But this move is very hard to justify to a Minimalist.
First of all, they're atomists, so switching between features and constraints is not an innocuous step.
If you're doing that, you've already made a category mistake, so anything that follows from that is dubious at best.
Fair enough, I've thought about that point enough to have some comebacks, and I know that Minimalists trend towards atomist positions so I can address those questions before they even come up.
The harder part is the formalist-analyst split.

The analyst won't see the point of this shift at all because we have an established set of features with defined uses, so you can't repurpose them to encode something completely different.
Yes, the formalism may allow for it, but the set of established analyses --- i.e. the actual theory --- does not.
The formalist, on the other hand, will focus on how the original result rests on some assumptions that do not quite match up with their notion of features or selection.
There's answers for both, but they go in completely opposite directions.
The analyst doesn't want to hear about why the minor technical differences do not invalidate the result, and the formalist does not care all that much how this feature-coding fits into current analyses.
In fact, bringing up one of these points with the wrong audience may just cause confusion about why I'm going off on that tangent, and it will test their patience.
And if I already had a hard time pinning down whether I'm dealing with a formalist or an analyst, I'll definitely have a hard time once I've introduced talking points that they wouldn't have brought up on their own.
A few missteps like that, and all of a sudden I find myself in a debate where neither party quite understands what the other one is going on about.


## Wrapping up

The example above is just one of many.
The same problems arise when discussing generative capacity, parsing, learnability results, pretty much anything.
Heck, even island constraints or the *ABA generalization.
Talking across subfields is always difficult, and it takes lots of practice to figure out the right pitch for your target audience.
I think it's particularly difficult for mathematical and computational linguistics, both of which have a somewhat strained relation with theoretical linguistics for historical reasons.
The system above has helped me a bit in tailoring the message to the audience, but as I said, there's still plenty of opportunities for derailing the discussion.

Since I mostly interact with syntacticians, I don't know if there's comparable hurdles to navigate with phonologists, psycholinguists, and so on.
I suspect there are, anything else would be quite surprising.
But if you have some first-hand experiences to share, the comments section is all yours.
