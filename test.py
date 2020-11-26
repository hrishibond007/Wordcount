# list1=["this","this.","this","is","very","good"]

s="python."
s3="HTML,"
if s[-1::] == '.':
    s1=s.split(".")
    s1.pop()
    str1=""
    str1 +=s1[0]
    
    print(str1)
if s3[-1::]==",":
    s4=s3.split(",")
    s4.pop()
    s5=""
    s5 +=s4[0]
    print(s5)
    
else:
    print("not present")


