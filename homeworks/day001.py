"""
L1-Q1:
Sure, here is the extracted content from the image:

1.1. Let ($B$) be a ($4 \times 4 $) matrix to which we apply the following operations:
    1. double column 1,
    2. halve row 3,
    3. add row 3 to row 1,
    4. interchange columns 1 and 4,
    5. subtract row 2 from each of the other rows,
    6. replace column 4 by column 3,
    7. delete column 1 (so that the column dimension is reduced by 1).
    (a) Write the result as a product of eight matrices.
    (b) Write it again as a product ($ABC$) (same ($B$)) of three matrices.
"""


import torch

B = torch.range(1, 16).reshape(4, 4)
print("原始B")
print(B)

e1 = torch.tensor([
    [2, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    ], dtype=B.dtype)
print("第一列乘二")
print(B @ e1)

e2 = torch.tensor([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0.5, 0],
    [0, 0, 0, 1],
    ], dtype=B.dtype)
print("第三行除二")
print(e2 @ B)

e3 = torch.tensor([
    [1, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    ], dtype=B.dtype)
print("把第三行加到第一行上")
print(e3 @ B)

e4 = torch.tensor([
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    ], dtype=B.dtype)
print("把第四列和第一列交换位置")
print(e4 @ B)
print(B @ e4)
