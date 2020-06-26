import re
txt = str(input())
letterz= re.search(".z", txt)
if letterz:
    print("Found a match!")
else:
    print("Not matched!")