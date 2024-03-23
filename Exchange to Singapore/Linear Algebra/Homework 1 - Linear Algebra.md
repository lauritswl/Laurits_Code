**Name**: Laurits Wieslander Lyngbaek
**Student number**: A0290227H
**Tutorial class**: Tutorial 16 
#### 1) Solve the following linear systems by Gauss-Jordan Elimination

**System of equations:**
$$\begin{cases} 
x - 2y + z + w = 4 \\
2x + y − 3z − w = 6 \\
x − 7y − 6z + 2w = 6
\end{cases}$$
**Convert to matrix and us Gaussian Elimination:**
$$\begin{pmatrix}
1 & -2 & 1 & 1 & 4 \\
2 & 1 & -3 & -1 & 6 \\ 
1 & -7 & -6 & 2 & 6
\end{pmatrix}
=_{r_3-r_1}^{r_{2}-2r_1}
\begin{pmatrix}
1 & -2 & 1 & 1 & 4 \\
0 & 5 & -5 & -3 & -2 \\ 
0 & -5 & -7 & 1 & 2
\end{pmatrix} 
=^{r_3+r_2}
\begin{pmatrix}
1 & -2 & 1 & 1 & 4 \\
0 & 5 & -5 & -3 & -2 \\ 
0 & 0 & -12 & -2 & 0
\end{pmatrix}$$
**Gauss-Jordan Elimination:**
$$\begin{pmatrix}
1 & -2 & 1 & 1 & 4 \\
0 & 5 & -5 & -3 & -2 \\ 
0 & 0 & -12 & -2 & 0
\end{pmatrix}
=^{r_{2} =\frac{1}{5}r_2}_{r_{3}-\frac{1}{12}r_3}
\begin{pmatrix}
1 & -2 & 1 & 1 & 4 \\
0 & 1 & -1 & -\frac{3}{5} & -\frac{2}{5} \\ 
0 & 0 & 1 & \frac{1}{6} & 0
\end{pmatrix}
=^{r_{2}+r_{3}}_{r_{1}-r_{3}}
\begin{pmatrix}
1 & -2 & 0 & \frac{5}{6} & 4 \\
0 & 1 & 0 & -\frac{13}{30} & -\frac{2}{5} \\ 
0 & 0 & 1 & \frac{1}{6} & 0
\end{pmatrix}$$
$$
=^{r_{1}+2r_{2}} 
\begin{pmatrix}
1 & 0 & 0 & -\frac{1}{30} & \frac{16}{5} \\
0 & 1 & 0 & -\frac{13}{30} & -\frac{2}{5} \\ 
0 & 0 & 1 & \frac{1}{6} & 0
\end{pmatrix}
=^{r_{1}+\frac{\frac{1}{30}}{\frac{1}{6}}r_{3}}_{r_{2}+\frac{-\frac{13}{30}}{\frac{1}{6}}r_{3}}  
\begin{pmatrix}
1 & 0 & 0 & 0 & \frac{16}{5} \\
0 & 1 & 0 & 0 & -\frac{2}{5} \\ 
0 & 0 & 1 & \frac{1}{6} & 0
\end{pmatrix}$$
$$Solution = \begin{cases}
x = 3\frac{1}{5}\\
y = -\frac{2}{5}\\
z = 1 + \frac{1}{6}s
\end{cases}$$

#### 2a) Use Gauss-Jordan Elimination to reduce:

**Gaussian Elimination:**
$$A = \begin{pmatrix}0 & 1 & -3 \\ 2  & 3 & -1 \\ 4 & 5 & -2\end{pmatrix}$$
Step 1: The first column is the leftmost nonzero column
Step 2: Interchange the first and second row
$$A = \begin{pmatrix} 2  & 3 & -1 \\ 0 & 1 & -3 \\4 & 5 & -2\end{pmatrix}$$
Step 3: Subtract 2 times the first row to the third row
$$A = \begin{pmatrix} 2  & 3 & -1 \\ 0 & 1 & -3 \\0 & -1 & 0\end{pmatrix}$$
Step 4: Cover the first row and begin again with step 1 applied to the submatrix that remains
$$A = \begin{pmatrix} 2  & 3 & -1 \\  0 & 1 & -3 \\0 & -1 & 0\end{pmatrix}$$Step 1: The second column is the leftmost nonzero column
Step 2: No action needed
Step 3: Add the second row to the third row
$$A = \begin{pmatrix} 2  & 3 & -1 \\  0 & 1 & -3 \\0 & 0 & -3\end{pmatrix}$$

