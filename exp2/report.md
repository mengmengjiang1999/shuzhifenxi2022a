# report

- [report](#report)
  - [2-2 牛顿法和牛顿下山法](#2-2-牛顿法和牛顿下山法)

## 2-2 牛顿法和牛顿下山法

1. 先使用牛顿法进行求解，发现近似解的序列为`0 1 0 1 .....`可知牛顿法不收敛，只能使用牛顿下山法。
使用牛顿下山法求解并验证，可得结果为`-1.769`（保留4位有效数字）。
其中：
 (1) 迭代判停准则：同时使用残差判据和误差判据
 (2) 合适的下山因子序列：lambda的初始值设置为0.9，每次迭代时lambda是上一次迭代的一半，迭代一定次数之后（求解时设置为10次）不再使用下山因子进行调节。
 (3) 每次迭代的近似解及lambda的值在[2-1-1_newton_donw.txt](2-1-1_newton_down.txt)中。
 (4) 将求解结果带入`f`中验证发现结果为0

2. 这个方程使用牛顿法或牛顿下山法都可以求解，得到解为`2.236`（保留4位有效数字）。迭代判停准则等设置同上。