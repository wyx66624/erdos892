# Erdős 892 一般路线：带集中证书的 surplus rounding

## 0. 结论范围

本记录继续研究固定 dilation 下的有限 deadline-antichain 问题。主要结果是：

1. 给出一个完全有限、可用有理数核验的 Laplace 舍入判据；
2. 证明一个只使用 \(\rho_N^*\) 数值和精确前缀宽度的
   **width-saturation surplus-rounding theorem**，同时证明把该逐前缀
   并集界直接统一到无限长度会与经典必要条件严格矛盾；
3. 给出一个只使用前缀均值和方差的二阶矩舍入判据；
4. 证明一个非平凡的 **negative-association surplus-rounding theorem**：若
   \(\rho_N^*\ge 1+\varepsilon\) 有一个负关联的随机反链见证，并且有限个早期
   deadline 已逐点满足，那么明确的指数尾和条件推出一个真正的整数反链；
5. 将这个有限定理通过 König 引理提升为一个条件性的无限 domination 定理；
6. 精确核对 \(P_{15}\) 已知积分障碍的两相分数见证为何不满足集中条件：
   它在元素 \(2,3\) 上有严格正协方差。

这里绝不声称一般的 \(\rho_N^*>1\) 自动产生负关联见证，也不声称已经解决
Erdős 892。新定理的真正剩余任务，是从整数序列的算术条件构造具有统一余量和
统一集中性的随机反链。以下所有正式应用都在真实整除偏序 \(P_M\) 中进行；
一般概率引理只作为证明工具，绝不把抽象偏序的结论冒充为 \(P_M\) 的结构定理。

---

## 1. Deadline 随机反链与三个可检验量

固定整数 \(C\ge 1\)、严格递增整数

\[
 b_1<\cdots<b_N,
 \qquad U_i=Cb_i,
 \qquad M=U_N,
\]

并令 \(P_M=([1,M],\mid)\)。若 \(A\subseteq[1,M]\) 是整除反链，记

\[
 c_i(A)=|A\cap[1,U_i]|.
\]

存在满足全部 deadline 的整数反链，等价于存在 \(A\) 使

\[
 c_i(A)\ge i\qquad(1\le i\le N). \tag{D}
\]

令 \(\mu\) 是 \(P_M\) 的反链上的概率分布，随机反链记为
\(\mathbf A\sim\mu\)。定义

\[
 Z_i=c_i(\mathbf A),\qquad
 m_i=\mathbb E_\mu Z_i,\qquad
 V_i=\operatorname{Var}_\mu Z_i. \tag{1.1}
\]

若

\[
 m_i\ge(1+\varepsilon)i\qquad(1\le i\le N), \tag{1.2}
\]

称 \(\mu\) 是一个 \(\varepsilon\)-surplus fractional witness。特别地，
\(\rho_N^*\ge1+\varepsilon\) 当且仅当至少存在一个这样的 \(\mu\)。重要的
逻辑区别是：数值不等式 \(\rho_N^*\ge1+\varepsilon\) 本身并不指定见证的
高阶相关结构。

### 定义 1.1（早期安全）

给定 \(0\le r\le N\)。若

\[
 \mu(Z_i\ge i)=1\qquad(1\le i\le r), \tag{1.3}
\]

则称 \(\mu\) 在深度 \(r\) 以前早期安全。这里 \(r=0\) 表示没有额外条件。

### 定义 1.2（有理 Laplace 预算）

对 \(y\in(0,1)\)，定义第 \(i\) 个失败预算

\[
 Q_i(\mu;y)
 =y^{-(i-1)}\mathbb E_\mu y^{Z_i}. \tag{1.4}
\]

若 \(\mu\) 有有限支撑、权重为有理数且 \(y\in\mathbb Q\cap(0,1)\)，
则 (1.4) 是一个可精确计算的有理数。它记录的不只是元素的一阶边际，而是整个
前缀计数的一个单点概率母函数值。

### 定义 1.3（负关联）

令

\[
 X_m=\mathbf 1_{\{m\in\mathbf A\}}\qquad(1\le m\le M).
\]

若对任意不交坐标集 \(S,T\subseteq[1,M]\)，以及任意坐标单调不减函数
\(f,g\)，都有

\[
 \mathbb E[f(X_S)g(X_T)]
 \le \mathbb E f(X_S)\,\mathbb E g(X_T), \tag{1.5}
\]

