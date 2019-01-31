import re

s=input().strip()
ans=re.findall(r'[0-9]+',s)
opp=re.findall(r'[+-/*]',s)
flag=False
temp=int(ans[0])
if(len(ans)!=len(opp)+1):
    flag=True
if(flag==False):
    for i in range(len(opp)):
        if(opp[i]=='+'):
            temp=temp+int(ans[i+1])
        elif(opp[i]=='-'):
            temp=temp-int(ans[i+1])
        elif(opp[i]=='*'):
            temp=temp*int(ans[i+1])
        elif(opp[i]=='/'):
            temp=temp/int(ans[i+1])
        else:
            flag=True
if(flag==False):
    print(temp)
else:
    print("Worng Input")
    
