#!/usr/bin/python3
TEXT = "WELCOME"
if __name__ == "__main__":
    [height, width] = input().split()
    width = int(width)
    height = int(height)
    for i in range(1, (height - 1) // 2 + 1):
        print((width - 6 * i + 4) // 2 * "-", end="")
        print((2 * i - 1) * ".|.", end="")
        print((width - 6 * i + 4) // 2 * "-")

    print(((width - len(TEXT)) // 2) * "-", end="")
    print(TEXT, end="")
    print(((width - len(TEXT)) // 2) * "-")

    for i in range((height - 1) // 2, 0, -1):
        print((width - 6 * i + 4) // 2 * "-", end="")
        print((2 * i - 1) * ".|.", end="")
        print((width - 6 * i + 4) // 2 * "-")
