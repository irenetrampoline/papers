# Bringing Impressionism to Life with Neural Style Transfer in *Come Swim*

B. Joshi, K. Stewart, D. Shapiro. [Bringing Impressionism to Life with Neural Style Transfer in *Come Swim.*](https://arxiv.org/pdf/1701.04928v1.pdf) 2017.

## tl;dr
 - Authors explore parameter choices when applying style transfer to the film *Come Swim*
 - Choices made include cropping style image, number of iterations, and GPU instances
 - Hard to quantify performance since end-result is a film

## Thoughts

I had originally heard of this paper through a [Tech Crunch article](https://techcrunch.com/2017/01/19/kristen-stewart-co-authored-a-paper-on-style-transfer-and-the-ai-community-lost-its-mind/). Most of the press about the article focuses on the shock of Kristen Stewart, of *Twilight* fame, publishing a machine learning paper, much less citing TensorFlow! I'll admit that was my main reason for digging deeper into the paper as well. As a marketing ploy, the other authors were smart to include her name in the author list in order to highlight the paper and the film.

Technically, the paper explores style transfer through convolutional neural networks (CNNs); that is, given a photo and a painting style, can we recreate the photo in that style? Surprisingly (at least to me!) the parameter space of the algorithm is quite large, and the engineer, director, and producer of the movie (aka the three co-authors) spent considerable time and energy "tuning" these "parameters" in order to create the appropriate aesthetic for the movie. Note that parameters in this case does not refer to the actual style transfer algorithm, which is treated as a black box for the purposes of the paper. Instead, the parameters to tune include the style image, the number of iterations, and model execution times.

The authors are fairly succinct (only 3 pages!) on how they chose these paramters. All of the methods boil down to some form of heuristic choice. For example, the style image was cropped in order to feed a better sample into the style transfer CNNs. Additionally, a higher resolution style image helped create better resulting images. Likewise other parameters were tuned based on: "It looked better."

In its essence, machine learning provides a tool to help machines become "as smart as" or even smarter than humans. The paper's greatest contribution is combining the quantitative nature of machine learning with the filmmaking needs of *Come Swim*. What would a rigorous machine learning method of making a movie from style transfer even look like? As a society, would we be comfortable with that? 

It's clear that this paper outlines the struggles of one author who is more technically minded (Research Engineer at Adobe) and two authors who have a clear artistic vision (inspired by the style image!) to bring to life. One method would be to create generative algorithms in order to build the "best" movie given source material and a style image. Another option is to provide a series of options, allowing for manual selection of visual styles. I for one look forward to the days of computer-assisted art creation. Hopefully it doesn't put the artists out of work.
