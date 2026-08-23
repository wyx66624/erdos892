# 整数上半壳安全核：可验证容量准则与倒数负载边界

## 0. 状态与结论范围

**状态：已完成两次独立敌意审查的纸面结果；一般刻画仍未证明。**

本文继续 B23、B30 及 stopping-time Laplace-debt 定理的反向算术任务。
主要结果是一个完全确定、可由有限整数运算核验的安全壳容量准则：在每个
deadline 壳层的上半部删除历史反链的所有倍数后，若仍至少剩两个指定同余类
中的整数，则可逐历史构造真实整除反链核。该核既可确定性地每壳加入两个元素，
也可把两个元素作为一个正相关 Bernoulli 块；后一版本在
\(\theta=\log(7/3)\) 处有精确的条件 Laplace 常数 \(q_i=1\)。

作为具体正类，任意一致相对间隙的整数序列都满足该准则（放大常数可显式
给出）。特别地，输入 \(b_i=3^i\) 本身是一条整除链，但可以用完全由合数
组成的逐历史安全核支配。

这个序列类已包含于 B7 的 \(\sum_i1/b_i<\infty\) 定理；本文不把它冒充为
新的 characterization。新增内容是：

1. 把 B7 区域中的一个真实算术构造严格接入 safe-shell/Laplace 接口；
2. 给出比倒数负载更精确的有限整数容量证书；
3. 证明任何只使用粗估计
   \(|\bigcup_{h\in H}h\mathbb N\cap I|\le U\sum_{h\in H}1/h\)
   和逐壳下界 \(h\gg Cb_j\) 的统一机制，都不能越过
   \(\sum_j1/b_j<\infty\) 的 B7 边界。

因此 Erdős 892 仍为 OPEN，本文不开始 Lean 形式化。

---

## 1. 上半壳、同余池与逐历史安全性

固定严格递增正整数序列

\[
 b_1<b_2<\cdots,
\]

整数放大常数 \(C\ge1\)，以及模数 \(m\ge1\)。令

\[
 U_i=Cb_i,\qquad U_0=0,
\]

并定义

\[
 L_i=\max\{U_{i-1},\lfloor U_i/2\rfloor\},
 \qquad I_i=(L_i,U_i]\cap\mathbb Z. \tag{1.1}
\]

于是 \(I_i\subseteq(U_{i-1},U_i]\)，且其中每个整数严格大于
\(U_i/2\)。定义指定同余池

\[
 P_i=I_i\cap m\mathbb N, \qquad
 c_i=|P_i|=\left\lfloor\frac{U_i}{m}\right\rfloor
             -\left\lfloor\frac{L_i}{m}\right\rfloor. \tag{1.2}
\]

这里选择 \(m\mathbb N\) 不是必要条件；它允许在 \(m\ge2\) 时强制所有输出
（除不可能出现的小端点外）为合数，并显示构造不依赖“只选素数”。

### 定义 1.1（合法二块历史）

深度 \(i-1\) 的一个集合 \(H\) 称为合法二块历史，如果：

1. \(H\) 是整除反链；
2. 对每个 \(1\le j<i\)，有 \(H\cap I_j\subseteq P_j\) 且
   \(|H\cap I_j|\in\{0,2\}\)。

相对于历史 \(H\)，第 \(i\) 壳的安全池为

\[
 T_i(H)=P_i\setminus\bigcup_{h\in H}h\mathbb N. \tag{1.3}
\]

这一定义删除所有可能满足 \(h\mid x\) 的新点。

### 引理 1.2（逐历史反链性）

若 \(H\) 是合法二块历史，且 \(R\subseteq T_i(H)\)，则：

1. \(R\) 内部两两整除不可比；
2. \(R\) 中每个元素与 \(H\) 中每个元素不可比；
3. 因而 \(H\cup R\) 是整除反链。

#### 证明

若 \(x<y\) 都属于 \(I_i\) 且 \(x\mid y\)，则 \(y\ge2x>U_i\)，与
\(y\le U_i\) 矛盾，所以 \(R\) 内部不可比。

对 \(h\in H\) 与 \(x\in R\)，因 \(h\le U_{i-1}<x\)，不可能有
\(x\mid h\)。另一方面，\(x\in T_i(H)\) 的定义排除了 \(h\mid x\)。
故二者不可比。证毕。

特别地，如果整个原壳满足

\[
 U_i<2(U_{i-1}+1), \tag{1.4}
\]

则原壳中的最小整数 \(U_{i-1}+1\) 已严格大于 \(U_i/2\)，所以
\(I_i=(U_{i-1},U_i]\cap\mathbb Z\)，无需丢弃其下半部。

---

## 2. 精确有限容量证书

对 \(j<i\) 定义有限整数

