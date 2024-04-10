stack=[]

str = """<body>
    <p>
    I am wpa and my gf is myat
    </p>
</body1>"""
valid = True
st = str.splitlines()
for line in st:
    line = line.strip()
    if line.startswith("</"):
        tag = line[2:len(line)-1]
        end_tag =stack.pop()
        print("end tag",tag)
        if tag != end_tag: #p so /p , body so /body pyit ma Right mr mo (eg)=> p and /p1 lo error ko check
            valid = False
            break
    elif line.startswith("<"):
        tag = line[1:len(line)-1]
        stack.append(tag)
        print("start tag ",tag)
    else:
        print("Normal line",line)

if valid == False:
    print("Invalid")
elif len(stack) == 0:
    print("valid")
else:
    print("Invalid")
