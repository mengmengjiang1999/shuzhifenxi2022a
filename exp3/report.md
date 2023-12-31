# report

陈张萌 2017013678

- [report](#report)
  - [（1）计算残差和误差的无穷范数](#1计算残差和误差的无穷范数)
  - [（2）加上小扰动](#2加上小扰动)
  - [（3）改变n的值](#3改变n的值)
  - [（4）这个实验说明：](#4这个实验说明)

## （1）计算残差和误差的无穷范数

计算得到：
$$
||r||_{\infty} = 0.0001417 \\
||\Delta x||_{\infty} = 4.4408921e-16
$$

## （2）加上小扰动

随机一个 $i$，在 $b[i]$ 上增加 $1e-7$，得到：

$$
||r||_{\infty} = 16158.26808611 \\
||\Delta x||_{\infty} = 9.9999911e-08
$$


## （3）改变n的值

$ n=8$ 时有

$$
||r||_{\infty} = 1.28669679e-07 \\
||\Delta x||_{\infty} = 1.11022302e-16
$$

$n=12$ 时有

$$
||r||_{\infty} = 0.59300479 \\
||\Delta x||_{\infty} = 8.8817842e-16
$$

## （4）这个实验说明：

1. 随着n增大，残差和误差也会越来越大
2. H矩阵右边产生一个小扰动都会对结果产生巨大影响

H矩阵是一个病态矩阵。