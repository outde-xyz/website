---
title: >-
    Logical transductions: Bats, butterflies, and the paradox of an almighty God
authors:
    - Thomas Graf
date: 2020-09-21
bibliography: references.bib
series: >-
    Logical transductions
tags:
    - formal language theory
    - transductions
    - subregular
    - first-order logic
---

<!-- START_SUMMARY_BLOCK -->
Since we recently a had [a post about Engelfriet's work on transductions and logic]({filename}/Discussions/2020-09-02_graf_engelfriet-tribute.md), I figured I'd add a short tutorial that combines the two and talks a bit about **logical transductions**.
I won't touch on concrete linguistic issues in this post, but I will briefly dive into some implications for how MGs push PF and LF directly into "syntax" (deliberate scare quotes).
I also have an upcoming post on representations and features that is directly informed by the logical transduction framework.
So if you don't read anything here unless it engages directly with linguistics, you might still want to make an exception this time, even if today's post is mostly logic and formulas.
<!-- END_SUMMARY_BLOCK -->

## Logic for structure

In linguistics, logic is usually kept to its semantic habitat, rarely venturing out into the domain of syntax or phonology.
There are some exceptions, like [this phonology textbook](https://mitpress.mit.edu/books/phonology) by Alan Bale and Charles Reiss, but they are, as I said, exceptions.
That's unfortunate, logic is actually a great tool for talking about structures.
It's basically a more rigorous form of constraint-based formalisms in linguistics (old-school constraint-based, not ranked constraints as in OT).

I'll explain in a minute how exactly this works, but the key insight I want to relate to you right-away:
from the perspective of mathematical logic, talking about a structure isn't all that different from talking about a transduction that changes this structure into something else.
The common dichotomy between structures one the one hand and processes that manipulate those structures on the other hand just falls apart, like chlorine under sun light.

But let's not get too far ahead of ourselves.
For now, our focus is still on the more standard case of using logic to talk about structure.
Consider the following formula of first-order logic: 

$$
\forall x [a(x) \vee b(x) \vee c(x)]
$$

Without further context, this states that every $x$ has to satisfy predicate $a$, or predicate $b$, or predicate $c$.
But we can interpret it as a claim about graph structures.
Our domain of quantification is the nodes of the graph.
And we say that $a(x)$ is true iff node $x$ has the label $a$.
Given the same interpretation for $b(x)$ and $c(x)$, the formula above is a constraint that require every node to carry label $a$, or $b$, or $c$, or some combination of those three.

We can tighten this with another constraint to ensure that every node has exactly one label.

$$
\begin{align*}
\forall x \big [
                 & (a(x) \rightarrow \neg b(x) \wedge \neg c(x)) \wedge\\
                 & (b(x) \rightarrow \neg a(x) \wedge \neg c(x)) \wedge\\
                 & (c(x) \rightarrow \neg a(x) \wedge \neg b(x))
\big ]\\
\end{align*}
$$

Any graph in which both formulas a true is a **model** of this set of formulas.
Right now our logic is still too limited to do anything interesting, so let's add a bit of machinery to talk about how the nodes in a graph may be arranged.

Every graph defines a **reachability relation** $R$ $y$ is reachable from $x$ iff there is a sequence of edges that takes us from $x$ to $y$.
In syntactic trees, reachability would correspond to (proper) dominance.
We enrich our first-order logic with predicate $\triangleleft^+$ such that $x \triangleleft^+ y$ iff $y$ is reachable from $x$.
Based on this, we can also define a predicate $\triangleleft$:

$$
x \triangleleft y \Leftrightarrow
    x \triangleleft^+ y \wedge
    \neg \exists z [x \triangleleft^+ z \wedge z \triangleleft^+ y]
$$

This new predicate $\triangleleft$ only holds between nodes that are reachable via a single edge, rather than a sequence of two or more edges.
In syntactic trees, $\triangleleft$ would be the mother-of relation.

Note that $\triangleleft$ and $\triangleleft^+$ do not have equal status in our logic.
Whereas $\triangleleft^+$ must be stipulated as a primitive of our first-order language, $\triangleleft$ comes for free as it can be defined with the primitives that are already available in first-order logic:

- the universal quantifier $\forall$ and the existential quantifier $\exists$,
- the propositional connectives ($\neg$, $\wedge$, $\vee$, $\rightarrow$, $\leftrightarrow$),
- the binary predicate $\triangleleft^+$ for the reachability relation,
- three unary predicates $a$, $b$, and $c$ that we interpret as node labels.

So $\triangleleft$ is more like a LaTeX macro in that we can treat it as syntactic sugar to save us some typing.
Wherever you see a statement of the form $x \triangleleft y$ in this post, you can substitute the right-hand side of the formula above:

$$x \triangleleft^+ y \wedge \neg \exists z [x \triangleleft^+ z \wedge z \triangleleft^+ y]$$

Doing so yields a first-order formula that only uses the primitives listed above.
The difference between a primitive and a "macro" may seem overly pedantic, but it will be really important once we start talking about transductions.

Okay, so now that we have $\triangleleft^+$, and by extension $\triangleleft$, what are we gonna use it for?
Well, for instance, we can require every well-formed graph to be a string.

$$
\begin{align*}
\forall x,y,z \big [ &
      (x \triangleleft y \wedge x \triangleleft z \rightarrow y = z) \wedge\\
    & (x \triangleleft z \wedge y \triangleleft z \rightarrow x = y) \wedge\\
    & (x \triangleleft y \rightarrow \neg (x = y))
\big ]\\
\end{align*}
$$

This says that

- no node can have more than one outgoing edge ("if $x$ is related to $y$ and $z$, then $y$ and $z$ are the same node"), and
- no node can have more than one incoming edge ("if $x$ and $y$ are both related to $z$, then $x$ and $y$ are the same node"), and
- no node can be related to itself ("if $x$ is related to $y$, then $x$ and $y$ must be distinct nodes").

And now we could add yet another constraint so that the strings must consist of 0 or more iterations of *abc*, e.g. *abcabcabc* or the empty string $\varepsilon$.
To do this, we once again throw in some syntactic sugar:

$$
\mathrm{leftedge}(x) \Leftrightarrow
   \neg \exists y [y \triangleleft x]
$$

$$
\mathrm{rightedge}(x) \Leftrightarrow
   \neg \exists y [x \triangleleft y]
$$

These predicates check whether a node is the left edge or right edge of the string, which is the same as saying that the node has no predecessor or successor, respectively.
With these two additional predicates at our disposal, we now formulate the constraint that limits the strings to iterations of *abc*.

$$
\begin{align*}
\forall x \big [
    & (\mathrm{leftedge}(x) \rightarrow a(x)) \wedge\\
    & (\mathrm{rightedge}(x) \rightarrow c(x)) \wedge\\
    & (a(x) \rightarrow \exists y [x \triangleleft y \wedge b(y)]) \wedge\\
    & (b(x) \rightarrow \exists y [x \triangleleft y \wedge c(y)]) \wedge\\
    & (c(x) \wedge \neg \mathrm{rightedge}(x) \rightarrow \exists y [x \triangleleft y \wedge a(y)])
\big ]\\
\end{align*}
$$

In plain English: the left edge must be *a* (if it exists), the right edge must be *c* (if it exists), *a* must be followed by *b*, *b* must be followed by *c*, and non-final *c* must be followed by *a*.

Hopefully you'll agree with me that this is all fairly intuitive, even if first-order logic isn't the most succinct description language around.
Putting aside cumbersome notation, it's really just the familiar system of defining well-formed structures in terms of a finite collection of inviolable constraints. The only tweak is that the constraints are expressed in logic instead of plain English or some other metalanguage.
This system is very flexible in that it allows us to talk about arbitrary graph structures, be they strings, trees, multi-dominance trees, DAGs, or more general types of graphs.
In fact, my focus on strings in this post is really just a matter of keeping the exposition simple;
the first linguistic applications of this approach were all about trees [@Blackburn.etal93; @Backofen.etal95; @CornellRogers98; @Rogers98], and strings have only recently become more of a focus as part of the computational conquest of the phonological hinterland.


## Transductions as parasitic structure

Alright, now we have a basic understanding of how first-order logic (or rather, any logic) can be used to talk about structure.
As our concrete example, we have bunch of first-order constraints whose models are graphs that form strings of the form $\mathit{abc}^*$ (0 or more iterations of $\mathit{abc}$).
Now let's see how we go from this to using logic to talk about transductions, i.e. transformations of an input structure into some output structure.

Let's consider a particular graph, say, the one for *abcabcabcabc*.
Here's a depiction of this example that emphasizes the graph-based view of this string by

- arranging the nodes in a plane instead of the usual left-to-right order for strings, and
- listing each node with its numerical index; the label is attached in the top left corner to highlight that it is a specific predicate that holds of the node with that index.

![The string *abcabcabcabc* viewed through the lens of logic]({static}/img/thomas/tutorial_logicaltransductions/abc4.svg)

If you follow along the edges, you'll still get the string *abcabcabcabc*, so this is really just a matter of presentation, not content.

Now remember that we can also define all kinds of syntactic sugar or macros, like $\mathrm{leftedge}$, $\mathrm{rightedge}$, or $\triangleleft$.
Let me show you a very different kind of predicate we could have defined.
Spoilers: although this predicate only piggybacks on our existing structure, it essentially defines a new graph --- the output of a specific transduction.

First, we will need a predicate that connects the closest nodes that share a specific label.
Again we do not need to add this predicate to our language, it's just a convenient shorthand for a more complex formula.

$$
x \prec_a y \Leftrightarrow
   x \triangleft^+ y \wedge
   a(x) \wedge
   a(y) \wedge
   \neg \exists z [x \triangleleft^+ z \wedge
                   z \triangleleft^+ y \wedge
                   a(z)]
$$

In our example string *abcabcabcabc*, it holds that $0 \prec_a 3$ as both $0$ and $3$ are labeled $a$, and $3$ is the closet node that is reachable from $0$.
On the other hand, $0 \prec_a 5$ would be false because $5$ is not labeled $a$, $1 \prec_a 3$ would be false because $1$ is not labeled $a$, and $0 \prec_a 6$ is false because $3$ occurs between the two and is also labeled $a$.
We define analogous predicates $\prec_b$ and $\prec_c$ for labels $b$ and $c$, respectively.

Next, we will also relativize $\mathrm{leftedge}$ and $\mathrm{rightedge}$ to labels so that they pick out the first and last node with a specific label, respectively.
Here is what this looks like for $a$:

$$
\mathrm{leftedge}_a(x) \Leftrightarrow
   \neg \exists y [y \prec_a x]
$$

$$
\mathrm{rightedge}_a(x) \Leftrightarrow
   \neg \exists y [x \prec_a y]
$$

As you can see, that's almost the same formula as for $\mathrm{leftedge}$ and $\mathrm{rightedge}$, except that we have replaced $\triangleleft$ with $\prec_a$.
But since $\prec_a$ can be defined in terms of our logical primitives, this is a-okay, we haven't expanded the language in any way.
Okay, all the preparatory work has been done, time to move on to the main course:

$$
\begin{multline*}
x \blacktriangleleft y \Leftrightarrow
    x \prec_a y \vee
    x \prec_b y \vee
    x \prec_c y \vee
    (\mathrm{rightedge}_a(x) \wedge \mathrm{leftedge}_b(x)) \vee
    (\mathrm{rightedge}_b(x) \wedge \mathrm{leftedge}_c(x))
\end{multline*}
$$

What does this do?
Well, this is one of those cases where a picture says more than a thousand words.

![The relation $\blacktriangleleft$ in the string *abcabcabcabc*]({static}/img/thomas/tutorial_logicaltransductions/abc4_lexicalorder.svg)

The predicate $\blacktriangleleft$ has added a new order between nodes, depicted here as dashed blue arrows.
Instead of a sequence of triples *abc*, this order first connects all instances of *a*, followed by all *b*s, and finally all *c*s.
If we move through the graph using $\blacktriangleleft$ instead of $\triangleleft$, we get *aaaabbbbcccc* instead of *abcabcabcabc*.

Since the figure is a little cluttered, we'll clear things up a bit by drawing two separate instances of the graph, one using $\triangleleft$ and the other $\blacktriangleleft$.

![Separating the graph into two distinct structures]({static}/img/thomas/tutorial_logicaltransductions/abc4_split.svg)

But wait a second!
What if this isn't just a more convenient presentation, what if we attach a meaning to this?
What if the top figure is the input structure, and the bottom figure is the output structure?
Then we have just carried out a transduction.
From this perspective, our definition of $\blacktriangleleft$ isn't just syntactic sugar, it is a transformation that rearranges the nodes in the structure --- in combination with the constraints we put in place earlier, the formula for $\blacktriangleleft$ defines a mapping from strings of the form $\mathit{abc}^n$ to strings of the form $a^n b^n c^n$!

The first time I came across this idea --- in @Morawietz03, which builds on @Monnich99 and subsequent work --- it blew my mind.
Strictly speaking, all we have is a single structure with multiple relations defined over it.
But if we attach a specific interpretation to this, treating some as input relations and others as output relations, we get a transduction.
Ignore $\blacktriangleleft$ and you get an input structure, ignore $\triangleleft$ and you get an output structure.
We are translating a static structure into a dynamic process.
This is the key insight behind logical transductions: inputs and outputs are just specific ways of interpreting a single structure, and the difference between the two is what we analyze as a transformation.


## The paradoxical power of interpretation

This static picture of transductions might strike you as very unintuitive, but oh boy, you haven't seen yet just how unintuitive it can get.
Here's three mathematical facts for you to chew on:

1. A stringset can be defined in first-order logic with $\triangleleft^+$ iff it is star-free.
1. The stringset $a^n b^n c^n$ is mildly context-sensitive.
1. The star-free stringsets are a proper subclass of the mildly context-sensitive stringsets.

These three things do not seem to fit together.
We just used first-order logic to define all graphs that produce strings of the form $a^n b^n c^n$.
But this should be impossible because first-order logic can only produce star-free stringsets, and $a^n b^n c^n$ is not star-free.
This is a paradoxical situation.
It reminds me of the paradox of an almighty God: God can be almighty only if (s)he can create a rock even (s)he cannot lift, but then (s)he cannot be almighty.
The only way to resolve it is to say that God is so almighty (s)he can do things even (s)he cannot do.
Just like first-order logic apparently can do things first-order logic cannot do.

At least the paradox of first-order logic can be resolved, though.
The important thing to realize is that our collection of first-order formulas didn't actually define the stringset $a^n b^n c^n$, it defined graph structures with multiple relations over them, including $\triangleleft$ and $\blacktriangleleft$.
In order to get $a^n b^n c^n$ from this collection of graph structures, we have to use a yield function that maps the graph to a specific string.
In the case of $a^n b^n c^n$, the yield function uses $\blacktriangleleft$, which is actually just syntactic sugar for an intricate collection of formulas using $\triangleleft^+$.
The yield function converts $\blacktriangleleft$ from a parasitic relation defined over $\triangleleft^+$ into a structural primitive, and that conversion doesn't come for free.
The additional computation that goes into this is what allows us to go beyond the star-free boundary into the realm of mild context-sensitivity.

If you still find this confusing, here's an analogy.
Clearly a lot of computation has to go into assigning a tree structure to a string, that's why parsing is hard.
But the opposite is true, too: flattening a tree into a string doesn't come for free.
It often seems trivial to us because phrase structure trees make it very easy to compute the string, but yield mappings can be a lot more complex (the mapping from MG derivation trees to strings, for instance).
If you want to flatten a graph into a string, there's a lot of computation to be done.
Our first-order logic doesn't address the computations that go into the yield function.
The computation is hidden away in the interpretative step of considering only some relations for the output structure.
This process takes effort, just like I had to do some work to split the figure with both $\triangleleft$ and $\blacktriangleleft$ into two figures with distinct relations.


## Interfaces in static syntax: Bats and butterflies

As you might've guessed, I'm a big fan of the logical view of transductions, and I have used it a lot in my work on MGs.
One thing that sometimes comes up in connection with MGs is how they handle stuff that happens after syntax, at PF and LF.
My preferred answer is that they don't, because there's nothing special to handle there: It's syntax all the way down.
When linguists talk about interfaces, in my mind they are actually talking about specific ways of interpreting a single structure that already encodes all necessary information.
It's like syntax produces a Rorschach test image and depending on whether we look at it with PF googles or LF googles we see a bat or a butterfly.
It's all just a matter of interpretation.

Think about it.
In standard Minimalist syntax, we assume that there are pipelines that take some syntactic structure as input and then rewrite it into something the interfaces can work with.
PF is one pipeline (or the end-point of that pipeline), LF another.
So essentially we are dealing with two transductions that take a syntactic structure as input and produce some output structure for interface consumption.
But what does that mean from the logical perspective?
It means that we are defining ancillary predicates over our syntactic structure, some of which encode LF information, others PF information.
All we have is a single static representation with all kinds of relations defined over it.
Some relations are shared between the interfaces, others only one interface pays attention to.
Now we can make an ontological split and say "hey, relations X, Y, and Z are 'syntax', and the rest is post-syntactic", but from the perspective of logical transductions there's no bite to it.
You have primitive relations, you have parasitic relations that piggyback on them, and you have tons of different yield functions to choose from, some of which are empirically viable and others are not.
The formalism defines the static structure will all relevant relations, including the parasitic ones.
There is no formal split between syntax on the one hand and interfaces on the other, the action all happens in the syntactic formalism and the interfaces are just yield functions that filter out some parts of the structure (did I mention that this dovetails nicely with the [bi-morphism perspective of the T-model]({filename}2019-05-15_graf_tmodel.md)?).
As I said, it's syntax all the way down.

Now, none of that means that the more traditional view in terms of input-output mappings is wrong.
Quite to the contrary: they are both right!
Dynamic cascades of transformations VS a single static representation, they are different views of the same system.
Asking which one is really true is like asking whether light is a wave or a particle.

But don't we have an encapsulation problem, then?
If it's all in a single structure, can't everything be sensitive to everything, LF to PF, syntax to PF, and so on?
Yes, one thing the logical perspective shows us is that representational encapsulation doesn't get the way done.
And I think that's one of several ways how representations lead us astray in our thinking.
My hunch is that the answer lies in computation, not representation... more on that next time.

## References
