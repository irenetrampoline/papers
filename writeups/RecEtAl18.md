# Do CIFAR-10 Classifiers Generalize to CIFAR-10?

Benjamin Recht, Rebecca Roelofs, Ludwig Schmit, Vaishaal Shankar. [Do CIFAR-10 Classifiers Generalize to CIFAR-10?.](https://arxiv.org/pdf/1806.00451.pdf) 2018. 

## tl;dr
 - To understand overfitting, authors augmented CIFAR-10 with new (but similar) data. 
 - Large drop in accuracy from lots of deep learning models, but models with higher accuracy have smaller drop
 - Evidence that current accuracy numbers are brittle.

## CIFAR-10
One of the original AI datasets, CIFAR-10 has images from 10 classes (e.g. dog) and multiple correponding keywords. CIFAR-10 was drawn from a larger dataset called Tiny Images. In collecting new images and labelling from Tiny Images, authors ensured that the keyword distribution was roughly similar with a bias on more common keywords.

## Performance Results
Authors tested over 20 deep learning models spanning conventional (VGG, ResNet) to state-of-art (Shake-Drop) using publically available code. All models see a drop in accuracy (e.g. VGG saw 8% drop). 

## Explanations
The original CIFAR-10 dataset had near duplicates which may allow models to overfit and see test accuracy still remain high. This would only explain at most 1% difference. Another possible explanation is that hyperparameter tuning may have overfit to CIFAR-10. Even with hyperparameter tuning, the results still hold and no settings can be found to produce significantly higher accuracy.

The implication seems to be that years of CIFAR-10 training and testing have overfit to the CIFAR-10 test data. 

## What's next?
Certainly other common datasets (ImageNET, MIMIC-III) could be augmented and examined against existing algorithms. More broadly, we want to ensure that our models are not overfitting and are truly robust.