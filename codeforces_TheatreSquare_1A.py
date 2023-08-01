n, m, a = input().split()

#let n be the length
#let m be the breadth
n = int(n)
m = int(m)
a = int(a)

num_along_length = (n / a)
if num_along_length > (n//a):
    num_along_length = int(num_along_length) + 1
else:
    num_along_length = n // a

num_along_breadth = (m / a)
if num_along_breadth > (m//a):
    num_along_breadth = int(num_along_breadth) + 1
else:
    num_along_breadth = m // a

totalNum = int(num_along_breadth * num_along_length)
print(totalNum)