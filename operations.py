li=open("C:/Users/Lenovo/OneDrive/Desktop/example.txt","r")
txt=li.read().split()
txt.strip()
cnt=1
for i in txt:
    if i==" ":
        cnt+=1
print(cnt)