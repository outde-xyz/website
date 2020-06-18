---
title: >-
    LaTeX pet peeves
authors:
    - Thomas Graf
date: 2020-06-25
series: Tex advice
tags:
    - student advice
    - LaTeX
---

<!-- START_SUMMARY_BLOCK -->
Somehow I wound up with five students writing their theses this semester, and you know what this means: lots and lots of reading.
And when reading, I can't help but get riled up every time I see one of my $\LaTeX$ pet peeves.
I also like to read the source files in parallel with the PDF, and I've come across some nightmare-fuel coding in those files.

So, to save my future self's sanity, here's a list of all my LaTeX pet peeves.
Many of them are covered in your average LaTeX tutorial, but people rarely read those cover to cover and instead just go to specific parts that they need to solve whatever problem they're wrestling with.
Compiling it all into a single list might make for a more useful reference.
Future students of mine, read this and adhere to it.
You have been warned!
<!-- END_SUMMARY_BLOCK -->


# Using LaTeX where it isn't needed

Alright, let's start with the most important one: only use LaTeX if it's the best tool for the job.
LaTeX is amazing when you have to do a lot of heavy lifting: bibliographies, references, multi-part documents, math, trees, autosegmental tiers, automata, glossed examples, data plotting, a single document for producing both handouts and slides;
LaTeX handles all of that, um, perhaps not well, but better than any other solution on the market.
Beware, though: with great power comes great responsibility, and a lot of my pet peeves are actually examples of the writer not paying attention to the subtle details of LaTeX that are the source of its power.

