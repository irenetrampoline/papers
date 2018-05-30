# The Seven Pillars of Causal Reasoning 

Judea Pearl. [The Seven Pillars of Causal Reasoning with Reflections on Machine Learning.](http://ftp.cs.ucla.edu/pub/stat_ser/r481.pdf) Technical Report 2018. 

## tl;dr
 - Strong argument for the benefits of causal thinking
 - Formalization of SCMs and causal hierarchy
 - Description of seven pillars (or tasks) of causal questions, for example confounding and causal discovery.

## Causal Hierarchy
Pearl describes three topics of increasing difficulty: **association, intervention, and counterfactual**. Note that traditional machine learning deals primarily with association (e.g. What does this symptom tell me about this disease) compared to intervention (e.g. If I take stop eating gluten, what will my weight be?) and counterfactual (e.g. If my major and salary are this, what would have been my salary if I had majored in Art History?)

## Pillars
Given the structural causal model (graphical models, structural equations, and counterfactual and interventional logic), we can examine seven pillars of causal reasoning
 1. **Transparency** enables analysts to determine whether assumptions in the causal graph are encoded correctly. **Testability** through d-separation informs researchers which relationships are dependencies or independent.
 2. **Confounding** is the main concern for causal inference in that the an unmeasurable source is affecting both X and y. We can control for confounding through the *backdoor criterion*, which may not hold. In those cases, **do-calculus** predicts the effect of policy interventions.
 3. **Counterfactual** analysis can compute the probability of a sentence from the SCM with a focus on "causes of effects" as opposed to "effects of causes.
 4. **Mediation analysis** describes the mechanisms that transmit changes from a cause to its effects. That is, we want to decompose the total effect into direct and indirect effects of X -> M -> Y where there is also a link X -> Y. 
 5. **Adaptability, external validity, and sample selection** governs the ability for an SCM to move to a similar but different environment. We can achieve this by re-adjusting learned policies to overcome environment changes.
 6. **Missing data** provides yet another component that we can model. Missingness and variable value may be related, and we can formalize that relationship.
 7. **Causal discovery** allows us to find causal directions.

## Questions
 * What do we lose by focusing entirely on SCM?
 * How does temporal data play out?
 * How do we truly evaluate?