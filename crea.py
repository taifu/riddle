import sys
import random

f = file(sys.argv[1], "w")

for x in range(int(sys.argv[2])):
    for y in range(int(sys.argv[2])):
        f.write("%d" % random.randint(0, 9))
    f.write("\n")
f.close()
