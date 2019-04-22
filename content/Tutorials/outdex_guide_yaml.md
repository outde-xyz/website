---
title: >-
    Adding metadata to your article
series: >-
    Writing for the Outdex
authors:
    - Thomas Graf
date: 2019-04-20
toc: true
tags:
    - backend
    - metadata
    - YAML
---

<!-- START_SUMMARY_BLOCK -->
This is the second post on how to write submissions for the Outdex.
The first one covered the use of pandoc for the actual content of your submission.
However, a blog post is more than just its content.
It also involves crucial *metadata* such as the author(s), the date it was published, or topic tags.
Metadata also allows you to enable some advanced features.
It's a very powerful tool, but also very easy to use.
All you have to do is add a short YAML-header at the very top.
If that doesn't mean anything to you, don't despair, it only takes 2 minutes to learn.
<!-- END_SUMMARY_BLOCK -->

## Markdown file = metadata + content

Every Outdex post is created from a markdown file with a `.md` ending.
The bulk of the file will be the content of the post.
For the sake of argument, let's assume that you have created a file `my_first_post.md` that only contains the following:

```md
This is my **first** post!
It's still work in progress.
```

This is a perfectly fine markdown file, but it is still missing the metadata we need for the blog.
To fix this, we add a YAML-header, which is surrounded by `---` above and below to set it apart from the rest of the file.

```md
---
title: >-
    Still to be decided
authors:
    - J. Doe
date: 2039-03-12
tags:
    - some tag
    - another tag
---

This is my **first** post!
It's still work in progress.
```

And that's it!
Easy peasy.
Note the empty line between `---` and the content.
While not needed, this is generally considered good style.
You might also wonder about the use of `>-`.
That one is a bit more technical, but it basically ensures that your title comes out the right way even if it contains certain characters like `:`.

For the sake of reference, here's what the top of the file for this post looks like:

```md
---
title: >-
    Specifying metadata with the YAML header
authors:
    - Thomas Graf
date: 2019-04-20
series: Writing for the Outdex
tags:
    - backend
    - metadata
    - YAML
---

This is the second post on how to write submissions for the Outdex.
The first one covered the use of pandoc for the actual content of your submission.
```

Here I've also added `series` to indicate that this post belongs to a multi-part series.

At a later point, I might make some changes to this file.
I could then add a `modified` field to keep track of the date of the most recent update.

```md
---
title: >-
    Specifying metadata with the YAML header
series: >-
    Writing for the Outdex
authors:
    - Thomas Graf
date: 2019-04-20
modified: 2019-10-14
tags:
    - backend
    - metadata
    - YAML
---

This is the second post on how to write submissions for the Outdex.
The first one covered the use of pandoc for the actual content of your submission.
```

And if I want to use pandoc's citation functionality to add some references to this article, I have to specify the name of the bib-file to be used.

```md
---
title: >-
    Specifying metadata with the YAML header
series: >-
    Writing for the Outdex
authors:
    - Thomas Graf
date: 2019-04-20
modified: 2019-10-14
bibliography: references.bib
tags:
    - backend
    - metadata
    - YAML
---

This is the second post on how to write submissions for the Outdex.
The first one covered the use of pandoc for the actual content of your submission.
```

The order of the fields does not matter, nor does the order of the tags.
But as somebody who's very fond of consistency, I would be greatly pleased if you were to follow the order used in the examples.

## Adding a summary and table of contents

There are two more useful entries you can put in the YAML header.
If you add `toc: true`, a table of contents will be added to your article, just like the one at the top of this post.
Right now the styling is still very crude, but hopefully I'll have time to tweak that soon.

You can also provide a summary with `summary: some text here`.
The summary will be displayed on the front page.
But if you're like me, you probably just want to reuse the first few lines of your article as the summary.
In that case, you can insert the special markers `<!-- START_SUMMARY_BLOCK -->` and `<!-- END_SUMMARY_BLOCK -->` to indicate the start and end of the summary.
For example, the markdown file for this article actually starts as follows:

```md
---
title: >-
    Adding metadata to your article
series: >-
    Writing for the Outdex
authors:
    - Thomas Graf
date: 2019-04-20
toc: true
tags:
    - backend
    - metadata
    - YAML
---

<!-- START_SUMMARY_BLOCK -->
This is the second post on how to write submissions for the Outdex.
The first one covered the use of pandoc for the actual content of your submission.
However, a blog post is more than just its content.
It also involves crucial *metadata* such as the author(s), the date it was published, or topic tags.
Metadata also allows you to enable some advanced features.
It's a very powerful tool, but also very easy to use.
All you have to do is add a short YAML-header at the very top.
If that doesn't mean anything to you, don't despair, it only takes 2 minutes to learn.
<!-- END_SUMMARY_BLOCK -->

## Markdown file = metadata + content

Every Outdex post is created from a markdown file with a `.md` ending.
The bulk of the file will be the content of the post.
```

## Summary

The YAML header is crucial for specifying your article's metadata.
Right now, the following entries are supported:

```md
---
title: >-
    Title of post, with normal capitalization (mandatory)
series: >-
    only for use with multipart posts
authors:
    - author1 (mandatory)
    - author2
date: YYYY-MM-DD (mandatory)
modified: YYYY-MM-DD (only used when updating an existing post)
bibliography: some_bib_file.bib (if you use citations)
toc: true (if you want a table of contents)
summary: >-
     Some short description (use is discouraged)
tags:
    - tag1
    - tag2
    - tag3
---
```

While `summary` is supported, you're probably better off inserting the `<!-- START_SUMMARY_BLOCK>` and `<!-- END_SUMMARY_BLOCK>` markers right into the content of your article.
