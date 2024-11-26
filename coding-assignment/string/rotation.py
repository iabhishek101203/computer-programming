st1=input()
st2=input()
if len(st1)==len(st2) and st2 in (st1+st1):
    print("rotaion is possible")
else:
    print("rotaion not possible")