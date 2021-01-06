#!/usr/bin/env python3

import glob
import nltk
from collections import Counter

stopwords = list(nltk.corpus.stopwords.words('english'))
custom_stopwords = [",", ".", ";", "!", "?", ":", "@", "&", "%",
    "$", "$$", "<", ">", "{", "}", "(", ")", "[", "]",
    "-", "=", "`", "``", "|", "#", "--", "\\",
    "\\otimes", "static", "date", "authors", "tags", "\\mathrm", "filename",
    "\\begin", "\\end", "start_summary_block", "end_summary_block", "thomas",
    "graf", "b\\",
    "0", "1", "1.", "2", "2.", "3", "3.",
    "'", "''", "'m", "'s", "n't", "'re", "'ll", "'ve",
    "a", "b", "c", "ca", "h",
    "i", "you", "it", "us",
    "first", "one", "two", "would", "but", "might", "use",
    "like", "also", "much", "way", "actually", "even", "get", "still",
    "say", "many", "lot", "really", "see", "must", "need", "specific",
    "think", "every", "want", "make", "point", "may", "let", "could",
    "work", "post", "https", "things", "time", "look", "different", "right",
    "instance", "instead", "know", "means", "go", "thing", "title",
    "something", "take", "node", "number", "bit", "whether", "though",
    "matter", "well", "kind", "least", "good", "without", "quite", "last",
    "since", "pretty", "talk", "single",
    ]
to_remove = set(stopwords + custom_stopwords)
paths = ('../../../Discussions',
         '../../../Tutorials')
top_n = 80

# tokenize all posts into a single list
text = []
for path in paths:
    for post in glob.glob(path + '/**/*.md', recursive=True):
        with open(post, 'r') as to_tokenize:
            for line in to_tokenize:
                tokens = nltk.word_tokenize(line)
                for token in tokens:
                    token = token.lower()
                    if token not in to_remove:
                        text.append(token)

# find most common tokens 
counts = Counter(text)
most_common = [word for (word, count) in counts.most_common(top_n)]

# write most common tokens to file
with open('most_common.txt', 'w') as fout:
    print('\n'.join(most_common), end='\n', file=fout)
