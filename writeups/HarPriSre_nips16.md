# Equality of Opportunity in Supervised Learning

M. Hardt, E. Price, N. Srebro. [Equality of Opportunity in Supervised Learning.](https://arxiv.org/pdf/1610.02413v1.pdf) NIPS 2016. 

## tl;dr
 - Takeaway 1
 - Takeaway 2
 - Open question or critique

## Overall Thoughts
What is this paper showing? What are the contributions? What kind of paper is it: theoretical, applied, something in the middle? Where does it fit into the prior body of work?

With the rise of machine learning, there has come the backlash of discrminatory algorithms. Certainly no one wants to be accused of bias (either intentional or unintentional), and thus a new field of "fair" algorithms has been born. As with any new field, the definition themselves must be carefully constructed and ruthlessly tested. 

On a personal note, I've found the thorny topic of bias and discimination fascinating through my work with gender and racial bias on Airbnb as well as my work with women in STEM. Most often, bias is not intentional but rather the result of negligence and lack of formalization. If you "go from the gut," there is more room for error. How can we structure our models, our systems, and our lives to be fair to all?

Let Y (e.g. likelihood to be arrested) be the attribute to be predicted from features X (e.g. prior record, hair color, etc). 

One naive method would remove the protected attribute A entirely. This does not solve anything since there might still be latent factors. Another slightly more clever method, which sets the  P(Y = 1 | A = 0) = P(Y = 0 | A = 1), is that it makes the possibility that A is perfectly correlcted with Y impossible. Here with equalized odds, we require that the model be *oblivious* but not *blind*. 

Here the authors formalize their concept of *equalized odds*: essentially the true positive and false negative rates must be equal for a protected attribute A. 

![Equalized odds](../img/HarPriSre_nips16/obj.png)

A weaker notion of *equal opportunity* where only 

In the paper, we construct a predictor Y_tilda that is independent of X conditional on random variables R and protected attribute A. The rest of the paper goes about applying this to real valued predictors, Bayes optimal predictors, and empirical results.

## 

In particular, it does not evaluate the features in X nor the functional form of the predictor Y_hat(X) nor how it was derived.



Equal true positive rates and false negative rates across A = 0 and A = 1.

However, equalized odds enforces that the accuracy is equally
high in all demographics, punishing models that perform well only on the majority.

## Section 1
 - Something witty or just summarizing
 - Easy to read to remembmer what was in this paper

## Section 2
 - Elaborate on something else
 - What are the main contributions?
 - Point to relevant long parts of paper that are unable to be summarized


## Q's for authors
TODO

## Helpful
 - [Google blog post](https://research.googleblog.com/2016/10/equality-of-opportunity-in-machine.html)