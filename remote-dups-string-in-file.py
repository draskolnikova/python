d = {}

fp = open("data1.txt.nodup","w")
text_file = open("data1.txt", "r")
lines = text_file.readlines()
for line in lines:
    if not line in d.keys():
        d[line] = 0
    d[line] = d[line] + 1

for line in lines:
    if d[line] == 0:
        continue
    elif d[line] >= 2:
        fp.write(line)
        d[line] = 0
    else:
        fp.write(line)
