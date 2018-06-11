# An Alternative View: When Does SGD Escape Local Minima?

Robert Kleinberg, Yuanzhi Li, Yang Yuan. [An Alternative View: When Does SGD Escape Local Minima?](https://arxiv.org/pdf/1802.06175.pdf) ICML 2018.

## tl;dr
 - Tacking the question of "Why does deep learning work?", here we explore whether stochastic gradient descent (SGD) escapes local minima? Yes for convex, usually yes for non-convex.
 - Usually yes means the weighted average of the gradients of its neighborhoods must be one point convex with respect to desired x-star.
 - Empirically the authors show that the neural networks loss surface exhibits one point convexity locally.

## One point convexity
Informally, a function f is c-point convex with fixed point x-star, step size n, noise W(x), and y = x - n\*grad(f(x)) if: the inner product of the gradient of the expected value of the neighborhood of y and the direction x-star - y is greater than the 2-norm of c \*(x-star - y). We then know that y will converge to x-star with decent probability.

## Motivating example
The authors use the motivating example of a parabola with added spikey noise. It is conjectured that flat local minima leads to better generalization, so using an example of spikey noise represents the most extreme local minima to overcome.

## Main theorem
The main theorem shows that points y will converge to fixed point x-star and once there, it will stay there. The main assumption is L-smoothness.