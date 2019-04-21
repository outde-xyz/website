---
title: >-
    Adding metadata to your article
series: >-
    Writing for the Outdex
authors:
    - Thomas Graf
date: 2019-04-20
tags:
    - backend
    - metadata
    - YAML
---

This is the second post on how to write submissions for the Outdex.
The first one covered the use of pandoc for the actual content of your submission.
However, a blog post is more than just its content.
It also involves crucial *metadata* such as the author(s), the date it was published, and topic tags.
Don't despair, though, adding metadata to your post takes less than 2 minutes.
All you have to do is add a short YAML-header at the very top.
If that doesn't mean anything to you, read on.

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
This is a bit more technical, but it basically ensures that your title comes out the right way even if it contains certain characters like `:`.

For the sake of reference, here's what the top of the file for this post looks like:

```
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

```
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

And if I want to use pandoc's citation functionality to add some references to this article, I would have to specify the name of the bib-file to be used.

```
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
