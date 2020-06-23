import random as r

rel = 'relationships.txt'
sec = 'secrets.txt'

def numlines(file):
    count = 0
    with open(file, 'r') as f:
        for line in f:
            count += 1
    return count

def extract(file):
    randnum = r.randint(1, numlines(file))
    with open(file, 'r') as f:
        numline = 0
        for line in f:
            numline += 1
            if randnum == numline:
                return line