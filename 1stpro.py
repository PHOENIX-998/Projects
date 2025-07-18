if __name__ == '__main__':
    record = []

    for _ in range(int(input())):
        record.append([input(), float(input())])

    # Extract all unique scores and sort them
    scores = sorted(set([student[1] for student in record]))

    # Get the second lowest score
    second_lowest = scores[1]

    # Get all names with the second lowest score
    names = [student[0] for student in record if student[1] == second_lowest]

    # Sort the names alphabetically
    names.sort()

    # Print each name on a new line (as per most coding challenge requirements)
    for name in names:
        print(name)
