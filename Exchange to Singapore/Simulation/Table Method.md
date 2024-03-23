  Consider a random variable X with the following probability mass function:
$$p_{0} = 0.3,\ p_{1} = 0.2, \ p_{2} = 0.35, \ p_{3} = 0.15$$
1. Set up a table A of length 100, i.e. M = 100.  
2. For 0, define the first 30 elements as 0, the next 20 elements as 2, the following 35 entries as 2 and the final 15 elements as 3.  
3. Generate $U ∼ Unif (0, 1)$.  
4. Return $X = A(\lfloor100\cdot U\rfloor + 1)$.
