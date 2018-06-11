# Learning to Ask Good Questions

Sudha Rao, Hal Daume. [Learning to Ask Good Questions: Ranking Clarification Questions using Neural Expected Value of Perfect Information.](https://arxiv.org/pdf/1805.04655.pdf) ACL 2018.

## tl;dr
 - As the title suggests, the authors rank clarification questions for an original question to get more succinct help.
 - Since I did an NLP final project similar to this project, I am particularly intrigued. 
 - Neural network architecture is novel, and the real question seems to be dataset generation. 

## Test Time Pipeline
 1. Given a post p, retrieve 10 similar posts in the training set using Lucene 
 2. The questions asked by those 10 similar posts p_i are then q_i and become the candidate set Q. Edits made to post in response to the questions are answer set A.
 3. For each possible clarification question q_i, we generate an answer representation F(p, q_i) and calculate how close answer candidate a_j is to F(p, q_i)
 4. We then calculate utility gain to post p if it were updated with answer a_j
 5. Given expected utilities, we rank candidate questions by expected utility.

## Loss functions
From the pipeline, we see that a lot of steps involve quantifying "better" questions, answers, and utility functions. Without getting too mathematical (mostly because I haven't figured out how to implement MathJax on my Github pages), we describe the fucntions.

 1. Lucene uses a variant of TF-IDF to find related documents
 2. No math, just aggregation.
 3. Answer representation F(p, q_i) comes from a neural representation. Answer distance is calculated with cosine similarity of the average word vector of answer a_j.
 4. Expected utility depends on the probability of answer candidate a_j being the answer to question q_i and the utility value of adding the information. We model the probability P(a_j | p, q_i) as a negative exponential of the distance between F(p, q_i) and a-hat_j or the average word vector. The utility function is defined as the sigmoid of F_util where F_util is also a neural network.
 5. We sort by expected utilites then.

The neural networks mentioned are one joint model using a question LSTM and an answer LSTM with a loss function based on the existing triples (post, question, and answer). 

## Evaluation
Because of the tricky nature of the experimental setup, expert annotators are vital. Evaluations are conducted with expert annotations, against the original question, and excluding the original question.

## Next steps
For my person research, it might be useful to think about health question and answering and how to automate a health knowledge graph. Isn't this classification model another type of HKG?