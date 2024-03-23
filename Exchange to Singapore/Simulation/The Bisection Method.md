The Bisection method is used for continuous random variables.
It is implementable for cases where:
* We know the f(x) of the distribution.
* We can't find the inverse function. 


Algorithm in own words:
* We generate an U, from unif(0,1)
*  We take a large interval of X, with range(a, b)
* Until accuracy is sufficient:
	* Take the $x_{i}$ in the middle of the interval range ($x_{i}=\frac{ab}{2}$)
	* Find $f(x_{i})$ and check if $f(U)$ falls in range $[f(a), f(x_{i})]$ or $[f(x_{i}), f(b)]$
		* If in $[f(a), f(x_{i})]$, then update $b = x_{i}$.
		* If in $[f(x_{i}), f(b)]$, then update $a = x_{i}$
When interval is small enough, then return the $x_{i}$

![[Bisection_method_from_wiki.png]]
#### Pseudo-code from wikipedia
**input:** Function _f_, 
       endpoint values _a_, _b_, 
       tolerance _TOL_, 
       maximum iterations _NMAX_
**conditions:** _a_ < _b_, 
            either _f_(_a_) < 0 and _f_(_b_) > 0 or _f_(_a_) > 0 and _f_(_b_) < 0
**output:** value which differs from a root of _f_(_x_) = 0 by less than _TOL_
 
_N_ ← 1
**while** _N_ ≤ _NMAX_ **do** _// limit iterations to prevent infinite loop_
    _c_ ← (_a_ + _b_)/2 _// new midpoint_
    **if** _f_(_c_) = 0 or (_b_ – _a_)/2 < _TOL_ **then** _// solution found_
        Output(_c_)
        **Stop**
    **end if**
    _N_ ← _N_ + 1 _// increment step counter_
    **if** sign(_f_(_c_)) = sign(_f_(_a_)) **then** _a_ ← _c_ **else** _b_ ← _c_ _// new interval_
**end while**
Output("Method failed.") _// max number of steps exceeded_
