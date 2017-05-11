# Practical Bayesian Optimization of Machine Learning Algorithms

Jasper Snoek, Hugo Larochelle, Ryan P. Adams. [Practical Bayesian Optimization of Machine Learning Algorithms.](http://papers.nips.cc/paper/4522-practical-bayesian-optimization-of-machine-learning-algorithms.pdf) NIPS 2012. 

## tl;dr
 - Authors propose a fully Bayesian method for Gaussian Process hyperparameters
 - Empirical results on LR, online LDA, SVMs, and CNNs
 - Also covers the unkown cost or availability of multiple cores to run in parallel.

## Contributions
Considerations for Bayesian Optimization of Hyperparameters include: 1) covariance function selection and hyperparamethers, 2) function evaluation takes resources, 3) opitmization should take advantage of multi-core parallelism.
 1. Using a ARD Matern 5/2 kernel instead of the automatic releevance determination (ARD) squared exponential kernel gives a function that is not too perfectly smooth. Furthermore, we can marginalizae over hyperparameters to compute the integrated acquisition function. 
 2. We should optimize for improvement per second rather than improvement per iteration. We can also employ Gaussian processes to model cost functions.
 3. Sequential strategy using MC estimates of the acquisition function.

## Experiments
 1. Brainin-Hoo function (common Bayesian benchmark) and Tree-Parzen Algorithm on MNIST data using logistic regression.
 2. Online LDA involves two learning parameters to control learning rate to update variational parameters of LDA.
 3. Motif finding with Structure SVMs, which outperform SVMs when they can explicitly model problem-dependent hidden variables. Protein DNA sequences model the unknown location of praticular subsequences or motifs.
 4. CNNs on CIFAR-10 allow us to tune nine hyperparameters of a three-layer CNN. 

## Q's for authors
TODO