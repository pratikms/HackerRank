def merge_the_tools(string, k):
    # your code goes here
    from collections import OrderedDict
    print('\n'.join([''.join(list(OrderedDict.fromkeys(string[i:k + i]))) for i in range(0, len(string), k)]))