\[
 D_{ij}=\max_{h\in P_j}
 \left(\left\lfloor\frac{U_i}{h}\right\rfloor
       -\left\lfloor\frac{L_i}{h}\right\rfloor\right), \tag{2.1}
\]

空池 \(P_j=\varnothing\) 时约定 \(D_{ij}=0\)。这是单个第 \(j\) 壳历史
元素在第 \(i\) 安全池中最多禁止的倍数数目。注意最大值只遍历一个显式有限
整数区间；它不是渐近假设，也不需素数分布输入。

### 定义 2.1（二块安全容量条件）

称 \((b_i;C,m)\) 满足 **TSC(2)**，如果对每个 \(i\ge1\)，

\[
 c_i\ge 2+2\sum_{j<i}D_{ij}. \tag{2.2}
\]

### 定理 A（算术二块安全壳核）

若 TSC(2) 成立，则存在一个投影一致的逐壳随机生成器，使：

1. 每条样本路径在每个有限深度都是真实整除反链；
2. 给定任一正概率过去，第 \(i\) 壳加入元素数为
   \[
   Y_i=2\xi_i,
   \qquad \mathbb P(\xi_i=1)=\frac7{10},
   \quad \mathbb P(\xi_i=0)=\frac3{10}; \tag{2.3}
   \]
3. 在 \(\theta=\log(7/3)\) 处，条件 Laplace 常数精确为
   \[
   \mathbb E\!\left[e^{-\theta(Y_i-1)}\mid\mathcal F_{i-1}\right]=1. \tag{2.4}
   \]

因此 stopping-time Laplace-debt 定理可取

\[
 r=d=0,\qquad q_i=1,\qquad K_{0,N}=1<e^\theta, \tag{2.5}
\]

并对每个 \(N\) 给出一个反链 \(A_N\subseteq[1,U_N]\)，满足

\[
 |A_N\cap[1,U_i]|\ge i\qquad(1\le i\le N). \tag{2.6}
\]

故存在无限 primitive sequence \(a_1<a_2<\cdots\)，使

\[
 a_i\le Cb_i\qquad(i\ge1). \tag{2.7}
\]

#### 证明

递归构造。给定合法历史 \(H\)，由并集界和 (2.1)，

\[
 \begin{aligned}
 |P_i\setminus T_i(H)|
 &\le \sum_{h\in H}
 \left(\left\lfloor\frac{U_i}{h}\right\rfloor
       -\left\lfloor\frac{L_i}{h}\right\rfloor\right)\\
 &\le 2\sum_{j<i}D_{ij}. \tag{2.8}
 \end{aligned}
\]

由 (2.2)，\(|T_i(H)|\ge2\)。令 \(B_i(H)\) 为 \(T_i(H)\) 中最小的
两个元素；该规则消除了任何选择公理或未指定 tie-break。取彼此独立且与过去
独立的 Bernoulli 变量 \(\xi_i\)，当 \(\xi_i=1\) 时加入整个
\(B_i(H)\)，当 \(\xi_i=0\) 时不加入。引理 1.2 归纳保证每条路径始终是
整除反链，并且新历史仍满足每个壳层选零个或两个的定义。

给定过去，\(B_i(H)\) 已确定而 \(\xi_i\) 仍有 (2.3) 的分布，故

\[
 \begin{aligned}
 \mathbb E[e^{-\theta(Y_i-1)}\mid\mathcal F_{i-1}]
 &=\frac7{10}e^{-\theta}+\frac3{10}e^\theta\\
 &=\frac7{10}\frac37+\frac3{10}\frac73=1,
 \end{aligned}
\]

得到 (2.4)--(2.5)。有限结论 (2.6) 来自停时定理。取每个可行反链中最小
的 \(N\) 个元素递增排列，得到长度 \(N\) 的可行 primitive tuple；所有
有限可行 tuple 构成有限分支树，König 无穷引理给出 (2.7)。证毕。

### 注 2.2（确定性版本）

同一证明也允许每壳确定性加入 \(B_i(H)\)。此时 \(Y_i=2\)，所以对任意
\(\theta>0\)，

\[
 q_i=e^{-\theta}<1. \tag{2.9}
\]

而且计数每壳增加二，根本不需要概率舍入。随机版本的作用不是扩大本定理的
正类，而是严格验证 TSC(2) 所构造的真实整数核满足 stopping-time SLC 的
全部逐历史义务。不能用随机包装掩盖这一点。

---

## 3. 易核验的粗容量准则

令

\[
 t_j=\min P_j=m\left(\left\lfloor\frac{L_j}{m}\right\rfloor+1\right)
 \tag{3.1}
\]

（仅在 \(P_j\ne\varnothing\) 时使用）。显然

\[
 D_{ij}\le\left\lfloor\frac{U_i}{t_j}\right\rfloor. \tag{3.2}
\]

因而下述完全显式条件蕴含 TSC(2)：

