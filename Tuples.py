if __name__ == '__main__':
    n = int(input())
    t = ()
    integer_list = list(map(int, input().split()))
    t = tuple(integer_list)
    print(hash(t))
