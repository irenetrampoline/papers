# TITLE HERE

Michael Kearns, Seth Neel, Aaron Roth, Zhiwei Steven Wu. [Preventing Fairness Gerrymandering: Auditing and Learning for Subgroup Fairness.](https://arxiv.org/pdf/1711.05144.pdf) ICML 2018. 

## tl;dr
 - In order to defend against "gerrymandering" to find two subsets of populations for which an algorithm is unfair, the authors propose the definition where all exponentially many subgroups must be "fair.""
 - Auditing fairness is computational equivalent to weak agnostic learning, which implies theoretical intractability but heuristics may be successful
 - Two algorithms (one using *Follow the Perturbed Leader* and the other using best response and both using *Fictitious Play*) allow for reasonable convergence empirically

## Fairness Gerrymandering
We will examine FG from statistical parity (paper also include false positive). We define alpha(g, P) = Pr_P(g(x) = 1) aka the probability a datum belongs the protected group g and beta(g,D,P) = SP(D) - SP(D,g) where SP(D) = Pr_(D,P) [D(X) = 1] and SP(D,g) = Pr_(P,D) [D(X) = 1 | g(x) = 1] denote overall acceptance of D and acceptance of D on group g respectively. Then we say that D satisfies gamma-statistical parity if for every g \in G

alpha(g, P) beta(g, D, P) \leq gamma

## Experiments
Authors use Communities and Crime dataset from UCI, which contains 1994 records with 122 features to predict rate of violent crime in community. Because of the aggregate nature of the data, the dataset has a high number of real valued protected attributes: percentage of racial groups, per capita incomes, and percentage of police force. 

Interestingly the different iterations don't yield consistent results in error or unfairness (unclear where the randomness comes from).