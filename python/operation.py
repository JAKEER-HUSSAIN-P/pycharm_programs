def average(l):
    return sum(l)/len(l)
def grades(l):
    cnt=1
    for i in l:
        if i>=90:
            print(cnt,"S")
        elif i>=80:
            print(cnt,"A")
        elif i>=70:
            print(cnt,"B")
        elif i>=60:
            print(cnt,"C")
        else:
            print(cnt,"F")
        cnt+=1
