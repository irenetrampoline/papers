# Mining Frequent Graph Patterns with Differential Privacy

Entong Shen, Ting Yu. [Mining Frequent Graph Patterns with Differential Privacy.](https://arxiv.org/pdf/1301.7015.pdf) KDD 2013. 

## tl;dr
 - Frequent graph patterns denotes the number of graphs containing a subgraph G given a larger set of graphs
 - MCMC based on traveling between possible patterns, converged distribution gives exponential mechanism
 - Optimization includes finding the efficient neighbors: popular patterns have popular subgraphs, and unpopular patterns have unpopular supergraphs

## Approach
We are trying to find the number of graphs that have a specific subgraph within them. We reformulate such that MCMC can do a random walk in order to apply the classic differential privacy approach of an exponential mechanism (generalized form of Lapalcian mechanism). Note that subgraph isomorphism test is NP-complete, which makes counting the support of a pattern computationally difficult.


## MCMC Details
 - We create a super-graph (aka a Partial Order Full Graph) where each node is a subgraph pattern and each edge represents an addition or removal of a node between subgraph patterns.
 - At convergence, our MCMC distribution matches our target distribution in the exponential mechanism
 - Accept each proposed pattern with probability \alpha = min(1, exp(eps * u(y) / 2k\delta(u) q_yx) / exp(eps * u(x) / 2k\delta(u) q_xy)) where u() is the score function aka number of graphs in set with that pattern, q_ij is the transition probability, eps is the privacy budget, k is the threshold that we want that appear in patterns with >= k graphs. 

## Efficient Exploration of Neighbors
If a subgraph is very popular, any subgraph of that subgraph pattern must also be common in the dataset. Similarly if a subgraph pattern doesn't appear often, then the subgraph pattern plus any edge will also not appear. 

We can also save the subgraph isomorphism when we have pattern x and add any additional edge. This can modify our proposal distribution.

## Criticisms
 - Lots of space
 - Lots of time to converge

## Q's for authors
 - Can we do differential privacy for MCMC directly?
 - Can we do graphical models (HMM)?