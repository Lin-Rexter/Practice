import os
import random

for i in range(1, 10):
    for j in range(1, 10):
        print('%dx%d=%2d ' % (i, j, i * j), end=' ')
    print()
print("\n")

os.system("pause")


