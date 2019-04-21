---
title: >-
    Contribute
authors:
    - Thomas Graf
date: 2019-03-09
---

Want to make a guest post?
Great, it's easy!
Just email us your post as a text file: `submission@outde.xyz`.
No pdfs please, it needs to be an editable file.
A plain text file is best, but doc and docx are acceptable if necessary.
As long as your submission is suitable for the outdex, we'll post it directly under your name.
No registration, no special software, just writing.

If you're tech-savvy and want to make our life a little easier, read on.


## Level 1: Use markdown for writing

All posts are text file in markdown and automatically converted to HTML. 
Uploading a markdown submission only takes a few seconds for us, so it's greatly preferred to a `doc` or `docx` file.
Markdown is very easy to learn, it only takes about 30 minutes.
Here's two very accessible resources:

- [the interactive markdown tutorial](https://www.markdowntutorial.com/)
- [Github's markdown reference](https://guides.github.com/features/mastering-markdown/)

The first few lines of your markdown file specify the meta data: title, author(s), date, and optionally tags.
If your submission is on the long side, you can split it up into multiple posts that belong to the same series.
Here's a short example:

~~~
Title: Outdex doesn't use titlecase
Authors: Jane Doe, Alan Turing
Date: 2037-03-19
Series: Outdex usage advice
Tags: phonology, SPE, Minimalist grammars, well-formedness, job market

The post starts here.
Just keep writing, using markdown devices such as **bold** and *italic*.
Check the references above for the basics.
~~~

For converting markdown to HTML, we use Pelican with the `pandoc_reader` plugin.
This gives us access to the full [pandoc syntax](https://pandoc.org/MANUAL.html#pandocs-markdown), so we can do quite a few things that are not possible with standard markdown.
See the [tutorial post]({filename}../Tutorials/outdex_writing_guide.md) for details on math typesetting, syntax highlighting, and citation management, among others.


## Level 2: Submit via pull requests

If you expect to make several guest posts and know your way around git and github, it is easier to submit files as pull requests:

1.  Go to [our github repository](https://github.com/outde-xyz/website).
1.  [Fork it](https://help.github.com/en/articles/fork-a-repo).
1.  Write your post as a markdown file.
    Depending on the post's category, it should be saved in one of the following folders:
    - `content/Discussions` for open-ended posts that are meant to get a conversation going in the comments section
    - `content/News` for announcements, e.g. an interesting workshop, new journal, etc.
    - `content/Tutorials` for reader-friendly introductions to a technical topic or subject matter
1.  Sync the file to your fork.
1.  [Create a pull request](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork) against the `master` branch of our repository.


## Level 3: Check the test build after submitting

Outdex is deployed via [Netlify](https:/www.netlify.com).
Whenever a pull request is made, Netlify creates a preview and includes the link as part of the pull request.
Click that link to make sure that your submission will display the way you want.
If there's any issue, modify your pull request.
