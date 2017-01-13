# Combatting Police Discrimination in the Age of Big Data

S. Goel, M. Perelman, R. Shroff, D. Sklansky. [Combatting Police Discrimination in the Age of Big Data.](https://5harad.com/papers/policing-the-police.pdf) New Criminal Law Review 2016. 

## tl;dr
 - Courts historically have ruled against statistical evidence in stop and frisk cases as insufficient to prove intentional racial discimination
 - Authors propose a SHR (stop-level hit rate) model to analyze NYC police data and calculate how "successful" a stop will be
 - I'm curious about whether or not this is a data problem, a human problem, or a formalization problem. What probability would be sufficient? Are there latent variables not included that police officers are trained to act on? 

## Thoughts
With such a politically charged topic, the authors do not hide their displeasure about the lack of rigor in prior court cases against racial discrimination. In particular, the age of big data suggests that we should examine the context in which a Terry stop (stop-and-frisk intrusion named after Terry v Ohio) and in particular if the officer or department has a history of treating minorities unfairly. The court requires intentional discrimination on the police officer's part in this particular instance, whereas the police officer's justification for stopping may be less rigorous has long as they articulate "factual basis."

Much of the paper examines the legal history of racially motivated cases usually involving police officers or government officials. This is unsurprising since the paper appears in a law review journal. For me, however, that was less interesting. Essentially courts make monumental decisions based on case studies, and if various details of the case (e.g. the data wasn't collected in the same year or races like Hispanic are marked based on visual inspection) are flimsy, the entire argument could get thrown out. The nature of statistics relies on multiple instances, however, so the two seem to be at odds. That does not stop the authors from championing their SHR (stop-level hit rate model).

The SHR attempts to provide rigor, aka a predictive model in the form of logistic regression, to the fuzzy task of police supervision. The model is trained on 3 years of data gathered by the New York Police Department (NYPD) and then tested on the following two years of data. According to the authors, the model is fairly accurate, robust to errors (like miscalculating age, weight, and height), and could improve the NYPD practices. I am skeptical of the usefulness of this model given the possible overtraining of the model and the immense legal obstacles rather than data problems of the situation, but it does demonstrate that big police data models are possible!

One last non-PC note is that I wasn't entirely convinced by the authors that each of these instances were clearly egregious infractions. I do very much believe the police officers may target racial groups (for convenience, malice, or incompetence is unclear and probably unimportant), but I do see the side of the police officers in weighing various factors and attempting to do their job day-to-day. In one disappointing paragraph, the authors mention very briefly the idea that police officers do purposefully unsuccessful Terry stops as an effort to suppress organized crime in the area before rejecting the idea as "romanticized." I lack the context to make a judgement on that, but the authors gave no further supporting evidence for a strong claim. 

Overall, a welcome respite from the CS papers to something more applied. 

## Legal efforts to rule out Terry stops
 - Court has ruled that it's necessary for a police person's proper investigative function, but not outside scope of Fourth Amendment (police officer's hope) or flatly unconstitutional (civilian's hope)
 - Officer must articulate "factual basis", doesn't matter if racially motivated
 - Cannot use statistical alone to show discriminatory intent 
 - Courts skeptical that statistical analysis is rigorous enough, moving towards more amenable to statistics in recent years
 - Floyd v New York: outlined what statistical analysis would need to show
Terry stops under Fourteenth Amendment 

## SHR (stop-level hit rate) method for reducing police discrimination
- What is the probability that a stop with be "successful"?
- Authors fit a logistic regression, which was reasonably accurate and robust
- Found lots of stops with low probability of finding anything
- Controlling for location, still see racial effects
- "Romanticized" outlook for stop and frisk to suppress organized crimes
obstacles to full data analysis and considering stop and frisk as a policy
- SHR can help improve efficiency and fairness of stop and frisk
- SHR can revisit judicial assessment of stop and frisk policies (outright discrimination or aggressive policing)