**The matrix is now an upper triangular matrix.**
#### 2b) Find the 3 elementary matrixes used to perform 2a
**I did the following:**
1) Interchange first and second row
$$I =\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix} \rightarrow
\begin{pmatrix}0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1\end{pmatrix} = E_{1}$$
2) Subtract the first row from the third row twice
   $$I =\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix} \rightarrow
\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ -2 & 0 & 1\end{pmatrix} = E_{1}$$
3) Add the second row to the first row:
   $$I =\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix} \rightarrow
\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 1 & 1\end{pmatrix} = E_{1}$$
#### 3a) Consider the following matrix equation where x, y, z are unknowns and λ is a constant
$$
\begin{pmatrix}3 & -2 & 0 \\ -2 & 3 & 0 \\ 0 & 0 & 5\end{pmatrix}
\begin{pmatrix}x \\ y \\ z\end{pmatrix} =
\lambda \begin{pmatrix}x \\ y \\ z\end{pmatrix}$$
Rewrite the matrix equation as a homogeneous system of linear equations  
in variables x, y and z

$$
\begin{cases} 
3x - 2y + 0z = \lambda x \\
-2x + 3y − 0z = \lambda y \\
0x + 0y + 5z = \lambda z
\end{cases} 
\ 
\leftrightarrow 
\ 
\begin{cases}
3x- \lambda x - 2y =  0\\
-2x + 3y - \lambda y= 0 \\
5z - \lambda z =0 \\
\end{cases} 

\leftrightarrow 
\ 
\begin{cases}\begin{align*}
(3-\lambda)x - 2y =  0\\
-2x + (3-\lambda)y= 0 \\
(5-\lambda)z = 0 \\
\end{align*}\end{cases} 
$$
$$\begin{align*} (3-\lambda)x - 2y &= 0 \\ -2x + (3-\lambda)y &= 0 \\ (5-\lambda)z &= 0 \end{align*}$$



#### 3B) Find all possible values of λ such that (a) has a nontrivial solution
By Cramer's rule, for the linear system $Ax=b$, then the system only has one solution if A is invertible. A is only invertible if $det(A) \ne 0$. All cases of where $A = 0$ has a nontrivial solution.,   