则称 \(\mu\) 的元素指标负关联（negatively associated, NA）。

负关联是充分条件而不是必要条件。若不愿证明 NA，后面的主定理只需要逐个给出
有限个有理 Laplace 预算，因而仍可独立核验。

---

## 2. 主舍入引理：有限 Laplace 证书

### 定理 2.1（Laplace-budget rounding）

设 \(\mu\) 是真实整除反链上的任意概率分布，并且它在深度 \(r\) 以前早期
安全。若可以为每个 \(r<i\le N\) 选择 \(y_i\in(0,1)\)，使

\[
 \sum_{i=r+1}^N Q_i(\mu;y_i)<1, \tag{2.1}
\]

则 \(\mu\) 的支撑中至少有一个反链满足全部 deadline (D)。因而
\(\rho_N(C;b)\ge1\)。

#### 证明

令失败事件

\[
 B_i=\{Z_i<i\}=\{Z_i\le i-1\}.
\]

因为 \(0<y_i<1\)，在 \(B_i\) 上有

\[
 y_i^{Z_i}\ge y_i^{i-1}.
\]

Markov 不等式给出

\[
 \mathbb P(B_i)
 \le y_i^{-(i-1)}\mathbb E y_i^{Z_i}
 =Q_i(\mu;y_i). \tag{2.2}
\]

早期安全性给出 \(\mathbb P(B_i)=0\) 对 \(i\le r\) 成立。因此由并集界，

\[
 \mathbb P\!\left(\bigcup_{i=1}^N B_i\right)
 \le\sum_{i=r+1}^NQ_i(\mu;y_i)<1.
\]

故以正概率所有 \(B_i\) 同时不发生。取概率空间中的任一相应结果
\(A\in\operatorname{supp}\mu\)，它本来就是 \(P_M\) 的反链，并满足 (D)。
证毕。

### 注 2.2（严格的可检验性）

一个有限证书只需列出：

1. 反链 \(A^{(1)},\ldots,A^{(s)}\subseteq[1,M]\)；
2. 有理概率 \(p_1,\ldots,p_s\)；
3. 有理数 \(y_{r+1},\ldots,y_N\in(0,1)\)。

逐对检查每个 \(A^{(j)}\) 中没有整除关系，再精确计算

\[
 Q_i=y_i^{-(i-1)}\sum_{j=1}^s p_j y_i^{c_i(A^{(j)})},
\]

即可用整数／有理数运算核验 (2.1)。因此这个条件不是依赖浮点 LP 最优值的
存在性陈述。

### 定理 2.3（width-saturation surplus rounding）

令

\[
 W_i=\operatorname{width}(P_{U_i})=\left\lceil\frac{U_i}{2}\right\rceil.
 \tag{2.3}
\]

设 \(\varepsilon>0\) 且 \(\rho_N^*(C;b)\ge1+\varepsilon\)。若

\[
 \sum_{i=1}^N
 \frac{W_i-(1+\varepsilon)i}{W_i-i+1}<1, \tag{2.4}
\]

则存在满足全部 deadline 的整数反链。特别地，这个定理只需
\(\rho_N^*\) 的数值下界和可直接计算的 \((U_i)\)，不需要预先知道某个 NA
分解或任何二阶矩。

#### 证明

先核对 (2.3)。区间 \((U_i/2,U_i]\) 是大小 \(\lceil U_i/2\rceil\) 的
反链。反过来，对反链中每个 \(a\le U_i/2\)，把它沿
\(a,2a,4a,\ldots\) 映到第一个落入 \((U_i/2,U_i]\) 的元素。这个映射在
反链上单射，且像不能同时属于该反链，所以任意反链至多有
\(\lceil U_i/2\rceil\) 个元素。

由 \(\rho_N^*\ge1+\varepsilon\)，取分数见证 \(\mu\) 使
\(m_i\ge(1+\varepsilon)i\)。必有 \(W_i\ge m_i\)，所以 (2.4) 中每个
分子非负。记

\[
 p_i=\mathbb P(Z_i<i).
\]

在失败事件上 \(Z_i\le i-1\)，而总有 \(Z_i\le W_i\)。因此

\[
 m_i\le p_i(i-1)+(1-p_i)W_i
 =W_i-p_i(W_i-i+1).
\]

于是

