def split_and_join(line):
    lst = line.split()
    output = "-".join(lst)
    return output

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
