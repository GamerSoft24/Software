s=input("Please enter a text that you want to convert into binary: ")
li=list(s)
code=""
for x in range(len(li)):
    t1=li[x]
    t2=ord(t1)
    t3=bin(t2)
    t4=t3[2:]
    code=code+t4
print("This is your text converted into binary: ",code)
