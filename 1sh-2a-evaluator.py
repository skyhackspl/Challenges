import csv
import sys

#the levenhstein distance
def get_ld(s1, s2):
    if len(s1) < len(s2):
        return get_ld(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

check_filename = sys.argv[1]
filename = sys.argv[2]

scores = []
with open(filename, newline='') as csvfile_to_check:
    with open(check_filename, newline='') as csvfile_validation:
        reader1 = csv.reader(csvfile_to_check, delimiter=',')
        reader2 = csv.reader(csvfile_validation, delimiter=',')

        test = next(reader1)
        val = next(reader2)

        if (test[0] != val[0]):
            scores.append(0.0)
        else:
            length = len(val[1])
            ld = get_ld(test[1], val[1])/length
            score = 0.0 if ld > 1.0 else 1.0 - ld
            scores.append(score)

result = float(sum(scores)/float(len(scores)))
print("Score", result)
