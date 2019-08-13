if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    arr = list(filter(lambda score: score != max(arr), arr))
    print(arr[0])
