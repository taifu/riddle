html = """
    29 293
    95 89
    6  163
    91 1319
    74 79
    72 925
    37 1801
"""
numbers = list(int(x) for line in html.split("\n") if line for x in line.strip().split(" ") if x)
html = ""
for i in range(len(numbers)/2):
    a, b = numbers[i*2:i*2+2]
    html += ("&#%d;" % (a*b))
# &#8497; &#8455; &#978; &#120029; &#5846;  &#66600; &#66637;
name = "/tmp/uni.html"
file(name, "w").write(html)
import webbrowser
webbrowser.open(name)
