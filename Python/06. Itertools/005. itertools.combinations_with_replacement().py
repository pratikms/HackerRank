# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

string, size = input().split(' ')

for elem in list(combinations_with_replacement(sorted(string), int(size))):
    print(''.join(elem))