Great power also means a certain degree of clunkyness.
For simple jobs, simpler tools are more efficient.
If all you have to show me is a todo list, write that in a markdown dialect and convert it to PDF with [pandoc](https://pandoc.org/).


# Not using labels and references

If I see a hardcoded reference like `Section 1` in the source code, my blood pressure spikes.
The whole point of LaTeX is that you don't have to do these things.
Liberally assign labels, and then use them, e.g. `Section~\ref{sec:some_section}`.

Be systematic with your labels.
For instance, I like the format `\label{type:container_name}`, where type could be

- `cha` for chapters,
- `sec` for sections,
- `ssec` for subsections,
- `fig` for figure,
- `tab` for table,
- `ex` for example.

And container is the name of the containing unit.
If a thesis contains a subsection in a chapter with label `\label{cha:foo}`, then the subsection would get the label `\label{ssec:foo_bar}`.
That system isn't perfect as it creates quite a hassle when I decide to make a subsection its own section, but it provides a rudimentary typing system for the document.

And if you're reference a section that doesn't exist and/or doesn't have a label yet, don't just omit the reference, just use `\ref{type:container_name}` based on what the label should be.
That way, you won't forget to insert the reference later on, and when you finally get around to writing that section, you already have a record of which other sections tie into it.

Oh, and because I've seen this mistake an estimate 328 times by now: labels in a float (figures, tables) must be specified after the caption, not before.


# Not using macros

The whole point of LaTex is to separate content from presentation.
Don't write something like `$\text{the} :: =\mathrm{N} \mathrm{D} -\mathrm{nom}$`.
It's tedious, prone to errors, and lacks semantics.
Just define a bunch of custom macros:

```latex
\newcommand{\featfont}[1]{\ensuremath{\mathrm{#1}}}
\newcommand{\fsel}[1]{\ensuremath{=\featfont{#1}}}
\newcommand{\fcat}[1]{\ensuremath{\featfont{#1}}}
\newcommand{\flcr}[1]{\ensuremath{+\featfont{#1}}}
\newcommand{\flce}[1]{\ensuremath{-\featfont{#1}}}
\newcommand{\mlex}{2}{\ensuremath{\text{#1} :: #2}}
```

With those macros, you can rewrite the code above as `\mlex{the}{\fsel{N} \fcat{D} \flce{nom}}`.
That's easier to read, and it conveys clearly that you're defining a lexical item with selector feature `N`, category feature `D`, and licensee feature `nom`.
And if you decide later on that you want to use a different notation for features, you only have to change the macros.

```latex
\newcommand{\featfont}[1]{\ensuremath{\mathrm{#1}}}
\newcommand{\fsel}[1]{\ensuremath{\featfont{#1}^+}}
\newcommand{\fcat}[1]{\ensuremath{\featfont{#1}^-}}
\newcommand{\flcr}[1]{\ensuremath{\featfont{#1}^+}}
\newcommand{\flce}[1]{\ensuremath{\featfont{#1}^-}}
\newcommand{\mlex}{2}{\ensuremath{\text{#1} :: #2}}
```


# Subscripts

One quirk of LaTeX is that it only provides subscripts in math mode.
So a writer who wants, say, labeled bracketing with subscripts, might try the following code:

```latex
John [$_{VP}$ arrived $t$]
```

This is wrong, wrong, wrong.
In math mode, LaTeX treats each character as a separate mathematical variable and inserts some white space between them.
So `$_{VP}$` is actually interpreted as `$_{V P}$`.
Instead of a single subscript *VP*, you get two subscripts *V* and *P*.

The difference is pretty blatant once you're aware of it.
Here's the output produced from the code above.

$$
\text{John [$_{VP}$ arrived $t$]}
$$

And here's what it should look like:

$$
\text{John [$_\mathit{VP}$ arrived $t$]}
$$

The latter is produced by replacing `$_{VP}$` with `$_\mathit{VP}$`, which now typesets VP as a single variable in math italics.
Alternatively, you could also use `$_\text{VP}$` or `$_\textrm{VP}$` to have the label typeset as normal text.
Quite generally, may I suggest you define a custom macro for the subscripts of labeled brackets?

```latex
\newcommand{\labsub}[1]{\ensuremath{_\text{#1}}}
```

This way, you can change the definition of the macro to fit the layout of your paper.
This separation of code and output is exactly what makes LaTeX so powerful, so make plenty of use of it!
In fact, why don't you just use the following macro for your labeled bracketing:

```latex
\newcommand{\labbrack}[2][\unskip]{[\ensuremath{_\text{#1}} #2]}
```

This macro allows you to produce the output above from `\labbrack{CP}{John \labbrack{VP}{arrived $t$}}`.


# `\ensuremath`

Some of the macros above use a command some of you might not have seen before: `\ensuremath`.
The name tells you exactly what it does: it ensures that its argument is typeset in math mode.
When you need math mode inside a macro, you should always use `\ensuremath`.

Crucially, don't try to do something like the following:

```latex
\newcommand{\labsub}[1]{${_\text{#1}}$}
```

This is a disaster waiting to happen.
If you use this command while you're in already in math mode, then the first `$` will switch you back into text mode and LaTeX will complain that you can't use `_` in text mode.
This doesn't happen with `\ensuremath`: if you're not in math mode, it switches you into math mode, and if you're already in math mode, it keeps you in math mode.


# gb4e's automath

Some of you might say that we don't need any of that because the package `gb4e` redefines `_` so that it can be used in text mode.
This is a bad solution as it breaks tons of packages in weird ways that are difficult to debug.
Just spare yourself the hassle and turn that "feature" off:

```latex
\usepackage{gb4e}
\noautomath
```

And while you're at it, you might also want to add a bit more boilerplate around `gb4e` to make sure it actually loads correctly on recent TeX distros.

```latex
\makeatletter
\def\new@fontshape{}
\makeatother
\usepackage{gb4e}
\noautomath
```

Yes, `gb4e` is pretty broken by now.
But it's still better than linguex in that it actually respects LaTeX's split between commands and environments and doesn't encourage bad coding choices (`\Next` and `\Last` are a bad idea).
Here's hoping somebody comes up with a completely new package, based on tikz matrices.


# Punctuation

Alright, this one is really a major flaw in LaTeX's design, so I don't blame anybody who gets this wrong.
LaTeX makes a distinction between a sentence-ending dot and other uses of dots, in particular as part of an abbreviation.
The former has more whitespace after it to create a visual separation between sentences.
So far so good, that's a nice feature.

The problem is that LaTeX, in a misguided attempt to simplify the writer's life, automatically switches between those two types of dots.
By default, dots after lowercase characters are taken to be sentence-ending, and dots after uppercase characters are not taken to be sentence-ending.
This is a major pain in the butt.
Consider the following example.

```latex
The phrase then moves to the specifier of the CP.
This movement can be driven by various features, e.g. a wh-feature.
```

LaTeX's punctuation rules do exactly the wrong thing here.
The dot after `CP` will be interpreted as part of an abbreviation when it is in fact sentence-ending.
And the dot after `e.g.` will be interpreted as sentence-ending when it is in fact part of an abbreviation.

In order to fix this, we have to hack the code to override LaTeX's default choices.
We can put `\@` in front of a dot that we always want to be sentence-ending, and we can put a backslash before the space right after an abbreviation.

```latex
The phrase then moves to the specifier of the CP\@.
This movement can be driven by various features, e.g.\ a wh-feature.
```

This is just shitty design.


# `~` is your friend

There is actually a third solution for the spacing issue pointed out above.
Instead of adding a backslash before the space, we could have replaced by space with a tilde.

```latex
The phrase then moves to the specifier of the CP\@.
This movement can be driven by various features, e.g.~a wh-feature.
```

This also produces a normal-width space, but it also tells LaTeX that it shouldn't put a linebreak right after the abbreviation.
Abbreviations at the end of a line look rather odd, so I generally put `~` after every abbreviation I use.

It's a very minor thing, but again, once you're aware of it you'll be very annoyed when you see somebody not doing it.


# Ellipsis

Since we're already on the subject of punctuation, `...` is not how you typeset an ellipsis in LaTeX.
The command for that is `\ldots`, and again the difference is in the spacing.
Just compare:

1.  **End of sentence**
    - Three dots: $\text{This sentence ends prematu...}$
    - `\ldots`: $\text{This sentence ends prematu\ldots}$
1.  **Middle of sentence**
    - Three dots: $\text{My favorite numbers are 1, 2, ... and so on}$
    - `\ldots`: $\text{My favorite numbers are 1, 2, \ldots and so on}$


# Quotation marks

My next pet peeve is actually covered early on in every LaTeX tutorial, yet I still see people consistently get it wrong: don't use `"` for quotation marks.
You want `\`\`` for opening quotation marks and `''` (that's two single quotes) for closing quotation marks.
Again the difference in typesetting is immediately apparent:

- Using `"`: $\text{"something"}$
- Using `\`\`` and `''`: $\text{``something''}$

Yes, this is just ridiculous and could easily be handled automatically (many LaTeX editors will do it for you), but LaTeX gonna LaTeX.


# `/` and `\slash` are not the same slash

Another bit of LaTeX voodoo.
While `/` does indeed produce a slash, sometimes it's recommended that you use `\slash` instead.
The difference is that `/` is a non-breaking character, which means that LaTeX isn't allowed to insert a linebreak before or after it.
Sometimes that's a good thing.
You really don't want the CG type `S/NP` to be split across two lines.
But with, say, `consonantal/non-vocalic`, you'll probably get weird spacing if LaTeX isn't allowed to break this up into `consonantal/` and `non-vocalic`.
So even though their output looks the same, `/` and `\slash` don't do the same thing.

Personally, I think it would've been better to have a compositional system where we can use a special marker like `|` to indicate that the preceding symbol is a non-breaking character.
Then `~` would just be a shorthand for a space followed by `|`.
Oh well, the LaTeX code base is 40 years old by now, it's bound to have its quirks.


# `\epsilon` isn't the epsilon you want

You thought we were done with LaTeX curiosities, hmm?

This one is not the mistake I see most often, but that's just because not every paper has a need for the epsilon symbol.
But when it does, there's a good chance it will be the wrong symbol.
For some reason, most LaTeX fonts use a shape for epsilon that doesn't look like the typical epsilon.
They produce $\epsilon$ instead of $\varepsilon$.
If you want $\varepsilon$ instead, you have to use `\varepsilon`.


# ...and < and > aren't tuple brackets

Again this one doesn't show up that often simply because not every paper needs to typeset tuples, but when it's necessary, people get it wrong oh so often.
And in this case, it's not even LaTeX being needlessly obtuse.
Tuple brackets are not the same as $<$ and $>$, they have very different angles: $\langle$ and $\rangle$.
If you want the latter, you have to use `\langle` and `\rangle` (left and right angle).

Tuple brackets also have completely different spacing:

- Using `<` and `>`: $<a, b>$
- Using `\langle` and `\rangle`: $\langle a, b \rangle$

Again I'd suggest using a custom macro to make your life a little easier.

```latex
\newcommand{\tuple}[1]{\ensuremath{\langle #1 \rangle}}
```

You could also use a version with automatic sizing of the tuple brackets, but this will often give you problems if LaTeX needs to insert a linebreak.

```latex
\newcommand{\Tuple}[1]{\ensuremath{\left \langle #1 \right \rangle}}
```


# Math relations and operators

The spacing difference between `<` and `>` on the one hand and `\langle` and `\rangle` on the other is actually an instance of a more general principle.
In math mode, LaTeX distinguishes between normal symbols, operators, and relations, and they each have different spacing properties.
So instead of `a R b`, you should write `a \mathrel{R} b` to get the correct spacing.
If you want `|` to be an operator, you should write `a \mathop{|} b`.
Again it's a good idea to use custom macros for that.

- `a R b`: $a R b$
- `a \mathrel{R} b`: $a \mathrel{R} b$
- `a \mathop{R} b`: $a \mathop{R} b$


# So, many, dashes

Another subtle difference, this time with respect to hyphens and dashens.

- `-` is a hyphen and is used word-internally, e.g. in `sentence-ending`: $\text{sentence-ending}$
- `--` denotes a range, e.g. `pages 55--68`: $\text{pages 55--68}$
- `---` is an em-dash and is used with parentheticals, e.g. `John---as far as I'm aware---did not come home last night`: $\text{John---as far as I'm aware---did not come home last night}$
- `$-$` is a minus and should only be used in equations: $15 - 3$

I also like to add spaces around `---`, and every single copy editor tried to dissuade me from that.
I like the extra space, but I'm sure it's somebody's pet peeve, so, sorry about that.


# Bibtex capitalization

As you might know, your bibtex style automatically handles the capitalization of your references.
But it only works well if

1. your bibtex references are in sentence case, and
2. you explicitly indicate which characters should not be lowercased.

So don't write something like this:

```bibtex
title = {Some paper on MGs}
```

Instead, it should be:

```bibtex
title = {Some Paper on {MG}s}
```

This way, you will get lowercase or sentence case depending on the publisher's stylesheet, and either way `MGs` will stay MGs and won't be lowercased to `mgs`.


# More to come

Okay, this is already a laundry list of things that are easy to miss when writing but leap out at the reader that's aware of them.
But we're not done yet, I have another list that's all about doing figures with [TikZ](https://en.wikibooks.org/wiki/LaTeX/PGF/TikZ).
In comparison to LaTeX, TikZ feels a lot more like an actual programming language, so there's a much higher risk to write working but really nasty code.
Getting proficient with TikZ is hard, the manual is over a 1000 pages by now.
But I think there's some general design principles that even newbies can follow easily and that make TikZ code a lot more fun to work with.
So the next time we return to LaTeX, be prepared for some unsolicited TikZ advice by yours truly.

In the meantime, feel free to share your personal LaTeX pet peeves in the comments section.
There's so many subtle issues, I'm sure there's some common mistakes that I still make myself.
