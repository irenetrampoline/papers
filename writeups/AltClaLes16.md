# Large-scale Analysis of Counseling Conversations

Tim Althoff, Kevin Clark, Jure Leskovec. [Large-scale Analysis of Counseling Conversations: An Application of Natural Language Processing to Mental Health.](http://www.aclweb.org/anthology/Q16-1033) ACL 2016. 

## tl;dr
 - Analyzing 80k text conversations on a suicide hotline, researchers identify five key insights
 - Focus on texting volunteers in order to provide actionable recommendations
 - For example, counselors that adapt between conversations perform better.

## Data labelling and segmentation
Data was from Crisis Text Line and contained 80k text conversations with 15k survey response (aka labelled data). Dataset includes 408 counselors. 

Most sucessful 40 counselors and least successful 40 counselors were used for analysis. Counselors roughly dealt with same proportion of topics. Conversations were also separated into successful and less successful counselors. 

## Insights
**Adaptability:** TF-IDF vectors from positive and negative conversations differ more for successful counselors than less successful counselors. 

**Ambiguity:** Given ambiguous (aka short) responses, more succesful counselors use more check questions, check for suicide ideation more foten, show appreciation, and use more hedges (e.g. maybe, fairly). 

**Creativity:** More successful counselors use less common/templated questions measured by threadsholded cosine distance in TF-IDF space.

**Convesation Progress:** Hand defined conversation stages can reveal the pace at which counselors move through conversation. More successful counselors move past earlier stages quicker. 

**Perspective Change:** Counselor might be able to suggest new topic and have texter follow lead to change perspective aka topic. Paper uses LIWC PosEmo and NegEmo sentiment lexicons. 

## Observations
I enjoyed the focus on the counselor rather than the texter. I wonder if the dataset size (40 positive, 40 negative) is sufficient. 

How do these results relate to the training given to each counselor? Are successful counselors breaking rules or following them? Vice versa to less successful counselors. Are there repeat texters? How does that change the dynamics?