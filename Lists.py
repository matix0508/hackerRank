if __name__ == '__main__':
    N = int(input())
    lst = []
    commands = []
    for i in range(N):
        commands.append(input())
    for command in commands:
        com = command.split()[0]
        if com == "insert":
            lst.insert(int(command.split()[1]), int(command.split()[2]))
        elif com == "print":
            print(lst)
        elif com == "remove":
            lst.remove(int(command.split()[1]))
        elif com == "append":
            lst.append(int(command.split()[1]))
        elif com == "sort":
            lst.sort()
        elif com == "pop":
            lst.pop()
        elif com == "reverse":
            lst.reverse()
