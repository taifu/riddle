html = """
    34 281
    73 13
     1 1091
     3 317
   109 1
    27 35
   951 1
"""
numbers = list(int(x) for line in html.split("\n") if line for x in line.strip().split(" ") if x)
html = ""
for i in range(len(numbers)/2):
    a, b = numbers[i*2:i*2+2]
    html += ("&#%d;" % (a*b))
name = "/tmp/uni.html"
file(name, "w").write(html)
import webbrowser
webbrowser.open(name)