\[
 p_i\le\frac{W_i-m_i}{W_i-i+1}
 \le\frac{W_i-(1+\varepsilon)i}{W_i-i+1}. \tag{2.5}
\]

对失败事件使用并集界，再用 (2.4)，可知以正概率没有任何 deadline 失败。
相应样本就是所求整数反链。证毕。

### 注 2.4（该条件测量什么）

写

\[
 \delta_i=W_i-(1+\varepsilon)i\ge0.
\]

则 (2.4) 的第 \(i\) 项恰为

\[
 \frac{\delta_i}{\varepsilon i+\delta_i+1}. \tag{2.6}
\]

所以它要求分数余量不仅超过配额，而且在各尺度上接近该前缀允许的最大反链
容量。这个条件与 NA 条件作用机制不同：前者只使用硬上界和一阶均值，后者允许
很大的宽度余量，但要求概率质量不能以强正相关的“全早期／全晚期”相位分裂。
本记录不在两者之间声称任何一般蕴含关系。

### 命题 2.5（width-saturation 并集界的无限障碍）

固定 \(C\in\mathbb N\) 和 \(\varepsilon>0\)。设无限严格递增序列
\(b_1<b_2<\cdots\) 对每个 \(N\) 都满足
\[
 \rho_N^*(C;b)\ge1+\varepsilon. \tag{2.7}
\]
令 \(W_i=\lceil Cb_i/2\rceil\)。如果企图对每个 \(N\) 直接应用定理 2.3，
即要求
\[
 \sum_{i=1}^N
 \frac{W_i-(1+\varepsilon)i}{W_i-i+1}<1
 \qquad\text{对每个 }N, \tag{2.8}
\]
那么必有
\[
 b_i=\frac{2(1+\varepsilon)}{C}\,i+o(i). \tag{2.9}
\]
特别地，
\[
 \sum_i\frac1{b_i\log b_i}=\infty. \tag{2.10}
\]
因此任何满足经典必要条件
\(\sum_i1/(b_i\log b_i)<\infty\) 的候选序列，都不可能用 (2.8) 这一个
逐 deadline 并集界完成无限 domination。

#### 证明

由 (2.7)，对每个 \(i\) 都有 \(W_i\ge(1+\varepsilon)i\)。写
\[
 \delta_i=W_i-(1+\varepsilon)i\ge0,\qquad
 q_i=\frac{\delta_i}{\varepsilon i+\delta_i+1}.
\]
(2.8) 的非负部分和一致小于 \(1\)，所以 \(\sum_iq_i\le1\)，特别地
\(q_i\to0\)。

我们断言 \(\delta_i/i\to0\)。否则存在 \(\eta>0\) 和无穷多个 \(i\)，使
\(\delta_i\ge\eta i\)。在这些指标上
\[
 q_i\ge\frac{\eta i}{(\varepsilon+\eta)i+1},
\]
其右边趋于正常数 \(\eta/(\varepsilon+\eta)>0\)，与 \(q_i\to0\) 矛盾。
故
\[
 W_i=(1+\varepsilon)i+o(i).
\]
又因 \(W_i=\lceil Cb_i/2\rceil\)，有
\[
 Cb_i=2W_i+O(1)=2(1+\varepsilon)i+o(i),
\]
这就是 (2.9)。

于是存在常数 \(K\)，使充分大的 \(i\) 都有 \(b_i\le Ki\)。再增大起点可使
\(\log b_i\le2\log i\)，从而
\[
 \frac1{b_i\log b_i}\ge\frac1{2K\,i\log i}.
\]
右侧级数发散，得到 (2.10)。证毕。

### 注 2.6（严格关闭的范围）

命题 2.5 只关闭以下具体策略：

> 对每个前缀使用相同的固定 \(\varepsilon\)，逐坐标套用 (2.5)，再把所有
> 失败概率直接求和。

它不反驳有限 width-saturation 定理，也不反驳把 deadline 分块、使用停时／
最大不等式、或利用 NA 得到跨尺度相关控制。特别是第 4--5 节的 NA 路线并不
要求宽度预算 (2.8) 可求和。

---

## 3. 二阶矩版本

Laplace 预算最灵活，但还可以只保留二阶信息。

### 定理 3.1（Cantelli surplus rounding）

设 \(m_i\ge i\) 对所有 \(i\) 成立。若

