---
title: >-
    Gradience
authors:
    - Thomas Graf
date: 2020-04-28
tags:
    - phonology
    - syntax
    - algebra
    - gradience
---

<!-- START_SUMMARY_BLOCK -->
Omer has a [great post on gradience in syntax](https://omer.lingsite.org/blogpost-on-so-called-degrees-of-grammaticality/).
I left a comment there that briefly touches on why gradience isn't really that big of a deal thanks to **monoids** and **semirings**.
But in a vacuum that remark might not make that much sense, so here's some more background.
<!-- END_SUMMARY_BLOCK -->

## Gradience in the broad sense

My central claim is that linguists' worries about gradience are overblown because there isn't that much of a difference between categorical systems, which only distinguish between well-formed and ill-formed, and gradient systems, which have more shades of gray than that.
In practice, gradient systems are usually probabilistic, but there's no need for that.
The familiar system of rating sentences as well-formed, `?`, `??`, `?*`, and `*` would also be gradient.
This is an important fact that's frequently glossed over.
I really wish researchers wouldn't always jump right to probabilistic systems when they want to make something gradient.
Sure, probabilities are nice because they are easy to extract from the available data, but that doesn't mean that this is the right notion of gradience.
But whatever, it doesn't matter for this post because what I have to say applies to all gradient systems, whether they're probabilistic or not. 


## A formula for categorical grammars

Let's start with a very simple example in the form of a [strictly local grammar]({static}Tutorials/locality_sltsl.md).
SL grammars are usually negative, which means that they list all the *n*-grams that must not occur in a string.
But for the purposes of this post, it is preferable to convert the negative grammar into an equivalent positive grammar, which lists all the *n*-grams that may occur in a string.
For example, the positive SL-2 grammar $G$ below generates the language $(ab)^+$, which contains the strings $\mathit{ab}$, $\mathit{abab}$, $\mathit{ababab}$, and so on.

(@) **Positive SL-2 grammar for $\mathbf{(ab)^*}$**  
    $\{ \mathit{\$a}, \mathit{ab}, \mathit{ba}, \mathit{b\$} \}$

Now let's consider how one actually decides whether a given string is well-formed with respect to this grammar.
There's many equivalent ways of thinking about this, but right now we want one that emphasizes the algebraic nature of grammars.

Suppose we are given the string $\mathit{abab}$.
As always with an SL grammar, we first add edge markers to it, giving us $\mathit{\$abab\$}$.
That's just a mathematical trick to clearly distinguish the first and last symbol of the string, don't worry about it.
The SL grammar decides the well-formedness of the string based on whether the bigrams that occur in it are well-formed.
Those bigrams are (including repetitions)

1. $\mathit{\$a}$,
1. $\mathit{ab}$,
1. $\mathit{ba}$,
1. $\mathit{ab}$,
1. $\mathit{b\$}$.

We can write this as a single formula.

$$G(\mathit{\$abab\$}) := f(\$a) \otimes f(ab) \otimes f(ba) \otimes f(ab) \otimes f(b\$)$$

This looks fancy, but I haven't really done anything substantial here.
Let's break this formula down into its components:

- $G(\mathit{\$abab\$})$ is the value that the grammar $G$ assigns to the string $\mathit{\$abab\$}$.
- $:=$ means "is defined as".
- $f$ is some mystery function that maps each bigram to some value.
- $\otimes$ is another mystery function that combines the values produced by $f$.

All I'm saying is that if we want to know whether our SL grammar $G$ considers $\mathit(\$abab\$)$ well-formed, then we do this by first mapping each bigram in the string to some value and the computing a composite value from the values of all bigrams.
The only reason this looks weird is because I haven't told you what $f$ and $\otimes$ are.

The answer is, they can be lots of things.
But here is one system that will work for a categorical grammar.
First, $f$ maps a bigram $b$ to $1$ if it is a member of $G$, which means that $G$ lists $b$ as a licit bigram.
If $b$ is not a licit bigram, $f$ maps it to $0$.

$$
f(b) :=
\begin{cases}
1 & \text{if } b \in G\\
0 & \text{otherwise}
\end{cases}
$$

Let's do this for the formula above.

$$
\begin{align*}
G(\mathit{\$abab\$}) := & f(\$a) \otimes f(ab) \otimes f(ba) \otimes f(ab) \otimes f(b\$)\\
                      = & 1 \otimes 1 \otimes 1 \otimes 1 \otimes 1\\
\end{align*}
$$

Compare this to the formula for the illicit string $\mathit{\$abba\$}$.

$$
\begin{align*}
G(\mathit{\$abba\$}) := & f(\$a) \otimes f(ab) \otimes f(bb) \otimes f(ba) \otimes f(a\$)\\
                      = & 1 \otimes 1 \otimes 0 \otimes 1 \otimes 0\\
\end{align*}
$$

Notice how we get $1$ or $0$ depending on whether the bigram is licit according to grammar $G$.
Now we just need to know what $\otimes$ does.
Again there's equivalent multiple choices. 
But hey, let's keep it simple, let's say $\otimes$ is multiplication, that will do.

$$
\begin{align*}
G(\mathit{\$abab\$}) := & f(\$a) \otimes f(ab) \otimes f(ba) \otimes f(ab) \otimes f(b\$)\\
                      = & 1 \otimes 1 \otimes 1 \otimes 1 \otimes 1\\
                      = & 1 \times 1 \times 1 \times 1 \times 1\\
                      = & 1\\
\end{align*}
$$
$$
\begin{align*}
G(\mathit{\$abba\$}) := & f(\$a) \otimes f(ab) \otimes f(bb) \otimes f(ba) \otimes f(a\$)\\
                      = & 1 \otimes 1 \otimes 0 \otimes 1 \otimes 0\\
                      = & 1 \times 1 \times 0 \times 1 \times 0\\
                      = & 0\\
\end{align*}
$$

Tada, the well-formed string gets a 1, the ill-formed string a 0, just as intended.
Quite generally, any string that contains at least one illicit bigram will be mapped to 0 because whenever you multiply by 0, you get 0.
The only way for a string to get mapped to 1 is if only consists of well-formed bigrams.
This is exactly the intuition we started out with: a positive grammar deems a string well-formed iff it contains no illicit *n*-grams.


## A formula for gradient grammars

Now here comes the crucial twist: the formula above also works for gradient grammars, we just have to change $f$ and $\otimes$.
If we use probabilities, we can even keep $\otimes$ the same.
The math works exactly the same for categorical and probabilistic grammars.

First, let's make our example grammar probabilistic by assigning each bigram a probability.
I'll use completely random numbers here, in the real world those probabilities would usually come from a corpus.

(@) **Probabilistic SL-2 grammar for $\mathbf{(ab)^*}$**  
    $\{ \mathit{\$a}: 1.0, \mathit{ab}: 1.0, \mathit{ba} .75, \mathit{b\$} .25\}$

Our formula stays exactly the same, except that $f$ now gives us the probability of a bigram according to $G$.
If there is none listed, the probability is 0.

$$
\begin{align*}
G(\mathit{\$abab\$}) := & f(\$a) \otimes f(ab) \otimes f(ba) \otimes f(ab) \otimes f(b\$)\\
                      = & 1 \otimes 1 \otimes .75 \otimes 1 \otimes .25\\
                      = & 1 \times 1 \times .75 \times 1 \times .25\\
                      = & .1875\\
\end{align*}
$$
$$
\begin{align*}
G(\mathit{\$abba\$}) := & f(\$a) \otimes f(ab) \otimes f(bb) \otimes f(ba) \otimes f(a\$)\\
                      = & 1 \otimes 1 \otimes 0 \otimes .7 \otimes 0\\
                      = & 1 \times 1 \times 0 \times .7 \times 0\\
                      = & 0\\
\end{align*}
$$

It's exactly the same mechanism.
Nothing here has changed except the values.
The basic mechanisms of the grammar remain unaltered, in particular how the value of the whole is computed from the values of its parts.

What if we want to do a trivalent system, with well-formed, borderline, and ill-formed?
We could model that by assigning the values $1$, $.5$, and $0$, and a coarser version of multiplication that rounds in specific ways.
But that's lame, so let's do something nicer instead.
Our three values are $1$, $?$, $*$; and $\otimes$ is replaced by an operation that always picks the less licit value:

|              | $\mathbf{1}$ | $\mathbf{?}$ | $\mathbf{*}$ |
| --:          | :-:          | :-:          | :-:          |
| $\mathbf{1}$ | $1$          | $?$          | $*$          |
| $\mathbf{?}$ | $?$          | $?$          | $*$          |
| $\mathbf{*}$ | $*$          | $*$          | $*$          |

The grammar would have to specify for each bigram whether its value is $1$, $?$, or $*$, and we would get that value via $f$.
But the overall formula once again stays the same.
We compute the value of the whole string from the values of the bigrams.

We can even move beyond anything resembling well-formedness.
Suppose that $f$ maps each bigram $b$ to the singleton set $\{b\}$ that contains only $b$.
And now let's instantiate $\otimes$ as $\cup$, which is union of sets.
Then the formula above gives us for each string the set of bigrams that occur in it.

The general upshot is this: a grammar is a mechanism for determining the values of the whole from values of its parts.
The difference between grammars is what parts they look at and how they relate them to each other.
Basically, the overall shape of the formula they use for computing $G(o)$ for some object $o$.
The shape of this formula is what separates an SL grammar from a TSL grammar, an SP grammar, or a finite-state automaton.

But that's not what the categorical VS gradience divide is about.
That only kicks in once you have determined the overall shape of the formula and need to define $f$ and $\otimes$.
But for anything a linguist would like to do, the resulting system will always form a particular kind of algebraic structure that's called a **monoid**.
I won't bug you with [the mathematical details of monoids](https://en.wikipedia.org/wiki/Monoid).
Whether you prefer a categorical system or a gradient system, rest assured there's a suitable monoid for that.
And that's all that matters.
That's why linguists shouldn't worry about the categorical VS gradience divide --- linguistic insights are about the overall shape of the formula, not about plugging in specific operators.


## From string to trees: semirings

Okay, there's one minor complication that I'd like to cover just to cross all *t*s and dot all *i*s.
If you're already worn out, just skip ahead to the wrap-up.

Beyond the pleasant valleys of string land lies the thicket of tree land.
In tree land, things can get a bit more complicated depending on what your question is.
They don't necessarily do so, it really depends on what kind of value you're trying to compute.

If you just want to know whether a specific tree is well-formed, nothing really changes.
Take your standard phrase structure grammar.
A rewrite rule of the form `S -> NP VP` is a tree bigram where the root is `S` and the daughters are `NP` and `VP`.
Just like we can break down a string into its string bigrams, we can break down a tree into its tree bigrams.
And the value of the whole tree is computed by combining the values of its tree bigrams.
With more expressive formalisms like MGs, things are once again more complicated, just like a finite-state automaton uses a more complicated formula in string land than the one for SL grammars above.
But the general principle remains the same: once you have a formula for how the parts interact, you can plug in the operators you want.
As before, we can switch between gradient and categorical systems by tweaking the values of $f$ and $\otimes$, under the condition that this still gets us a monoid.

I think this is actually enough for syntax.
But perhaps you want to talk about the value of a string, rather than a tree.
This is a more complex value because one string can correspond to multiple trees.
For instance, in probabilistic syntax the probability of the string

(@) I eat sushi with edible chopsticks.

is the **sum** of the probabilities of two distinct trees:

(@) [I eat [sushi with edible chopsticks]]
(@) [I [[eat sushi] [with edible chopsticks]]

So $\otimes$ by itself is not enough, there is yet another operation.
For probabilistic grammars it's $+$, but we may again replace it with a more general mystery operation $\oplus$.
The job of $\oplus$ is to combine all the values computed by $\otimes$.
Like $\otimes$, $\oplus$ has to yield a monoid of some kind, and the combination of $\oplus$ and $\otimes$ has to form a **semiring**.
Again I'll completely [gloss over the math](https://en.wikipedia.org/wiki/Semiring).
Let's focus only on the essential point: once again the split between categorical systems and gradient systems is not very large because either way we end up with a semiring.
The nature of the grammar stays the same, only the system for computing compound values uses different functions and operators.

You might be wondering what a categorical grammar looks like from the semiring perspective.
What is the mysterious operation $\oplus$ in that case?
It can't be addition because $1 + 1$ would give us $2$, which isn't a possible value in a categorical system.
No, with categorical systems, $\oplus$ behaves like logical *or*: it returns 1 if there is at least one 1.
Suppose, then, that we want to know if some string *s* is well-formed according to some categorical grammar $G$.
Here is how this would work in a very simplified manner:

1. We look at all possible trees that yield the string *s*, even if those strings are ill-formed according to $G$.
1. We use $\otimes$ to compute the compound value for each tree.
   As before, $\otimes$ is multiplication (but it could also be logical *and*, if you find that more pleasing).
   Well-formed tress will evaluate to $1$, ill-formed ones to $0$.
1. We then use $\oplus$, i.e. logical *or*, to combine all those compound values into a single value for the string *s*.
   Then *s* will get the value $1$, and hence be deemed well-formed, iff there is at least one well-formed tree that yields *s*.

Okay, that's not how we usually think about well-formedness.
We view the grammar as a system for specifying a specific set of well-formed trees, rather than a function that maps every logically conceivable tree to some value.
But as you hopefully remember from your semantics intro, there is no difference between a set and its characteristic function.
The procedure above treats the grammar as the characteristic function of the set of well-formed trees.
Most of the time that's not very illuminating for linguistics, but when it comes to the split between categorical and gradient it is really useful because it reveals the monoid/semiring structure of the grammar formalism.


## Wrapping up: Don't worry, be happy

Monoids and semirings are a very abstract perspective of grammars, and I rushed through them in a (failed?) attempt to keep the post at a manageable length.
But behind all that math is the simple idea that syntacticians, and linguists in general, don't need to worry that a categorical grammar formalism is somehow irreconcilable with the fact that acceptability judgments are gradient.
Even if don't factor that out as a performance phenomenon, even if we want to place it in the heart of grammar, that does not require us to completely retool our grammar formalisms.
The change is largely mathematical in nature and doesn't touch on the things that linguists care about.
Linguists care about representations and how specific parts of those representations can interact.
In the mathematical terms I used in this post, those issues are about the shape of the formula for computing $G(o)$ for some object $o$.
It is not about the specific values or operators that appear in the formula.

In many cases, there's actually many different operators that give the same result.
We interpreted $\otimes$ as multiplication for categorical SL grammars, but we could have also used logical *and* or the *min* function.
They all produce exactly the same values.
No linguist would ever worry about which one of those functions is the right choice.
The choice between categorical, probabilistic, or some other kind of gradient system isn't all that different.
Again you are needlessly worrying about the correct way of instantiating $f$, $\otimes$, and possibly $\oplus$.

That's not to say that switching out, say, a categorical semiring for a probabilistic one is a trivial affair.
It can create all kinds of problems.
But those are mathematical problems, computational problems, they are not linguistic problems.
It's stuff like computing infinite sums of bounded reals.
It's decidedly not a linguistic issue.
So don't worry, be happy.
