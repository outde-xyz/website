---
title: >-
    Authoring articles with pandoc
series: >-
    Writing for the Outdex
authors:
    - Thomas Graf
date: 2019-03-09
modified: 2019-04-19
bibliography: references.bib
tags:
    - backend
    - markdown
    - pandoc
---

<!-- START_SUMMARY_BLOCK -->
This is the first post in an ongoing series of mini-tutorials for Outdex contributors.
I'll give a brief overview of some of the lovely [pandoc features](https://pandoc.org/MANUAL.html#pandocs-markdown) that authors can use for their outdex articles:
formatting with markdown, syntax highlighting, Latex-style math, bibtex-style citations, and example numbering.

In the near future, there will be follow-up posts that cover the use of YAML headers for metadata, how to submit articles via [Github](https://github.com), and some aspects of the [talkyard commenting system](https://www.talkyard.io) we use.
If anything's unclear, please leave a comment.
<!-- END_SUMMARY_BLOCK -->

## Basic markdown features

All the basic markdown features are available.
If you've never used markdown before, you might want to start with the [interactive markdown tutorial](https://www.markdowntutorial.com/) to get a hang of the basics.
It doesn't take long, and it's really well-made.

### A simple example

You may use **bold** or *italic*.
There's also `verbatim text`, which is useful for code, e.g. `print("some string")`.
Feel free to use subscript~i~ and superscript^i^.
Some things you might want to ~~erase~~.

Of course you can use links, like <https://outde.xyz>,
and [create named links](https://outde.xyz).

- Bullet points work just fine.
- Including several in a row.
    - Subpoints might be overkill, though.

1.  Or perhaps you'd like a numbered list?
    - We can mix and match the two.
1.  It really is pretty easy.

How about a table, dear prospective author?

| First column | Second column | Third column |
| :--          | --:           | :-:          |
| left         | right         | center       |

> A quote is also nice once in a while.
> And quoting works just like in an email.

### How it works

The output above is produced from the markdown code below:

```
## Basic markdown features

All the basic markdown features are available.
You may use **bold** or *italic*.
There's also `verbatim text`, which is useful for code, e.g. `print("some string")`.
Feel free to use subscript~i~ and superscript^i^.
Some things you might want to ~~erase~~.

Of course you can use links, like <https://outde.xyz>,
and [create named links](https://outde.xyz).

- Bullet points work just fine.
- Including several in a row.
    - Subpoints might be overkill, though.

1.  Or perhaps you'd like a numbered list?
    - We can mix and match the two.
1.  It really is pretty easy.

How about a table, dear prospective author?

| First column | Second column | Third column |
| :--          | --:           | :-:          |
| left         | right         | center       |

> A quote is also nice once in a while.
> And quoting works just like in an email.
```

The use of `##` indicates a level-2 header.
The highest level of posts is `##`, since the post title itself should be the only level-1 header.
So don't use `# Some section`.
You should always start with `## Some section`.
You can then create subsections with `### Some subsection` and subsubsections with `#### Some subsubsection` (if you need them).

Not all of the features above may work in the comments section.
That's because the comments use a different markdown implementation that is not as powerful as pandoc.
There's nothing we can do about this.


## Advanced features

### Images

Adding images is already supported by standard markdown.
So the code
`![outdex logo](../img/logo.svg)`
will show the lovely outdex logo with the caption *outdex logo* underneath.

![outdex logo]({static}/img/logo.svg)

But as you might have noticed, the size isn't quite appropriate.
Pandoc allows us to also specify various image attributes as a semicolon-separated list.
This includes `width` and `height`.
So here's what we we get with
`![](../img/logo.svg){ width=50% }`.

![]({static}/img/logo.svg){ width=50% }

Much better, don't you agree?

### Syntax highlighting

Code is difficult to read if it's all black and white.
Fortunately, we have an automatic syntax highlighter. 

```python
print("some highlighted code")
for x, y in [(True, "Awesome!"),
             (False, "Lame!!!1!!")]:
    if x:
        print(y)
```

Just put your code between named code-fences like this:

~~~
```python
print("some highlighted code")
for x, y in [(True, "Awesome!"),
             (False, "Lame!!!1!!")]:
    if x:
        print(y)
```
~~~

Change the name to match your programming language.

```java
System.out.println("Java works, too.")
```

~~~
```java
System.out.println("Java works, too.")
```
~~~

And so does Haskell.

```haskell
putStrLn "See, I didn't lie!"
```

~~~
```haskell
putStrLn "See, I didn't lie!"
```
~~~

This also works in the comments section, but there it requires some finicky Javascript injections and thus might not work on every browser.

### Mathematics

Math is super-easy: just use the standard LaTeX commands.
For instance

```latex
$\mathrm{language} \otimes \mathrm{computation}$
```

will output $\mathrm{language} \otimes \mathrm{computation}$.
We're not limited to oneliners, more complex commands are fine, too.

\begin{align*}
    \text{outdex} :=
    \begin{cases}
        \text{awesome} & \text{if math is possible}\\
        \text{lame}^2  & \text{otherwise}\\
    \end{cases}
\end{align*}

The code for this is really just standard Latex:

```latex
\begin{align*}
    \text{outdex} :=
    \begin{cases}
        \text{awesome} & \text{if math is possible}\\
        \text{lame}^2  & \text{otherwise}\\
    \end{cases}
\end{align*}
```

There's **two caveats**, though.

1. Support for custom macros is limited, so please try to avoid that.
1. The code is rendered with MathJAX, which means that it does not work if JavaScript is disabled in the browser.

So as a reminder to all readers: if you're using *umatrix* or a similar browser plugin, make sure you allow access to `cloudflare.com` from `outde.xyz`.


## Features for academic writing

### Citing from the literature

Blog posts aren't academic papers, but once in a while it's appropriate to cite existing work.
Thanks to pandoc, we can use a system that's very similar to bibtex.
Consider the piece of code below

```
Instead of Joshi (1985:235), just write @Joshi85 [235].
Or did you want (Joshi 1985:235)?
Well that would be [@Joshi85, 235].
Use a semi-colon for multiple citations, e.g. [@Joshi85; @Stabler97].
```

Here's how this will render after being processed by pandoc:

Instead of Joshi (1985:235), just write @Joshi85 [235].
Or did you want (Joshi 1985:235)?
Well that would be [@Joshi85, 235].
Use a semi-colon for multiple citations, e.g. [@Joshi85; @Stabler97].

Check the pandoc manual for additional citation options.
All citations will be added at the end of the post.
So it makes sense to end your post with `## References` to get a nice header for the bibliography.

**Caveat:** Just like bibtex, pandoc requires a well-formed bib-file for citations.
So if you're using citations, make sure to send along a bib-file.

### Footnotes

Another staple of academic writing that might not be the best fit for a blog.
Still, if you absolutely want to add a footnote, do not despair.[^remark]

[^remark]: You see, I just added one. Here's the code for that:
    ```
    Still, if you absolutely want to add a footnote, do not dispair.[^remark]

    [^remark]: You see, I just added one. Here's the code for that:
    ```
    Oh, that got scary for a second.
    Infinite loop avoided.


Footnotes are inserted after the references.
As far as I know, there is no easy way of fixing this.[^fixit]

[^fixit]: Feel free to investigate, though, perhaps there is a hack.

### Example numbers

Alright, let me be blunt here: outdex can't offer you the sophisticated example numbering scheme of the average linguistics paper.
No fancy (2a') or anything like that.
No auto-aligned glosses, either.
So, that's one annoying limitation for now.

But there's some basic support for examples with increasing numbers.

(@) This is a decent example.
(@) But there are no subexamples.

```
(@) This is a decent example.
(@) But there are no subexamples.
```

(@) But at least the numbering does not get reset to (1) later on.

```
(@) But at least the numbering does not get reset to (1) later on.
```

Now example numbering is pretty pointless if you don't actually reference the numbers in the text, like (@an_example_label_is_always_useful) insists you should do.

(@an_example_label_is_always_useful)
    Don't just write `(@)`, give your example a name.
    I have a very long one, but names can be short, too.

```
(@an_example_label_is_always_useful)
    Don't just write `(@)`, give your example a name.
    I have a very long one, but names can be short, too.
```

You can now refer to this example with `(@an_example_label_is_always_useful)`, like I did in the previous paragraph.


## Wrapping up

Pandoc is a very powerful language, and this post could only highlight the most important features.
This should be enough for 99% of all Outdex articles.
But if you think you need more, check the [pandoc manual](https://pandoc.org/MANUAL.html#pandocs-markdown). 
Odds are, it's already in there.

## References