\[
 \sum_{i=1}^N
 \frac{V_i}{V_i+(m_i-i+1)^2}<1, \tag{3.1}
\]

则存在满足全部 deadline 的整数反链。

特别地，若 \(m_i\ge(1+\varepsilon)i\)，则下面更强、只含显式余量的条件
也充分：

\[
 \sum_{i=1}^N
 \frac{V_i}{V_i+(\varepsilon i+1)^2}<1. \tag{3.2}
\]

#### 证明

由于 \(Z_i\) 取整数值，事件 \(Z_i<i\) 蕴含

\[
 m_i-Z_i\ge m_i-i+1.
\]

单边 Chebyshev--Cantelli 不等式给出

\[
 \mathbb P(Z_i<i)
 \le \frac{V_i}{V_i+(m_i-i+1)^2}. \tag{3.3}
\]

对所有 \(i\) 使用并集界即得 (3.1) 的结论。(3.2) 由
\(m_i-i+1\ge\varepsilon i+1\) 立即推出。证毕。

### 注 3.2（方差的算术形式）

\[
 V_i=\sum_{m,n\le U_i}\operatorname{Cov}(X_m,X_n). \tag{3.4}
\]

所以 (3.1) 精确测量“同一随机相位中许多整数一起出现”造成的正相关成本。
一阶 LP \(\rho_N^*\) 看不见 (3.4)，而本判据正是向一阶松弛加入的第一个
可核验高阶量。

---

## 4. 负关联下的显式 surplus-rounding theorem

定义

\[
 \phi(\varepsilon)=\varepsilon-\log(1+\varepsilon)>0
 \qquad(\varepsilon>0). \tag{4.1}
\]

### 引理 4.1（负关联的前缀 Laplace 界）

若元素指标 \((X_m)_{m\le M}\) 负关联，则对任意 \(i\) 和
\(0<y<1\)，

\[
 \mathbb E y^{Z_i}
 \le \prod_{m\le U_i}\mathbb E y^{X_m}
 \le \exp((y-1)m_i). \tag{4.2}
\]

#### 证明

负关联对全部单调不增函数同样成立：若 \(f,g\) 不增，则 \(-f,-g\) 不减，
且两者协方差不变。函数 \(x\mapsto y^x\) 非负且不增。迭代应用负关联，得到
(4.2) 的第一个不等式。再记 \(p_m=\mathbb E X_m\)，则

\[
 \mathbb E y^{X_m}=1-p_m+p_my=1+(y-1)p_m
 \le e^{(y-1)p_m}.
\]

对 \(m\le U_i\) 相乘，并用 \(\sum_{m\le U_i}p_m=m_i\)，得到第二个
不等式。证毕。

### 定理 4.2（NA surplus rounding）

设 \(\rho_N^*(C;b)\ge1+\varepsilon\) 有一个见证 \(\mu\)，满足：

1. \(m_i\ge(1+\varepsilon)i\) 对每个 \(i\) 成立；
2. 元素指标负关联；
3. \(\mu\) 在深度 \(r\) 以前早期安全。

若

\[
 \frac{1}{1+\varepsilon}
 \sum_{i=r+1}^N e^{-\phi(\varepsilon)i}<1, \tag{4.3}
\]

则存在满足全部 deadline 的整数反链。一个与 \(N\) 无关的更易检查的充分
条件是

\[
 \frac{e^{-\phi(\varepsilon)(r+1)}}
 {(1+\varepsilon)(1-e^{-\phi(\varepsilon)})}<1. \tag{4.4}
\]

#### 证明

固定 \(i>r\)，令 \(R_i=m_i/i\ge1+\varepsilon\)，并在定理 2.1 中取

\[
 y_i=R_i^{-1}=i/m_i.
\]

由引理 4.1，

\[
\begin{aligned}
 Q_i(\mu;y_i)
 &\le y_i^{-(i-1)}\exp((y_i-1)m_i)\\
 &=\exp\!\left((i-1)\log R_i+i-m_i\right)\\
 &=R_i^{-1}
   \exp\!\left[-i(R_i-1-\log R_i)\right]. \tag{4.5}
\end{aligned}
\]

函数 \(R\mapsto R-1-\log R\) 在 \(R>1\) 上严格递增。因此

\[
 Q_i(\mu;y_i)
 \le\frac{1}{1+\varepsilon}e^{-\phi(\varepsilon)i}. \tag{4.6}
\]

