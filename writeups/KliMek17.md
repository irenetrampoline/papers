# Learning Graphical Models Using Multiplicative Weights

Adam R. Klivans, Raghu Meka. [Learning Graphical Models Using Multiplicative Weights.]() 2017. 

## tl;dr
 - Propose algorithm that learns graphical models or Markov random fields
 - Learn t-wise MRF with poly-complexity and poly-runtime.

## Algorithm
The intuition is a weighted voting scheme where all vertices could be initially neighbors of v_i, so each neighbor candidate is weighted equally. As we draw from the Ising model, each Z_j is a vote for j,+ or j,- for a node possible neighbor node j. The prediction is then the weighted sum of the votes given each draw of Z. The penalty of the prediction according to (sigma(-2p) - (1-Z_i) / 2) Z_j where correct guesses will be penalized less than incorrect guesses.

## Uses
 - We can then use this Sparsitron algorithm for learning sparse generalized linear models
 - Similarly we can recover affine functions from l2 minimization
 - As noted earlier, we can learn Ising models as well
 - We can also recover polynomials from l2 minimization

# Note to self
Will need to reread again before Guy Bresler's reading club