if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst = []
    for item in arr:
        lst.append(item)
    greatest = lst[0]
    for item in lst:
        if item > greatest:
            greatest = item
    runner_up = 0
    for item in lst:
        if item > runner_up and item != greatest:
            runner_up = item
    print(runner_up)
