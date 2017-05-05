# Random Features for Large-Scale Kernel Machines

Ali Rahimi, Ben Recht. [Random Features for Large-Scale Kernel Machines.](https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips) NIPS 2007. 

## tl;dr
 - Maps input data to randomized low-dimensional feature space, apply fast linear methods
 - Randomized features designed so inner product of the transformed data are approximately equal to those in the feature space of shift-invariant kernel
 - Applied to two examples: Fourier transform and binning features

## Contributions
A **kernel machine** allows for feature generation that depends only on the inner product between pairs of input points. Unlike traditional kernel tricks which, for example, can project a dataset into a high dimension in order to find a linearly-separable hyperplane, today we are concerned about mapping to a low-dimensional Euclidean inner product space so that the pair of transformed points approximates their kernel evaluation. 

## Fourier Transform
 - The first example includes random Fourier bases cos(w'x + b), which projects data points on a randomly chosen line into a sinusoidal function.  
 -  Bochner's theorem states that a continuous kernel k(x,y) = k(x-y) is positive definite if and only if k(delta) is the Fourier transform of a non-negative measure.

## Binning Features
 - Binning divides the features space into rectangles and assigns a point to a bin with probability proportional to k(x,y)