\[
 c_i\ge2+2\sum_{\substack{j<i\\P_j\ne\varnothing}}
 \left\lfloor\frac{U_i}{t_j}\right\rfloor. \tag{3.3}
\]

下面把它化为序列条件。置 \(b_0=0\)，并定义相对上半壳厚度

\[
 \delta=\inf_{i\ge1}
 \min\left\{\frac{b_i-b_{i-1}}{b_i},\frac12\right\}. \tag{3.4}
\]

### 推论 B（一致相对间隙正类）

假设 \(\delta>0\)，令

\[
 S=\sum_{j\ge1}\frac1{b_j}. \tag{3.5}
\]

则 \(S<\infty\)。固定任意 \(m\ge1\)，若整数 \(C\) 满足

\[
 \frac{C\delta}{m}\ge4S+\frac3{b_1}, \tag{3.6}
\]

则 \((b_i;C,m)\) 满足 (3.3)，从而有定理 A 的 primitive dominator。

#### 证明

由 (3.4)，\(b_{i-1}\le(1-\delta)b_i\)。迭代得

\[
 b_i\ge b_1(1-\delta)^{-(i-1)},
\]

故 \(S\le1/(\delta b_1)<\infty\)。另一方面，若
\(\ell_i=U_i-L_i\)，则

\[
 \ell_i\ge C\delta b_i,
 \qquad
 c_i\ge\frac{\ell_i}{m}-1
      \ge\frac{C\delta b_i}{m}-1. \tag{3.7}
\]

每个 \(t_j>L_j\ge\lfloor U_j/2\rfloor\)，所以 \(t_j>U_j/2\)，从而

\[
 2\sum_{j<i}\left\lfloor\frac{U_i}{t_j}\right\rfloor
 <4b_i\sum_{j<i}\frac1{b_j}
 \le4Sb_i. \tag{3.8}
\]

由 (3.6)--(3.7) 及 \(b_i\ge b_1\)，

\[
 c_i\ge4Sb_i+3\frac{b_i}{b_1}-1
      \ge4Sb_i+2. \tag{3.9}
\]

结合 (3.8)，得到 (3.3)。证毕。

### 例 3.1（输入为整除链，输出强制为合数）

取

\[
 b_i=3^i,\qquad m=6,\qquad C=36. \tag{3.10}
\]

则 \(\delta=1/2\)、\(S=1/2\)，且

\[
 \frac{C\delta}{m}=3
 =4S+\frac3{b_1}. \tag{3.11}
\]

故推论 B 适用。输入 \((3^i)\) 中每个元素整除其后所有元素，绝非 primitive；
安全核的每个候选数却是大于 \(6\) 的六的倍数，因而是合数。定理给出一个
合数组成的 primitive sequence，满足 \(a_i\le36\cdot3^i\)。这个例子不是
素数壳层，也没有借助素数定理。

---

## 4. 严格障碍：粗倒数负载机制不能越过 B7

对任意历史反链 \(H\subseteq[1,L_i]\)，最粗的倍数并集估计是

\[
 \left|I_i\cap\bigcup_{h\in H}h\mathbb N\right|
 \le\sum_{h\in H}\left\lfloor\frac{U_i}{h}\right\rfloor
 \le U_i\sum_{h\in H}\frac1h. \tag{4.1}
\]

它忽略倍数是否真正落在 \((L_i,U_i]\) 以及不同倍数集的大量重叠。

### 定理 C（倒数负载证明模式的 B7 边界）

考虑任何固定 \(C\) 的逐壳证明模式，它只使用以下两项来保证第 \(i\) 壳
存在安全点：

1. 候选池大小的平凡界 \(|I_i|\le U_i\)；
2. 对历史负载的逐壳先验上界
   \[
   \sum_{h\in H_{i-1}}\frac1h
   \le\frac{\kappa}{C}\sum_{j<i}\frac1{b_j}, \tag{4.2}
   \]
   其中固定 \(\kappa>0\)，并通过 (4.1) 要求
   \[
   U_i\frac{\kappa}{C}\sum_{j<i}\frac1{b_j}<|I_i|. \tag{4.3}
   \]

若 (4.3) 要对所有 \(i\) 成立，则必有

\[
 \sum_{j\ge1}\frac1{b_j}\le\frac C\kappa<\infty. \tag{4.4}
\]

因此这一个具体的“全局倒数负载 + 粗倍数并集界”机制不可能证明任何
\(\sum1/b_j=\infty\) 的新正类。

#### 证明

由 \(|I_i|\le U_i\) 和 (4.3)，

\[
 \frac\kappa C\sum_{j<i}\frac1{b_j}<1
\]

对每个 \(i\) 成立。令 \(i\to\infty\)，单调收敛即得 (4.4)。证毕。

定理 C 只关闭这个被精确定义的标量证明模式，不关闭以下路线：

