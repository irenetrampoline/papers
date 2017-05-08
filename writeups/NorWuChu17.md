# Learning with Confident Examples: Rank Pruning for Robust Classification with Noisy Labels

Curtis G. Northcutt, Tailin Wu, Isaac L. Chuang. [Learning with Confident Examples: Rank Pruning for Robust Classification with Noisy Labels.](https://arxiv.org/pdf/1705.01936.pdf) 2017. 

## tl;dr
 - Examines binary classification with false positive rate p1 and false negative rate p0
 - Model combines previous methods including noise estimation, PN (pos/neg labeled, maybe wrongly), PU (some pos labelled, rest unlabled), any prob classifier, prob estim robustness, and added noise
 - Rank pruning estimates noise rates and then uncovers true classifications

## Rank pruning
 1. Let subset of X and potentially false labels s have thresholds to predict chich pos and neg entries in s are incorrect. 
 2. Use those to estimate noise rates.
 3. Using noise rates, prune set for unlikely pos and neg entries
 4. Retrain on more confident subset.

## Q's for authors
 - How does this extend to multi-dimensional?
 - Correlated noise?