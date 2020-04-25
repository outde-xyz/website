---
title: >-
    Just your regular regular expression
authors:
    - Thomas Graf
date: 2020-04-24
tags:
    - coding
    - fun allowed
    - methodology
---

<!-- START_SUMMARY_BLOCK -->
Outdex posts can be a dull affair, always obsessed with language and computation (it's the official blog motto, you know).
Today, I will deviate from this with a post that's obsessed with, wait for it, computation and language.
Big difference.
Our juicy topic will be regular expressions.
And don't you worry, we'll get to the "and language" part.
<!-- END_SUMMARY_BLOCK -->


## Some simple, boring examples

If you don't know what a regular expression is, think of it as search (or search and replace) on steroids.
If you work with a lot of text files --- surprise, I do --- regular expressions can make your life a lot easier, but they also have a nasty habit of turning into byzantine symbol salad that's impossible to decipher.
Allow me to demonstrate.
Or maybe skip ahead to the next section, this one here is just a slow introductory build-up to the interesting stuff. 

Suppose you want to change every instance of *regular expression* to the shorter *regex*.
If you're like me, you will use `sed` for this, the **s**tream **ed**itor.
Here's the relevant command.

```bash
s/regular expression/regex/g
```

Okay, that's not exactly user-friendly in these days of GUIs and colorful buttons to click on, but it's manageable.
The command breaks down into a few simple components.

1. `s`: substitute
1. `/`: argument separator
1. `regular expression`: anything matching this regular expression should be replaced
1. `/`: argument separator
1. `regex`: replace the match with this string instead
1. `/`: argument separator
1. `g`: do a global replace; that is to say, process the whole line, don't just stop after the first match on the line

Suppose we have the input text below.

(@) A Note on Regular Expressions: Since "regular expression" is a long term, regular expressions are also called regexes.

This will be rewritten as follows.

(@) A Note on Regular Expressions: Since "regex" is a long term, regexs are also called regexes.

Note that in either case the rewriting targets every instance of *regular expression*, even if it is followed by other characters like *s*.
But without `g`, only the first instance of *regular expression* would have been replaced.

(@) A Note on Regular Expressions: Since "regex" is a long term, regular expressions are also called regexes.

As you can see in the examples above, capitalization matters, so by default `regular expression` does not match `Regular Expression`.
We can fix that by specifying alternatives (there's better ways for handling upper and lower case, but then I wouldn't get to demonstrate alternatives).

```bash
s/[Rr]egular [Ee]xpression/regex/g
```

Here `[Rr]egular [Ee]expression` will match *Regular Expression*, *Regular expression*, *regular Expression*, and *regular expression*.
So now we would get this output

(@) A note on regexs: Since "regex" is a long term, regexs are also called regexes.

But these instances of *regexs* are pretty ugly.
Let's extend the match so that it can include an optional *s*.

```bash
s/[Rr]egular [Ee]xpressions\?/regex/g
```

We use `\?` to indicate that the preceding character is optional for the match.
If there is an *s*, include it in the rewriting, otherwise ignore whatever comes after the *n*.
With this, we get yet another output.

(@) A note on regex: Since "regex" is a long term, regex are also called regexes.

We could play this game for a few more rounds, but I think you get the gist.
Now let's look at how quickly regular expressions can get nasty.


## Cranking up the weird

Things have been perfectly reasonable so far.
Just to mix things up a bit, here's a regular expression I use a lot to rewrite things like `**foo**` as `<b>foo</b>` (don't ask why I need to do that, it's a quick hack while the long-term solution is still being worked on).

```bash
s/\*\*\([^*]*\)\*\*/<b>\1<\/b>/g
```

If you're curious, here's how you read that regex:[^1]

[^1]: The second part isn't a regular expression in the original sense of formal language theory because it uses backreferences, which require unbounded copying and simply aren't regular. For the specific rewriting step I'm doing there, it would be trivial to specify a finite-state transducer, though. And the existence of backreferences is an interesting point in its own right: Even though every regex (in the formal language theory sense) can be converted to an equivalent deterministic finite-state automaton, most regex implementations actually use a context-free parsing mechanism --- and once you have that, backreferences are an easy addition. Sometimes, a powerful thing can be more efficient than a very restricted thing.


1. `s`: substitute
1. `/`: argument separator
1. `\*\*`: match \*\*
1. `\(`: start matching group 1
1. `[^*]*`: match any string of 0 or more characters that are not \*
1. `\)`: close matching group 1
1. `\*\*`: match \*\*
1. `/`: argument separator
1. `<b>`: insert \<b\>
1. `\1`: insert the content of matching group 1
1. `<\/b>`: insert \</b\>
1. `/`: argument separator
1. `g`: do a global replace

It actually makes a lot of sense if you come up with it yourself and remind yourself every 5 minutes how it works.
In all other cases, it's a Lovecraftian nightmare that will drive you mad.

But this is just the tip of the iceberg.
True regex wizards can do stuff that is so crazy it tears apart the fabric of reality.
Did you ever wonder how you can match lines of the form `a b c` such that `a + b = c`?
Well, [somebody wrote a `sed` program for that](http://www.drregex.com/2018/11/how-to-match-b-c-where-abc-beast-reborn.html?m=1), because why wouldn't they?
Here's a part of the very first command:

```bash
(?=[-+]?(?:0\B)*+(\d*?)((?:(?=\d+(?:\.\d+)?\ [-+]?(?:0\B)*+(\d*?)(\d(?(4)\4))(?:\.\d+)?\ [-+]?(?:0\B)*+(\d*?)(\d(?(6)\6))(?:\.\d+)?$)\d)++)\b)
```

Don't look at me, I have no clue what's going on here.
But it works, somehow.
If you want to figure it out, it might help to use [desed](https://github.com/SoptikHa2/desed/), a debugger for `sed`.
If you give it a try, please also try this [`sed`-based solution for a shortest path problem](https://tildes.net/~comp/b2k/programming_challenge_find_path_from_city_a_to_city_b_with_least_traffic_controls_inbetween#comment-2run).
I'd really appreciate an in-depth explanation.

Regular expressions weren't designed to handle any of that stuff.
But somebody with way too much time on their hand hunkered down and pushed them to their limits.
It's insane, but it works.
And that's the point that gets me to the bit of linguistics I need as an excuse for showing off some cool regex stuff.


## Regexes in linguistics

The regex examples above show that there is a big difference between what a system can do and what a system can do in a manner that's easily digestible for a human reader.
And that distinction is too often glossed over in linguistics.
The literature is full of claims of the form "proposal X cannot account for phenomenon Y".
And very often, that's not true, just like it isn't true that you can't use regular expressions to calculate a shortest path.
For instance, you don't need copy movement to produce pronounced copies, but oh boy will the grammar look weird.
What these claims actually mean is "proposal X cannot elegantly account for phenomenon Y".
And that's a big difference.

Elegance is a tricky criterion.
For one thing, elegance depends a lot on the specification language.
What may look clunky as a (standard) regular expression may be very elegant as a formula of monadic second-order logic, even though the two are intertranslatable.
And the elegance of a specification language depends a lot on how much has been abstracted away.
Specification X may be better than Y as long as you only have to account for phenomena P, Q, and R, but throw in S and T and all of a sudden Y scales much better and wins.
It's all very fuzzy, very tentative, mostly based on hunches, personal taste, aesthetics.

That's okay.
In general, researchers should do whatever makes them more productive, and in general it is the case that elegance = simplicity = productivity.
But we should acknowledge that this is a methodological criterion.
Lack of elegance is not a knockout argument and does not tell us much about the cognitive reality of a proposal.
Reality might in fact be messy.
Even though that `a + b = c` program is just a one-liner in Python, the human brain might actually be using the [humongous `sed` clusterfuck](http://www.drregex.com/2018/11/how-to-match-b-c-where-abc-beast-reborn.html?m=1).
That doesn't mean our theories have to be ugly --- there's nothing wrong with being better than reality --- but we should be much more cautious with the use of elegance criteria in theory comparison.

And if you think learning considerations provide a natural push towards elegance, may I introduce you to [this lovely regex generator](https://github.com/MaLeLabTs/RegexGenerator) that infers the intended regex from a data sample?
Yes, I only brought up learning so that I could link to that.
