# The Golem of Prague
The golem of Prague is the most famous story of the golem, and animated clay figure inscribed with *emet*, truth in Hebrew, on its brow. Animated by truth, but lacking free will, the golem always does exactly what is told. The golem of Prague got the wrong orders, and by mistake wrecked Prague. 

## Statistical golems
Scientists make golems too. These golems are scientific models following computational rules.
There are multiple types of model-golems with great logic and power, but *without wisdom*,  that is the **model doesn't know when something is wrong**. It just does as it's told!
All the classical statistical test are fragile, as they often break when introduced to novel data/situations. The classical tools are not diverse enough to handle many common research questions.

## Statistical rethinking:
When choosing a test, rather than **utilizing Bayesian statistics** one may feel *anxious* of **choosing the right test**.  When using **Bayesian statistics** the *anxiety is focused* on *doing it wrong*.
But that *anxiety* **forces** you to *understand the computational* nuts and bolts of the **golem** (model).  If you don't understand how the golem works, you can't interpret the output of the golem.

1) **Hypotheses are not models**.
	   The relations among hypotheses and different kinds of models are complex. 
	   Many models correspond to the same hypothesis, and many hypotheses correspond to a single model. *This makes strict falsification impossible.*
2) **Measurements matters**.
	   Even when we **think the data falsify a model**, *another observer* will *debate* out **methods and measurement**. They don't trust the data. Sometimes they are right.

For both these reasons, **deductive falsification never works**. *The Scientific Method* cannot be reduced to a *statistical procedure*. But **keep the complex world** of priors, methods and other studies **in mind**.

### Hypotheses are not models.
**Hypotheses** do not imply **unique models**, and **models** do not imply **unique hypotheses**. This fact greatly complicates statistical inference.
![[Hypotheses are not models.png]]

1) **Any given statistical model (M)** may *correspond to more* than one **process model (P).**
2) **Any given hypothesis (H)** may *correspond to more* than one **process model (P).**
3) **Any given statistical model (M)** may *correspond to more* **than one hypothesis (H)**.

## Measurement matters.
The **logic of falsification is very simple**. We have a **hypothesis H**, and we show that it *entails some observation D*. Then we *look for D*. If we **don’t find D**, we must conclude that **H is false**.
> [!INFO] The black swans of Australia
> Before discovering Australia, **all swans that any European had ever seen had white feathers.**
> This led to the belief that all swans are white. Let’s call this a formal hypothesis:
>> [!question] H0: All swans are white.
 >
> When *Europeans reached Australia*, however, they *encountered swans with black feathers*.
> This **evidence seemed to instantly prove H0 to be false**. Indeed, not all swans are white. Some swans are certainly black, according to all observers.

**The key insight** here is that, *before voyaging to Australia*, *no number of observations* of **white swans could prove H0** to be *true*.  However it required only one observation of a black swan to prove it false.

### Observation error.
All **observers** will agree under most **conditions** that a swan is either **black or white**. 
But this **kind of example** is *hardly commonplace in science*, at least in mature fields. Instead, we routinely confront contexts in which **we are not sure** if we have *detected a disconfirming result.* 
There are *mistaken confirmations (false positives)* and **mistaken disconfirmations (false negatives).**

### Continuous hypotheses. 
Another problem for the swan story is that *most* interesting *scientific hypotheses* are not of the kind “all swans are white” but rather of the kind:
> [!question] $H_0$: 80% of swans are white

or:
> [!question] $H_0$:  Black swans are rare

**What can one say after seeing one black swan?** The task here is not to *disprove* or *prove* a **hypothesis**, but *rather* to *estimate* and *explain* a **distribution of swan coloration**. 


### [[Tools of model engineering]]