if __name__ == '__main__':

    n, m = input().split()
    array = list(input().split())
    n, m = int(n), int(m)

    for j in range(n-1):
        print(*array[j:j+m])
    print(*array[m*(n-1):])
