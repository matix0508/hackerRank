def lst_average(lst):
    n = len(lst)
    output = 0
    for item in lst:
        output += item
    output = output / n
    output = "{0:.2f}".format(output)
    return output

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(lst_average(student_marks[query_name]))