(4.3) 与定理 2.1 给出所需反链。(4.4) 只是把有限和扩大为从 \(r+1\)
开始的无穷几何级数。证毕。

### 推论 4.3（任意正余量只留下有限早期窗口）

对每个 \(\varepsilon>0\)，定义

\[
 r_\varepsilon=\min\left\{r\in\mathbb Z_{\ge0}:
 \frac{e^{-\phi(\varepsilon)(r+1)}}
 {(1+\varepsilon)(1-e^{-\phi(\varepsilon)})}<1\right\}. \tag{4.7}
\]

则定理 4.2 对所有 \(N\) 同时有效，只需逐点保证前
\(r_\varepsilon\) 个 deadline，后面的全部 deadline 由余量和负关联自动
舍入。

当 \(\varepsilon\downarrow0\) 时，
\(\phi(\varepsilon)\sim\varepsilon^2/2\)，所以

\[
 r_\varepsilon
 =O\!\left(\varepsilon^{-2}\log(1/\varepsilon)\right). \tag{4.8}
\]

这是“正余量吸收无限多个晚期约束”的精确定量形式。

### 推论 4.4（无需早期审计的大余量区间）

令 \(\varepsilon_0\) 是方程

\[
 \frac{e^{-\phi(\varepsilon_0)}}
 {(1+\varepsilon_0)(1-e^{-\phi(\varepsilon_0)})}=1 \tag{4.9}
\]

的唯一正根；数值上

\[
 \varepsilon_0\approx1.1461932206.
\]

事实上，利用 \(e^{-\phi(\varepsilon)}=(1+\varepsilon)e^{-\varepsilon}\)，
(4.9) 等价于

\[
 e^{\varepsilon_0}=\varepsilon_0+2.
\]

函数 \(e^\varepsilon-\varepsilon-2\) 在 \(0\) 处为负，并在
\(\varepsilon>0\) 上严格递增到 \(+\infty\)，所以该正根确实存在且唯一。

若 \(\varepsilon>\varepsilon_0\)，则可取 \(r=0\)，而 (4.4) 对任意
\(N\) 成立。因此一个 NA 见证若在每个前缀上有超过约 \(2.1462\) 倍的期望
配额，就必含有一个同时满足全部配额的整数反链。

这里的常数只是本 Chernoff--并集界的显式常数，不声称最优。

---

## 5. 从有限舍入到无限 domination

### 定理 5.1（统一集中见证的 König 提升）

设 \(b_1<b_2<\cdots\) 是无限整数序列。假设存在固定整数 \(C\)、
\(\varepsilon>0\) 和 \(r\ge0\)，使 (4.4) 成立，并且对每个 \(N>r\)，
在 \(P_{Cb_N}\) 的反链上存在一个分布 \(\mu_N\)，满足：

1. \(\mathbb E_{\mu_N}|A\cap[1,Cb_i]|\ge(1+\varepsilon)i\)
   对所有 \(i\le N\) 成立；
2. \(\mu_N\) 的元素指标负关联；
3. \(\mu_N\) 在前 \(r\) 个 deadline 上早期安全。

则存在无限 primitive sequence \(a_1<a_2<\cdots\)，满足

\[
 a_i\le Cb_i\qquad\text{对所有 }i. \tag{5.1}
\]

#### 证明

对每个 \(N>r\)，定理 4.2 给出满足长度 \(N\) 全部 deadline 的整数反链。
对 \(N\le r\)，从任意一个长度 \(r+1\) 的上述整数反链截取最小的 \(N\)
个元素即可。因此每个深度都有可行 tuple。将相应反链最小的 \(N\) 个元素
递增排列，得到一个长度 \(N\) 的 primitive tuple
\((a_1,\ldots,a_N)\)，且 \(a_i\le Cb_i\)。

以所有这类 tuple 为有限分支树，父节点由删除末项得到。每个深度都有节点，且
每个节点只有有限多个孩子，因为 \(a_{N+1}\le Cb_{N+1}\)。König 无穷引理
给出无限支，该支就是满足 (5.1) 的无限 primitive sequence。证毕。

### 逻辑意义

定理 5.1 不要求 \(\mu_N\) 彼此投影一致；有限整数解由 König 树完成一致化。
因此剩余算术任务可以逐个有限前缀构造概率见证。另一方面，条件中的
“统一 \(\varepsilon,r\)”不能删除：若余量随 \(N\) 消失，几何尾预算未必
可求和。

