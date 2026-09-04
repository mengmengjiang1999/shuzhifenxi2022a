# 数值分析课程作业与实验（2022）

本仓库整理了数值分析课程的 Python 作业、实验代码、实验数据与报告。原始计算结果和报告均予以保留，便于复核实验过程。

## 仓库结构

| 路径 | 内容 |
| --- | --- |
| `exp1/` | 截断误差、舍入误差与无穷级数求和 |
| `exp2/` | 牛顿法、牛顿下山法与 Bessel 函数零点 |
| `exp3/` | Hilbert 矩阵、Cholesky 分解与误差分析 |
| `exp4/` | Jacobi、Gauss-Seidel 与 SOR 迭代法 |
| `hw/` | 非线性方程、迭代法与特征值相关作业 |
| `hw2/` | 差商相关作业 |
| `hw3/` | 不动点迭代与数值积分相关作业 |

实验目录中通常包含以下内容：

- `src/` 或同目录下的 `.py` 文件：实验代码；
- `data/`、`output*.txt`：计算数据与运行结果；
- `images/`、`report.png`：报告插图或报告预览；
- `report.md`、`report.pdf`：Markdown 与 PDF 格式的实验报告。

## 运行环境

- Python 3.9 或更高版本
- NumPy
- SciPy
- Matplotlib

建议使用虚拟环境安装依赖：

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## 运行示例

在仓库根目录执行：

```bash
python3 exp1/src/1-1.py
python3 exp2/src/2-2.py
python3 exp3/exp3.py
python3 exp4/exp4.py
```

部分脚本会输出较多迭代数据或打开绘图窗口。仓库中已经保留了对应的历史输出和图片，无需重新运行也可以直接查看实验结果。

## 实验报告

- [实验一](exp1/report.md)
- [实验二](exp2/report.md)
- [实验三](exp3/report.md)
- [实验四](exp4/report.md)
