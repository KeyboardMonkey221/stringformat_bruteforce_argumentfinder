import sys

input = "aaaa"

for i in range(1, int(sys.argv[1])):
    input += "{}:%{}$p ".format(i,i)

print input