---

## 6. 对 \(P_{15}\) 积分障碍的独立核对

取已有真实整除偏序例子的 deadline

\[
 (U_1,\ldots,U_7)=(3,5,7,9,11,13,15),
\]

以及两个反链

\[
\begin{aligned}
 A_0&=\{2,3,5,7,11,13\},\\
 A_1&=\{4,6,7,9,10,11,13,15\}.
\end{aligned}
\]

其计数向量分别是

\[
 (2,3,4,4,5,6,6),\qquad(0,1,3,4,6,7,8).
\]

各取概率 \(1/2\) 时，

\[
 (m_1,\ldots,m_7)=(1,2,7/2,4,11/2,13/2,7), \tag{6.1}
\]

而

\[
 (V_1,\ldots,V_7)=(1,1,1/4,0,1/4,1/4,1). \tag{6.2}
\]

### 6.1 二阶矩证书正确地拒绝该混合物

将 (6.1)--(6.2) 代入定理 3.1，七个 Cantelli 预算之和为

\[
 \frac12+\frac12+\frac1{10}+0+\frac1{10}+\frac1{10}+\frac12
 =\frac95>1. \tag{6.3}
\]

所以新定理没有错误地把已知分数解舍入成不存在的整数解。

### 6.2 失败机制是严格正相关

在这个两相混合物中，元素 \(2\) 和 \(3\) 同时恰在相位 \(A_0\) 出现。因此

\[
 \mathbb E(X_2X_3)=\frac12,\qquad
 \mathbb E X_2\,\mathbb E X_3=\frac14,\qquad
 \operatorname{Cov}(X_2,X_3)=\frac14>0. \tag{6.4}
\]

取 \(f(X_2)=X_2\)、\(g(X_3)=X_3\)，(6.4) 直接违反负关联定义。因此
\(P_{15}\) 障碍的本质是：早期元素成块共同出现，而另一个相位用它们全部缺席
换取大量晚期元素。NA surplus theorem 精确排除了这种已经识别的失败机制。

这并不证明所有具有严格正余量的 \(P_M\) 实例都存在 NA 见证；该命题仍然
开放。

---

## 7. 基本性质、简单实例与极端情形

1. **确定性极端。** 若 \(\mu\) 集中在单个反链上，则所有 \(V_i=0\)。只要
   \(m_i\ge i\)，定理 3.1 立即返回该反链；没有人为积分损失。

2. **一个真实 \(P_9\) 的 width-saturation 实例。** 取
   \(N=2\)、\((U_1,U_2)=(5,9)\)，以及三个整除反链

   \[
   A_0=\{2,3,5,7\},\qquad
   A_1=\{4,5,6,7,9\},\qquad
   A_2=\{6,7,8,9\}.
   \]

   它们的计数向量分别为 \((3,4),(2,5),(0,4)\)。令
   \[
   \mu(A_0)=\frac25,\qquad
   \mu(A_1)=\frac12,\qquad
   \mu(A_2)=\frac1{10}.
   \]
   则

   \[
   (m_1,m_2)=\left(\frac{11}{5},\frac92\right)
   \ge\frac{11}{5}(1,2).
   \]

   因而可取 \(\varepsilon=6/5\)。这里 \(W=(3,5)\)，而 (2.4) 左边为
   \[
   \frac{3-11/5}{3-1+1}+\frac{5-22/5}{5-2+1}
   =\frac4{15}+\frac3{20}=\frac5{12}<1.
   \]
   定理 2.3 因而返回一个满足基础配额 \((1,2)\) 的整数反链。这个例子有两点
   非平凡性：\(A_2\) 确实违反第一个 deadline；并且三个支撑点各自的余量
   \(\min_i c_i(A_j)/i\) 分别为 \(2,2,0\)，都小于混合物的
   \(11/5\)。所以这里确实发生了“分数混合提高最小余量，再舍入回整数可行性”。

3. **零余量极端。** 当 \(\varepsilon=0\) 时，
   \(\phi(\varepsilon)=0\)，定理 4.2 的几何尾控制消失。\(P_{15}\) 的
   \(\rho_7^*=1>\rho_7=6/7\) 证明零余量处确实不能期待一般舍入。

