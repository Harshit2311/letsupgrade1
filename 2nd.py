l1='harshit is going to market'
d1={}
for i in l1:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]=d1[i]+1
print (d1)