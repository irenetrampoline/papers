# Probabilistic Topic Models

D. Blei. [Probabilistic Topic Models.](https://www.cs.princeton.edu/~blei/papers/Blei2012.pdf) Communications of the ACM 2012. 

## tl;dr
 - Topic models find themes across unstructured documents through assuming latent structure
 - Estimating posterior denominator (aka evidence) requires sampling methods or variational methods 
 - Model checking (measuring performance) and data discovery are two big open areas in order for topic models to be maximally useful

## Thoughts
From the master himself, David Blei covers a survey of probabilistic topic models--from his canonical LDA and beyond. I appreciated the easily digestible format with very little math except for some formalization and then only the definition of the posterior in order to explain the difficulties in calculating the marginal probability of the denominator. A great number of pages focused on next steps for topic modeling--including additional information to include (order of words, order of documents, metadata) and usability overall.

I'll admit I admire topic models on a mathemtical beauty level and am less convinced about the broad applicability (yet). This skepticism is echoed in the author's section addressing the interpretability and model checking of topic models. 

Overall the explanations were clear and simple, and the figures were deeply enlightening. Most importantly, Blei highlights the importance of topic modeling, which will motivate future researchers.

Topic models provide an algorithmic solution to managing, organizing, and annotating large archives of texts

## About topic models
At its heart, topic models allow us to find themes across documents containing unstructured textual data. The latent Dirichlet allocation (LDA) is the simplest of topic models and is best thought of in its generative process:
 - randomly choose distribution over topics
 - for each word in document
 	- choose topic from distribution of topics
 	- randomly choose word from word distribution of chosen topic

Difficulty of calculating probability distribution comes from the marginalizing of the denominator in the posterior term. Consider conditional prob: p(beta, theta, z | w) = p(beta, theta, z, w) / p(w) . In this case, the denominator (aka evidence) is much harder to calculate because marginal probability requires summation over all topic distributions. The two ways of dealing with this are
 - sampling collect to empirically plot the estimated distribution 
 - variation methods to use optimization to find closest parameterized family of distributions over hidden structure

# Research in Topic Modeling

What about the order of words? Assuming a bag of words gives a coarse semantic structure whereas using the ordering gives more sophistication and theoretically a better model. Approaches include word distributions conditioned on the previous word or switching between the topic model and standard HMM. Although this quickly expands the parameter space, researchers note improved language modeling performance.

Next up, order of words? If the topic is a sequence of distributions over words, can we find how topics change over time? What if the topics themselves change? Beyond that, we have topic correlation (one topic appears with another topic more often), spherical topic modeling (some words are unlikely in each topic), and bursty topic models.

Additionally, we can include more metadata. For example authors could give more information about the topics, and multiple authors also give additional information. 

Applications beyond textual data include population genetics and computer vision (images and captions, classify images, etc). 

# Open questions
Of the questions raised by Blei, I found the model checking and data discovery questions most compelling. A natural question is how do you even evaluate performance of a topic model? The traditional method involves a hold-out set, training the model on the rest of the data, and assessing the probability of the hold-out set occuring with your new model. Computationally, this evaluation technique holds, but it doesn't extend well to how humans would actually use it. 

Additionally, if we have these topics, so what? What can we learn from the language or the data as a result? Data discovery allows researchers to detect trends or learnings from the data. Because this is more than a computational problem, it could have a fundamental impact on how topic models are used in the future

# Ideas based on reading
 - Semi-supervised topic models?
 - How can topic models affect healthcare? Can it detect trends and classify groups of diseases better?
 - Mathematically what are the tradeoffs between variational and sampling methods? Is there a heuristic to decide based on the data?