4. **小正余量。** 任意固定 \(\varepsilon>0\) 都使
   \(\phi(\varepsilon)>0\)，故只留下有限的早期审计窗口
   \(r_\varepsilon\)。余量越小，窗口按 (4.8) 增大，但不依赖最终长度
   \(N\)。

5. **NA 不是反链性的同义词。** “每个样本都是反链”只排除可比元素在同一
   样本中共同出现；不可比元素仍可像 (6.4) 那样高度正相关。因此从
   chain-polytope LP 得到的任意凸分解不能自动用于定理 4.2。

6. **有理 Laplace 证书比 NA 更弱。** 定理 2.1 只检查所需的有限个前缀和
   有限个 \(y_i\)，即使全局 NA 失败，也仍可能通过 (2.1)。所以搜索算法应先
   优化直接预算，而不是把 NA 当作必要条件。

---

## 8. 与 \(\rho_N^*\)、加权对偶和最终问题的严格关系

加权 Hall 对偶只确定一阶可行性：

\[
 \rho_N^*\ge1+\varepsilon
 \iff
 \exists\mu\quad m_i\ge(1+\varepsilon)i\ \ (1\le i\le N).
\]

本记录证明的是下面这条有附加条件的依赖链：

\[
\begin{gathered}
\text{fractional surplus witness}\\
+\ \text{早期安全}\\
+\ \text{Laplace 尾预算（例如由 NA 推出）}
\end{gathered}
\quad\Longrightarrow\quad
\text{一个整数 deadline 反链}. \tag{8.1}
\]

另有一条不经过相关性控制的独立支路：

\[
 \rho_N^*\ge1+\varepsilon
 \quad+\quad
 \sum_{i=1}^N\frac{W_i-(1+\varepsilon)i}{W_i-i+1}<1
 \quad\Longrightarrow\quad
 \rho_N\ge1. \tag{8.2}
\]

它在分数均值接近每个前缀的最大宽度时最近于原始 LP；NA 支路则允许宽度很大，
但要求排除相位型正相关。有限的 (8.2) 应保留作为局部／临界 dilation 工具；
然而命题 2.5 已严格关闭“对所有 \(N\) 直接逐项累加 (8.2) 预算”这一具体
无限策略，因为它会违反经典必要条件。尚未关闭的是避免逐 deadline 求和的分块、
停时或相关性方法，以及 NA/Laplace 支路。

因此最近的三个精确缺口是：

1. **余量缺口：** 从原序列的假设推出某个固定 \(C,\varepsilon>0\)，使所有
   有限前缀都有 \(\rho_N^*(C;b)\ge1+\varepsilon\)；
2. **相关性缺口：** 在保持相同一阶余量时，把任意 LP 见证替换为 NA 见证，
   或至少直接控制有理 Laplace 预算；
3. **早期窗口缺口：** 用一次有限构造固定前 \(r_\varepsilon\) 个 deadline，
   且不破坏后续随机反链的集中性。

只有三者同时闭合，定理 5.1 才给出一般 domination。当前没有任何论证证明
第 1 或第 2 条在经典两个必要条件下必然成立，因而不得声称 Erdős 892 已解决。

---

## 9. 审计结论

- 定理 2.1 是有限 Markov--并集界证明，并给出了精确有理证书格式。
- 定理 2.3 只使用真实初始整除偏序的精确宽度
  \(W_i=\lceil U_i/2\rceil\)，没有把一般偏序宽度公式误用于 \(P_M\)。
- 命题 2.5 给出该一阶宽度并集界不能直接跨越无限长度的严格障碍，而不是因
  暂时无法推进就放弃路线。
- 定理 3.1 使用整数阈值带来的 \(+1\)，不是把双边 Chebyshev 错当单边界。
- 定理 4.2 的额外因子 \((1+\varepsilon)^{-1}\) 来自整数失败阈值
  \(Z_i\le i-1\)，见 (4.5)，没有遗漏。
- 定理 5.1 的概率分布可以随 \(N\) 改变；跨 \(N\) 的一致性由整数 tuple 树
  和 König 引理完成。
- \(P_{15}\) 的方差和正协方差均由两个显式反链直接算出，不依赖枚举。
- 本记录没有开始 Lean；按 proof-first 规则，只有在最终猜想的全部数学缺口
  闭合并经独立审查后才进入形式化。