**Find the determinant of A**:
$$A =
\begin{pmatrix}
3-\lambda & -2 & 0\\ 
-2 & 3-\lambda & 0\\ 
0 & 0 & 5-\lambda
\end{pmatrix}$$
$$det(A)=a_{31}A_{31}+a_{32}A_{32}+a_{33}A_{33}$$
where, $A_{ij} = (-1)^{ij} det(M_{ij})$.
$$ det(A) = 0A_{31}+0A_{32}+(5-\lambda)(-1)^{3+3}det(\begin{pmatrix}3-\lambda & -2 \\ -2 & 3-\lambda\end{pmatrix})$$
$$det(A) = (5-\lambda)((3-\lambda)^2-(-2)^2)=(5-\lambda)(\lambda^2-6\lambda+9-4)$$
$$det(A) = (5-\lambda)(\lambda^2-6\lambda+5)$$
We have now found the determinant. The determinant isn't 0, unless except the following cases:
$$Det(A) = 0, when \begin{cases}
0 = 5-\lambda \\
0 = \lambda^{2}-6\lambda+5
\end{cases}$$
**CASE 1**:
$$0 = 5-\lambda \leftrightarrow \lambda=5$$
**CASE 2:**
$$0 = \lambda^{2}-6\lambda+5 \rightarrow \frac {-b \pm \sqrt{b^{2}-4ac}}{2a} = \frac {-(-6) \pm \sqrt{(-6)^{2}-4\cdot1\cdot5}}{2\cdot 1}$$
$$\lambda = \frac{6 \pm 4}{2} \begin{cases}
\lambda = \frac{6 + 4}{2} = 5 \\
\lambda = \frac{6 - 4}{2} = 1
\end{cases}$$
**CONCLUSION**; (a) has a nontrivial solution when $\lambda = 1$ or $\lambda = 5$.
#### 3C) For each λ found in (3b), find the corresponding general solution set
**CASE 1**: Solution set when $\lambda = 5$
$$
\lambda =5 \rightarrow 
\begin{pmatrix}
-2  & 3-5 & 0  \\ 
3-5 & -2 & 0  \\ 
0 & 0 & 5-5 
\end{pmatrix}
=
\begin{pmatrix}
-2  & -2 & 0  \\ 
-2 & -2 & 0  \\ 
0 & 0 & 0 
\end{pmatrix}
=
\begin{pmatrix}
-2  & -2 & 0  \\ 
0 & 0 & 0  \\ 
0 & 0 & 0 
\end{pmatrix}
=
\begin{pmatrix}
1  & 1 & 0  \\ 
0 & 0 & 0  \\ 
0 & 0 & 0 
\end{pmatrix}
$$
$$\begin{cases}
x_{1} = -x_{2} \\
x_{2} = arbitrary \\
x_{3} = arbitrary
\end{cases}$$
**CASE 2:** Solutions set when $\lambda = 1$
$$
\lambda = 1 \rightarrow 
\begin{pmatrix}
-2  & 3-1 & 0  \\ 
3-1 & -2 & 0  \\ 
0 & 0 & 5-1 
\end{pmatrix}
=
\begin{pmatrix}
-2  & 2 & 0  \\ 
2 & -2 & 0  \\ 
0 & 0 & 4 
\end{pmatrix}
=
\begin{pmatrix}
-2  & 2 & 0  \\ 
0 & 0 & 0  \\ 
0 & 0 & 4 
\end{pmatrix}
=
\begin{pmatrix}
1  & -1 & 0  \\ 
0 & 0 & 0  \\ 
0 & 0 & 1 
\end{pmatrix}
$$

$$\begin{cases}
x_{1} = x_{2} \\
x_{2} = arbitrary \\
x_{3} = 0 
\end{cases}$$
#### 4) For which value of t does the following system have (a) no solution, (b) exactly one solution, or (c) infinitely many solutions? Justify your answers

First the system is transformed to 
$$\begin{cases}
\begin{align*}
x + y + z = 4 \\
z = 2\\
(t^{2} − 4)z = (t − 2)
\end{align*}
\end{cases} 
\rightarrow
\begin{pmatrix}1 & 1 & 1 & 4 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & (t^{2}-4) & (t-2)\end{pmatrix}$$

I perform gaussian elimination to reduce the matrix to row echelon form, by subtracting $r_{3}- (t^{2}-4)r_{2}$:
$$\begin{pmatrix}1 & 1 & 1 & 4 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & (t^{2}-4) & (t-2)\end{pmatrix} = \begin{pmatrix}1 & 1 & 1 & 4 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & -2(t^{2}-4)+t-2\end{pmatrix}= \begin{pmatrix}1 & 1 & 1 & 4 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & -2t^{2}+t-6\end{pmatrix}$$
**CASE 1:** $-2t^{2}+t-6 = 0$ (**Infinitely many solutions**)
In case 2 the last row of the matrix would be a zero-row, thus making the system consistent.
As the first row has a non-pivot column this system would qualify for infinitely many solutions.
We can solve the equation using the quadratic formula: 
$$\frac{1 \pm \sqrt{1-4*2*(-6)}}{2*2}= \frac{1 \pm \sqrt{49}}{4} = \frac{1 \pm 7}{4}$$
So, there exists **infinitely many solutions** for these two t values:  
$$\begin{cases}
t = \frac{1+7}{4} = \frac{8}{4} = 2\\
t = \frac{1-7}{4} = -\frac{6}{4} = -\frac{3}{2} 
\end{cases}$$
**CASE 2**: $-2t^{2}+t-6 \neq 0$. (**No solutions**)

