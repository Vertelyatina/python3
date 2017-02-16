if __name__ == '__main__':

    data = [int(number) for number in input().split()]
    n, goods = data[0], data[1:]

    goods.sort()
    print(sum(goods[n//2:]))
