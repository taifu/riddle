import StringIO
import sys
old_out = sys.stdout
new_out = StringIO.StringIO()
sys.stdout = new_out
import this
sys.stdout = old_out
new_out.seek(0)
msg = new_out.read()
#from collections import defaultdict
#pos = defaultdict(list)
#for i, c in enumerate(msg):
#    pos[c].append(i)
#for c, i in sorted(pos.items()):
#    print c, ",".join(str(n) for n in i)[:30]

solution = ""
for i in (11, 104, 82, 212, 183, 67, 198, 73, 668, 3, 540, 236, 16, 855):
    solution += msg[i]
print solution