1. 使用 (2.1) 的真实短区间倍数增量而非 (4.1)；
2. 利用不同倍数集的重叠、Möbius/筛法抵消或大素因子；
3. 让核的选择规则主动降低未来的局部倍数负载；
4. 允许坏壳层并用 stopping-time Laplace 债务在后续偿还；
5. 使用不由 \(\sum1/h\) 控制的结构性反链不变量。

### 例 4.1（不剔除倍数的固定块严格失败）

取两个壳层 \((6,12]\) 和 \((12,24]\)。若一个“上半壳块”规则不看历史，
分别选择

\[
 \{8,10\},\qquad\{14,16\}, \tag{4.5}
\]

则两个块各自内部都是反链，但 \(8\mid16\)。若以任何正概率同时开启两个块，
就有正概率输出不是整除反链。故只验证壳内反链性和 \(Y_i\) 的 Laplace 变换
并不够；定义 (1.3) 的逐历史倍数剔除是不可省略的算术义务。

这不是所有非适应性块核的不可能定理；例如全局预先给定的 primitive 候选族
当然无需剔除。它严格反驳的只是“任意上半壳块自动跨壳安全”这一说法。

---

## 5. 与 B7、B23、B30 和最终问题的关系

逻辑依赖链为

\[
\text{TSC(2)}
\Longrightarrow
\text{逐历史真实反链核且 }q_i=1
\Longrightarrow
\text{stopping-time SLC}
\Longrightarrow
\text{固定常数 primitive domination}. \tag{5.1}
\]

推论 B 的一致相对间隙蕴含 \(\sum1/b_i<\infty\)，所以就“哪些输入序列已知
可支配”而言，它是 B7 的严格子区域，而不是 B7 的改进；例如
\(b_i=i^2\) 满足 B7 的倒数和条件，却有 (3.4) 中的 \(\delta=0\)，不属于
推论 B。其价值在于第一次把
一个不靠素数的真实整数核逐历史接入 stopping-time 条件；B23/B30 只提供抽象
舍入接口，没有完成这里的倍数剔除和跨壳反链证明。

定理 C 反向说明，若要从 stopping-time 路线接近仍允许
\(\sum1/b_i=\infty\) 的最终未知区域，下一步不能继续只优化常数。至少需要
证明以下更强命题之一：

1. **短区间筛重叠：** 沿核产生的每个正概率历史，证明
   \[
   \left|I_i\cap\bigcup_{h\in H}h\mathbb N\right|
   \le (1-\eta)|I_i|
   \]
   的结构性界，其中 \(\eta>0\) 不由 \(\sum_{h\in H}1/h\) 给出；
2. **主动负载不变量：** 定义比倒数和更精细、在随机 greedy 更新下具有
   超鞅或势函数漂移的局部倍数覆盖量；
3. **坏壳偿债：** 即使个别历史没有两个安全点，也构造合法的 \(Y_i\) 分布，
   直接控制 \(\log q_i\) 的所有前缀和，而不是逐壳强制 \(q_i\le1\)。

以上缺口均未闭合。本文只证明 TSC(2) 正类、其合数实例和粗负载机制的严格
边界；不得据此声称解决 Erdős 892。

---

## 6. 敌意自审清单

1. **端点：** \(L_i\) 使用 \(\lfloor U_i/2\rfloor\)，而候选满足
   \(x>L_i\)，所以即使 \(U_i\) 为奇数也严格有 \(x>U_i/2\)。
2. **整除方向：** 新点大于全部历史点；只需剔除 \(h\mid x\)，但证明中也
   明确排除了不可能的 \(x\mid h\)。
3. **重数：** 每个旧壳至多两个历史点，故 (2.8) 的系数恰为二；倍数集合
   重叠只使并集更小。
4. **条件分布：** 候选块依赖过去，但 Bernoulli 硬币在给定过去后仍独立，
   所以 (2.4) 是逐历史条件等式，不是无条件平均。
5. **投影一致性：** 第 \(i\) 步只读以前历史和固定端点，规则不依赖最终
   截断 \(N\)。即使不用这一点，有限可行性加 König 也足够。
6. **随机性不是证明替代物：** 注 2.2 明确记录同一容量条件已有确定性强解；
   随机版本只审计 SLC 接口。
7. **B7 边界：** 只对推论 B 和定理 C 所定义的粗负载机制声称位于 B7
   区域；没有声称精确 TSC(2) 必然推出 \(\sum1/b_i<\infty\)。
8. **反例范围：** 例 4.1 只反驳忽略跨壳整除的固定块捷径，不反驳所有
   非适应性或预先全局 primitive 的候选族。
9. **形式化门：** 本文虽已完成双重纸面审查，但不是最终
   characterization；不包含 Lean 骨架、`sorry`、`admit` 或自定义公理。
