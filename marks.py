if __name__ == '__main__':
    marks = {}
    names = []
    scores = []
    output = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks[name] = score
        names.append(name)
        scores.append(score)
    greatest = 0
    for item in scores:
        if scores.count(item) != 1:
            scores.pop(scores.index(item))
    scores.sort()
    for name in names:
        if marks[name] == scores[1]:
            output.append(name)
    output.sort()
    for item in output:
        print(item)
