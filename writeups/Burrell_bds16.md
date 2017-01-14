# How the machine 'thinks': Understanding opacity in machine learning algorithms

J. Burrell. [How the machine 'thinks': Understanding opacity in machine learning algorithms.](http://journals.sagepub.com/doi/pdf/10.1177/2053951715622512) Big Data and Society 2016.

## tl;dr
 - Opacity comes in three flavors: corporate secrecy, technical illiteracy, and characteristics of machine learning algorithms
 - Author examines only neural networks and SVMs based off of Andrew Ng's [Coursera class](https://www.coursera.org/learn/machine-learning)
 - Suggestion: Would have appreciated more formalization in the definition of opacity. Which features caused the classifier result? Tradeoff between opacity and performance? 
 - Reflection: ML people refer to opacity as the third. General public cares about first two. Conflating the three is not helpful.

## Thoughts
I'm reading this paper since it was listed in the Spotlight section of the [FATML 2016 proceedings.](http://www.fatml.org/schedule/2016) Unlike many of the other papers, the author comes from a less technical background, which shows in the familiarity with the machine learning models and assessments of opacity. Instead the author covers a more layman's approach to machine learning and opacity, complete with a reference to a public service announcement about people who die because of these strange algorithms. 

The three types of opacity outlined include:
 1. intentional coporate or state secrecy
 2. technical illiteracy to understand the algorithm
 3. mismatch between characteristics of machine learning algorithms and what humans can comprehend

My main critique of the enumeration above is that opacity is not inherent to an algorithm, rather the opacity definitions listed depend on the viewer. A computer programmer may be able to dispell opacities 2 and 3, but 1 will elude her if she doesn't work at the company creating the algorithm. More broadly, opacity in how I understand it is generally definition 3 whereas the general public without a thorough computer science background may define it as 1 and 2.

The paper itself only describes two machine learning algorithms and briefly the opacity of the algorithm as based on the author's rudimentary understanding of Andrew Ng's Coursera class. (As an aside, the distinction between models and learnings for the classification and training portion of a supervised algorithm felt unnecessary.) Neural networks strike some as more opaque because the lack of intuitive understanding of the weights. The author visualizes the weights, but I still didn't really see the use. Support vector machines (SVMs), however, have a clearer coefficient with each feature, but the author pointed out instances where it may not be clear from human inspection. 

I feel a little cheated having read this paper for my daily consumption. At the same time, the topic of opacity has not been defined as precisely to assuage the public's fear of algorithms. I predict transparency will become increasingly important in bridging the gap of understanding for applications people deem supremely important: medical care, police discrimination, loan approval, etc.

## Possible extensions
 - Define opacity in terms of the model. Given data, can we select features or combinations of features that strongly influenced the prediction? Would exposing this allow people to game the system better? (e.g. Gmail spam filter explanation)
 - Can we formalize the equivalent of [equalized odds](HarPriSre_nips16.md) for transparency? We could reason about the loss of performance if we have guarantees about transparency.