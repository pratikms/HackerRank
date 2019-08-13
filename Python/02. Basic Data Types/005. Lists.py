def join_args(args):
    return ', '.join(args)
  
if __name__ == '__main__':
    N = int(input())

    lst = []

    for _ in range(N):

        command, *args = input().split()

        if command != 'print':
            eval(f'lst.{command}({join_args(args)})')
        else:
            print(lst)
