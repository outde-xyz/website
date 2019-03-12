Title: Authoring articles with pandoc
Authors: Thomas Graf
Date: 2019-03-09
Series: Outdex guide
Tags: backend, markdown, pandoc

This post gives a brief overview of the [pandoc features](https://pandoc.org/MANUAL.html#pandocs-markdown) that authors can use for their outdex articles.
This is for authors only.
The comments are much more limited, unfortunately, and only support github-flavored markdown.

If anything's unclear, please leave a comment.

<!-- PELICAN_END_SUMMARY -->

## Basic markdown features

All the basic markdown features are available.

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

The use of `###` indicate a level-3 header.
The highest level of posts is `##`, since the post title itself should be the only level-1 header.
So don't use `# Some section`.
You should always start with `## Some section`.

Not all of the features above may work in the comment section.
That's because comments are converted directly by Github, which uses a more limited markdown dialect than pandoc.
Check the github reference that's linked in the comment field.


## Advanced features

### Images

Adding images is already supported by standard markdown.
So the code
`![outdex logo](../img/logo.svg)`
will show the lovely outdex logo with the caption *outdex logo* underneath.

![outdex logo](../img/logo.svg)

But as you might have noticed, this is a little large.
Pandoc allows us to also specify various image attributes as a semicolon-separated list.
This includes `width` and `height`.
So here's what we we get with
`![](../img/logo.svg){ width=50% }`.

![](../img/logo.svg){ width=50% }

Much better, don't you agree?

### Syntax highlighting

Code is difficult to read if it's all black and white.
Fortunately, we have an automatic syntax highlighter running in the background.

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

This also works in the comments section and does not depend on any javascript.

### Mathematics

Math is super-easy: just use the standard LaTeX commands.
For instance

```latex
$\mathrm{language} \otimes \mathrm{computation}
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

**Caveat:** you can only use references that are already in our central [bibtex file](https://raw.githubusercontent.com/outde-xyz/website/master/bib/references.bib).
So if your post cites some papers that are not in there, send along a bibtex file so that we can merge in the references.

### Footnotes

Another staple of academic writing that might not be the best fit for a blog.
Still, if you absolutely want to add a footnote, do not dispair.[^remark]

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

## References
