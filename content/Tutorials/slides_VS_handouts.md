---
title: >-
    To slide or not to slide?
authors:
    - Thomas Graf
date: 2019-11-21
bibliography: references.bib
series: Slide advice
tags:
    - talks
    - student advice
---

<!-- START_SUMMARY_BLOCK -->
Even though I'm slowly growing into my role as tenured professor, I still haven't developed a taste for saying the same thing over and over again --- at least not when I'm aware it's the same thing over and over again.
One thing that comes up a lot is questions by new students about their presentations, be it in class or at a conference.
So I figured I might actually be able to save everybody some time by just posting my standard remarks on the Outdex, preserved for eternity.
Who knows, it might even be hilarious 30 years from now to read about how we did things in the academic stone age.
Just like it's hard to talk about mimeographs nowadays without a smirk on your face.

Okay, then let's tackle the very first issue, one that is still so contentious in some parts of the field that it might rip asunder the fabric of space and time: slides or handouts?
<!-- END_SUMMARY_BLOCK -->

# That's not the right question to start with

Before you even start thinking about the medium of presentation, you should have already asked yourself some fundamental questions about the content:

- What is my talk about?
  No, seriously, behind all that jargon, behind all that data, behind all that machinery, what is the real insight here?
- How can I summarize that in a take-home message of 25 words?
- What parts are needed to get the audience to a point where they can see why that is the take-home message?
  What parts do not help with that and thus can be excised?
- What is the format of the key information?
  Graphs, formulas, proofs, code, linguistic examples, abstract ideas that need to be visualized?

Until you are fairly certain about the answers to these questions, don't even ask yourself if it should be slides or a handout.

# That's still not the right question

Okay, so let's assume you have a rough idea of what your talk should look like.
Now we can finally decide if you should be preparing slides or a handout, right?
Well, sort of, except that's not really the issue nowadays.

(@) **The real question**  
    Slides + handout, or just a handout?

Back in the days, handouts had many advantages over slides.
For one thing, everybody in the audience has something **permanent** from the talk that they can store in a binder in their office.
The idea is that they might then be able to consult your handout in the future, but in practice that doesn't happen all that often.
Still, it's nice to have the possibility of it happening.
Second, handouts allow for **non-linearity**.
Audience members can jump around during the talk, for instance to ponder a data point you discussed earlier.
They can also look ahead if they aren't quite sure where all of this is going (strictly speaking that should never happen with a good talk, but it's nice to have a safety net).
Permanence and non-linearity are two boons of handouts.

However, permanence and non-linearity are no longer exclusive to handouts.
If you have a website (which you should!), then you can make your slides available on your website.
Ideally, you share them as a pdf so that everybody can view them on any device.
You can add a QR code to the title slide.
Audience members scan it, download the pdf, and then they can look back and forward as they see fit during your talk.
Voila non-linearity.
It is also very likely that you'll take better care of your website than somebody else will of your handout.
Which means that digital handouts are at least as permanent as physical ones for most audience members.

If that's still not enough, you can produce a physical handout from slides.
If you make your slides with the $\LaTeX$ beamer package, for instance, you can use the same source file for creating slides and handouts.
And that's why the question is no longer slides VS handouts, it's slides + handouts VS just handouts.

So is there any reason to ever go with just handouts?
Isn't slides + handouts by definition at least as good as just handouts?
Well, not quite.

# Con: Slides are a time sink

Slides take a lot of time by default, and good slides take tons of time.
Those [slides of my UMass talk](https://thomasgraf.net/output/graf19umasstalk.html)?
Almost a full day of uninterrupted work even though I reused a lot of existing code from other presentations.
But I wanted to draw some new trees and uncover them bit by bit, had to change the layout here or there to make it fit the slides, yada yada yada.
I like nice slides, I like making nice slides... there might a presupposition violation here.
But slides are a time sink.

Slides have the **temptation of the possible**.
The mere fact that you can illustrate ideas with animations means that you'll probably spend a lot of time trying to do that.
With a handout, on the other hand, you might have just had a static image there and quickly done the rest on the board if necessary.
The constraints of the medium naturally limit how much effort you devote to it.

Slides also require quite a bit of polish to work well.
I'll have a follow-up post soon where I talk about some of that in detail.
For now, let's just say that a dry, monochrome, badly arranged handout does not leave as bad an impression as dry, monochrome slides with nothing to break up the monotony.
It's probably because the slides are always in your face whereas the handout leaves the #1 spot to the speaker.
Whatever the reason, slides will take more time if you want them to be good.

In particular if you're a beginner, this might cause you to spend all your time on the slides rather than practicing your talk.
Remember, the real medium for the talk is you, the speaker.
Everything else is just adornment to assist you in that task.
The nicest slides won't do diddly squad if you're stumbling through them with awkward pauses and flat intonation while staring at a corner.

# Con: Slides aren't papers

Slides not only take a lot of time, they take a lot of time in an unproductive manner.
Many handouts I've seen are essentially full papers where the paragraphs have been roughly sketched out with bullet points.
A handout like that doesn't take too much effort to turn into a paper, and papers are the currency of academia.
Nobody gives a hoot about slides or handouts, but the latter you can turn into something that people do care about.

# Pro: Slides aren't papers

At the same time, I'd say the main advantage of slides is exactly that they don't work like papers.
A talk is a talk, not a paper speed reading session.
It requires a very different approach if you want your audience to get something out of it, in particular if that audience has a very different background from yours.

Slides can't hold a lot of information, and splitting text over multiple slides doesn't work well.
In fact, not at all.
Slides force you to simplify, to break down your ideas into easily digestible, bite-sized pieces.
Don't use sentences, use phrases.
Don't use phrases, use pictures.
Don't include an argument if it isn't needed to make your point --- that stuff can go in an appendix.
Streamline, simplify, focus on the essentials and the big picture.
Make it slick, make it stick.

Not only will your audience appreciate the fact that they can actually follow what you're saying, it's also a good exercise for yourself.
Telling the important from the ancillary requires a deep understanding of the subject matter.
You cannot develop this understanding without constantly asking yourself what needs to stay and what can go.
I have seen students present an argument by going through X, then Y, then Z simply because that's how they've seen it done before.
But actually their argument hinges only on Y, not Z, and Y can be established without X.
They could've gone straight to Y without X or Z, but they never realized that because they weren't forced to simplify, which means they weren't forced to think deeply about X, Y, and Z.
Slides force you to think about these things.

# Pro: Slides can do things handouts can't

Sometimes you just need animations, multimedia, or at least (colorblind-friendly) use of color.
Sometimes your audience expects slides and nothing less will do --- just like linguists would be amused at best and appalled at worst by a philosopher reading out their paper, computer scientists would be flabbergasted at the sight of a linguist showing up with a handout.
When you need something handouts can't do, slides are your only option unless you're brave enough to give a blackboard talk.
Assuming your conference venue even has a blackboard.

# Conclusion: Slides unless they aren't worth your time

So here's the take-home message:

1. Don't even look at this take-home message until you have a good idea of what your talk is about and how it should be structured.
1. If you need something a handout cannot do, go with slides.
1. If you go with slides, make a pdf available online to get the permanence and non-linearity of handouts.
1. If slides and handouts are equally viable, it's a matter of how much time you're willing to spend on something that has no tangible benefit besides possibly making your audience a bit happier.

By the way: this take-home message has a tiny bit more than 25 words.
But that's a-okay because this ain't slides.
