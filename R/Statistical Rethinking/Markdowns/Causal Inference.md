# What is Causal Inference?
*Attempt to understand a model using data.*
More than a **association** between variables.
## Causal prediction
Casual inference is a very special type of prediction 
	> Knowing a *cause* means being able to predict the *consequences* of an *intervention*. 
		-> *"What if I do this?"*
**Example of trees moving:**
Imagine you create a experiment where a bunch of your friends shake a tree. You will know that if you shake a tree, the trees leaves will move. But if the trees shakes, you wont think that your friends is shaking the tree, you would rather believe the wind is blowing.

## Causal Imputation
Knowing a **cause** means being able to construct unobserved **counterfactual outcomes**.
	> *"What if I had done something else?"*
This is often thought of as explanation



# Directed Acyclic Graphs ([[Statistical Rethinking Vocabulary#DAGs|DAGs]])

Is a Heuristic casual models (you can analyse them with your eyes)
Can be analysed to deduce appropriate statistical models
![[Directed_Acyclic_Graphs_DAGs.png]]
The letters are variables.
The arrows are causes.
All queries need different DAGs.
****