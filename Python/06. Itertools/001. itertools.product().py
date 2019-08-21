# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

lst1 = map(int, input().split(' '))
lst2 = map(int, input().split(' '))

print(' '.join(map(str, list(product(lst1, lst2)))))
