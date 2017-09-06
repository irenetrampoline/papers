# Classification of common human diseases derived from shared genetic and environmental determinants

Kanix Wang,	Hallie Gaitsch,	Hoifung Poon, Nancy J Cox, Andrey Rzhetsky. [Classification of common human diseases derived from shared genetic and environmental determinants.](http://www.nature.com/ng/journal/v49/n9/full/ng.3931.html) Nature Genetics 49, 2017. 

## tl;dr
 - Look at genetic and environmental correlations between disesases to construct etiological disease taxonomy.
 - Takeaway 2
 - Open question or critique

## Contributions
What is this paper showing? What are the contributions? What kind of paper is it: theoretical, applied, something in the middle? Where does it fit into the prior body of work?


## Data

The paper uses insurance claims from Truven MarketScan, which contains information from roughly one third of the US population.
 
 - Of available data, only used 129k due to inclusion criteria
 - Focuses on parents and children that were both "visible" for at least 6 years

## Heritability
 - The more heritable, the less prevalent a disease is.
 - Of 65 diseases that had previously published heritability estimates, 52 agreed with estimates within 95% CI interval. 
 - Verify common wisdom that early onset has higher heritability w/ correlation, and showed no correlation across all diases but showed links within smaller categories

## Genetic and environmental correlations
 - Focused on 29 diseases which are well represented in parents and children in data. Applied pairwise correlation assuming a 1% false discovery rate.
 - Genetic correlations stronger than environmental correlations. For neuropsychiatric disease pairs, genetic and environmental correlations were equal.
 - Confidence intervals for family-based estimates were much narrower than an earlier genome-wise association study, due to the large sample size of the dataset.
 - Some common diseases (asthma, rhinitis, dermatitis) were surprisingly correlative genetically.
 - Used ICD-9 taxonomy to compared against genetic and environmental correlations. Migranes is considered a digestive illness?

## Nosologies
 - Defining distance as 1 - correlation, we can sample distances from the posterior distribution of a disease. I'm assuming classification is nearest neighbors based on distances as probabilities. 

## Discussion
 - Considerations for bias: urban, more affluent, assortive mating, lack of ethnicity and race information.

## Methodology (updated)
 - Starts with linear model of y = X\beta + a + c + s + f + e
 - Variance of y can be decomposed into different factors

## Extensions
 - David's student took BCBS data and did a similar study about genetic and environment. Had race data
 - Probability of getting disease if your parent had it?
 - Diseases diagnosed after age of 30 would be missed.

## Questions
 - What are GCS and GC models? What methods in addition to straight correlation are done? Could be done?
 - What does unique environment vs common-couple mean? Common couple probably means a couple that has a child, but what about unique environment?
 - What kind of enviornmental data did they have? 
 - Why these spiral visualizations? Hard to compare y-values but does give long x-axis for bar chart.
 - Still confused about classification by sampling stuff?