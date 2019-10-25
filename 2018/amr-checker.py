##############################
# Python 3.7 required
# usage: python3 amr-checker.py <csv-file-name>
# you need to run this script from a directory where you have amr files to check with
# where csv file is your solution file
#
# IMPORTANT NOTE:
# Comments have to be removed from the amr files you check you solution with
# You can use following regex to match them: (^#(.)+$\n)+
##############################


import csv
import sys
import os
import subprocess
import re

result_filename = sys.argv[1]

scores = []


def balance_and_fix(infile):

    content = []
    count = 0
    balance = 0

    for i, char in enumerate(infile.strip()):
        if balance == 1 and char == ")":
            count += 1

        if char == "(":
            balance += 1

        if char == ")":
            balance -= 1

        content.append(char)
        if balance == 0:
            content.append("\n\n")

    return (balance, count, "".join(content))


with open(result_filename, newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

    for i, row in enumerate(reader):
        name, tree = row[0], row[1]

        with open(name) as rel_file:
            rel_tree = rel_file.read()
            rel_balance, rel_count, rel_content = balance_and_fix(rel_tree)
        balance, count, content = balance_and_fix(tree)

        print("#### name: {}    balance: {}    count: {}".format(name, balance, count))
        print("#### relname: {}    relbalance: {}    relcount: {}".format(name, rel_balance, rel_count))

        if balance != 0:
            print("Tree {} (row {}) is not balanced: {}".format(name, i, balance))
            continue
        
        with open("tmp.txt", "w") as f:
            f.write(content)
        
        result = subprocess.run(["python3", "smatch.py", "-f", name, "tmp.txt"], capture_output=True)
        output = str(result.stdout)
        output = output.strip()
        _, score = output.split()
        score = score[:-3]
        float_score = float(score)

        total_score = float_score / rel_count * count

        print(name, total_score)


