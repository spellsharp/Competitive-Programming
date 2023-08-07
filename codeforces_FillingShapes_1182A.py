import sys
n = int(input())

if n % 2 != 0:
    print(0)
    sys.exit()

# consider 2 of those blocks as one block of size 3x2
# these blocks can be formed in 2 different ways.

blocksAccomodated_perRow = n / 2
print(int(pow(2, blocksAccomodated_perRow)))