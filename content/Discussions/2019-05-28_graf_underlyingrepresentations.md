---
title: >-
    Underappreciated arguments: Underlying representations
series: >-
    Underappreciated arguments
authors:
    - Thomas Graf
date: 2019-05-28
tags:
    - phonology
    - morphology
    - underlying representations
    - abstractness
    - bimorphisms
    - T-model
---

<!-- START_SUMMARY_BLOCK -->
Time for another entry in the *Underappreciated arguments* series.
This post will be pretty short as it is a direct continuation of the previous entry on how the inverted T-model emerges naturally from the bimorphism perspective.
You see, the very same argument also gives rise to underlying representations in phonology and morphology.
<!-- END_SUMMARY_BLOCK -->


## The UR hullabaloo

Whereas underlying representations (URs) were a pillar of theoretical linguistics in the 20th century, they have recently become a lot more contentious even among phonologists.
I'm not qualified to do the topic justice, but fortunately Larry Hyman has an [excellent survey paper](https://doi.org/10.1017/S0022226718000014) where he presents a number of arguments against URs and how they miss the point.
His bottom line is that URs are a useful tool, and I fully agree.
But I think one can make an even stronger point: just like rejecting the T-model, rejecting URs is an inconsistent position.

One baseline that everybody agrees on is that speakers are aware of relations between surface forms.
Speakers know that *dog* and *dogs* go together in a way that *dog* and *cat* do not.
One can debate the nature of these relations, how they are learned and stored, but nobody flat out denies the existence of these abstract relations.
Another basic fact about these relations is that they are symmetric.
If a speaker knows that *dogs* is related to *dog*, they also know that *dog* is related to *dogs*.
Now consider the toy case where the only two surface forms are *dog* and *dogs*.
We can depict that as follows:

![Direct mappings between *dog* and *dogs*]({static}/img/thomas/underappreciated_ur/directmapping_dog.svg){ width=30% }

Does that look familiar?
[It should]({filename}2019-05-15_graf_tmodel.md#bimorphisms-and-the-t-model).
As in the previous post, we can use the bimorphism approach to decompose this into a system with an interpolant and two mappings.

![Bimorphism for *dog* and *dogs*]({static}/img/thomas/underappreciated_ur/bimorphism_dog.svg){ width=30% }

Voilà UR!
Admittedly this toy example only uses two forms.
But the complete picture isn't all that different.
Instead of individual surface forms, we have to consider the whole set of surface forms.
And the mapping we are interested in is a mapping from surface forms to related surface forms.

![Bimorphism for surface forms]({static}/img/thomas/underappreciated_ur/bimorphism_sf.svg){ width=35% }

Since the two sets are identical, we can conflate them.

![Reduced bimorphism for surface forms]({static}/img/thomas/underappreciated_ur/bimorphism_sf_reduced.svg){ width=18% }

So overall the picture looks a bit different from syntax, but it still follows the basic idea behind bimorphisms.

Alright, let's step back from the math for a second and focus what this really tells us.
In the bimorphism picture, two surface forms $a$ and $b$ are related iff there is an interpolant $c$ such that both $a$ and $b$ can be obtained from $c$.
For any surface form $a$, its set of related forms contains all $b$ that can be obtained from some $c$ that $a$ can also be obtained from.
From this perspective, we can even define URs as sets of surface forms because in the end that's all we actually want from an interpolant like $c$.

Just like the T-model, then, URs are a simple way to define a specific kind of mapping or relation.
Seriously denying URs means denying that such relations between surface forms exist, and nobody does that.

## Why URs?

In the case of syntax, the T-model is the natural choice because nobody knows how to directly compute the mappings between physical forms and meanings without invoking syntactic objects as the middle man.
Afaik, the same does not hold for phonology and morphology.
There are theories that directly relate surface forms without any kind of mediating interpolant.
But that does not mean that URs have nothing to offer.

For instance, there is a lot of interest right now in the subregular complexity of the mappings from URs to surface forms.
It might well be the case that the attested mappings form a natural, very limited class from this perspective while mappings between surface forms are harder.
If so, the factorization into URs and mappings would provide a crucial insight:
Once the interpolant has been identified, the actual mapping process is simple, and consequently any increased complexity in the direct mappings between surface forms corresponds to the analytic workload of inferring a UR.
Or in the words of the bimorphism perspective: the hard part is reversing the mapping from URs to surface forms, once you're there it's easy to go back.

Overall, rejecting URs simply isn't a coherent position to take.
One has to reject

1. the mathematical truth that mappings can be factorized, or
1. the obvious fact that speakers are aware of at least some relations between surface forms.

At best one can deny the cognitive reality of URs, but that is a weak point because, as always, relating grammatical specifications to the observed performance systems is a very hard problem.
And even if one could do that, it does not undermine the validity of work that uses URs.
That would only be the case if every component of a theory must be cognitively real in order for the theory as a whole to be cognitively real.
But that amounts to hardcore [atomism]({filename}2019-05-20_graf_talking-past.md).
Based on my own experience, phonologists and morphologists are increasingly hesitant to make large cognitive commitments.
So cognitive atomism can't be what's driving the push against URs, and I can't think of anything else that would be a valid argument.
