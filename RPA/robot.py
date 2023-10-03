a="811"
b="1114"
c="1417"
d="1720"
e="2023"
f="2302"

A="L"
B="MA"
C="ME"
D="J"
E="V"
F="S"
G="D"
l=[a,b,c,d,e,f]
L=[A,B,C,D,E,F,G]
po='<th id="btn" class="' 
pa='" onclick="fct()">Check</th>'
res=""
for i in l:
    for j in L:
        print(po+i+j+pa)