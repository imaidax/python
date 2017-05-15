fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
words = 0
for line in fh:
    line = line.rstrip()
    words = line.split()
    if words not in fh:
        lst.append(words)
lst.sort()
print lst