For the remaining values of t, it can be derived from the structure of the matrix that the system is inconsistent, and therefore has no solution.  (As the last non-zero row only has a single non-zero value in the right most column).
This is true for values of $t \in \mathbb{R} \land (t \neq 2 \land t \neq -\frac{3}{2})$.
#### 5) Let A = ($a_{ij}$) and B = ($b_{ij}$) be two n × n lower triangular matrices. i.e. $a_{ij} = b_{ij} = 0$ if $i < j$.
##### A) show that the ($i, j$)-entry of AB is 0 if $i < j$, i.e. AB is a lower triangular matrix.
From the definition of a matrix product we have:
$$AB_{ij} = \sum\limits^n_{k = 1}a_{ik}b_{kj}$$


This can be diverted into two cases.
$$
AB_{ij} = \sum\limits^n_{k = 1}a_{ik}b_{kj} =I + II \begin{cases}
I = \sum\limits^{i}_{k = 1}a_{ik}b_{kj} \\
II = \sum\limits^{n}_{k = i+1}a_{ik}b_{kj}
\end{cases}$$
As both $a_{ik}$ and $b_{kj}$ are lower  triangular matrices, we have:
1. For case $I$, it is always true that $k < j$ when $i < j$. 
    If $k < j$ then $b_{kj} = 0$ since B is a lower triangular matrix. Hence $a_{ik}b_{kj} = 0$ when i < j.
2. If $i < k$ then $a_{ik} = 0$ since A is lower triangular. Hence $a_{ik}b_{kj} = 0$.
Since $i < j$, then for every k we have $i < k < j$, and all possible k are covered by the two cases.

##### B) Find the (i, i)-entry of AB.
We start by the AB definition:
$$AB_{ij} = \sum\limits^n_{k = 1}a_{ik}b_{kj}$$
$j$ is substituted by $i$:
$$AB_{ii} = \sum\limits^n_{k = 1}{a_{ik}b_{ki}} 
=I + II + III = \begin{cases}
I_{k<i} = \sum\limits^{i-1}_{k = 1}a_{ik}b_{ki} =0 \\
II_{k=i} = a_{ii}b_{ii}  \\
III_{i < k} = \sum\limits^{n}_{k = i+1}a_{ik}b_{ki} = 0
\end{cases} = II = a_{ii}*b_{ii}$$
The $(i,i)$-entry of the AB matrix is therefore:
$$(AB)_{ii}=a_{ii}​b_{ii}​$$
#### 6) For which real numbers a and b does the following linear system have (a) no solution, (b) exactly one solution, or (c) infinitely many solutions? Justify your answers.
$$
\begin{pmatrix} 
(a-1) & (a+3) & 1 & 1 \\ 
a & a^{2} & 1 & 1 \\ 
1 & a & 1 & b
\end{pmatrix}
=
\begin{cases}\begin{align*}

(a − 1)x +(a + 3)y +z = 1 \\
ax +a^{2}y +z = 1 \\
x+ay +z = b
\end{align*}
\end{cases}$$
$$R_{1} \leftrightarrow R_{3}: 
\
\begin{pmatrix} 
1 & a & 1 & b \\ 
a & a^{2} & 1 & 1 \\ 
(a-1) & (a+3) & 1 & 1
\end{pmatrix}$$
$$R_{2} -aR_{1} \rightarrow R_{2}:
\
\begin{pmatrix} 
1 & a & 1 & b \\ 
a-a & a^{2}-a^2 & 1-a & 1-ab \\ 
(a-1) & (a+3) & 1 & 1
\end{pmatrix} =
 \begin{pmatrix} 
