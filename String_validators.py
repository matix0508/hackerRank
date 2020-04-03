#!/usr/bin/python3
if __name__ == '__main__':
    s = input()
    output = False
    for char in s:
        if char.isalnum():
            output = True
    print(output)

    output = False
    for char in s:
        if char.isalpha():
            output = True
    print(output)

    output = False
    for char in s:
        if char.isdigit():
            output = True
    print(output)

    output = False
    for char in s:
        if char.islower():
            output = True
    print(output)

    output = False
    for char in s:
        if char.isupper():
            output = True
    print(output)
