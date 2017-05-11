# Large-Scale Physiological Waveform Retrieval via Locality-Sensitive Hashing

Y. Bryce Kim, Una-May O'Reilly. [Large-Scale Physiological Waveform Retrieval via Locality-Sensitive Hashing.](http://people.csail.mit.edu/ybkim/papers/EMBC15A.pdf) EMBC 2015. 

## tl;dr
 - Locality Sensitive Hashing involves a family of hash functions such that probability of collision is higher when hashing points that are close together in a higher-dimensional space
 - Using this, we can find distances between time-series data for near-neighbors approaches

## Locality Sensitive Hashing
LSH states for points p, q:
 * If ||p - q|| \leq R, then P(h(p) = h(q)) \geq P_1
 * If ||p - q|| \geq cR, then P(h(p) = h(q)) \leq P_2

 We choose hash family H = {h} such that

 h(p) = 0 if p_i < t and 1 if p_i \geq t

Choose p_i as i-th coordinate of time-series data where i is uniformly random and t is a threshold. Construct L hash tables using m independent hash functions. 

To find nearest neighbor of query point q, we hash query and retrieve points stored in matching bucket g(q) in each hash table T_l. From this candidate set, we linearly compute distance from q to each point in the candidate set to find k nearest neighbors of q. 

## Complexity
Initial stage of setup, but each retrieval is sublinear to size of data.

## Q's for authors
 - Application: clustering based on distance?
 - How does this handle missing data or errors in the dataset (entry error or noise)?