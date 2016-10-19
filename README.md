# Usage
Example usage of score_positions:
```
from Kidera import kidera

sequence = 'ANCEHLMPTY'
m = kidera.score_positions(sequence)
print(m)
```
Console output:
```
     1     2     3     4     5     6     7     8     9     10
A -1.56 -1.67 -0.97 -0.27 -0.93 -0.78 -0.20 -0.08  0.21 -0.48
N  1.14 -0.07 -0.12  0.81  0.18  0.37 -0.09  1.23  1.10 -1.73
C  0.12 -0.89  0.45 -1.05 -0.71  2.41  1.52 -0.69  1.13  1.10
E -1.45  0.19 -1.61  1.17 -1.31  0.40  0.04  0.38 -0.35 -0.12
H -0.41  0.52 -0.28  0.28  1.61  1.01 -1.85  0.47  1.13  1.63
L -1.04  0.00 -0.24 -1.10 -0.55 -2.05  0.96 -0.76  0.45  0.93
M -1.40  0.18 -0.42 -0.73  2.00  1.52  0.26  0.11 -1.27  0.27
P  2.06 -0.33 -1.15 -0.75  0.88 -0.45  0.30 -2.30  0.74 -0.28
T  0.26 -0.70  1.21  0.63 -0.10  0.21  0.24 -1.15 -0.56  0.19
Y  1.38  1.48  0.80 -0.56 -0.00 -0.68 -0.31  1.03 -0.05  0.53
```
Example usage of score_sequence:
```
v = kider.score_sequence(sequence)
print(v)
```
Console output:
```
1    -0.090
2    -0.129
3    -0.233
4    -0.157
5     0.107
6     0.196
7     0.087
8    -0.176
9     0.253
10    0.204
```

# Reference
Kidera A, Konishi Y, Oka M, Ooi T, and Scheraga HA. "Statistical analysis of the physical properties of the 20 naturally occurring amino acids". Journal of Protein Chemistry 4(1):23--55 (1985)