1 & a & 1 & b \\ 
0 & 0 & 1-a & 1-ab \\ 
(a-1) & (a+3) & 1 & 1
\end{pmatrix}$$
$$R_{3} -(a-1)R_{1} \rightarrow R_{3}:
\

\begin{pmatrix} 
1 & a & 1 & b \\ 
0 & 0 & 1-a & 1-ab \\ 
(a-1)-(a-1) & (a+3)-(a^{2}-1a) & 1-(a-1) & 1-(ab-b)
\end{pmatrix}$$
$$= 
\begin{pmatrix} 
1 & a & 1 & b \\ 
0 & 0 & 1-a & 1-ab \\ 
0 & a^{2}+2a+3 & 2-a & 1-ab+b
\end{pmatrix}$$
$$R_{1} \leftrightarrow R_{3}:
\begin{pmatrix} 
1 & a & 1 & b \\ 
0 & a^{2}+2a+3 & 2-a & 1-ab+b\\ 
0 & 0 & 1-a & 1-ab 
\end{pmatrix}
$$

We now need to make assumptions to continue:
##### CASE 1a: $a = 1$, $b \ne 1$ (**NO SOLUTIONS**) 
If $a=1$ then the matrix has the following form:
$$\begin{pmatrix} 
1 & 1 & 1 & b \\ 
0 & 6 & 1 & 1\\ 
0 & 0 & 0 & 1-b 
\end{pmatrix}
$$
This system is **inconsistent** and results in *no* solutions, if $b \ne 1$.

##### CASE 1b: $a = 1$, $b = 1$ (INFINITELY MANY SOLUTIONS) 
If $b = 1$ then the system the following form
$$\begin{pmatrix} 
1 & 1 & 1 & 1 \\ 
0 & 6 & 1 & 1\\ 
0 & 0 & 0 & 0 
\end{pmatrix}$$
And has infinitely many solutions as column 3 has no pivot point.

##### CASE 2: $a \ne 1$, $b = \mathbb{R}$ (ONE SOLUTION)
If $a \ne 1$ then $\frac{1}{1-a} \ne \frac{1}{0}$ and thereby we are allowed to do $\frac{1}{1-a} R_{3}$.
$$\begin{pmatrix} 
1 & a & 1 & b \\ 
0 & a^{2}+2a+3 & 2-a & 1-ab+b\\ 
0 & 0 & 1-a & 1-ab 
\end{pmatrix}$$
$$

\frac{1}{1-a}R_{3} \rightarrow R_{3}:
\begin{pmatrix} 
1 & a & 1 & b \\ 
0 & a^{2}+2a+3 & 2-a & 1-ab+b\\ 
0 & 0 & 1 & \frac{1-ab}{1-a} 
\end{pmatrix}
$$
$$R_{2}-(2-a)R_{3}:
\begin{pmatrix} 
1 & a & 1 & b \\ 
0 & a^{2}+2a+3 & 0 & 1-ab+b-\frac{(2-a)(1-ab)}{1-a}\\ 
0 & 0 & 1 & \frac{1-ab}{1-a} 
\end{pmatrix}$$
If we can reduce $a^{2}+2a+3$ to $1$ then the system is consistent, and has one solution. This is possible if $a^{2}+2a+3 \ne 0$. We therefore check using the quadratic formula:
$$\sqrt{b^{2}-4ac} \rightarrow \sqrt{2^{2}-4*1*3} = \sqrt{4-4*1*3} = \sqrt{-8}$$
As $b^{2}-4ac < 0$ there is no value of a where $a^{2}+2a+3 = 0$, and the system is therefore complete with only one solution, if $a \ne 1$.


**RECAP**:
**NO SOLUTIONS**: $a = 1$, $b \ne 1$  
**INFINITELY MANY SOLUTIONS**: $a = 1$, $b = 1$ 
**ONE SOLUTION**: $a \ne 1$, $b = \mathbb{R}$ 
