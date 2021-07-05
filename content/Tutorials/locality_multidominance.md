---
title: >-
    The subregular complexity of multidominance trees
authors:
    - Dakotah Lambert
date: 2019-12-18
bibliography: references.bib
series: >-
    The subregular locality zoo
tags:
    - subregular
    - syntax
    - locality
    - strictly local
    - tier-based strictly local
    - Minimalist grammars
    - Merge
    - Move
---

<!-- START_SUMMARY_BLOCK -->
We have seen that Merge and Move are SL and TSL, respectively, when a sentence is represented by a dependency tree.
But that's just one representation.
What happens if we make movement explicit in the structure as well?
<!-- END_SUMMARY_BLOCK -->

## Dependency trees
As has been discussed previously, we'll want to use dependency trees to represent our sentences if we want a subregular analysis.

![Well-formed dependency tree for *the book, somebody gave to Bill*]({static}/img/dakotah/md/dtree-01.svg)

With this kind of representation, Merge is SL~2~ and Move is TSL~2~.

## Multidominance trees
We had to use TSL to account for movement in a standard dependency tree because a mover might be arbitrarily far away from its landing site.
What if we made Move explicit in the same way that Merge is, by adding a new type of edge to our trees?
Each node may then have more than one mother, so the result is a directed acyclic graph (a DAG), but the same kind of reasoning still applies.
Let us modify the example graph from earlier to explicitly show movement:

![*The book, somebody gave to Bill* augmented with explicit Move edges.]({static}/img/dakotah/md/mdtree-01.svg)

We'll use these red dashed edges to represent Move and call them movement-edges.
The other edges are selection-edges.
These trees will be referred to as multidominance dependency trees.

## Merge is still SL~2~ over multidominance dependency trees.
Just like in standard dependency trees, Merge defines a mother-daughter relationship.
If we look only at selection-edges, the characterization of Merge is unchanged from the standard characterization:

Merge constraint

: The category feature of the *i*th selection-daughter *d* from the right must match the *i*th selector feature of the mother of *d*.

For example, we can check the features of the verb and its arguments on our example sentence:

![Checking Merge on the verb]({static}/img/dakotah/md/mdtree-02.svg)

The verb has the right number and type of daughters, so that is a valid configuration.
It is easy to check each of the other 2-windows and show that this is indeed a valid construction.

## What about Move?
We could try exactly the same kind of constraint for Move as we had for Merge:

Move constraint

: The licensee feature of the *i*th movement-daughter *d* from the right must match the *i*th licensor feature of the mother of *d*

One problem with this definition is that it fails to account for multiple movements by a single lexical item, but we'll go with it for now and come back to that issue later.
It seems to work fine for our example sentence.

![Checking Move]({static}/img/dakotah/md/mdtree-01.svg)

The top^+^ of C corresponds to the top^-^ of "the", and the nom^+^ on T corresponds to the nom^-^ of "somebody".
So that's it, done, right?
Wrong.
Let's look at a slightly more complex sentence:

![Well-formed dependency tree for *John thinks that Mary left*]({static}/img/dakotah/md/dtree-02.svg)

Seems fine, let's just toss in some movement edges that satisfy that rule:

![An ill-formed derivation that satisfies this Move constraint]({static}/img/dakotah/md/mdtree-03.svg)

Oh.
Oh no.
That's not what we want at all!
Can we try again?

![The well-formed derivation for that example]({static}/img/dakotah/md/mdtree-04.svg)

Much better.
But how do we allow this one but disallow the other one?

## Move is still TSL~2~ over multidominance dependency trees.
Well, SL~2~ didn't work.
And since there can be arbitrarily much distance between a mover and its landing site, it's unlikely a larger window size will help us any.
Let's try TSL.

Move constraint (revised)

: For every movement feature f, the following two conditions must hold of every node on the f-tier.

  1. If the node carries an f^-^ feature, then it must have a movement-mother carrying an f^+^ feature
  1. If the node carries and f^+^ feature, then it must have exactly one movement-daughter carrying an f^-^ feature.

Alright, let's look at the nom tier of that complex example sentence.
We'll use the normal red dashed lines for the movement we want, and we'll throw in some blue dot-dashed lines to represent the other one.

![Two movement options]({static}/img/dakotah/md/mdtree-05.svg)

Turns out that characterization wasn't quite enough; either the red dashed edges or the blue dot-dashed edges represent valid movements under these rules.
But we note that with the intended movement, the movement-mother is the same as the selection-mother.
Let's add that as a constraint to the rule:

Move constraint (final)

: For every movement feature f, the following two conditions must hold of every node on the f-tier.

  1. If the node carries an f^-^ feature, then it must have a movement-mother carrying an f^+^ feature that is also its selection-mother.
  1. If the node carries an f^+^ feature, then it must have exactly one movement-daughter carrying an f^-^ feature that is also a selection-daughter.

## Multidominance gains us nothing
This requirement that the movement-edges and selection-edges overlap simply enforces a standard tree structure rather than an arbitrary DAG structure.
We already know that the sentence must be coded in single-movement normal form (SMNF) for these standard trees for the TSL characterization of movement to hold.
In conclusion, explicitly marking movement with new edges in a dependency tree offers no advantages in terms of subregular complexity.
It seems that the only reason you might want to use multidominance trees, then, is if you want the locality for other reasons, such as the Spec-Head analysis of agreement.
