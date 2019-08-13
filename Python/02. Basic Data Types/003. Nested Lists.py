if __name__ == '__main__':

    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])

    students.sort(key=lambda student: student[1])
    students = list(filter(lambda student: student[1] != students[0][1], students))

    try:
        second_lowest_students = [student[0] for student in students if student[1] == students[0][1]]
        second_lowest_students.sort()
        print('\n'.join(second_lowest_students))
    except Exception:
        print(students[0][0])
