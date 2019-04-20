---
title: FAQ
authors: Thomas Graf
date: 2019-03-10
---

## Technical issues

### Do I need an account to comment?

Yes.
You can either create one, or use an existing Github, Facebook, Gmail, or Twitter account.

### I don't see the commenting dialog, where is it?

It's at the bottom of each page.
If you can't see it, make sure Javascript is activated in your browser.

Advanced users: If you use [uMatrix](https://addons.mozilla.org/en-US/firefox/addon/umatrix/) or a comparable browser add-on, set up your permissions as follows:

| Domain                                | cookie | css   | media | script | XHR   | frame | other |
| -:                                    | :-:    | :-:   | :-:   | :-:    | :-:   | :-:   | :-:   |
| `outde.xyz`                           |        | allow |       | allow  |       |       |       |
| `talkyard.net`                        | allow  | allow |       | allow  | allow | allow |       |
| `comments-for-outde-xyz.talkyard.net` | allow  | allow |       | allow  | allow | allow |       |
| `ty-cdn.net`                          |        | allow |       | allow  |       |       |       |     
| `c1.ty-cdn.net`                       |        | allow |       | allow  |       |       |       |     

### When I login, I get an error message that says `Cannot read property 'id' of null`. 

Your browser is blocking 3rd party cookies.
You have to whitelist 3rd party cookies for `outde-xyz.talkyard.net`.
See [this post](https://www.talkyard.io/-217/disabling-3rd-party-cookies-in-ones-browser-breaks-blog-comments-login) for details.

### Whenever I use LaTeX math in the comment, linebreaks gets ignored.

Short answer: use `\\\\` instead of `\\`.

Long answer: All content in the comments is parsed as pure Markdown first.
In Markdown, `\` is used to escape characters.
If you type `\\` in Markdown, this gets converted to `\` in the HTML output. 
But the math typesetting engine uses the HTML output, not the Markdown input.
So if you want to get `\\`, you have to type two escaped backslashes, i.e. `\\\\`.

### This all sounds awfully tedious. Is there no alternative that's more convenient?

We looked at many alternatives, and the current solution has the fewest drawbacks.
It respects user privacy, is easy to host and integrate, allows for math and syntax highlighting, has reasonable spam countermeasures in place, and doesn't cost an arm and a leg.

### Speaking of spam, I noticed a message from a spam bot. You should remove that.

Actually, outdex relies entirely on user moderation.
If you see a spam message, flag it as such:

1. Go to the spam message.
1. Click on the button with three lines, to the left of the message's reply button.
1. Click `Report`.

Once a message has been reported as spam by a sufficient number of students, it is automatically hidden.

### What is all the Javascript for? I thought this was a static blog.

It largely is, but some things just don't work without Javascript.
Here's a brief overview of what gets loaded:

- `cloudflare.com`: MathJAX for typesetting math in articles (does not apply to comments)
- `talkyard.net`, `ty-cdn.net`, and subdomains thereof: needed for the commenting system
- `outde.xyz`: provide [JSON linked data](https://json-ld.org/); can be safely blocked


### What else is loaded from remote domains?

Not much, and all of it can be safely blocked without breaking the site:

- `creativecommons.org`: load the license in the footer
- `licensebuttons.net`: load the license button in the footer
- `fonts.googleapis.com`: load some fonts for the theme
- `*.gstatic.com`: also used for font loading
- `polyfill.io`: dependency of the talkyard commenting system


### Do you use Google analytics or similar tracking scripts?

No. Zilch, nada, none.
