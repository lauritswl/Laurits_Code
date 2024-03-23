---
title: "Tutorial_1_Simulation"
author: "Laurits"
date: "2024-02-01"
output:
  pdf_document: default
  html_document: default
---

# Tutorial 1
## Q1
### a) i
We return Y when x greater than or equal to the CDF off y.
1. We check if $x \le \sum{p_0} <=> x \le P(Y=0)<=> x \le 0.2 $ 
if this is not true we check for the second k.
2. We check if $x \le \sum{p_1} <=> x \le P(Y=0)+P(Y=1)<=> x \le 0.2 + 0.3 <=> x \le 0.5 $ 
if this is not true we check for the third k.
3. We check if $x \le \sum{p_2} <=> x \le P(Y=0)+P(Y=1)+P(Y=2)<=> x \le 0.2 + 0.3 + 0.4 <=> x \le 0.9 $ 
if this is not true we check for the fourth k.
4. We check if $x \le \sum{p_3} <=> x \le P(Y=0)+P(Y=1)+P(Y=2)+P(Y=3)<=> x \le 0.2 + 0.3 + 0.4 + 0.1<=> x \le 1 $ 

If any of these statements were true, the algorithm ends, by returning the Y. Statement 4 will always be true.

### a) ii
The probability that Y = 2 is 0.4

### b) i
The interval of X on which we will get Y = k is:
$$(\sum^{y}_{k=0}{p_{k-1}}:\sum^{y}_{k=0}{p_{k}}]$$




### b) ii
So, the probability is:
$$\frac{\sum^{y}_{k=0}{p_{k}}-\sum^{y}_{k=0}{p_{k-1}}}{1-0}$$
## Q2
### a) 
**Find the CDF:**
F(i) = $p(Y \le i)$ = $\sum^{i}_{k=1}{\frac{1}{k(k+1)}}$ = $\sum^{i}_{k=i}{\frac{1}{k}-\frac{1}{k+1}}$ 

### b)
**Find G() for $x \ge 0$**
$G(i + 1)$ = $1-\frac{1}{i+1}$

### c)
**Find $G^{-1}(x)$**
$G(i+1) = 1-\frac{1}{i+1}$ 
$y=1-\frac{1}{x}$ 
$1-y=\frac{1}{x}$ 
$x=\frac{1}{1-y} = G^{-1}(y)$ 


### d)
Step 1. Generate X ~Unif(0,1)
Step 2. Let Y = [1/(1-X)]
Step 3. Return Y


## Q3
For the following integrals, please write out the pseudo code to calculate them with the
Monte Carlo integration:

```r
set.seed(2024)
```

### a)


```r
q3a <- function(X){
  exp(1)^(X+X^2)
}
```


```r
# integral[-2:2](e^{x+x^2})
from <- -2
to <- 2
total_length <- to-from
N <-  100000
sim_a <- runif(N)*total_length+from
sim_y_a <- q3a(sim_a)

integral_approx <- (total_length/N)*sum(q3a(sim_a))
paste("The Monte Carlo integration is approximated too:",round(integral_approx,2))
```

```
## [1] "The Monte Carlo integration is approximated too: 92.69"
```


### b)


```r
h <- function(x) {
    exp(1)^-(x^2)
}
```


```r
N=10000
Z <- runif(N)
negative <-  1-1/Z
positive <-  1/Z-1
int_positive <- h(positive)*1/(Z^2)
int_negative <- h(negative)*1/(Z^2)
new_z <- int_negative + int_positive
paste("The Monte Carlo integration is approximated too:",round(mean(new_z),2))
```

```
## [1] "The Monte Carlo integration is approximated too: 1.78"
```

**How do we find out that we need to 1/Z^2 to get the correct scale?**

### c) 

```r
h <- function(x,y) {
    exp(1)^(x+y)^2
}
```

```r
N=10000
X <- runif(N)
Y <- runif(N)

paste("The Monte Carlo integration is approximated too:",round(mean(h(X,Y)),2))
```

```
## [1] "The Monte Carlo integration is approximated too: 4.92"
```
### d)
Is it possible to see the code of how prof expected this to be solved?


4)

```r
N <- 10000
num_iterations <- 1000
results <- vector("numeric", length = num_iterations)

for (i in 1:num_iterations) {
  U <- runif(N)
  result <- cov(U, exp(1)^U)
  results[i] <- result
}
paste("Mean:",mean(results))
```

```
## [1] "Mean: 0.140906404247999"
```

```r
paste("SD:",sd(results))
```

```
## [1] "SD: 0.001288881455618"
```









