# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

string, size = input().split(' ')

for i in range(int(size)):
  for elem in list(combinations(sorted(string), i + 1)):
    print(''.join(elem))
