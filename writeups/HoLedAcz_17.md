# The Dependence of Machine Learning on Electronic Medical Record Quality

L. Ho, D. Ledbetter, M. Aczon. [The Dependence of Machine Learning on Electronic Medical Record Quality.](https://arxiv.org/pdf/1703.08251.pdf) 2017.

## tl;dr
 - Tested three ML methods against variants of EMR data
 - Methods were logistic regression, 2-layer neural network, LSTM RNN
 - Data variants were training data size, input data types, and drug data encoding
 - Training data size had biggest effect; others were slight

## Thoughts
Exploration on sensitivity of popular machine learning methods on LA pediatric healthcare data. Not terribly novel, but important for a first glance at the reliability of EMR in the context of machine learning models

Authors describe the effects of the cross product of three methods (LR, NN, LSTM):
 * logistic regression: binary predictor of in-ICU predictor
 * neural network: two hidden layer neural network model with 256 hidden nodes each
 * recurrent neural network: long short term memory with 2 layers of 397 hidden nodes

with three data alterations
 * what percent of data is used for training
 * what type of features is used: internal, external, or both
 * how to encode the drug labels: values, binary, or group endoing based on medical subject heading

 Data used was cardiothoracic ICU and pediatric ICU data. In some cases, data was trained on CICU and then tested on PICU.

## Results
 - Training data size had the largest effect on performance (decreased)
 - Small differences between other models and data variants 

## Next steps
 - ML models on more sensitive temporal models (removing minutes here and there)
 - other tasks (besides ICU mortality) including disease onset