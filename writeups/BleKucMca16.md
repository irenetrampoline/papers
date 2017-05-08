# Variational Inference: A Review for Statisticians

D. Blei, A. Kucukelbir, J. McAuliffe. [Variational Inference: A Review for Statisticians.](https://arxiv.org/pdf/1601.00670.pdf) 2016. 

## tl;dr
 - Takeaway 1
 - Takeaway 2
 - Open question or critique

## Thoughts
What is this paper showing? What are the contributions? What kind of paper is it: theoretical, applied, something in the middle? Where does it fit into the prior body of work?

## Outline
* Basics
	* Variational inference is an optimization problem (vs sampling in MCMC) using KL divergence
	* Pros: VI better on large datasets, faster
	* Cons: no guarantees on variance, not exact samples
* Simplest example
	* "evidence" is demominator of p(z|x), aka p(x), exponential to calc
	* evidence lower bound (ELBO) allows us to get around difficulty calculating p(x)
	* mean-field assumes all latent variables are mutually independent

## Q's for authors
TODO